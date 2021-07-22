#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:03:51 2021

@author: Kenedy Matiasso Portella

email:kenedyportella@hotmail.com
"""
from numpy import sqrt, pi, array, tan, radians, linspace
import matplotlib.pyplot as plt


def printFuselage(X, ZU, ZL, R, Zoff):
    X = array(X)
    R = array(R)
    ZU = array(ZU)
    ZL = array(ZL)
    Rn = -array(R)
    Zoff = array(Zoff)
    
    plt.figure()
    plt.plot(X, ZL, color = 'k')
    plt.plot(X, ZU, color = 'k')
    plt.plot(X, Zoff, color = 'r')

    plt.xlim([0, max(X)])
    plt.ylim([-max(X)/2, max(X)/2])
    plt.title('Lateral View')
    
    plt.figure()
    plt.plot(X, R, color = 'k')
    plt.plot(X, Rn, color = 'k')
    plt.xlim([0, max(X)])
    plt.ylim([-max(X)/2, max(X)/2])
    plt.title('Upper View')
    
def printWing(NS, CHRDTP, CHRDR, CHRDBP, SSPNE, SSPN, SSPNOP, SAVSI, SAVSO,
              TWISTA, CHSTAT, DHDADI, DHDADO, ALIW):
        
    if NS ==1:
        
        XC = linspace(0, SSPN, 50) #panels on X axis
        LocalChord = linspace(CHRDR, CHRDTP, 50)
        ZC = XC*tan(radians(DHDADI))
        YC = XC*tan(radians(SAVSI)) + CHSTAT*CHRDR
        Yinf = YC - CHSTAT*LocalChord
        Ysup = YC + (1-CHSTAT)*LocalChord
        
        plt.figure()
        plt.plot(XC, YC, color = 'r')
        plt.plot(XC, Ysup, color = 'k')
        plt.plot(XC, Yinf, color = 'k')
        plt.plot([XC[0],XC[0]], [Yinf[0], Ysup[0]], color = 'k')
        plt.plot([XC[-1],XC[-1]], [Yinf[-1], Ysup[-1]], color = 'k')
        plt.plot(XC, 0*XC, linestyle = ':', color= 'b')
        plt.title('Upper View')
        
        plt.figure()
        plt.plot(XC, ZC, color = 'k')
        plt.plot(XC, 0*XC, linestyle = ':', color ='b')
        plt.title('Front View')
        plt.ylim([-XC[-1]/2, XC[-1]/2])
        
    if NS ==2:
        XCInner = linspace(0, SSPN - SSPNOP, 25)
        XCOut = linspace(SSPN - SSPNOP, SSPN, 25)
        
        LocalChordInner = linspace(CHRDR, CHRDBP, 25)
        LocalChordOut = linspace(CHRDBP, CHRDTP, 25)
        
        ZCInner = XCInner*tan(radians(DHDADI))
        ZCOut = ZCInner[-1] + (XCOut - XCInner[-1])*tan(radians(DHDADO))
        
        YCInner = XCInner*tan(radians(SAVSI)) + CHSTAT*CHRDR
        YCOut = YCInner[-1] + (XCOut - XCInner[-1])*tan(radians(SAVSO))
        
        YinfInner = YCInner - CHSTAT*LocalChordInner
        YinfOut = YCOut - CHSTAT*LocalChordOut
        
        YsupInner = YCInner + (1-CHSTAT)*LocalChordInner
        YsupOut = YCOut + (1-CHSTAT)*LocalChordOut
        
        
        plt.figure()
        plt.plot(XCInner, YCInner, color = 'r')
        plt.plot(XCOut, YCOut, color = 'r')

        plt.plot(XCInner, YsupInner, color = 'k')
        plt.plot(XCInner, YinfInner, color = 'k')
        plt.plot(XCOut, YsupOut, color = 'k')
        plt.plot(XCOut, YinfOut, color = 'k')
        plt.plot([XCInner[0], XCInner[0]], [YinfInner[0], YsupInner[0]], color = 'k')
        plt.plot([XCInner[-1], XCInner[-1]], [YinfInner[-1], YsupInner[-1]], color = 'k')
        plt.plot([XCOut[-1], XCOut[-1]],[YinfOut[-1], YsupOut[-1]], color = 'k')
        plt.plot(XCInner, 0*XCInner, linestyle = ':', color= 'b')
        plt.plot(XCOut, 0*XCInner, linestyle = ':', color= 'b')

        plt.title('Upper View')
        
        plt.figure()
        plt.plot(XCInner, ZCInner, color = 'k')
        plt.plot(XCOut, 0*XCOut, linestyle = ':', color ='b')
        plt.plot(XCInner, 0*XCOut, linestyle = ':', color ='b')

        plt.plot(XCOut, ZCOut, color = 'k')
        plt.title('Front View')
        plt.ylim([-XCInner[-1]/2, XCInner[-1]/2])
        
    
        
        