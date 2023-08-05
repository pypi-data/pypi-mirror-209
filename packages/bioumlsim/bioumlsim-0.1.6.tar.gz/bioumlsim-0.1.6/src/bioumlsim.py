import jpype
import jpype.imports

class BioUMLSim:
    
    bioUMLPath = None
    atol = 1E-8
    rtol = 1E-8
    
    def __init__(self, path = 'C:/BioUML_2023.1'):
        self.bioUMLPath = path
        print("JVM is starting up")
        jpype.startJVM(classpath=[self.bioUMLPath+'/plugins/*',self.bioUMLPath+'/plugins/cern.jet.random_1.3.0/colt.jar'])
 
    def runJVM(path):
        self.bioUMLPath = path
        print("JVM is starting up")
        jpype.startJVM(classpath=[self.bioUMLPath+'/plugins/*',self.bioUMLPath+'/plugins/cern.jet.random_1.3.0/colt.jar'])
       
    def load(self, file):
        """
        Loads SBML file and transforms it into object which represents mathematical model.
        Args:
            file (str): path to file
        Returns:
            model
        """
        print(f"SBML file is loading: {file}.")
        diagram = jpype.JClass("biouml.plugins.sbml.SbmlModelFactory").readDiagram(file)
        engine = jpype.JClass("biouml.plugins.simulation.java.JavaSimulationEngine")()
        engine.setDiagram(diagram)
        engine.setClassPath(self.bioUMLPath +'/plugins/biouml.plugins.simulation/src.jar')
        engine.setOutputDir(self.bioUMLPath+'/temp')
        engine.disableLog()
        return engine.createModel()
        