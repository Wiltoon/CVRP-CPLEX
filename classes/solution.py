
from docplex.mp.model import Model
class Solution:
    def __init__(self, solution, model: Model, x):
        self.solution = solution
        self.model = model
        self.vetor_x = x
        self.objetivo = 0
        # self.pKmeans = possibleKmeans