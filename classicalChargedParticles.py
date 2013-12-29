# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 00:48:39 2013

@author: joseph
"""
import math

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation

coulumbForceConstant = 1.0
speedOfLight = 137.0
    
class ChargedParticle(object):
    
    def __init__(self, charge, 
                    initialPosition = (0,0), 
                    initialMomentum =(.1,.1), 
                    mass = 1, 
                    stationary = False,
                    radiates = False):
        "A charged particle which lives in a two-dimensional universe"
        self.charge = charge
        self.mass = mass
        
        self.stationary = stationary
        self.radiates = radiates
        
        if charge < 0:
            self.plottingColorFloat = 100.0
            self.plottingColor = "Red"
        else:
            self.plottingColorFloat = 0.0
            self.plottingColor = "Blue"
        
        self.plotCircleSize = 100 * self.charge**2
        
        self.initialX = float(initialPosition[0])
        self.initialY = float(initialPosition[1])
            
        self.initialPx = float(initialMomentum[0])
        self.initialPy = float(initialMomentum[1])
        
        self.historyX = [self.initialX]
        self.historyY = [self.initialY]
        self.positionTimes = [0]
        
        self.historyPx = [self.initialPx]
        self.historyPy = [self.initialPy]
        self.momentumTimes = [0]
    
    def currentX(self):
        return self.historyX[-1]
        
    def currentY(self):
        return self.historyY[-1]
    
    def currentPx(self):
        return self.historyPx[-1]
        
    def currentPy(self):
        return self.historyPy[-1]
        
    def momentumKick(self, forceVectorToKickBy, dt):
        "takes a force and changes the momentum"
        newXMomentumWithoutRadiation = self.historyPx[-1] + dt * forceVectorToKickBy[0] / self.mass
        newYMomentumWithoutRadiation = self.historyPy[-1] + dt * forceVectorToKickBy[1] / self.mass
        
        if self.radiates and len(self.historyPx) > 1:
#            dt = self.momentumTimes[-1] - self.momentumTimes[-2]
            commonAccelerationDivider = self.mass * dt
            xAcceleration = (self.historyPx[-1] - self.historyPx[-2]) / commonAccelerationDivider
            yAcceleration = (self.historyPy[-1] - self.historyPy[-2]) / commonAccelerationDivider
            
            commonRadiatedEnergyMultiplier = dt * 2.0 * self.charge**2 / (3.0 * speedOfLight**3) 
            xRadiatedEnergy = commonRadiatedEnergyMultiplier * xAcceleration**2
            yRadiatedEnergy = commonRadiatedEnergyMultiplier * yAcceleration**2
            
            #now we assume this energy lost is all in kinetic energy which = dp**2 / 2 m
            xMomentumLost = math.sqrt(xRadiatedEnergy * 2.0 * self.mass)
            yMomentumLost = math.sqrt(yRadiatedEnergy * 2.0 * self.mass)
        else:
            self.historyPx.append(newXMomentumWithoutRadiation)
            self.historyPy.append(newYMomentumWithoutRadiation)
            return
        #if the total momentum is already negative, we have to add momentum, not subtract 
        if newXMomentumWithoutRadiation < 0:
            xMomentumLost = -xMomentumLost
        if newYMomentumWithoutRadiation < 0:
            yMomentumLost = -yMomentumLost
        self.historyPx.append(self.historyPx[-1] + dt * forceVectorToKickBy[0] / self.mass - xMomentumLost)
        self.historyPy.append(self.historyPy[-1] + dt * forceVectorToKickBy[1] / self.mass - yMomentumLost)
        self.momentumTimes.append(self.momentumTimes[-1])

    def movePosition(self, dt):
        "takes the current momentum and moves the position accordingly"
        self.historyX.append(self.historyX[-1] + dt * self.currentPx() / self.mass)
        self.historyY.append(self.historyY[-1] + dt * self.currentPy() / self.mass)
        self.positionTimes.append(self.positionTimes[-1])
        
    def kineticEnergy(self):
        return (self.currentPx()**2 + self.currentPy()**2) / (2 * self.mass)
    
    def distanceFromOtherParticle(self, otherChargedParticle):
        return math.sqrt( (self.currentX() - otherChargedParticle.currentX())**2 + (self.currentY() - otherChargedParticle.currentY())**2)
        
    def energyWithOtherParticle(self, otherChargedParticle):
        return coulumbForceConstant * self.charge * otherChargedParticle.charge / self.distanceFromOtherParticle(otherChargedParticle)

    def gradientValueAtOtherParticle(self, otherChargedParticle):
        return coulumbForceConstant * self.charge * otherChargedParticle.charge / self.distanceFromOtherParticle(otherChargedParticle)

    def forceOnOtherParticle(self, otherChargedParticle):
        overallTerm = coulumbForceConstant * self.charge * otherChargedParticle.charge / self.distanceFromOtherParticle(otherChargedParticle)**3
        xValue = overallTerm * (otherChargedParticle.currentX() - self.currentX())
        yValue = overallTerm * (otherChargedParticle.currentY() - self.currentY())
        return np.array([xValue, yValue])
        
    def plotPositionAtIndex(self, index):
        return plt.scatter(self.historyX[index], self.historyY[index], s = self.plotCircleSize, c = self.plottingColor)
        
    def __plotMomentumArrowAtIndex(self, index):
        return plt.quiver(self.currentX(), self.currentY(), self.currentPx(), self.currentPy())
            
    def plotCurrentPosition(self):
        self.plotPositionAtIndex(-1)
        
    def plotCurrentMomentumArrow(self):
        self.__plotMomentumArrowAtIndex(-1)
    
    def plotPositionHistory(self):
        for i in range(len(self.historyX)):
            self.plotPositionAtIndex(i)
        
    def currentAngularMomentum(self):
        return self.currentX() * self.currentPy() - self.currentY() * self.currentPx()
        

class chargedParticleUniverse(object):
    "A two dimensional universe of several particles"
    
    def __init__(self, listOfChargedParticles, timeStep):
        
        self.myChargedParticles = listOfChargedParticles
        
        self.numberOfParticles = len(listOfChargedParticles)
        
        self.timeStep = timeStep
        
        self.totalEnergyHistory = [self.currentTotalEnergy()]
        self.totalAngularMomentumHistory = [self.currentTotalAngularMomentum()]
        
    
    def currentTotalPotentialEnergy(self):
        output = 0
        for firstIndex in range(self.numberOfParticles):
            for secondIndex in range(self.numberOfParticles):
                if secondIndex > firstIndex:
                    output = output + self.myChargedParticles[firstIndex].energyWithOtherParticle(self.myChargedParticles[secondIndex])
        return output
    
    def currentTotalKineticEnergy(self):
        output = 0
        for firstIndex in range(self.numberOfParticles):
            output = output + self.myChargedParticles[firstIndex].kineticEnergy()
        return output
        
    def currentTotalEnergy(self):
        return self.currentTotalKineticEnergy() + self.currentTotalPotentialEnergy()
        
    def currentTotalAngularMomentum(self):
        total = 0
        for particle in self.myChargedParticles:
            total = total + particle.currentAngularMomentum()
        return total
        
    def timeStepForward(self):
        #move each particle forward in momenum half of a time step
        for particle in self.myChargedParticles:
            myForce = np.zeros(2)
            for otherParticle in self.myChargedParticles:
                if otherParticle is not particle:
                    myForce = myForce + otherParticle.forceOnOtherParticle(particle)
            if not particle.stationary:
                particle.momentumKick(myForce, self.timeStep / 2)
        
        #now recitfy all the positions
        for particle in self.myChargedParticles:
            if not particle.stationary:
                particle.movePosition(self.timeStep)
        
        #do momentum again
        for particle in self.myChargedParticles:
            myForce = np.zeros(2)
            for otherParticle in self.myChargedParticles:
                if otherParticle is not particle:
                    myForce = myForce + otherParticle.forceOnOtherParticle(particle)
            
            if not particle.stationary:
                particle.momentumKick(myForce, self.timeStep / 2)
        
        self.totalAngularMomentumHistory.append(self.currentTotalAngularMomentum())
        self.totalEnergyHistory.append(self.currentTotalEnergy())
        
    def evolveNTimeSteps(self, N):
        for i in range(N):
            self.timeStepForward()
    
    def plotCurrent(self, momentumArrows = False):
        plt.figure()
        for particle in self.myChargedParticles:
            if momentumArrows:
                particle.plotCurrentMomentumArrow()
            particle.plotCurrentPosition()
    
    def plotHistory(self):
        plt.figure()
        for particle in self.myChargedParticles:
            particle.plotPositionHistory()
            
    def animateHistory(self, lengthInFrames, fileName, xLimits=(-2,2), yLimits=(-2,2)):
        
        fig =  plt.figure()                
        ax = fig.add_subplot(111)
#        ax.grid(True, linestyle = '-', color = '0.75')
        ax.set_xlim(xLimits)
        ax.set_ylim(yLimits)
        scatter = plt.scatter([], [], animated=True)
        
        def animate(i, fig, scatter):
            positions = []
            colors = []
            sizes = []
            for particle in self.myChargedParticles:
                if particle.stationary:
                    x = particle.currentX()
                    y = particle.currentY()
                else:
                    x = particle.historyX[i]
                    y = particle.historyY[i]
                positions.append([x,y])
                colors.append(particle.plottingColorFloat)
                sizes.append(particle.plotCircleSize)
            
            scatter.set_offsets(tuple(positions))
            scatter._sizes = np.array(sizes)            
            scatter.set_array(np.array(colors))
            return scatter,
            
        anim = animation.FuncAnimation(fig, animate,
                               frames=lengthInFrames, interval=20, blit=False, fargs=(fig, scatter, ))
        anim.save(fileName, fps=50, dpi=200)#, extra_args=['-vcodec', 'libx264'])
        
        
if __name__ == "__main__":
    print "Try hydrogen.py or helium.py"
    
    
            
            