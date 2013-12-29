# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:36:48 2013

@author: joseph
"""
from classicalChargedParticles import *

proton = ChargedParticle(charge = 1, mass = 1836, 
                            initialPosition = (0.0,0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = True)
electron1 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (1.0, 0.0), 
                            initialMomentum = (0.0, 1.0), 
                            radiates = True)

hydrogen = chargedParticleUniverse([proton, electron1], timeStep = .05)

hydrogen.evolveNTimeSteps(4000)
hydrogen.plotHistory()
#hydrogen.animateHistory(3000, "hydrogen.mp4")

#plt.figure()
#plt.plot(hydrogen.totalEnergyHistory)
#plt.title("Energy")
#
#plt.figure()
#plt.plot(hydrogen.totalAngularMomentumHistory)
#plt.title("Angular Momentum")
