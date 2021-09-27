from classes.relaxFixCVRP import RelaxFixCVRP


def relaxAndFix(partitions, timeLimit):
    # Retorna uma lista com a respostas fixadas das partitions
    auxSet = partitions.copy()
    length = len(partitions)
    setCurrent      = auxSet.pop(0)
    relaxFixCvrp    = RelaxFixCVRP()
    relaxFixCvrp.set_int    = relaxFixCvrp.set_int.append(setCurrent)
    relaxFixCvrp.relax      = auxSet.copy()
    while length != len(relaxFixCvrp.fix):
        model       = relaxFixCvrp.constructProblem()
        resultFix   = relaxFixCvrp.solveRF(model) ## local onde é resolvido o modelo
        relaxFixCvrp.fix.append(resultFix)
        setCurrent  = relaxFixCvrp.relax.pop(0)
        relaxFixCvrp.set_int     = []
        relaxFixCvrp.set_int     = relaxFixCvrp.set_int.append(setCurrent)
    return relaxFixCvrp.fix