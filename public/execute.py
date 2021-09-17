
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
    # Resolver Programa
    # Construir a saída