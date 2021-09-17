from docplex.mp.model import Model

import numpy as np

def createModelMath(name,ins):
    model = Model(name)
    x, u = createVariable(model)
    createObjectiveFunction(model,ins,x)
    createConstraints(model, x, u, ins)
    return model, x, u

def createVariable(model, ins):
    x = model.binary_var_dict(ins.A, name='x')
    u = model.continuous_var_dict(ins.N, ub=ins.Q, name='u')
    return x,u

def createObjectiveFunction(model, ins, x):
    model.minimize(model.sum(ins.c[i,j] * x[i,j]) for i,j in ins.A)

def createConstraints(model, x, u, ins):
    model.add_constraints(model.sum(x[i, j] for j in ins.V if j != i) == 1 for i in ins.N)
    model.add_constraints(model.sum(x[i, j] for i in ins.V if i != j) == 1 for j in ins.N)
    model.add_indicator_constraints(
        model.indicator_constraint(x[i, j], u[i]+q[j] == u[j]) for i, j in ins.A if i != 0 and j != 0)
    model.add_constraints(u[i] >= q[i] for i in ins.N)

def solve(model, time_execution):
    model.parameters.timilimit = time_execution
    return model.solve(log_output=True)