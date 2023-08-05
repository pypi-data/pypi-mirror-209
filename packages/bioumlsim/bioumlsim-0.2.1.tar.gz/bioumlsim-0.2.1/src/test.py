import bioumlsim2
import numpy

sim = bioumlsim.BioUMLSim()
model = sim.load("C:/Users/Damag/BioUML_Scripts/models_selected/BIOMD0000000003.xml")
result = model.simulate(100, 10)

print(result)
print()
print(result.getTimes())
print()
print(result.getNames())
print()
print(result.getValues())
print()
print(result.getValues('X'))