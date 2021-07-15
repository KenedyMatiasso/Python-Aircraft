# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
from numpy import zeros, array
from mpl_toolkits.mplot3d import Axes3D
                
fusres = 20;      #Fuselage resolution
wgres  = 20;      #Wing,HT,VT resolution

XW=0
ZW=0
ALIW=0
XH=0
ZH=0
ALIH=0
XV=0
ZV=0
YV=0
numVT=1
VERTUP=1
NX=0
X=zeros(20)
S=zeros(20)
R=zeros(20)
ZU=zeros(20)
ZL=zeros(20)  
CHRDR_WG=0
CHRDBP_WG=0
CHRDTP_WG=0
SSPN_WG=0
SSPNOP_WG=0
SAVSI_WG=0  
SAVSO_WG=0
CHSTAT_WG=0
DHDADI_WG=0
DHDADO_WG=0
TC_WG=.12             
CHRDR_HT=0
CHRDBP_HT=0
CHRDTP_HT=0
SSPN_HT=0
SSPNOP_HT=0
SAVSI_HT=0  
SAVSO_HT=0
CHSTAT_HT=0
DHDADI_HT=0
DHDADO_HT=0
TC_HT=.12             
CHRDR_VT=0
CHRDBP_VT=0
CHRDTP_VT=0
SSPN_VT=0
SSPNOP_VT=0
SAVSI_VT=0 
SAVSO_VT=0
CHSTAT_VT=0
TC_VT=.12                                     
SPANFI_F=0
SPANFO_F=0
CHRDFI_F=0
CHRDFO_F=0
DELTA_F=0            
SPANFI_A=0
SPANFO_A=0
CHRDFI_A=0
CHRDFO_A=0
DELTAL_A=0
DELTAR_A=0    
SPANFI_E=0
SPANFO_E=0
CHRDFI_E=0
CHRDFO_E=0
DELTA_E=0                

# body parameters
NX = 20.0

ZU=[0.0,0.562,1.017,1.345,1.542,2.565,3.248,3.773,4.035,4.232,4.265,4.035,
    4.068,4.101,4.101,4.101,4.035,3.97,3.871, 3.773]

ZL=[0.0,-0.562,-1.017,-1.345,-1.509,-1.608,-1.608,-1.608,-1.575, -1.509,
    -1.411,-1.214,-0.984,-0.689,-0.131,0.262,0.656,0.984,1.181,1.345]

X=[0.0,0.689,2.231,3.773,5.151,6.955,8.727,10.40,11.614,12.959,14.60,16.864,
   18.865,20.932,24.869,27.854,31.004,33.629,35.892,38.00]

S=[0.0,0.991,3.25,5.684,7.534,10.087,12.005,13.449,14.198,14.891,15.207,
   14.339,13.878,13.398,12.033,10.531,8.708,7.269,6.381,5.359]

P=[0.0,3.529,6.39,8.452,9.768,11.556,12.862,13.836,14.24, 14.58,14.692,
   14.038,13.76,13.354,12.472,11.576,10.48,9.586,8.976,8.23]

R=[0.0,0.562,1.017,1.345,1.509,1.542,1.608,1.608,1.64, 1.64,1.64,1.673,
   1.673,1.673,1.673,1.673,1.608,1.509,1.476,1.378]


Rn=-array(R)

# Wing parameters
CHRDTP_WG=2.84
SSPNE_WG=20.21
SSPN_WG=21.92
CHRDR_WG=9.487
SAVSI_WG=10.0
CHSTAT_WG=0.25
TWISTA_WG=0.0
DHDADI_WG=0.0
TC_WG=.15

#Horizontal Tail
CHRDTP_HT=2.318
SSPNE_HT=7.216
SSPN_HT=7.525
CHRDR_HT=7.736 
SAVSI_HT=28.848
CHSTAT_HT=0.25
TWISTA_HT=0.0
DHDADI_HT=0.0
TC_HT=.09

#Vertical Tail
CHRDTP_VT=3.12
SSPNE_VT=6.6
SSPN_VT=6.7
CHRDR_VT=10.4 
SAVSI_VT=42.588
CHSTAT_VT=0.25
TC_VT=.09


plt.figure()
plt.plot(X, ZL, color = 'k')
plt.plot(X, ZU, color = 'k')
plt.xlim([0, max(X)])
plt.ylim([-max(X)/2, max(X)/2])
plt.title('Lateral View')

plt.figure()
plt.plot(X, R, color = 'k')
plt.plot(X, Rn, color = 'k')
plt.xlim([0, max(X)])
plt.ylim([-max(X)/2, max(X)/2])
plt.title('Upper View')

