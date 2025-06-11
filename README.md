## MBIHC

What is MBIHC? It's a Schiff base containing an indole moiety, a thiocarbazone group, and with favorable bidentate and tridentate coordination modes with iron, zinc, and nickel. Its complexes are of increasing interest to bioinorganic research and have antifungal properties. For more information, check the paper out (in the References section).

To that end I used DFT to compute its molecular properties, using its provided IUPAC structure ((E)-2-((1-benzyl-1H-indol-3-yl)methylene)-N-methylhydrazine-1-carbothioamide) and generated a preliminary 3d structure via RDKIT, optimized by MMFF. We then used ORCA with the wB97X-D3 functional (more accurate than the workhorse BL3YP) and the def2-SVP basis set. I actually found a few errors in the DFT calculations in the paper- for example, in the paper it said the calculated dipole was 12.1 Debye, which is entirely inconsistent with my results in the lab, which showed 5% EtoAc was sufficient for TLC, and 15% was too far. This means the molecule is quite nonpolar, and 1.44 Debye is significantly more reasonable. That, and their energy of ~-900 Hartree vs mine at -1312.89 makes me suspect they ran a single-point calculation on the XRD-obtained structure, versus doing a DFT optimization of the molecule in gas/solution phase and running electronic structure calculations on it.

# Synthesis

You can make it by a pretty simple reaction. Take N-benzylindole-3-carboxaldehyde (1) and 4-Methyl Thiosemicarbazide (2) with the structural formulas shown below. Weigh them in a 1:1 stoichiometric ratio (we used 0.21 mmol, 50mg of the aldehyde, and 22.34mg of the thiosemicarbazide). Structural formulae of (1) and (2) are provided below:

![image](https://github.com/user-attachments/assets/126b8d41-aeb9-45e6-87d8-af077697cd54)

The target molecule MBIHC (3) has structural formula:

![image](https://github.com/user-attachments/assets/324b4682-1b45-4ff1-b44c-0d78fb1a2f13)

To make MBIHC from these two, is not a particularly difficult process. You need:

- A distillation (simple or vacuum) setup
- Methanol
- Reagents 1, 2
- A heating plate/method of heating at 70 C
- Glassware
- Oil/Parrafin
- Acetic Acid

Take 50 mg of reagent (1) and dissolve in a round bottom flask with 10-15mL of methanol (preferrably with a clean magnetic stirrer) to homogeneity. Take 22.34 mg of reagent (2) and dissolve. Add 2-3 drops of dilute acetic acid to the mixture, then place in a 70 C heated oil bath under reflux for at least 20 hours. Take it off the heat. If you see dull yellowish precipitate on the walls you've likely got it. I'll soon provide images of the precipitate and TLC stains for you to be able to observe it with greater ease.

![image](https://github.com/user-attachments/assets/9aa48128-db68-4fe6-ae90-813b8a9304ea)


Take TLC at 5% EtoAc, 95% Hexane, and view under short UV and long UV, or use chemical methods if accessible. Previous results reported 15%, but 5% is more optimal, as 15% runs a significant risk of MBIHC advancing beyond the solvent front, due to its nonpolarity, calculated by DFT to be 1.44 Debye (and this improvement has been greenlit by the first author of the paper introducing MBIHC, Jugminder Singh). 

Then, if it's likely MBIHC, distill at 50 C to evaporate all the methanol. Dry in the flask for 1-2 days in a cool, dry place, ensuring there are tiny holes in the covering to allow ventilation. To crystallize, use DCM, followed by hexane, carefully layered, and store. Crystallization takes an unknown period of time, and is recommended for use in ligand-metal complexes. Currently, complexes with zinc, iron, nickel and cobalt are known, with tridentate modes possible for three of four of these. The degree of nuclearity can be controlled by varying the stoichiometric ratios, and complexes can be formed at room temperature. For more information check out the MBIHC.pdf in the repo (note I wrote the 15% EtoAc step before I realized 5% was preferable. It's a recent identification, so use 5% instead).

More information on MBIHC (particularly visuals) are in the supplementary information section at the bottom of this readme.

# Usage

It's a file. Download the file.

# Which File?

The .xyz one. If you open it in [Avogadro](https://avogadro.cc/) it should look like this:

![image](https://github.com/user-attachments/assets/7a18d23c-900a-422b-b846-68574e6ca065)

Used [ORCA](https://orcaforum.kofo.mpg.de/app.php/dlext/) to optimize the geometry with DFT. It's free and better than Gaussian. Energy's -1312.89 Hartree and dipole moment's 1.44 Debye. Orca seemed pretty happy about the results, optimized in about 30 geometry steps with a pretty high-quality functional with dispersion corrections. I did use MMFF to generate it rather than hand-drawing it, but even then the workflow took a few hours at the most, and didn't require any handholding. 

Functional: ωB97X-D3. Basis set: def2-SVP. Geometry's optimized and the .out files are in .txt formats instead, so you don't have to run anything. All the electronic structure identification and geometry optimization is complete and accessible, so feel free. If you need anything else, email me at rishiitsharma@gmail.com.

# Thanks

Of course.

# Supplementary Images

MBIHC precipitated to the side of the flask:

![1000134970](https://github.com/user-attachments/assets/8b9bd7c0-6543-4c55-800d-a155b81a0eea)

MBIHC under short-UV (the first one is reactant (1), the second is reactant (2), the third is product (3)). Note reactant 1 has not fully reacted, but there is a new Rf value not present in either reactant 1 or reactant 2 (very weakly visible under short UV):

![1000134979](https://github.com/user-attachments/assets/5653af4f-dffb-4813-9225-8cb475efa9e8)

Under long UV it becomes even more apparent that something novel has been created since only MBIHC fluoresces:

![1000134978](https://github.com/user-attachments/assets/d4ff83c2-a3f3-40d4-b0c8-0d35e2f71da4)

5% EtoAc, 95% Hexane used for these. Using 4% or 3% may help in making the Rf values more reasonable than the 70-90% they were hovering at here, but 5% provides sufficient, consistent performance in minutes.

How crystals of MBIHC look like (sample courtesy of Jugminder Singh, PhD student and faculty at Deshbandhu College, University of Delhi, and the original synthesizer of MBIHC):

![1000135003](https://github.com/user-attachments/assets/e1e4c923-5ee1-45c3-bb8f-ebb157013907)

# References:
J. Singh, S. Gautam, M. B. Singh, P. Singh, U. Kumar, Chem. Biodiversity 2024, 21, e202401301. https://doi.org/10.1002/cbdv.202401301
