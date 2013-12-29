# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:36:48 2013

@author: joseph
"""
from classicalChargedParticles import *

def randomInitialCondition():
    return np.random.normal(scale = 1.0, size = 2)
    
    
proton = ChargedParticle(charge = 2, mass = 2*1836, 
                            initialPosition = (0.0,0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = True)
electron1 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (-.9, 0.0), 
                            initialMomentum = (0.0, 1.0), 
                            radiates = True)
electron2 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (1.1, 0.0), 
                            initialMomentum = (0.0, -1.0), 
                            radiates = True)

helium = chargedParticleUniverse([proton, electron1, electron2], timeStep = .05)

helium.evolveNTimeSteps(300)

#helium.plotHistory()
#plt.xlim((-2, 2))
#plt.ylim((-2, 2))

helium.animateHistory(200, "helium.mp4")

#plt.figure()
#plt.plot(helium.totalEnergyHistory)
#plt.title("Energy")
#
#plt.figure()
#plt.plot(helium.totalAngularMomentumHistory)
#plt.title("Angular Momentum")
