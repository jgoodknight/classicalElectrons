# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:36:48 2013

@author: joseph
"""
from classicalChargedParticles import *

bondLength = 2.5204

berllyium = ChargedParticle(charge = 3, mass = 16420, 
                            initialPosition = (0.0, 0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = True)
proton1 = ChargedParticle(charge = 1, mass = 1836, 
                            initialPosition = (bondLength, 0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = False)
                            
proton2 = ChargedParticle(charge = 1, mass = 1836, 
                            initialPosition = (-bondLength, 0.0), 
                            initialMomentum = (0.0, 0.0), 
                            stationary = False)
                            
electron1 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (-bondLength,  bondLength), 
                            initialMomentum = (1.2, 0.0), 
                            radiates = True)

                            
electron2 = ChargedParticle(charge = -1, mass = 1,
                            initialPosition = (bondLength,  -bondLength), 
                            initialMomentum = (-1.2, 0.0), 
                            radiates = True)

hydrogen2Plus = chargedParticleUniverse([berllyium, proton1, proton2, electron1, electron2], timeStep = .05)

hydrogen2Plus.evolveNTimeSteps(780)

hydrogen2Plus.plotHistory()

#hydrogen2Plus.animateHistory(400, "hydrogen2Plus.mp4")

#plt.figure()
#plt.plot(hydrogen.totalEnergyHistory)
#plt.title("Energy")
#
#plt.figure()
#plt.plot(hydrogen.totalAngularMomentumHistory)
#plt.title("Angular Momentum")
