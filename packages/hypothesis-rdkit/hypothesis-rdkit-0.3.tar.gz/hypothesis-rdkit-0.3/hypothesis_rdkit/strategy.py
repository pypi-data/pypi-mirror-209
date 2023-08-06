import string
from collections import defaultdict
from functools import reduce

import hypothesis.strategies as st
import pkg_resources
from rdkit.Chem import (
    BRICS,
    CombineMols,
    Mol,
    MolFromSmiles,
    MolToMolBlock,
    MolToSmiles,
    RemoveHs,
    SanitizeMol,
    rdMolDescriptors,
    BondType,
)
from rdkit.Chem.BRICS import reverseReactions

__all__ = ["mols", "smiles", "mol_blocks"]


# load a set of fragments (encoded as smiles) from a file
with pkg_resources.resource_stream(__name__, "fragments.smi") as f:

    def _parse_line(line):
        m = MolFromSmiles(line)
        rotatable_bonds = rdMolDescriptors.CalcNumRotatableBonds(m)
        return m, rotatable_bonds

    fragments = [_parse_line(line) for line in f]

possible_dummy_labels = set(
    [
        a.GetIsotope()
        for fragment, _ in fragments
        for a in fragment.GetAtoms()
        if a.GetSymbol() == "*"
    ]
)


def has_dummy_atom(fragment, dummy_label):
    if isinstance(dummy_label, Mol):
        dummy_label = dummy_label.GetAtomWithIdx(0).GetIsotope()
    return any(
        (
            a.GetSymbol() == "*" and a.GetIsotope() == dummy_label
            for a in fragment.GetAtoms()
        )
    )


# all reactions and fragments compatible with each other
# reaction = fragment + X --> product
# reaction = X + fragment --> product
compatible_reactions = {
    dummy_label: [
        (r, True)
        for r in reverseReactions
        if has_dummy_atom(r._matchers[0], dummy_label)
    ]
    + [
        (r, False)
        for r in reverseReactions
        if has_dummy_atom(r._matchers[1], dummy_label)
    ]
    for dummy_label in possible_dummy_labels
}

# mapping dummy atom d to fragments containing d
compatible_fragments = defaultdict(list)
for fragment, n in fragments:
    for a in fragment.GetAtoms():
        if a.GetSymbol() == "*":
            dummy_label = a.GetIsotope()
            compatible_fragments[dummy_label].append((fragment, n))


# sort the lists in each key by number of dummy atoms in the fragment and fragment size
def num_dummy_atoms(mol):
    return sum([1 for a in mol.GetAtoms() if a.GetSymbol() == "*"])


for dummy_label in possible_dummy_labels:
    compatible_fragments[dummy_label] = sorted(
        compatible_fragments[dummy_label],
        key=lambda x: (num_dummy_atoms(x[0]), x[0].GetNumAtoms()),
    )


dummy_pattern = MolFromSmiles("[*]")


@st.composite
def mols(
    draw,
    name=st.text(alphabet=list(string.ascii_lowercase), min_size=1),
    max_rotatable_bonds=st.just(10),
    n_connected_components=st.just(1),
):
    """Strategy for generating random molecules.

    Parameters
    ----------
    name : str or hypothesis.strategies.SearchStrategy
        Name of the molecule.
    max_rotatable_bonds : int or hypothesis.strategies.SearchStrategy
        Maximum number of rotatable bonds in the molecule. If
        n_connected_components > 1, each individual component will have less
        rotatable bonds than max_rotatable_bonds.
    n_connected_components : int or hypothesis.strategies.SearchStrategy
        Number of connected components in the molecule.
    """
    if isinstance(name, str):
        name = st.just(name)
    if isinstance(n_connected_components, int):
        n_connected_components = st.just(n_connected_components)
    if isinstance(max_rotatable_bonds, int):
        max_rotatable_bonds = st.just(max_rotatable_bonds)

    max_rotatable_bonds = draw(max_rotatable_bonds)
    n_connected_components = draw(n_connected_components)

    # draw connected components independently
    if n_connected_components > 1:
        components = [
            draw(
                mols(
                    max_rotatable_bonds=max_rotatable_bonds,
                    n_connected_components=1,
                )
            )
            for _ in range(n_connected_components)
        ]
        seed = reduce(CombineMols, components)
    else:
        # repeat this process until a valid molecule is drawn
        while True:
            # start by drawing a random fragment and use it as seed
            # make sure that the seed has less rotatable bonds than max_rotatable_bonds
            suitable_seeds = [
                (f, n) for (f, n) in fragments if n <= max_rotatable_bonds
            ]
            seed, n_rotatable_bonds_current = draw(st.sampled_from(suitable_seeds))
            display(seed)

            # extend the seed by running compatible reactions on the seed
            # stop when molecule has no dummy atoms anymore (i.e. is fully built)
            rep = 0
            while seed.HasSubstructMatch(dummy_pattern):
                if rep > 10:
                    raise ValueError("Could not build molecule")
                while True:
                    # find a free substitution site
                    for atom in seed.GetAtoms():
                        if atom.GetSymbol() == "*":
                            dummy_label = atom.GetIsotope()
                            break

                    # draw a random reaction compatible with the chosen dummy atom
                    reaction, right = draw(
                        st.sampled_from(compatible_reactions[dummy_label])
                    )
                    other_label = (
                        reaction._matchers[int(right)].GetAtomWithIdx(0).GetIsotope()
                    )
                    reaction_adds_rotatable_bond = (
                        reaction.GetProducts()[0].GetBondWithIdx(0).GetBondType()
                        != BondType.DOUBLE
                    )

                    # draw a random fragment compatible with the drawn reaction
                    # (but filter all fragments that would exceed the maximum number of rotatable bonds)
                    # note: compatible_mapping[dummy_label] was sorted by number of dummy atoms and size
                    #       --> shrinking is done automatically
                    def _induced_rotatable_bonds(fragment, n):
                        # IF reaction adds a rotatable bond AND fragment has more than 2 atoms
                        # --> add 1 to the number of rotatable bonds
                        # note: this is only an approximation
                        # ... but: the actual number of rotatable bonds will be less
                        #          than this estimate
                        return n + (
                            reaction_adds_rotatable_bond
                            and (fragment.GetNumAtoms() > 2)
                        )

                    n_remaining_rotatable_bonds = (
                        max_rotatable_bonds - n_rotatable_bonds_current
                    )
                    feasible_fragments = [
                        (f, n_induced)
                        for (f, n) in compatible_fragments[other_label]
                        if (n_induced := _induced_rotatable_bonds(f, n))
                        <= n_remaining_rotatable_bonds
                    ]
                    fragment, n = draw(st.sampled_from(feasible_fragments))
                    print("fragment")
                    display(fragment)

                    # run the reaction and collect the products
                    if right:
                        products = reaction.RunReactants((seed, fragment))
                    else:
                        products = reaction.RunReactants((fragment, seed))

                    # remove duplicate products
                    unique_smiles = set()
                    results = []
                    if products:
                        for product in products:
                            s = MolToSmiles(product[0])
                            if s not in unique_smiles:
                                unique_smiles.add(s)
                                results.append(product[0])

                    # if reactions were unsuccessful, try again (works only because of randomly drawing reactions)
                    if len(results) == 0:
                        continue

                    # if reactions were successful, pick a random product and use it as the new seed
                    # note: shrinking is not applicable here, because all products have the same size
                    seed = draw(st.sampled_from(results))

                    # update the number of rotatable bonds
                    n_rotatable_bonds_current += n

                    break

            try:
                seed.UpdatePropertyCache()
                SanitizeMol(seed)
                seed = RemoveHs(seed)
            except:
                continue

    name = draw(name)
    if name is not None:
        seed.SetProp("_Name", name)

    # TODO: create conformer

    return seed


@st.composite
def smiles(draw, **kwargs):
    mol = draw(mols(**kwargs))

    return f"{MolToSmiles(mol)} {mol.GetProp('_Name')}"


@st.composite
def mol_blocks(draw, **kwargs):
    mol = draw(mols(**kwargs))

    return MolToMolBlock(mol)
