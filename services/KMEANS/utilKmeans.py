from classes.kluteres import Klusteres
from sklearn.cluster import KMeans

def createKMeans(search,init,iteration,dataframe):
    possibleKmeans = []
    for k in range(search[0], search[1]):
        kmeans = KMeans(
            n_clusters=k,
            init=init,
            max_iter=iteration
        )
        kmeans.fit(dataframe)
        possibleKmeans.append(kmeans)
    return possibleKmeans

def createSubSetDelivery(klusters) -> list:
    # Retorna um vetor de dicionarios, que apresenta
    # [dotes:{qtd_kluster : [pedidos_do_kluster[i]]}]
    subVRP = []
    VRPKmeans = []
    for vrp in klusters:
        dotes = {}
        for k in range(vrp.n_clusters):
            dotes[k] = []
        for i in range(len(vrp.labels_)):
            dotes[vrp[i]].append(i+1)
        subVRP.append(dotes)
        VRPKmeans.append(vrp)
    klusterVRP = Klusteres(VRPKmeans,subVRP)
    return klusterVRP