from ast import Match
import plotly.graph_objects as go
import random as rd
from random import randint as rdi # inteiros
from random import uniform as rdu # fracionarios
from funções_planeta import *
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Nomenclaturas
    #qd = quantidade
    #pl =  planetas
    #sz = tamanho
    #temp = temporario

# ajustes inicias
contador_geral = 0

# nome do sistema solar
nome_sistema = 'Sistema Solar ' + rdpalavra()

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
sistema_solar_habitado ='n'
while contador_geral <8:
    contador_geral +=1
    contorno_simbolo = 0
    

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
        case 3:
            #verifica se é um sistema propicio a ter naves
            if sistema_solar_habitado == 's':
                qd = rdi(3,12) # naves
            else:
                qd = rdi(0,1)*rdi(0,1)*rdi(0,4) # naves
        case 4: qd = rdi(1,4)*rdi(0,1) # Assinatura energética, possíveis conflitos   
        case 5: qd = rdi(0,1)*rdi(0,1) # buraco negro  
        case 6: qd = rdi(0,2)*rdi(0,2) # Objeto desconhecido      
        case 7: qd = rdi(0,1)*rdi(0,1)*rdi(0,1) # Supernova
        case 8: qd = rdi(0,1)*rdi(0,1)*rdi(0,1) # Pulsar         
        
    for zero in range(qd):
        x_temp = rdu(1,4)
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
                tmed = int(float(f'{(rgb1 - rgb3) :_.2f}'))
                tmin = tmed - rdi(1,100)
                tmax = tmed + rdi(1,100)
                if rdi(1,10)>9: texto_temp = '????'
                elementos = rd_elementos(tmin,tmed,tmax)
                tecnologia = rd_nivel_tecnologico()
                hidrografia = rd_hidrografia(elementos)
                habitantes = rd_habitantes (hidrografia,tecnologia)                
                temperatura_texto = '<br><br>T ' + str(tmin) + ' | ' + str(tmed) + ' | ' + str(tmax) + ' °C'
                elemento_texto = '<br>' + divisor_text(elementos,30)
                if hidrografia > 0:
                    hidrografia_texto = '<br>Hidrografia: ' + str(hidrografia) + '%'
                else:
                    hidrografia_texto = ''                    
                if habitantes > 0:
                    tecnologia_texto = '<br>' + divisor_text(tecnologia,30)
                    habitantes_texto = '<br><br>Densidade: ' + str(habitantes) + ' hab/km²'
                    sistema_solar_habitado ='s'
                else:
                    tecnologia_texto = ''
                    habitantes_texto = ''
                texto.append(tipo_temp + texto_temp + temperatura_texto + elemento_texto + hidrografia_texto + habitantes_texto + tecnologia_texto)
                symbols ='circle'
                contorno_simbolo = 0.5
                    
            case 2: # estrelas
                sz_temp = rdu(2,2)
                rgb_temp = 'rgb(255,255,255)'
                tipo_temp = ''
                symbols ='circle'   
                             
            case 3: # naves
                sz_temp = rdu(12,12)
                rgb_temp = 'rgb(0,'+ str(rdi(50,255)) +',0)'   
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
                rgb_temp = 'black'   
                tipo_temp = 'Buraco Negro '
                texto.append(tipo_temp + str(zero+1))
                symbols ='star-square'
                contorno_simbolo = 1

            case 6: # Objeto desconhecido
                sz_temp = rdu(8,8)
                rgb_temp = 	'rgb(255,155,0)'   
                tipo_temp = 'Objeto Desconhecido '
                texto.append(tipo_temp + str(zero+1))
                symbols ='x'

            case 7: # Supernova
                sz_temp = rdu(10,10)
                rgb_temp = 	'lightskyblue'
                tipo_temp = 'Supernova '
                texto.append(tipo_temp + str(zero+1))
                symbols ='star-triangle-up'
                contorno_simbolo = 1

            case 8: # Pulsar
                sz_temp = rdu(10,10)
                rgb_temp = 	'lightskyblue'   
                tipo_temp = 'Pulsar '
                texto.append(tipo_temp + str(zero+1))
                symbols ='bowtie'
                contorno_simbolo = 1

                                            
        angulo.append(rdu(0,359))
        x.append(x_temp)
        y.append(y_temp)
        xy +=[(x_temp,y_temp)]
        rgb.append(rgb_temp)
        sz.append(sz_temp)
        
        # criando lua
        if rdi(1,10) > 7 and contador_geral == 1:
            angulo.append(rdu(0,359))
            x.append(x_temp+0.01)
            y.append(y_temp+0.01)
            xy +=[(x_temp+0.01,y_temp+0.01)]
            rgb.append('rgb(125,125,125)')
            sz.append(int(sz_temp/2))
            texto.append('Lua ' + rdpalavra() + ' do Planeta ' + texto_temp)     

        fig.add_trace(go.Scatterpolar(
            r = x,
            theta = y,
            text = texto,
            hoverinfo = 'text',
            name ='',
            mode = 'markers',
            marker=dict(size=sz, color = rgb, symbol=symbols, line=dict(width=contorno_simbolo),angle=angulo)
        ))            

#tema
cor_tema = 'rgb(204, 255, 51)'
cor_tema2 = 'black'
# mostra o grafico
fig.update_layout(title = nome_sistema,title_font =dict(color=cor_tema),
                  showlegend=False,
                  polar_bgcolor=cor_tema2 , paper_bgcolor=cor_tema2 , 
                  polar = dict(
        radialaxis = dict(color=cor_tema, angle=10, gridcolor=cor_tema, linecolor=cor_tema),
        angularaxis = dict(color=cor_tema, gridcolor=cor_tema)
    ),
    dragmode=False #remove zoom 
)

fig.show()

nome_do_arquivo = nome_sistema + '.html'
fig.write_html('sistema_solar/'+nome_do_arquivo)