# Decidir os valores minimos e maximos de 'k'
# Otimizar com CPLEX cada um dos 'k's subVRPs construídos
# Mostrar as respostas encontradas para cada 'k' em um arquivo
# Selecionar o melhor 'k' para mostrar na figura

from services.CPLEX.utilOtimization import solveCPLEX
from services.KMEANS.utilKmeans import createKMeans, createSubSetDelivery

def returnMinimumValueDict(kMin):
    for i in sorted(kMin, key = kMin.get):
        return [i, kMin[i]]

def selectBetterKMeans(subVRP, instance, time_exec):
    kMin = {}
    for sub in subVRP:
        objetivo = 0
        for k in sub:
            subIntance = sub[k]
            subSet = [0]+subIntance
            result = solveCPLEX(
                subSet=subSet, 
                instance=instance, 
                tempo_exec = 1
            )
            objetivo += result.objetivo
        kMin[sub] = objetivo
    return returnMinimumValueDict(kMin)

def otimizarInstancia(instance):
    Kmin = 5
    Kmax = instance.M/2
    possibles = createKMeans(
        dataframe   = instance.df_positions_deliverys,
        init        = 'random',
        iteration   = 300,
        search      = [Kmin,Kmax]  
    )
    #Capturar a lista de um subVRP e otimizar com o CPLEX
    subVRP = createSubSetDelivery(possibles)
    kSelect = selectBetterKMeans(
        subVRP = subVRP, 
        instance = instance, 
        time_exec=1
    )
    # deve entregar uma solução contendo, x, centroids, e a entrada do arquivo
    return kSelect
    
    
        
