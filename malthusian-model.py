# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:28:39 2020
A Simple Malthusian Growth Model; based off Williamson(2014)
@author: LJ Valencia
"""
# Import packages
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol

plt.close('all') # close all open figures

"Define the variables as mathematical symbols"
z,L,N,theta,gamma = Symbol('z'), Symbol('L') , Symbol('N'), Symbol('theta'), Symbol('gamma')
Y = z*(N)**(theta)*(L)**(1-theta) # Cobb-Douglas production function

"Calculate partial derivatives L, N"
Yprime_l = Y.diff(L)
Yprime_n = Y.diff(N)
print(Yprime_l, Yprime_n) # print partial derivatives

"Define parameters and arrays"
# parameters 
z = 1 # total factor productivity
N = 27 # labour stock
L = 10 # stock of land; fixed value
theta = 0.4 # output elasticity of land/capital
gamma = 0.4
# arrays
n = np.arange(1,N) # create an array of N
b_r = np.arange(5.2,2.6,-0.1) # birth rate
d_r = np.arange(1,3.6,0.1) # death rate
N_f = n+n*(b_r-d_r) # future population

"Calculate consumption per capita"
def production(z,L): # function for cobb-douglas equation
    Y = z * L**(theta) * n**(1-theta)
    return Y
def consumption_worker(Y): # function for consumption per capita/consumptuon per worker
    C_N = (Y/n)**gamma
    return C_N
def pop_growth(N_f): # population growth rate; equivalent to 1 + growth rate
    N_n = N_f/n
    return N_n
# calculate values
Y = production(z,L)
cons_worker = consumption_worker(Y)
pop_growth = pop_growth(N_f)

"Deriving N' through application of CRS property"
def future_pop(C_N):
    future_pop = (C_N/n)*n
    return future_pop
# calculate values
future_pop = future_pop(Y)

"Calculate Per Worker Production Function"
def production_capita(z,L):
    y = z * L**(theta) / n**(1+theta)
    return y
y = production_capita(z,L)
y_n = Y/n # output per capita

"Plot"
# population growth and cons. per capita;
fig, ax = plt.subplots(figsize=(10,8))
ax.set(title="Population Growth Depends on Consumption per Worker", xlabel="Consumption per Worker (C/N)", ylabel="Pop. Growth Rate (N'/N)")
ax.grid()
ax.plot(cons_worker,pop_growth, label='g(C/N)')
ax.legend()
# future population and current population;
fig, ax = plt.subplots(figsize=(10,8))
ax.set(title="Determination of Population in the Steady State", 
       xlabel="Current Population, N \n Note: The point where the curve intersects with the 45-degree line is the steady state.", 
       ylabel="Future Population, N")
ax.grid()
ax.plot(n,future_pop, label='g(zF(L/N,1))N')
# 45-degree line for steady state
x = np.linspace(*ax.get_xlim())
ax.plot(x, x, label='45-degree line')
ax.legend()
# per worker production function;
fig, ax = plt.subplots(figsize=(10,8))
ax.set(title="Per Worker Production Function", xlabel="Land per worker, l", ylabel="Output per worker, y")
ax.grid()
ax.plot(y, y_n, label='zf(l)')
ax.legend()

fig, ax = plt.subplots(3,figsize=(10,8))
fig.suptitle('Determination of the Steady State in the Malthusian Model')
ax[0].set(xlabel="Current Population, N", ylabel="Future Population, N") 
ax[0].plot(n,future_pop,label='g(zF(L/N,1))N')
x = np.linspace(*ax[0].get_xlim())
ax[0].plot(x,x,label='45-degree line')
ax[0].legend()
ax[1].set(xlabel="Land per worker, l", ylabel="Output per worker, y")
ax[1].plot(y, y_n, label='zf(l)')
ax[1].legend()
ax[2].set(xlabel="Consumption per Worker (C/N)", ylabel="Pop. Growth Rate (N'/N)")
ax[2].plot(cons_worker,pop_growth, label='g(C/N)')
ax[2].legend()
plt.tight_layout()

"Scenarios"
y_1 = production_capita(z+1,L)
fig, ax = plt.subplots(2,figsize=(10,8))
ax[0].set(xlabel="Land per worker, l", ylabel="Output per worker, y")
ax[0].plot(y, y_n, y_1, y_n)
ax[1].set(xlabel="Consumption per Worker (C/N)", 
          ylabel="Pop. Growth Rate (N'/N)")
ax[1].plot(cons_worker,pop_growth, 
           label='g(C/N)')
ax[1].legend()
fig.suptitle('Effect of Increase in Z in the Malthusian Model')
plt.tight_layout()