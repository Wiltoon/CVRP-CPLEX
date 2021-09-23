# Decidir os valores minimos e maximos de 'k'
# Otimizar com CPLEX cada um dos 'k's subVRPs construídos
# Mostrar as respostas encontradas para cada 'k' em um arquivo
# Selecionar o melhor 'k' para mostrar na figura

from classes.output import OutputSolutionModel
from classes.solution import Solution
from classes.result import Result
from classes.modeloEntrada import IntanceModelSolomon
from services.CPLEX.utilOtimization import solveCPLEX
from services.KMEANS.utilKmeans import createKMeans, createSubSetDelivery

def returnMinimumValueDict(kMin: dict):
    for i in sorted(kMin, key = kMin.get.objetivo):
        return [i, kMin[i]]

def selectBetterKMeans(subVRP:list(int), instance: IntanceModelSolomon, time_exec: int) -> OutputSolomon:
    # Retorna a melhor seleção em uma lista, onde cada posição:
    # [qtd_klusters_necessarios, Result(
    #   objetivoTotalCalculado,
    #   [lista de (Result) de cada subVRP dentro do VRP]
    # )]
    kMin = {}
    for sub in subVRP:
        objetivoTotal = 0
        results = []
        for k in sub:
            subIntance = sub[k]
            subSet = [0]+subIntance
            solution : Solution = solveCPLEX(
                subSet      = subSet, 
                instance    = instance, 
                tempo_exec  = time_exec
            )
            results.append(solution)
            objetivoTotal += solution.objetivo
        kMin[sub] = Result(objetivoTotal, results)
    return returnMinimumValueDict(kMin)

def otimizarInstancia(instance: IntanceModelSolomon):
    Kmin = 5
    Kmax = instance.M/2
    possibles = createKMeans(
        dataframe   = instance.df_positions_deliverys,
        init        = 'random',
        iteration   = 300,
        search      = [Kmin,Kmax]  
    )
    #Capturar a lista de um subVRP e otimizar com o CPLEX
    klusterVRP = createSubSetDelivery(possibles)
    kExists = klusterVRP.vrpList
    subVRP = klusterVRP.subVrpList
    kSelect = selectBetterKMeans(
        subVRP      = subVRP, 
        instance    = instance, 
        time_exec   = 5
    )
    qKluster = kSelect[0]
    solutions = kSelect[1]
    centroids = kExists[qKluster]
    output = OutputSolutionModel(
        instance = instance, 
        num_kluster= qKluster, 
        partialSolutions= solutions,
        centroids=centroids
    )
    # deve entregar uma solução contendo, x, centroids, e a entrada do arquivo
    return output
    
    
        
