def createConstraints(model, x, u, ins):
    model.add_constraints(model.sum(x[i, j] for j in ins.V if j != i) == 1 for i in ins.N)
    model.add_constraints(model.sum(x[i, j] for i in ins.V if i != j) == 1 for j in ins.N)
    model.add_indicator_constraints(
        model.indicator_constraint(x[i, j], u[i]+ins.q[j] == u[j]) for i, j in ins.A if i != 0 and j != 0)
    model.add_constraints(u[i] >= ins.q[i] for i in ins.N)
