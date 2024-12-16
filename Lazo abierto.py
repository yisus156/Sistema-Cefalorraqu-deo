import numpy 
import matplotlib.pyplot as plt 
import control
import math

x0,t0,tF,dt = 0,0,15,1E-3
N = round ((tF-t0)/dt)+1
t = numpy.linspace(t0,tF,N)
u= numpy.sin(1.5708*t) #Funcion senosoidal

#Funcion de control
 
Re= 2 #ohms
Lw= 0.01 #Henrios
Cs= 0.05 #Faradios
Rp= 1    #ohms
Cw=0.5   
Cl=0.5

a3=Cw*Cs*Lw*Rp*Cl
a2=Cw*Cs*Lw+Cw*Lw*Cl+Cs*Lw*Cl+Cw*Cs*Re*Rp*Cl
a1=Cw*Cs*Re+Cw*Re*Cl+Cs*Re*Cl+Cw*Rp*Cl
a0=Cw+Cl

num = [a0]
den = [a3,a2,a1,a0]
sys = control.tf(num,den) #Funcion de Transferencia del Control
print("control")
print(sys)

#Funcion de transferencia control

Rp=8.5
Cw=1

a3=Cw*Cs*Lw*Rp*Cl
a2=Cw*Cs*Lw+Cw*Lw*Cl+Cs*Lw*Cl+Cw*Cs*Re*Rp*Cl
a1=Cw*Cs*Re+Cw*Re*Cl+Cs*Re*Cl+Cw*Rp*Cl
a0=Cw+Cl

num= [a0]
den = [a3,a2,a1,a0]
sysE = control.tf(num,den) #Funcion de Transferencia del Control
print("caso")
print(sysE)

#Sistema normal

fig1=plt.figure()
plt.plot(t,u, '-',color=[0.93,0.69,0.13], label='$Pe(t)$')                      #Voltaje de entrada
ts,Vs=control.forced_response(sys,t,u,x0)
plt.plot(t,Vs, '-',color=[0,0.25,0.43], label=r'$Pa(t): Control$')               #Sano
ts,Ve=control.forced_response(sysE,t,u,x0)
plt.plot(t, Ve,'-', color=[0.64,0.08,0.18], label=r'$Pa(t): Caso$')             #enfermo
#ts,pid=control.forced_response(sysPID,t,Vs,x0)
#plt.plot(t, pid,':', linewidth=3, color=[0.47,0.67,0.19], label=r'$PA(t): Tratamiento$')
plt.grid(True)
plt.xlim(-0.5,15)
plt.ylim(-1.3,1.3)
plt.xlabel("$t$ [segundos]")
plt.ylabel("$V(t)$ [Volts]")
plt.title("Sistema cefalorraquideo - Lazo abierto")
plt.legend(loc="lower right")
plt.legend(bbox_to_anchor=(0.5,-0.23), loc='center', ncol=4)
plt.show()
fig1.set_size_inches(10,4)
fig1.savefig('sys.png', dpi=600, bbox_inches='tight')
fig1.savefig('sys.pdf', dpi=600, bbox_inches='tight')
