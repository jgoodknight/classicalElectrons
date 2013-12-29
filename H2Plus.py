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
                            initialPosition = (0.0, 0.0), 
                            initialMomentum = (1.0, 1.0), 
                            radiates = True)

hydrogen2Plus = chargedParticleUniverse([proton1, proton2, electron1], timeStep = .05)

hydrogen2Plus.evolveNTimeSteps(500)

#hydrogen2Plus.plotHistory()

hydrogen2Plus.animateHistory(400, "hydrogen2Plus.mp4")

#plt.figure()
#plt.plot(hydrogen.totalEnergyHistory)
#plt.title("Energy")
#
#plt.figure()
#plt.plot(hydrogen.totalAngularMomentumHistory)
#plt.title("Angular Momentum")
