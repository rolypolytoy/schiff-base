## MBIHC

What is MBIHC? It's a Schiff base containing an indole moiety, a thiocarbazone group, and with favorable bidentate and tridentate coordination modes with iron, zinc, and nickel. Its complexes are of increasing interest to bioinorganic research and requires using state-of-the-art computational organometallic chemistry methods.

To that end we've used DFT to compute its molecular properties, using its provided IUPAC structure ((E)-2-((1-benzyl-1H-indol-3-yl)methylene)-N-methylhydrazine-1-carbothioamide) and generated a preliminary 3d structure via RDKIT, optimized by MMFF. We then used ORCA with the wB97X-D3 functional (more accurate than the workhorse BL3YP) and the def2-SVP basis set.

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

# Usage

It's a file. Download the file.

# Which File?

The .xyz one. If you open it in [Avogadro](https://avogadro.cc/) it should look like this:

![image](https://github.com/user-attachments/assets/7a18d23c-900a-422b-b846-68574e6ca065)

Used [ORCA](https://orcaforum.kofo.mpg.de/app.php/dlext/) to optimize the geometry with DFT. It's free and better than Gaussian.

# Thanks

Of course.

# References:
J. Singh, S. Gautam, M. B. Singh, P. Singh, U. Kumar, Chem. Biodiversity 2024, 21, e202401301. https://doi.org/10.1002/cbdv.202401301
