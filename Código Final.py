from numpy import linspace
from scipy.integrate import odeint
import math
import matplotlib.pyplot as plt

entre_eixos = 2.5
dt = 2
dd = 0.5

m = 1600
mt = m * (dd / entre_eixos)
md = m * (dt / entre_eixos)

g = 10
pt = mt * g
pd = md * g

mie = 1.0
mic = 0.8

fatdemax = pd * mie
fattemax = pt * mie

fatdc = pd * mic
fattc = pt * mic

I = ((mt * md) / (mt + md)) * (entre_eixos ** 2)

angulo_ideal = (2 * math.pi) * (1/4) * (5/6)

def func(Y, t):
    W = Y[0]
    A = Y[1]
    fd = ((m * velocidade ** 2) / raio) * (dt / (dt + dd))
    ft = fd * dd / dt
    if ft > fattemax:
        if A < angulo_ideal:
            fd = (m * velocidade ** 2) / raio - fattc
            dwdt = ((fd * dd) - (fattc * dt)) / I
            dadt = W
        else:
            dwdt = 0
            dadt = 0
    else:
        dwdt = 0
        dadt = W
    return dwdt, dadt
    
velocidade = 10.5
raio = 11

t = linspace(0, 2, 20001)
A0 = 0
W0 = 0
Y = [W0, A0]

angulos = odeint(func, Y, t)

plt.plot(t, angulos[:,1],'g')
plt.ylabel('Angulação (radianos)')
plt.xlabel('Tempo (segundos)')
plt.title(r'Angulação do carro em relação à tangente em função do tempo')
plt.show()
    
velocidade = 5
raio = 10

t = linspace(0, 2, 20001)
A0 = 0
W0 = 0
Y = [W0, A0]

angulos = odeint(func, Y, t)

plt.plot(t, angulos[:,1],'g')
plt.ylabel('Angulação (radianos)')
plt.xlabel('Tempo (segundos)')
plt.title(r'Angulação do carro em relação à tangente em função do tempo')
plt.show()

t = linspace(0, 2, 20001)
A0 = 0
W0 = 0
Y = [W0, A0]

velocidade = 5
raio = 11

angulos_1 = odeint(func, Y, t)

velocidade = 10
raio = 11

angulos_2 = odeint(func, Y, t)

velocidade = 10.5
raio = 11

angulos_3 = odeint(func, Y, t)

velocidade = 15
raio = 11

angulos_4 = odeint(func, Y, t)

velocidade = 20
raio = 11

angulos_5 = odeint(func, Y, t)

velocidade = 25
raio = 11

angulos_6 = odeint(func, Y, t)



plt.plot(t, angulos_1[:,1],'g')
plt.plot(t, angulos_2[:,1],'r')
plt.plot(t, angulos_3[:,1],'b')
plt.plot(t, angulos_4[:,1],'orange')
plt.plot(t, angulos_5[:,1],'yellow')
plt.plot(t, angulos_6[:,1],'grey')
plt.axis([0, 2, - 0.2, (max(angulos_6[:,1]) + 0.2)])
plt.ylabel('Angulação (radianos)')
plt.xlabel('Tempo (segundos)')
plt.title(r'Angulação do carro em relação em função do tempo')
plt.show()



lista_raios = linspace(1, 25, 250)
lista_velocidades = linspace(1, 50, 2000)
lista_velocidades_necessarias = []
lista_raio_ideal = []

#t = linspace(0, 20, 2001)


for raio in lista_raios:
    distancia_percorrida = raio * math.pi * 2 / 8
    for velocidade in lista_velocidades:
        A0 = 0
        W0 = 0
        Y = [W0, A0]
        tempo = distancia_percorrida / velocidade
        t = linspace(1, tempo, tempo * 100 + 0.2)
        angulos = odeint(func, Y, t)
        if max(angulos[:,1]) >= angulo_ideal:
            lista_velocidades_necessarias.append(velocidade)
            lista_raio_ideal.append(raio)
            break
        else:
            continue

plt.plot(lista_raio_ideal, lista_velocidades_necessarias,'g')
plt.ylabel('Velocidade ideal (metros por segundo)')
plt.xlabel('Raio da curva (metros)')
plt.title(r'Velocidade ideal para executar um drift natural em função do raio da curva')
plt.show()