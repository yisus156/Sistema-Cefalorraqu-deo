import numpy  
import matplotlib.pyplot as plt 
import control
import math

x0, t0, tF, dt = 0, 0, 15, 1E-3
N = round((tF - t0) / dt) + 1
t = numpy.linspace(t0, tF, N)
u = numpy.sin(1.5708 * t) # Funcion senoidal

# Funcion de caso
 
Re = 4 # ohms
Lw = 0.02 # Henrios
Cs = 0.10 # Faradios
Rp = 2    # ohms
Cw = 1   
Cl = 1

a3 = Cw * Cs * Lw * Rp * Cl
a2 = Cw * Cs * Lw + Cw * Lw * Cl + Cs * Lw * Cl + Cw * Cs * Re * Rp * Cl
a1 = Cw * Cs * Re + Cw * Re * Cl + Cs * Re * Cl + Cw * Rp * Cl
a0 = Cw + Cl

num = [a0]
den = [a3, a2, a1, a0]
sys = control.tf(num, den) # Funcion de Transferencia del caso
print("control")
print(sys)

# Funcion de transferencia caso

Rp = 8.5
Cw = 1

a3 = Cw * Cs * Lw * Rp * Cl
a2 = Cw * Cs * Lw + Cw * Lw * Cl + Cs * Lw * Cl + Cw * Cs * Re * Rp * Cl
a1 = Cw * Cs * Re + Cw * Re * Cl + Cs * Re * Cl + Cw * Rp * Cl
a0 = Cw + Cl

num = [a0]
den = [a3, a2, a1, a0]
sysE = control.tf(num, den) # Funcion de Transferencia del caso
print("caso")
print(sysE)

# Sistema enfermo

fig1 = plt.figure()
ts, Vs = control.forced_response(sys, t, u, x0)
plt.plot(t, Vs, '-', color=[0, 0.25, 0.43], label=r'$Pa(t): Control$')               # Sano
ts, Ve = control.forced_response(sysE, t, u, x0)
plt.plot(t, Ve, '-', color=[0.64, 0.08, 0.18], label=r'$Pa(t): Caso$')             # Enfermo

# Tratamiento sobre "Pa(t): Caso" como línea punteada
ts, Vt = control.forced_response(sysE, t, u, x0)
plt.plot(t, Vt, '--', linewidth=1.5, color='yellow', label=r'$Pa(t): Tratamiento$')

plt.grid(False)
plt.xlim(0, 15)
plt.ylim(-0.2, 0.3)
plt.xticks(numpy.arange(0, 16, 1)) # Configura los ticks de los segundos de 1 en 1
plt.xlabel("$t$ [segundos]")
plt.ylabel("$V(t)$ [Volts]")
plt.legend(loc="lower right")
plt.legend(bbox_to_anchor=(0.5, -0.23), loc='center', ncol=4)
plt.show()
fig1.set_size_inches(10, 4)
fig1.savefig('sys.png', dpi=600, bbox_inches='tight')
fig1.savefig('sys.pdf', dpi=600, bbox_inches='tight')
