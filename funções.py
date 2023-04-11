import names
import random # random.randint
import datetime
from python_random_strings import random_strings # random_strings
import xlrd
from fpdf import FPDF # pdfs
import pandas as pd
from pathlib import Path
import string
from deep_translator import GoogleTranslator
import discord
import asyncio
import random
import re
import heapq
import numpy as np
import os





from PIL import Image
import matplotlib.pyplot as plt


def ext_n(texto):
    #extrai numeros de um texto
    return re.sub('[^0-9]', '', texto)

def partpos(texto,caracter,posição=1):
    #parte do texto após o caracter
    if (texto.count(caracter)>0) and (caracter !=''):       
        texto_cortado = texto.split(caracter)[posição]
    else: texto_cortado = texto
    return texto_cortado

def partant(texto,caracter,posição=0):
    #parte do texto antes do caracter
    if (texto.count(caracter)>0) and (caracter !=''):       
        texto_cortado = texto.split(caracter)[posição]
    else: texto_cortado = texto
    return texto_cortado

def gerar_txtnum(x,y):
    gerado = ''
    if x>y: x=y
    for i in range(random.randint(x,y)):
        a = random.randint(1,2)
        if a ==1: gerado += random_strings.random_lowercase(1)
        else: gerado += str(random_strings.random_digits(1))
    return gerado

def rdline(x,index_da_aba=0):
# random line for .txt, or xls
# from daniel_funcoes import rdline
	if partpos(x,'.') == 'txt':
		z = random.choice(open(x).read().splitlines())
	elif partpos(x,'.') == 'xls':
		y = xlrd.open_workbook(x).sheet_by_index(index_da_aba)
		w = random.randint (0,y.nrows-1)
		z = y.cell_value(w, 0)
	return z

def txtlist(x,index_da_aba=0):
# .txt (line) to list, or xls	
	if partpos(x,'.') == 'txt':
		y = Path(x).read_text().splitlines()
	elif partpos(x,'.') == 'xls':
		from xlrd import open_workbook
		book = open_workbook(x)
		sheet = book.sheet_by_index(index_da_aba)
		list = []
		for row in range(0,sheet.nrows):
			# Remove str(...) if you want the values as floats.
			list.append(str(sheet.cell(row,0).value))  # Changed this line
	return list

def rdlistcls(x,e=0,m=0,f=0):
# random element for list(x), and remove element
    if m == 0: y = len(x)-1
    else: y = m
    if e==0: minimo = 0
    else: minimo = e
    w = random.randint(minimo,y)
    z = x[w]
    x.remove(z)
    if f == 0: numero_na_lista = ''
    else: numero_na_lista = ',' + str(w)
    return z + numero_na_lista

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def verifica(texto, palavrasProibidas):
    for palavra in palavrasProibidas:
        if palavra.lower() in texto.lower():
            return False
    return True

def verificainverso(texto, palavrasProibidas):
    for palavra in palavrasProibidas:
        if palavra.lower() in texto.lower():
            return True
    return False

def rdpalavra (x=5,y=1,z=3,w=1):
	#retorna palavra aleatoria, x minimo 3. y quantidade de palavras maxima, x tamanho maximo da palavra
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

#em criação rolador de dados
def rpgdado(x=6,y=1):
	resultados=[]
	for i in range(y):
		resultados.append(random.randint(1,x))
	return resultados
#print (rpgdado(10,8))

def ex_minutos(variavel=60):
#extrai minutos de uma variavel
    b = variavel
    return int(b.total_seconds()/60)



def dado_octa(x):
    if x == 1:
        return 'd4'
    elif x == 2:
        return 'd6'
    elif x == 3:
        return 'd8'
    elif x == 4:
        return 'd8'
    elif x == 5:
        return 'd10'
    elif x == 6:
        return 'd12'
    elif x == 7:
        return 'd12'
    elif x > 7:
        return 'd20'


#tradutor
def traduzir(texto,de='pt',para='en'):
    tradução = GoogleTranslator(source=de,target=para).translate(texto)
    return tradução




# GERAR O PDF
def var_pdf(variavel='',arquivo='teste.pdf'):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', '', 9) # 'B' negrito, I italico, U anderline
    #pdf.cell(40, 10, npc_gerado)
    pdf.multi_cell(h=5.0, align='L', w=0, txt=variavel, border=0)
    pdf.output(arquivo, 'F')



