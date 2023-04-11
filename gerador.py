import plotly.graph_objects as go
import random as rd
from random import randint as rdi
from funções_planeta import *

# Nomenclaturas
    #qd = quantidade
    #pl =  planetas
    #sz = tamanho

# quantidade minima e máxima de planetas
qd_pl_min = 5; qd_pl_max = 12

# quantidade aleatória de planetas
qd_pl = rdi(qd_pl_min,qd_pl_max)

#lista de coordenada de distância do ponto central
x =[]
#lista de coordenada de angulo 
y =[]
#lista de tamanhos dos planetas
sz_pl = []
# lista de cores de acordo com a distancia do sol
rgb =[]
# texto no planeta
texto_pl = []
# listas lua
x_lua =[]
y_lua =[]
rgb_lua =[]
nome_lua =[]
sz_lua =[]
texto_lua=[]




# cria posições aleatórias para cada planeta
for i in range(qd_pl):
    #sorteia coordenada
    x_temp = rd.uniform(1,6)
    y_temp = rd.uniform(0,359)
    # cria um padrão rgb, baseado em azul e vermelho
    variação_cor = rdi(31,41)
        #variação de vermelho, quanto mais próximo do sol
    rgb1_temp = str((7-x_temp)*variação_cor)
        #variação de azul, quanto mais distante do sol
    rgb3_temp = str(x_temp*variação_cor)
        #composição final do rgb
    rgb_temp = 'rgb('+rgb1_temp+',0,'+rgb3_temp+')'
    # variação de tamanho do planeta
    sz_pl_temp = rd.uniform(9,27)
    nome_pl_temp = rdpalavra()
    # acrescenta as informações as devidas listas
    x.append(x_temp)
    y.append(y_temp)
    rgb.append(rgb_temp)
    sz_pl.append(sz_pl_temp)
    texto_pl.append('Planeta ' + nome_pl_temp)
    
    #sorteia lua de 0 a 100    
    chance_de_ter_lua = 10
    if (chance_de_ter_lua/10) >= rdi(1,10):
        x_lua_temp = x_temp+0.01
        y_lua_temp = y_temp+0.01
        rgb_lua_temp = 'rgb(128,128,128)'
        nome_lua_temp = 'Lua '+rdpalavra() +' do Planeta '+nome_pl_temp
        sz_lua_temp = rd.uniform(sz_pl_temp/3,sz_pl_temp/2)        

        x_lua.append(x_lua_temp)
        y_lua.append(y_lua_temp)
        rgb_lua.append(rgb_lua_temp)
        sz_lua.append(sz_lua_temp)
        texto_lua.append(nome_lua_temp)        
        
        
        
         

# cria estrelas
x_estrela =[]
y_estrela=[]
for i in range(100):
    # acrescenta as informações as devidas listas
    x_estrela.append(rd.uniform(1,6))
    y_estrela.append(rd.uniform(0,359))

# gera o grafico
contador =0
fig = go.Figure(data=
    go.Scatterpolar(
        r = x,
        theta = y,
        text = texto_pl,
        hoverinfo = 'text',
        name ='',
        mode = 'markers',
        marker=dict(size=sz_pl, color = rgb)
    ))

# adicionar o sol
fig.add_trace(go.Scatterpolar(
        r = [0],
        theta = [0],        
        text = 'Sol',
        hoverinfo = 'text',
        name ='',
        mode = 'markers',
        marker=dict(size=50, color = 'rgb(255,215,0)')
    ))




# adicionar as luas
if x_lua !=['']:
    fig.add_trace(go.Scatterpolar(
            r = x_lua,
            theta = y_lua,  
            name ='',
            mode = 'markers',
            text=texto_lua,
            hoverinfo = 'text',
            marker=dict(size=sz_lua, color = rgb_lua)
        ))





# adicionar as estrelas
fig.add_trace(go.Scatterpolar(
        r = x_estrela,
        theta = y_estrela,  
        name ='',
        mode = 'markers',
        text='',
        hoverinfo = 'text',
        marker=dict(size=2, color = 'rgb(255,255,255)')
    ))






#tema
cor_tema = 'rgb(127, 255, 212)' #azul claro
# mostra o grafico
fig.update_layout(showlegend=False, polar_bgcolor='black', paper_bgcolor='black', 
                  polar = dict(
        radialaxis = dict(color=cor_tema, angle=10, gridcolor=cor_tema, linecolor=cor_tema),
        angularaxis = dict(color=cor_tema, gridcolor=cor_tema)
    )
                  
                  
                  
                  
                  
                  
                  
                  )
fig.show()