from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "O=Cc1cn(Cc2ccccc2)c3ccccc13" #N-benzylindole-3-carboxaldehyde
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)

writer = Chem.SDWriter('Aldehyde.sdf')
writer.write(mol)
writer.close()

conf = mol.GetConformer()
with open('Aldehyde.xyz', 'w') as f:
    f.write(f"{mol.GetNumAtoms()}\n")
    f.write("1-benzylindole-3-carboxaldehyde\n")
    for i, atom in enumerate(mol.GetAtoms()):
        pos = conf.GetAtomPosition(i)
        f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")