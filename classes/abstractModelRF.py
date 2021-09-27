from abc import ABC, abstractmethod

class AbstractModelRF(ABC):
    def __init__(self):
        self.fix         = []
        self.set_int     = []
        self.relax       = []
        super().__init__()
    
    @abstractmethod
    def constructProblem(self):
        pass

    @abstractmethod
    def solveRF(self):
        pass