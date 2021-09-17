import numpy as np
import matplotlib.pyplot as plt

def plotResultVRPwithKmeans(image_file, instance, result, kmeans):
    plt.figure(figsize=(15,15))
    plotterDeposit(plt, instance)
    plotterDeliverys(plt, instance, kmeans)
    plotterCentroids(plt, kmeans)
    plotterEdges(plt, kmeans)
    plotterOptions(plt)
    saveImagePlot(plt,image_file)

def plotterDeposit(plt, instance):
    plt.scatter(
        instance.deposit_position[0], 
        instance.deposit_position[1],
        s = 100, 
        c = 'blue',
        marker = 's'
    )

def plotterDeliverys(plt, instance, kmeans):
    plt.scatter(
        instance.df_positions_deliverys.values[:,0], 
        instance.df_positions_deliverys.values[:,1],
        s = 100, 
        c = kmeans.labels_
    )

def plotterCentroids(plt, kmeans):
    plt.scatter(
        kmeans.cluster_centers_[:,0],
        kmeans.cluster_centers_[:,1],
        s = 250,
        c = 'red',
        labels = 'Centroids'
    )

def plotterEdges(plt, kmeans):
    # printar todos os arcos, os arcos estão separados em regiões dentro do kmeans

def plotterOptions():
    plt.title('CVRP WITH KMEANS')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

def saveImagePlot(plt, image_file):
    fig = plt.gcf()
    plt.show()
    fig.savefig(image_file, format='png')