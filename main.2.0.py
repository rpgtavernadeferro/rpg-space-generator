import plotly.graph_objects as go
import random as rd
from random import randint as rdi # inteiros
from random import uniform as rdu # fracionarios
from funções_planeta import *
###
# Nomenclaturas
    #qd = quantidade
    #pl =  planetas
    #sz = tamanho
    #temp = temporario


# criando listas gerais
x = []
y = []
xy = []
sz = []
rgb = []
texto = []

# ajustes inicias
contador_geral = 0
contador_atual = 0

# Cria o Sol
fig = go.Figure(data=
    go.Scatterpolar(
        r = [0],
        theta = [0],        
        text = 'Sol',
        hoverinfo = 'text',
        name ='',
        mode = 'markers',
        marker=dict(size=50, color = 'rgb(255,215,0)')
    ))

#criação do grafico
while contador_geral <1:
    contador_geral +=1

    # define quantidade gerada
    Match contador_geral:
        case 1: qd = rdi(5,10) # planetas
        case 2: qd = rdi(100,200) # estrelas
        case 3: qd = rdi(5,10) # naves       

    for i in range(qd):
        x_temp = rdu(1,6)
        y_temp = rdu(0,359)
        sz_temp = rdu(9,27)
        
        if contador_geral == 1: #planetas
            variação_cor = rdi(31,41)
            rgb1 = str((7-x_temp)*variação_cor)
            rgb3 = str(x_temp*variação_cor)
            rgb_temp = 'rgb('+rgb1+',0,'+rgb3+')'
            tipo_temp = 'Planeta '
            
        texto_temp = rdpalavra()
        x.append(x_temp)
        y.append(y_temp)
        xy.append(x_temp+y_temp)
        rgb.append(rgb_temp)
        sz.append(sz_temp)
        texto.append(tipo_temp  + texto_temp)
        
    fig.add_trace(go.Scatterpolar(
        r = x,
        theta = y,
        text = texto,
        hoverinfo = 'text',
        name ='',
        mode = 'markers',
        marker=dict(size=sz, color = rgb)
    ))            
    
    










#tema
cor_tema = 'rgb(127, 255, 212)' #azul claro
cor_tema2 = 'black'
# mostra o grafico
fig.update_layout(showlegend=False, polar_bgcolor=cor_tema2 , paper_bgcolor=cor_tema2 , 
                  polar = dict(
        radialaxis = dict(color=cor_tema, angle=10, gridcolor=cor_tema, linecolor=cor_tema),
        angularaxis = dict(color=cor_tema, gridcolor=cor_tema)
    )
                  
                  
                  
                  
                  
                  
                  
                  )
fig.show()