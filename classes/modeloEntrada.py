from pedido import Pedido

import numpy as np

import pandas as pd
import io

class IntanceModelSolomon:
    def __init__(self, instance, subSet):
        self.deposit = instance.deposit
        
        self.deliverys = []
        for i in subSet:
            self.deliverys.append(instance.deliverys[i])
        self.Q = instance.capacity_drivers # capacity homogenius
        self.M = instance.num_drivers
        self.N = [i for i in range(1, len(self.deliverys))]
        self.V = [0] + self.N
        self.A = [(i,j) for i in self.V for j in self.V if i != j]
        self.c = {(i, j): np.hypot(self.deliverys[i].x-self.deliverys[j].x, self.deliverys[i].y-self.deliverys[j].y) for i, j in self.A}


    def __init__(self, namefile, num_drivers, capacity_drivers):
        self.df_main = pd.read_csv(namefile)
        self.df_positions = self.df_main.drop(['CUSTOMER CUST NO.',' DEMAND','READY TIME','SERVICE TIME','AVAIL. TIME','DUE DATE'], axis=1)
        self.df_positions_deliverys = self.df_positions.drop([0],axis=0)
        self.deposit = Pedido(
            identifier=self.df_main['CUSTOMER CUST NO.'][0],
            x=self.df_main['XCOORD.'][0],
            y=self.df_main['YCOORD.'][0],
            carga=self.df_main[' DEMAND'][0]
        )
        self.deposit_position = [self.deposit.x,self.deposit.y]
        self.deliverys = []
        self.q = []
        for i in len(self.df_main):
            delivery = Pedido(
                identifier=self.df_main['CUSTOMER CUST NO.'][i],
                x=self.df_main['XCOORD.'][i],
                y=self.df_main['YCOORD.'][i],
                carga=self.df_main[' DEMAND'][i]
            )
            self.q.append(delivery.carga)
            self.deliverys.append(delivery)
        self.Q = capacity_drivers # capacity homogenius
        self.M = num_drivers
        self.N = [i for i in range(1, len(self.df_main))]
        self.V = [0] + self.N
        self.A = [(i,j) for i in self.V for j in self.V if i != j]
        self.c = {(i, j): np.hypot(self.deliverys[i].x-self.deliverys[j].x, self.deliverys[i].y-self.deliverys[j].y) for i, j in self.A}