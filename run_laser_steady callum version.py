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
gam_up = linspace(0, 2.5, 50)
kappa = 0.1

g=g/sqrt(ntls)
delta = omega-omega0

#time evolution
tmax = 10
dt = 0.1

nphot0 = 0

na_values = []
sz_values = []

# setup basis with ntls spin, each of Hilbert space dimentsion
# 2 and photon with dimension nphot
setup_basis(ntls, 2, nphot)

#run other setup routines
list_equivalent_elements()
setup_convert_rho()
from basis import nspins, ldim_p, ldim_s

na = tensor(create(ldim_p)*destroy(ldim_p), qeye(ldim_s))
sz = tensor(qeye(ldim_p), sigmaz())

#setup inital state and calculate Liouvillian
for x in gam_up:
    L = setup_laser(g, delta, kappa, gam_dn, x, 0,4)
    #print("setup L")

#operators to calculate expectation values for
    ss = steady(L)

    #print("steady state")
    
    expects = expect_comp([ss], [na,sz])
    na_expect = expects[0][0]
    sz_expect = expects[1][0]

    #print(na_expect)
    #print(sz_expect)
    
    na_values.append(na_expect)
    sz_values.append(sz_expect)
    
figure(1)
plot(gam_up, na_values)
plt.xlabel('Gamma up (Pumping)')
plt.ylabel('a a†/N')


figure(2)
plot(gam_up, sz_values)
plt.xlabel('Gamma up (Pumping)')
plt.ylabel('Sigma Z')


#system size
ntls = 4

nphot = 10

#define parameters
omega=0.0
omega0=0.0
g=0.5

gam_dn =1
gam_up = linspace(0, 2.5, 50)
kappa = 0.1

g=g/sqrt(ntls)
delta = omega-omega0

#time evolution
tmax = 10
dt = 0.1

nphot0 = 0

na_values = []
sz_values = []

# setup basis with ntls spin, each of Hilbert space dimentsion
# 2 and photon with dimension nphot
setup_basis(ntls, 2, nphot)

#run other setup routines
list_equivalent_elements()
setup_convert_rho()
from basis import nspins, ldim_p, ldim_s

na = tensor(create(ldim_p)*destroy(ldim_p), qeye(ldim_s))
sz = tensor(qeye(ldim_p), sigmaz())

#setup inital state and calculate Liouvillian
for x in gam_up:
    L = setup_laser(g, delta, kappa, gam_dn, x, 0,4)
    #print("setup L")

#operators to calculate expectation values for
    ss = steady(L)

    #print("steady state")
    
    expects = expect_comp([ss], [na,sz])
    na_expect = expects[0][0]
    sz_expect = expects[1][0]

    #print(na_expect)
    #print(sz_expect)
    
    na_values.append(na_expect)
    sz_values.append(sz_expect)
    
figure(1)
plot(gam_up, na_values)
plt.xlabel('Gamma up (Pumping)')
plt.ylabel('a a†/N')

figure(2)
plot(gam_up, sz_values)
plt.xlabel('Gamma up (Pumping)')
plt.ylabel('Sigma Z')

#system size
ntls = 6
nphot = 10

#define parameters
omega=0.0
omega0=0.0
g=0.5

gam_dn =1
gam_up = linspace(0, 2.5, 50)
kappa = 0.1

g=g/sqrt(ntls)
delta = omega-omega0

#time evolution
tmax = 10
dt = 0.1

nphot0 = 0

na_values = []
sz_values = []

# setup basis with ntls spin, each of Hilbert space dimentsion
# 2 and photon with dimension nphot
setup_basis(ntls, 2, nphot)

#run other setup routines
list_equivalent_elements()
setup_convert_rho()
from basis import nspins, ldim_p, ldim_s

na = tensor(create(ldim_p)*destroy(ldim_p), qeye(ldim_s))
sz = tensor(qeye(ldim_p), sigmaz())

#setup inital state and calculate Liouvillian
for x in gam_up:
    L = setup_laser(g, delta, kappa, gam_dn, x, 0,4)
    #print("setup L")

#operators to calculate expectation values for
    ss = steady(L)

    #print("steady state")
    
    expects = expect_comp([ss], [na,sz])
    na_expect = expects[0][0]
    sz_expect = expects[1][0]

    #print(na_expect)
    #print(sz_expect)
    
    na_values.append(na_expect)
    sz_values.append(sz_expect)
    
figure(1)
plot(gam_up, na_values)
plt.xlabel('Gamma up (Pumping)')
plt.ylabel('a a†/N')

figure(2)
plot(gam_up, sz_values)
plt.xlabel('Gamma up (Pumping)')
plt.ylabel('Sigma Z')
    