from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "CNC(=S)NN" #4-methyl thiosemicarbazide
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)

writer = Chem.SDWriter('Amine.sdf')
writer.write(mol)
writer.close()

conf = mol.GetConformer()
with open('Amine.xyz', 'w') as f:
    f.write(f"{mol.GetNumAtoms()}\n")
    f.write("4-methyl thiosemicarbazide\n")
    for i, atom in enumerate(mol.GetAtoms()):
        pos = conf.GetAtomPosition(i)
        f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")