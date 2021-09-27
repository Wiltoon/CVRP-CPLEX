from classes.abstractModelRF import AbstractModelRF
from docplex.mp.model import Model

class RelaxFixCVRP(AbstractModelRF):
    def __init__(self):
        self.fix         = []
        self.set_int     = []
        self.relax       = []
        
    def constructProblem(self):
        # Deverá retornar o modelo com as variaveis fixas, inteiras e relaxadas
        model = Model('CVRP')
        for f in self.fix:
            self.createVariablesFixed(model, f)
        for s in self.set_int:
            self.createVariablesVars(model, s)
        for r in self.relax:
            self.createVariablesRelaxed(model, r)
        self.constructConstraints(model,self)
        return model
    
    def solveRF(model: Model, time):
        # Deve retornar as variáveis fixadas 
        return super().solveRF()

    def createVariablesFixed(model: Model, f):
        
        return

    def createVariablesVars(model: Model, s):
        return

    def createVariablesRelaxed(model: Model, r): 
        return
    
    def constructConstraints(model: Model,vars):

        return