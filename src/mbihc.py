from rdkit import Chem
from rdkit.Chem import AllChem

smiles = "CN(C(=S)N/N=C/c1cn(Cc2ccccc2)c3ccccc13)C" #MBIHC. Full IUPAC nomenclature: (E)-2-((1-benzyl-1H-indol-3-yl)methylene)-N-methylhydrazine-1-carbothioamide
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)

writer = Chem.SDWriter('MBIHC.sdf')
writer.write(mol)
writer.close()

conf = mol.GetConformer()
with open('MBIHC.xyz', 'w') as f:
    f.write(f"{mol.GetNumAtoms()}\n")
    f.write("MBIHC molecule\n")
    for i, atom in enumerate(mol.GetAtoms()):
        pos = conf.GetAtomPosition(i)
        f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")
