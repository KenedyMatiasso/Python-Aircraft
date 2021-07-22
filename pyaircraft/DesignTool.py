#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:54:36 2021

@author: Kenedy Matiasso Portella

email:kenedyportella@hotmail.com
"""

from numpy import sqrt, pi, array
import matplotlib.pyplot as plt
from tools import printFuselage, printWing


class DesignTool():
    def __init__(self):
        #Geral
        self.XCG = 0 #Posi<ão do CG no eixo X
        self.ZCG = 0 # posição vertical do CG
        self.SCALE = 1
        
        #Fuselagem
        self.X = []
        self.R = []
        self.ZU = []
        self.ZL = []
        self.BNOSE = 2
        self.BTAIL = 2
        self.BLN = 0
        self.BLA = 0
        self.DS = 0
        self.ITYPE = 2
        self.METHOD = 2
        
        #Wing info
        self.NSW = 1
        self.CHRDTP_W = 0 #Corda na ponta da asa
        self.CHRDR_W = 0 # Corda na raiza
        self.CHRDBP_W = 0 # Corda no breakpoint
        self.SSPNE_W = 0 #Semi-envergadura molhada
        self.SSPN_W = 0 #Semi-envergadura teórica
        self.SSPNOP_W = 0 #painel externo da semi-envergadura
        self.SAVSI_W = 0 #enflexamento da sessão interna
        self.SAVSO_W = 0 # enflexamento da sessão externa
        self.TWISTA_W = 0 #ângulo de torção da asa
        self.CHSTAT_W = 0 #Porcentagem da MAC que o afilamento será referenciado
        self.DHDADI_W = 0 #  Diedro da seção interna
        self.DHDADO_W = 0 # Diedro da seção externa
        self.XW = 0 #Posição horizontal do apex da asa
        self.ZW = 0 #Posição vertical do apez da asa
        self.ALIW = 0 #Angulo de incidência da corda na raiz da asa
        
    @property
    def NX(self):
        return len(self.X)
    
    @property
    def Z(self):
        Z = []
        for i in range(0, len(self.ZU)):
            Z.append(self.ZU[i]/2 - self.ZL[i]/2)
        return Z
    
    @property
    def Zoff(self):
        Zoff = []
        for i in range(0, len(self.Z)):
            Zoff.append(self.Z[i] + self.ZL[i])
        return Zoff
    
    @property
    def P(self):
        P = []
        for i in range(0, len(self.R)):
            P.append(2*pi*sqrt((self.R[i]**2 + self.Z[i]**2)/2))
        return P
    
    @property
    def TYPE(self):
        if self.NSW == 2:
            A = (self.CHRDR_W + self.CHRDBP_W)/2*(self.SSPNE_W - self.SSPNOP_W) + (self.CHRDBP_W + self.CHRDTP_W)/2*self.SSPNOP_W
            C = A/self.SSPNE_W
        else:
            C = (self.CHRDTP_W + self.CHRDR_W)/2
        
        if (self.SSPNE_W/C)<=3:
            return 2
        else:
            return 3
    
    def printFuselage(self):
        return printFuselage(self.X, self.ZU, self.ZL, self.R, self.Zoff)
    
    def printWing(self):
        return printWing(self.NSW, self.CHRDTP_W, self.CHRDR_W, self.CHRDBP_W,
                         self.SSPNE_W, self.SSPN_W, self.SSPNOP_W, self.SAVSI_W,
                         self.SAVSO_W, self.TWISTA_W, self.CHSTAT_W, self.DHDADI_W,
                          self.DHDADO_W, self.ALIW)
        
A = DesignTool()

A.X = [0.0,0.689,2.231,3.773,5.151,6.955,8.727,10.40,11.614,12.959,14.60,16.864,
   18.865,20.932,24.869,27.854,31.004,33.629,35.892,38.00]


A.R=[0.0,0.562,1.017,1.345,1.509,1.542,1.608,1.608,1.64, 1.64,1.64,1.673,
   1.673,1.673,1.673,1.673,1.608,1.509,1.476,1.378]

A.ZU=[0.0,0.562,1.017,1.345,1.542,2.565,3.248,3.773,4.035,4.232,4.265,4.035,
    4.068,4.101,4.101,4.101,4.035,3.97,3.871, 3.773]

A.ZL=[0.0,-0.562,-1.017,-1.345,-1.509,-1.608,-1.608,-1.608,-1.575, -1.509,
    -1.411,-1.214,-0.984,-0.689,-0.131,0.262,0.656,0.984,1.181,1.345]

# Wing parameters
A.NSW =2
A.CHRDTP_W = 2.84
A.SSPNE_W = 20.21
A.SSPN_W = 21.92
A.CHRDR_W = 9.487
A.SAVSI_W = 10.0
A.CHSTAT_W = 0.25
A.TWISTA_W = 0.0
A.DHDADI_W = 8.0
A.SSPNOP_W = 9
A.CHRDBP_W = 6
A.SAVSO_W = 7
A.TC_W = .15
A.DHDADO_W = 15

A.printWing()