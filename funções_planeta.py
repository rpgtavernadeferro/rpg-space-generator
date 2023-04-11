import asyncio
import random
from funções import *

def rd_nivel_tecnologico():
    n=[]
    texto ='' 
    lista_energia = txtlist('planetas.xls',5)
    energia1 =rdlistcls(lista_energia,0,0,1)
    nt_maximo =  partpos(energia1,',')
    nt_minimo = int(nt_maximo) -2
    if nt_minimo < 0:
       nt_minimo = 0 
    sem_nt = partant(energia1,',')  
    energia = sem_nt
    posição_energia = txtlist('planetas.xls',5).index(energia)+1
    n.append(posição_energia)
    energia = energia.split(';')
    energia = rdlistcls(energia)
    texto += '\nEnergia: '+energia.lower()
    #
    lista_transporte = txtlist('planetas.xls',3)
    transporte =rdlistcls(lista_transporte,int(nt_minimo),int(nt_maximo))
    posição_transporte = txtlist('planetas.xls',3).index(transporte)+1
    n.append(posição_transporte)
    transporte = transporte.split(';')
    transporte = rdlistcls(transporte)    
    texto += '\nTransporte: '+transporte.lower()
    #
    lista_combate = txtlist('planetas.xls',4)
    combate =rdlistcls(lista_combate,int(nt_minimo),int(nt_maximo))
    posição_combate = txtlist('planetas.xls',4).index(combate)+1
    n.append(posição_combate)
    combate = combate.split(';')
    combate = rdlistcls(combate)  
    texto += '\nCombate: '+combate.lower()
    #
    lista_biotecnologia = txtlist('planetas.xls',6)
    biotecnologia =rdlistcls(lista_biotecnologia,int(nt_minimo),int(nt_maximo))
    posição_biotecnologia = txtlist('planetas.xls',6).index(biotecnologia)+1
    n.append(posição_biotecnologia)
    biotecnologia = biotecnologia.split(';')
    biotecnologia = rdlistcls(biotecnologia) 
    texto += '\nBiotecnologia: '+biotecnologia.lower()
    #
    ntm = str(int((posição_transporte + posição_combate + posição_energia + posição_biotecnologia)/4))
    texto = 'Nível Tecnologico Médio: '+ntm + ' ['+ str(min(n, key=int)) + '-' + str(max(n, key=int)) +']'+texto 
    return texto

def rd_governo():
    n=[]
    texto =''
    lista_governo = txtlist('planetas.xls',2)
    governo = rdlistcls(lista_governo)
    posição_governo = txtlist('planetas.xls',2).index(governo)+1
    n.append(posição_governo)
    texto += '\nGoverno: ' + governo.lower()
    return texto

def rd_elementos(tmin=0,tmed=20,tmax=30):
    n=[]
    n1 =[]
    texto=''
    virgula=''
    lista_elementos = txtlist('planetas.xls',1)
    lista_elementos_basicos = txtlist('planetas.xls',7)
    porcentagem_total=0    
    while porcentagem_total !=100:
        porcentagem = random.randint(1,100-porcentagem_total) 
        porcentagem_total += porcentagem
        aleatorio = random.randint(1,50) 
        if (aleatorio<=20) or (lista_elementos_basicos ==''):       
            elementos = rdlistcls(lista_elementos)
        elif aleatorio==50:
            elementos = 'Desconhecido(?).'+str(random.randint(-299,6000))
        else:      
            elementos = rdlistcls(lista_elementos_basicos)
        temperatura_elemento = int(partpos(elementos,'.'))        
        anexo=''
        if tmin >= temperatura_elemento: anexo = '(gasoso)'
        else:
            if tmed >= temperatura_elemento: anexo = f'(gasoso a partir {temperatura_elemento}C)'
            if tmax >= temperatura_elemento: anexo = f'(gasoso a partir {temperatura_elemento}C)'
        elementos = partant(elementos,'.')
        if texto!='': virgula=', '       
        texto += virgula + str(porcentagem) + '% ' + elementos.lower()+anexo 
    texto = ('\nElementos: ' + texto)
    return texto

def rd_temperatura():
    if random.randint(1,10)==10:
        a = -250
        b = 1333
    else:
        a = -100
        b = 100
    tmin = random.randint(a ,b)
    tmed = tmin + random.randint(0,b)
    tmax = tmed + random.randint(0,b)
    lista=[]
    lista.append(tmin)
    lista.append(tmed)
    lista.append(tmax)
    return lista

def rd_hidrografia(lista_elementos):
    a = 'oxigênio'
    b = 'hidrogênio'
    e =0
    if (lista_elementos.count(a)>0) and (lista_elementos.count(b)>0):
        lista=lista_elementos.split(',')    
        tamanho_lista = len(lista)
        contador = -1
        c = 0
        d =0
        for i in range(tamanho_lista):
            contador +=1
            if lista[contador].count(a) ==1:
                c = int(ext_n(lista[contador]))
            if lista[contador].count(b) ==1:
                d = int(ext_n(lista[contador]))        
        if c>d: c=d
        if d>c*4: d=c
        e = (c+d)*2
        if e>100: e=99
    return e

def rd_habitantes(hidro=0, tecno=''):
    if tecno !='':
        tecno_int = int(partant(partpos(tecno,'Nível Tecnologico Médio: '),' ['))
    else:
        tecno_int =1
    if hidro ==0:
        if random.randint(0,4)<4: densidade = 0        
        else: densidade = random.randint (0,1*tecno_int)
    else:
        densidade = random.randint (0,hidro*tecno_int)
    return densidade

def rd_conflitos(densidade=1):
    if densidade >0:
        return rdlistcls(txtlist('planetas.xls',8))
    else: return ''

def rdpalavra(x=5,y=1,z=3,w=1):
	#retorna palavra aleatoria, x minimo 3. y quantidade de palavras maxima, x tamanho maximo da palavra
	import random
	if x<z:
		x=z+1
	if y<w:
		y = w+1
	total = ''
	rangey = random.randint(w,y)
	contay = rangey
	if random.randint(1,3)<3:
		espaço = ' '
	else:
		espaço = '-'
	for i in range (rangey):
		contay -=1
		part = 0
		alist = ['a','e','i','o','u']
		clist=['b','c', 'd','f','g','h','j','l','m','n','p','q','v','x','z','k','y','w']
		cclist=['br','pr','qu','ch','ps','bl','tl','vr']
		ccclist=['sc','mb','ch','ps','nt','dv','rc','pn','rr','ss']
		flist =['m','s','z','r']
		palavra = ''
		rangex = random.randint(z,x)
		contar = rangex
		for i in range(rangex):
			a = random.randint(1,3)
			contar -= 1
			if contar ==0 and part == 2:
				palavra =palavra + random.choice(flist)
			else:			
				if a==1 and part==0:
					palavra += random.choice(alist).upper()
					part = 2
				elif a ==2 and part ==0:
					palavra += random.choice(clist).upper()
					part = 1
				elif a ==3 and part ==0:
					palavra += random.choice(cclist).title()
					part = 1
				elif a ==1 and part ==2:
					palavra += random.choice(clist)
					part = 1
				elif a==2 and part ==2:
					palavra += random.choice(cclist)
					part = 1
				elif a ==3 and part ==2:
					palavra += random.choice(ccclist)
					part = 1
				elif part ==1:
					palavra += random.choice(alist)
					part = 2
		if contay ==0:
			palavra = palavra
		else:
			palavra = palavra + espaço
		total = total + palavra
	return total






    



def rd_planeta(tipo=0, planeta_anterior='',tamanho_anterior=0):
    temperatura_lista =rd_temperatura()    
    elementos = rd_elementos(temperatura_lista[0],temperatura_lista[1],temperatura_lista[2])
    hidro = rd_hidrografia(elementos)
    tecno ='\n'+rd_nivel_tecnologico() 
    habit = rd_habitantes(hidro,tecno) 
    if (habit <1) and random.randint(1,20)==1: nome_a = '???'
    else: nome_a = rdpalavra(5,2,3)
    if tipo==0:
        nome = 'Planeta: '+nome_a
    else: nome = 'Lua: '+nome_a + ' do planeta ' + planeta_anterior
    
    if (random.randint(1,10)==1) and (habit>0):
        extinção = ' (extinta)'
    else: extinção = ''
    habitantes = '\nHabitantes: '+str(habit) + ' habitantes/km²' +extinção 
    governo = rd_governo() 
    conflito = '\nÚltimos Acontecimentos: '+rd_conflitos(habit)    
    if habit ==0:
        tecno =''
        governo =''
        conflito =''
    if tamanho_anterior ==0:
        t = random.randint(4500,260000)
    else:
        t = random.randint(int(tamanho_anterior/10),int(tamanho_anterior/2))
    tam = f'{t:_}'
    tam = tam.replace('.',',').replace('_','.')
    tamanho = '\nTamanho: '+str(tam)+'km de diâmetro'
    
    if tipo == 0:
        if random.randint(1,4)>1: di = random.randint(50000000,100000000)
        else: di = random.randint(50000000,5000000000)
        dis = f'{di:_}'
        dis = dis.replace('.',',').replace('_','.')
        lu = int((di/299800)/60)
        luz = f'{lu:_}'
        luz = luz.replace('.',',').replace('_','.')
        distancia = '\nDistância para o Sol: '+str(dis)+'km, ' + str(luz) + ' minutos-luz'
    else:
        di = random.randint(20,300)
        distancia = '\nDistância para o Planeta: '+str(di)+'km'
    if random.randint(1,3)>1: g = random.uniform(0,2)
    else: g = random.uniform(0,10)
    gra = (f'{g:.2f}').replace('.',',')
    gravidade = f'\nGravidade: {gra}G'
    hidrografia = '\nHidrografia: ' + str(hidro) + '%'
    txt_teperatura = '\nTemperatura: ' +  str(temperatura_lista[0]) + '°C/ '+ str(temperatura_lista[1]) + '°C/ '+ str(temperatura_lista[2])+'°C'  
    texto = nome+ habitantes + tecno + governo + elementos + txt_teperatura + hidrografia +conflito+tamanho+gravidade+distancia
    return  texto

def rd_solar(qd_minima_planetas=8,qd_maxima_planetas=16):
    contador = 0
    acumulado =''
    for i in range(random.randint(qd_minima_planetas,qd_maxima_planetas)):
        contador +=1
        if contador ==1:
            planeta = rd_planeta()
            nome_planeta = (partpos(partant(planeta,'Habitantes'),': ')).replace("\n", "")
            tamanho_planeta = (partpos(partant(planeta,'km de di'),'Tamanho: ')).replace('.','')
            texto = planeta
            tipo = 0 #planeta
        if (contador >1):
            if random.randint(1,4)>1: tipo=0
            else: tipo=1 #lua
            if tipo == 1:
                texto = rd_planeta(1,nome_planeta,int(tamanho_planeta))
            else:
                planeta = rd_planeta()
                nome_planeta = (partpos(partant(planeta,'Habitantes'),': ')).replace("\n", "")
                tamanho_planeta = (partpos(partant(planeta,'km de di'),'Tamanho: ')).replace('.','')
                texto = planeta
                tipo = 0 #planeta                
        acumulado += texto + '\n'+ '\n'
    return acumulado

def rd_espaço(diretorio_imagem,extensão_imagem):
    pasta = './'+diretorio_imagem
    lista_imagem=[]
    texto_imagem=''
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            texto_imagem+= os.path.join(arquivo)
    lista_imagem=texto_imagem.split('.'+extensão_imagem) 
    lista_imagem.pop()  
    texto_imagem = diretorio_imagem+'/'+rdlistcls(lista_imagem)+'.'+extensão_imagem
    with open(texto_imagem, 'rb') as f:
        picture = discord.File(f)
    return picture

