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