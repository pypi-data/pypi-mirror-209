import bioumlsim

sim = bioumlsim.BioUMLSim('C:/BioUML_2023.1')
model = sim.load("C:/Users/Damag/BioUML_Scripts/models_selected/BIOMD0000000857.xml")
print(model)