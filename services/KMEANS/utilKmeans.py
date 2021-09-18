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

def createSubSetDelivery(klusters):
    subVRP = []
    for vrp in klusters:
        dotes = {}
        print(vrp.n_clusters)
        for k in range(vrp.n_clusters):
            dotes[k] = []
        for i in range(len(vrp.labels_)):
            dotes[vrp.labels_[i]].append(i+1)
        subVRP.append(dotes)
    return subVRP