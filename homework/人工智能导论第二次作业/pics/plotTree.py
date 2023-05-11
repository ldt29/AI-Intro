import matplotlib.pyplot as plt
import numpy as np

rho1=np.arange(0.4,0.6,0.001)
eta1=0.1*np.ones(len(rho1))
eta2 =np.arange(0.1,1,0.001) 
rho2 = 0.4*np.ones(len(eta2))
rho3 = np.arange(0.6,1,0.001)
eta3 = 0.2*np.ones(len(rho3))
eta4 = np.arange(0.1,0.2,0.001)
rho4 = 0.6*np.ones(len(eta4))

plt.figure(1)
plt.plot(rho1,eta1)
plt.plot(rho2,eta2)
plt.plot(rho3,eta3)
plt.plot(rho4,eta4)
plt.ylabel("eta")
plt.xlim((0,1))
plt.ylim((0,1))
plt.xlabel("rho")
plt.text(0.7, 0.7, 'good', ha='center', va='bottom', fontsize=10.5)
plt.text(0.2, 0.2, 'bad', ha='center', va='bottom', fontsize=10.5)
plt.show()

eta5 = np.arange(0,1,0.001)
rho5 = 0.4-0.05*eta5
eta6 = np.arange(0,1,0.001)
rho6 =0.44 + eta6

plt.figure(2)
plt.plot(rho5,eta5)
plt.plot(rho6,eta6)

plt.ylabel("eta")
plt.xlim((0,1))
plt.ylim((0,1))
plt.xlabel("rho")
plt.text(0.7, 0.7, 'good', ha='center', va='bottom', fontsize=10.5)
plt.text(0.2, 0.2, 'bad', ha='center', va='bottom', fontsize=10.5)
plt.show()
