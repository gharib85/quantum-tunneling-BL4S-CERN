import matplotlib.pyplot as plt
import numpy as np
from math import *
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')



a = int(input("render level "))
l = float(input("lenght = "))
r = float(input("size of potential barrer = "))
V_o = float(input("V_o = "))
n = int(input("n = "))
h = 6.62607015
h_bar = h/(2*np.pi)
m = 9.1093837015
E = ((n**2)*(h**2))/(8*m*l**2)
print("the total energy of the particle is ", E)
q = 5.2
alpha = (np.sqrt(2*m*(V_o-E)))/h_bar
print("alpha ", alpha)


def delta(x):
    s = np.exp(-alpha*x)/((2*np.sin(((n*np.pi)/l)*x))**2)
    return(s)

print("q d exp ", np.exp(-alpha*q), "q d sin^2 ", ((2*np.sin(((n*np.pi)/l)*q))**2))
print("q+r d exp ", np.exp(-alpha*(q+r)), "q+r d sin^2 ", ((2*np.sin((n*np.pi/l)*(q+r)))**2))

print("delta q ", delta(q))
print("delta q+r ", delta(q+r))

Constant = np.sqrt((1/((delta(q))*(q - (l/(2*n*np.pi)) * (np.sin(((2*n*np.pi)/l) * q))) - ((1/(2*alpha)) * ((np.exp(-2*alpha*q))) * ((np.exp(-2*alpha*r)) + 1)) + ((delta(q+r))*(l - (q+r) - (l/(2*n*np.pi)) * (np.sin(((2*n*np.pi)/l) * (q+r))) )) ) ))

A = 2*Constant*(delta(q))
B = Constant
C = 2*Constant*(delta(q+r))

c = np.sqrt(1/(delta(q)*(q-(l/(2*n*np.pi)*np.sin((2*n*np.pi/l)*q))) - (1/(2*alpha))*((e**(-alpha*q))*((e**(-alpha*r))+1)) + delta(q+r)*(l-q+r-(l/(2*n*np.pi))*np.sin((2*np.pi/l)*(q+r)))))



xa = np.linspace(0, q, a)
xb = np.linspace(q, q+r, a)
xc = np.linspace(q+r, l, a)

t = np.linspace(0, 40, a)

x_a, t_ = np.meshgrid(xa, t)
x_b, t_ = np.meshgrid(xb, t)
x_c, t_ = np.meshgrid(xc, t)

def aR(x,t):
    s = np.cos(-(E/h_bar)*t)*(A*np.sin((n*np.pi/l)*x))
    return(s)

def aC(x,t):
    s = np.sin(-(E/h_bar)*t)*(A*np.sin((n*np.pi/l)*x))
    return(s)

def aP(x):
    s = (A*np.sin((n*np.pi/l)*x))**2
    return(s)


def bR(x,t):
    s = np.cos(-(E/h_bar)*t)*B*e**(-alpha*x)
    return(s)

def bC(x,t):
    s = np.sin(-(E/h_bar)*t)*B*e**(-alpha*x)
    return(s)

def bP(x):
    s = (B*e**(-alpha*x))**2
    return(s)


def cR(x,t):
    s = np.cos(-(E/h_bar)*t)*(C*np.sin((n*np.pi/l)*x))
    return(s)

def cC(x,t):
    s = np.sin(-(E/h_bar)*t)*(C*np.sin((n*np.pi/l)*x))
    return(s)

def cP(x):
    s = (C*np.sin((n*np.pi/l)*x))**2
    return(s)

ZaR = aR(x_a,t_)
ZaC = aC(x_a,t_)

ZbR = bR(x_b,t_)
ZbC = bC(x_b,t_)

ZcR = cR(x_c,t_)
ZcC = cC(x_c,t_)

ax.plot_surface(x_a, t_, ZaR, cmap = cm.plasma, linewidth=0, antialiased=True, color = 'blue')
ax.plot_surface(x_a, t_, ZaC, cmap = cm.plasma, linewidth=0, antialiased=True, color = 'green')

ax.plot_surface(x_b, t_, ZbR, cmap = cm.plasma, linewidth=0, antialiased=True, color = 'blue')
ax.plot_surface(x_b, t_, ZbC, cmap = cm.plasma, linewidth=0, antialiased=True, color = 'green')

ax.plot_surface(x_c, t_, ZcR, cmap = cm.plasma, linewidth=0, antialiased=True, color = 'blue')
ax.plot_surface(x_c, t_, ZaC, cmap = cm.plasma, linewidth=0, antialiased=True, color = 'green')

ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('value of the quantum wave')

ax.legend()

plt.show()


plt.plot(xa, aP(xa), color = 'red')
plt.plot(xb, bP(xb), color = 'red')
plt.plot(xc, cP(xc), color = 'red')

plt.show()
