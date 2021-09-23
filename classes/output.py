from classes.modeloEntrada import IntanceModelSolomon


class OutputSolutionModel:
    def __init__(self,instance: IntanceModelSolomon,num_kluster,partialSolutions: list,centroids):
        self.instance = instance
        self.num_kluster = num_kluster
        self.partialSolutions = partialSolutions
        self.centroids = centroids