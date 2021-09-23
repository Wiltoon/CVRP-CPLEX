def relaxAndFix(sets, setBinSize, windowType, overLap, timeLimit):
    auxSet = sets.copy()
    length = len(sets)
    setCurrent  = auxSet.pop(0)
    fix         = []
    set_int     = []
    relax       = []
    set_int     = set_int.append(setCurrent)
    relax       = auxSet.copy()
    condition   = True
    while condition:
        model       = constructProblem(fix, set_int, relax)
        resultFix   = solveRF(model) ## local onde é resolvido o modelo
        fix.append(resultFix)
        setCurrent  = relax.pop(0)
        set_int     = setCurrent

    setVarBin = fix
    return setVarBins