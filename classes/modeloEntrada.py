import pandas as pd
import io

class IntanceModelSolomon:
    def __init__(self, namefile, num_drivers, capacity_drivers):
        self.df_main = pd.read_csv(namefile)
        self.df_positions = df_main.drop(['CUSTOMER CUST NO.',' DEMAND','READY TIME','SERVICE TIME','AVAIL. TIME','DUE DATE'], axis=1)
        self.df_positions_deliverys = df_positions.drop([0],axis=0)
        self.deposit = Pedido(
            identifier=df_main['CUSTOMER CUST NO.'][0],
            x=df_main['XCOORD.'][0],
            y=df_main['YCOORD.'][0],
            carga=df_main[' DEMAND']][0]
        )
        self.deposit_position = [deposit.x,deposit.y]
        self.deliverys = []
        for i in len(self.df_main):
            delivery = Pedido(
                identifier=df_main['CUSTOMER CUST NO.'][i],
                x=df_main['XCOORD.'][i],
                y=df_main['YCOORD.'][i],
                carga=df_main[' DEMAND']][i]
            )
            self.deliverys.append(delivery)
        self.Q = capacity_drivers # capacity homogenius
        self.N = [i for i in range(1, len(self.df_main))]
        self.V = [0] + self.N
        self.A = [(i,j) for i in self.V for j in self.V if i != j]
        self.c = {(i, j): np.hypot(self.deliverys[i].x-self.deliverys[j].x, self.deliverys[i].y-self.deliverys[j].y) for i, j in self.A}