
from utils.estrategy import otimizarInstancia
from classes.modeloEntrada import IntanceModelSolomon
import os
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--instance", type = str, required = True)
    parser.add_argument("--drivers", type = int, required = True)
    parser.add_argument("--capacity", type = int, required = True)
    parser.add_argument("--output", type = str, required = True)

    args = parser.parse_args()

    # Receber a entrada
    instance = IntanceModelSolomon(
        instance            = args.instance,
        num_drivers         = args.drivers,
        capacity_drivers    = args.capacity,
        output              = args.output
    )

    # Resolver Programa
    dict_result = otimizarInstancia(instance=instance)
    # solution (dicionario)
    #   indice representa o numero de klusters necessarios
    # Construir a saída
    #   - Os pontos -> deve ter em uma solução
    #   - As rotas -> estará no x
    #   - Os centroids -> estará na resolução dos centroids
    #   - O deposito -> Ta na entrada