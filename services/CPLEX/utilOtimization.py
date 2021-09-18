from classes.solution import Solution
from classes.modeloEntrada import IntanceModelSolomon
from constraints import createConstraints
from docplex.mp.model import Model

import numpy as np

def solveCPLEX(subSet, instance, time_exec):
    subInstance = IntanceModelSolomon(
        instance = instance,
        subSet = subSet
    )
    model, x, u, obj= createModelMath('CVRP', subInstance)
    result = solve(model,time_execution=time_exec)
    solution = Solution(
        solution=result,
        model=model,
        x=x
    )
    solution.objetivo = obj()
    return solution

def createModelMath(name,ins):
    model = Model(name)
    x, u = createVariable(model)
    obj = createObjectiveFunction(model,ins,x)
    createConstraints(model, x, u, ins)
    return model, x, obj

def createVariable(model, ins):
    x = model.binary_var_dict(ins.A, name='x')
    u = model.continuous_var_dict(ins.N, ub=ins.Q, name='u')
    return x,u

def createObjectiveFunction(model, ins, x):
    return model.minimize(model.sum(ins.c[i,j] * x[i,j]) for i,j in ins.A)


def solve(model, time_execution):
    model.parameters.timilimit = time_execution
    return model.solve(log_output=True)