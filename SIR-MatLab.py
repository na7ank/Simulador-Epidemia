'''
    Exemplo de implementação do modelo S.I.R
    (S) --> (I) --> (R)

    Por: NATAN
'''

import numpy as np                 # Arrays
import matplotlib.pyplot as graph  # Módulo para plotar os gráficos
from scipy.integrate import odeint # Integrar as diferenciais


N  = 50000          # População, N
I0 = 1              # Número de infectados inicialmente
R0 = 0              # Número de recuperados inicialmente
S0 = N - I0 - R0    # Número de indivíduos suscetíveis
D  = 200            # Dias totais
MS = 10000          # Máximo de Pessoas que o sistema de saúde comporta
beta = 0.2          # Taxa de contato
gamma = 0.05        # Taxa de Recuperação
y0 = S0, I0, R0     # Condições iniciais


t = np.array(range(0, D))   # Array com os dias 0 a D (Eixo X)
M = np.array(D*[MS])        # Máx. Sistema de saúde comporta

# Sistema de equações diferenciais do modelo
def dif_SIR(y, t, N, beta, gamma):
    '''
        Equações diferenciais (EDO) do SIR
    '''
    S, I, R = y # Tripla de Funções dependentes de t
    dS_sobre_dt = -beta * (I/N) * S                 # dS(t)/dt
    dI_sobre_dt =  beta * (I/N) * S  - (gamma * I)  # dI(t)/dt
    dR_sobre_dt =  gamma * I                        # dR(t)/dt
    
    return dS_sobre_dt, dI_sobre_dt, dR_sobre_dt



# Resolve as diferenciais para cada valor de D
integral = odeint(dif_SIR, y0, t, args=(N, beta, gamma))
S, I, R = integral.T # S(t) , I(t), R(t)




# Plotando as Linhas
G = graph.figure(facecolor='w')
ax = G.add_subplot(111, facecolor='lightgray', axisbelow=True)
ax.plot(t, S, 'b', lw = 2, label = 'Suscetível (S)')
ax.plot(t, I, 'r', lw = 2, label = 'Infectado (I)')
ax.plot(t, R, 'g', lw = 2, label = 'Recuperado (R)')
ax.plot(t, M, 'black', lw = 2, ls='--' ,label = 'Sistema de Saúde')
legend = ax.legend()

ax.set_xlabel('Dias')
ax.set_ylabel('N.Pessoas')
ax.grid(b=True, which='major', c='gray', lw=1, ls='-')
 
graph.show()
