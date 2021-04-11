# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:43:18 2021

@author: David
"""
import matplotlib.pyplot as plt
from pylab import figure, plot, show, contourf
from numpy import sqrt, array, linspace
from time import time

from operators import basis, tensor, destroy, create, qeye, sigmap, sigmam, sigmaz
from basis import setup_basis, setup_rho
from models import setup_laser
from propagate import time_evolve, steady
from expect import expect_comp, setup_convert_rho, wigner_comp
from indices import list_equivalent_elements


#system size
ntls = 2
nphot = 10

#define parameters
omega=0.0
omega0=0.0
g=0.5

gam_dn =1
gam_up = 2.5
kappa = 0.1

g=g/sqrt(ntls)
delta = omega-omega0

#time evolution
tmax = 75
dt = 0.1

nphot0 = 0


# setup basis with ntls spin, each of Hilbert space dimentsion
# 2 and photon with dimension nphot
setup_basis(ntls, 2, nphot)

#run other setup routines
list_equivalent_elements()
setup_convert_rho()
from basis import nspins, ldim_p, ldim_s

#setup inital state and calculate Liouvillian
L = setup_laser(g, delta, kappa, gam_dn, gam_up, 0,4)
initial = setup_rho(basis(ldim_p, nphot0), basis(ldim_s,1))
print("setup L")

#operators to calculate expectation values for
na = tensor(create(ldim_p)*destroy(ldim_p), qeye(ldim_s))
sz = tensor(qeye(ldim_p), sigmaz())

t0=time()
resultscomp = time_evolve(L, initial, tmax, dt, [na, sz])
tf=time()-t0

print("Time evollution complete")
print(tf)

#plot time evolution
figure(1)
plot(resultscomp.t, resultscomp.expect[0]/ntls)
plt.xlabel('time (s)')
plt.ylabel('a a†/N')

figure(2)
plot(resultscomp.t, resultscomp.expect[1])
plt.xlabel('time (s)')
plt.ylabel('Sigma Z')

#system size
ntls = 4
nphot = 10

#define parameters
omega=0.0
omega0=0.0
g=0.5

gam_dn =1
gam_up = 2.5
kappa = 0.1

g=g/sqrt(ntls)
delta = omega-omega0

#time evolution
tmax = 75
dt = 0.1

nphot0 = 0


# setup basis with ntls spin, each of Hilbert space dimentsion
# 2 and photon with dimension nphot
setup_basis(ntls, 2, nphot)

#run other setup routines
list_equivalent_elements()
setup_convert_rho()
from basis import nspins, ldim_p, ldim_s

#setup inital state and calculate Liouvillian
L = setup_laser(g, delta, kappa, gam_dn, gam_up, 0,4)
initial = setup_rho(basis(ldim_p, nphot0), basis(ldim_s,1))
print("setup L")

#operators to calculate expectation values for
na = tensor(create(ldim_p)*destroy(ldim_p), qeye(ldim_s))
sz = tensor(qeye(ldim_p), sigmaz())

t0=time()
resultscomp = time_evolve(L, initial, tmax, dt, [na, sz])
tf=time()-t0

print("Time evollution complete")
print(tf)

#plot time evolution
figure(1)
plot(resultscomp.t, resultscomp.expect[0]/ntls)
plt.xlabel('time (s)')
plt.ylabel('a a†/N')

figure(2)
plot(resultscomp.t, resultscomp.expect[1])
plt.xlabel('time (s)')
plt.ylabel('Sigma Z')

#system size
ntls = 6
nphot = 10

#define parameters
omega=0.0
omega0=0.0
g=0.5

gam_dn =1
gam_up = 2.5
kappa = 0.1

g=g/sqrt(ntls)
delta = omega-omega0

#time evolution
tmax = 75
dt = 0.1

nphot0 = 0


# setup basis with ntls spin, each of Hilbert space dimentsion
# 2 and photon with dimension nphot
setup_basis(ntls, 2, nphot)

#run other setup routines
list_equivalent_elements()
setup_convert_rho()
from basis import nspins, ldim_p, ldim_s

#setup inital state and calculate Liouvillian
L = setup_laser(g, delta, kappa, gam_dn, gam_up, 0,4)
initial = setup_rho(basis(ldim_p, nphot0), basis(ldim_s,1))
print("setup L")

#operators to calculate expectation values for
na = tensor(create(ldim_p)*destroy(ldim_p), qeye(ldim_s))
sz = tensor(qeye(ldim_p), sigmaz())

t0=time()
resultscomp = time_evolve(L, initial, tmax, dt, [na, sz])
tf=time()-t0

print("Time evollution complete")
print(tf)

#plot time evolution
figure(1)
plot(resultscomp.t, resultscomp.expect[0]/ntls)
plt.xlabel('time (s)')
plt.ylabel('a a†/N')

figure(2)
plot(resultscomp.t, resultscomp.expect[1])
plt.xlabel('time (s)')
plt.ylabel('Sigma Z')