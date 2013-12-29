# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:36:48 2013

@author: joseph
"""
from classicalChargedParticles import *

impactParameter = 1.2
impactMomentum = 2.2

startingDistanceApart = 9.0

positron = ChargedParticle(charge = 1, mass = 1.0, 
                            initialPosition = (startingDistanceApart / 2.0, impactParameter / 2), 
                            initialMomentum = (-impactMomentum / 2.0, 0.0), 
                            radiates = True)
electron1 = ChargedParticle(charge = -1, mass = 1.0,
                            initialPosition = (-startingDistanceApart / 2.0, -impactParameter / 2), 
                            initialMomentum = (impactMomentum / 2.0, 0.0), 
                            radiates = True)

positronium = chargedParticleUniverse([positron, electron1], timeStep = .05)

positronium.evolveNTimeSteps(700)

positronium.plotHistory()

positronium.animateHistory(600, "positronium.mp4")

#plt.figure()
#plt.plot(hydrogen.totalEnergyHistory)
#plt.title("Energy")
#
#plt.figure()
#plt.plot(hydrogen.totalAngularMomentumHistory)
#plt.title("Angular Momentum")
