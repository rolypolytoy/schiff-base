from rdkit import Chem
from rdkit.Chem import AllChem

ligands = {
    'L1': 'O=C(CSc1ccccc1)Nc2cccc3cccnc23',
    'L2': 'O=C(CSc1ccc(Cl)cc1)Nc2cccc3cccnc23',
    'L3': 'O=C(CSc1ccc(C)cc1)Nc2cccc3cccnc23',
    'L4': 'O=C(CSc1ccc(OC)cc1)Nc2cccc3cccnc23'
}

for name, smiles in ligands.items():
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, randomSeed=42)
    AllChem.MMFFOptimizeMolecule(mol)
    
    conf = mol.GetConformer()
    num_atoms = mol.GetNumAtoms()
    
    xyz = [str(num_atoms), f"{name}"]
    for i in range(num_atoms):
        atom = mol.GetAtomWithIdx(i)
        pos = conf.GetAtomPosition(i)
        xyz.append(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}")
    
    with open(f"{name}.xyz", 'w') as f:
        f.write("\n".join(xyz))