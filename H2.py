# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:36:48 2013

@author: joseph
"""
from classicalChargedParticles import *

proton1 = ChargedParticle(charge = 1, mass = 1836, 
                            initialPosition = (-1.89/2.0, 0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = True)
proton2 = ChargedParticle(charge = 1, mass = 1836, 
                            initialPosition = (1.89/2.0, 0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = False)
electron1 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (-0.2, 0.2), 
                            initialMomentum = (1.0, 1.0), 
                            radiates = True)
electron2 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (0.2, -0.2), 
                            initialMomentum = (-1.0, -1.0), 
                            radiates = True)

hydrogen2 = chargedParticleUniverse([proton1, proton2, electron1, electron2], timeStep = .05)

hydrogen2.evolveNTimeSteps(5000)

hydrogen2.plotHistory()

hydrogen2.animateHistory(2000, "hydrogen2.mp4", xLimits=(-7,7), yLimits=(-7,7))

#plt.figure()
#plt.plot(hydrogen.totalEnergyHistory)
#plt.title("Energy")
#
#plt.figure()
#plt.plot(hydrogen.totalAngularMomentumHistory)
#plt.title("Angular Momentum")
