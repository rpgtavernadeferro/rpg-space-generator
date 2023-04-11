from ast import Match
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
while contador_geral <5:
    contador_geral +=1

    # criando listas gerais
    x = []
    y = []
    xy = []
    sz = []
    rgb = []
    texto = []
    angulo=[]

    # define quantidade gerada
    match contador_geral:
        case 1: qd = rdi(5,10) # planetas
        case 2: qd = rdi(100,200) # estrelas
        case 3: qd = rdi(3,6) # naves
        case 4: qd = rdi(3,3) # Assinatura energética, possíveis conflitos   
        case 5: qd = rdi(1,3) # Assinatura energética, possíveis conflitos   
        
    for zero in range(qd):
        x_temp = rdu(1,6)
        y_temp = rdu(0,359)       
        texto_temp = rdpalavra()         
        
        match contador_geral:
            
            case 1: # planetas
                sz_temp = rdu(9,27)
                variação_cor = rdi(31,41)
                rgb1 = (7-x_temp) * variação_cor
                rgb3 = (x_temp * variação_cor)
                rgb_temp = 'rgb('+ str(rgb1) + ',0,' + str(rgb3) + ')'
                tipo_temp = 'Planeta '
                temperatura_temp = f'{(rgb1 - rgb3) :_.2f}' 
                if rdi(1,10)>9: texto_temp = '????' 
                texto.append(tipo_temp + texto_temp + '</br></br>Tméd ' + str(temperatura_temp) + '°C')
                symbols ='circle' 
                
            case 2: # estrelas
                sz_temp = rdu(2,2)
                rgb_temp = 'rgb(255,255,255)'
                tipo_temp = ''
                symbols ='circle'   
                             
            case 3: # naves
                sz_temp = rdu(12,12)
                rgb_temp = 'rgb(0,'+ str(rdi(100,255)) +',0)'   
                tipo_temp = 'Nave '
                classe_temp = rdi(1,12)
                if rdi(1,10)>5: texto_temp = '????' 
                texto.append(tipo_temp + texto_temp + ' (T' + str(classe_temp) + ')')
                symbols ='arrow' 
                
            case 4: # Assinatura energética
                sz_temp = rdu(8,8)
                rgb_temp = 'rgb('+ str(rdi(50,255)) + ',0,0)'   
                tipo_temp = 'Assinatura energética '
                texto.append(tipo_temp + str(zero+1))
                symbols ='hexagram'

            case 5: # Buraco Negro
                sz_temp = rdu(8,8)
                rgb_temp = 'white'   
                tipo_temp = 'Buraco Negro '
                texto.append(tipo_temp + str(zero+1))
                symbols ='star-square'



                                
        angulo.append(rdu(0,359))
        x.append(x_temp)
        y.append(y_temp)
        xy +=[(x_temp+y_temp)]
        rgb.append(rgb_temp)
        sz.append(sz_temp)        
            
        fig.add_trace(go.Scatterpolar(
            r = x,
            theta = y,
            text = texto,
            hoverinfo = 'text',
            name ='',
            mode = 'markers',
            marker=dict(size=sz, color = rgb, symbol=symbols, line=dict(width=0),angle=angulo)
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