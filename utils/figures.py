from classes.solution import Solution
import numpy as np
import matplotlib.pyplot as plt

from classes.modeloEntrada import IntanceModelSolomon

def plotResultVRPwithKmeans(image_file, instance: IntanceModelSolomon, result: Solution, kmeans):
    plt.figure(figsize=(15,15))
    plotterDeposit(plt, instance)
    plotterDeliverys(plt, instance, kmeans)
    plotterCentroids(plt, kmeans)
    plotterEdges(plt, kmeans)
    plotterOptions(plt)
    saveImagePlot(plt,image_file)

def plotterDeposit(plt: plt, instance: IntanceModelSolomon):
    plt.scatter(
        instance.deposit_position[0], 
        instance.deposit_position[1],
        s = 100, 
        c = 'blue',
        marker = 's'
    )

def plotterDeliverys(plt: plt, instance: IntanceModelSolomon, kmeans):
    plt.scatter(
        instance.df_positions_deliverys.values[:,0], 
        instance.df_positions_deliverys.values[:,1],
        s = 100, 
        c = kmeans.labels_
    )

def plotterCentroids(plt: plt, kmeans):
    plt.scatter(
        kmeans.cluster_centers_[:,0],
        kmeans.cluster_centers_[:,1],
        s = 250,
        c = 'red',
        labels = 'Centroids'
    )

def plotterEdges(plt: plt, x, instance: IntanceModelSolomon):
    active_arcs = [a for a in instance.A if x[a].solution_value > 0.9]
    for i,j in active_arcs:
        deliveryOrigin = instance.deliverys[i]
        deliveryDestiny = instance.deliverys[j]
        plt.plot(
            [deliveryOrigin.x, deliveryDestiny.x], [deliveryOrigin.x, deliveryDestiny.y],
            c = 'g',
            alpha = 0.3
        )
    # printar todos os arcos, os arcos estão separados em regiões dentro do kmeans

def plotterOptions(plt: plt):
    plt.title('CVRP WITH KMEANS')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

def saveImagePlot(plt: plt, image_file: str):
    fig = plt.gcf()
    plt.show()
    fig.savefig(image_file, format='png')