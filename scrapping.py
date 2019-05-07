import requests
from bs4 import BeautifulSoup
import json
url = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"

r = requests.get(url)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find('table')

contenido = items.find_all('tr')

lista = []

contenido.pop(0)
contenido.pop(0)

def captura1(indice):
    info = contenido[indice]
    reg = {
       "nrc": info.find_all(class_='tddatos')[0].text,
       "clave": info.find_all(class_='tddatos')[1].text,
       "materia": info.find_all(class_='tddatos')[2].text,
       "seccion": info.find_all(class_='tddatos')[3].text,
       "creditos": info.find_all(class_='tddatos')[4].text,
       "cupos": info.find_all(class_='tddatos')[5].text,
       "disponible": info.find_all(class_='tddatos')[6].text,
       "hora": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[1].text,
       "dias": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[2].text,
       "edificio": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[3].text,
       "aula": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[4].text,
       "periodo": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[5].text,
       "maestro": info.find_all(class_='tddatos')[7].find_all(class_='tdprofesor')[1].text
            }
    lista.append(reg)

def captura2(indice):
    info = contenido[indice]
    reg = {
       "nrc": info.find_all(class_='tddatos')[0].text,
       "clave": info.find_all(class_='tddatos')[1].text,
       "materia": info.find_all(class_='tddatos')[2].text,
       "seccion": info.find_all(class_='tddatos')[3].text,
       "creditos": info.find_all(class_='tddatos')[4].text,
       "cupos": info.find_all(class_='tddatos')[5].text,
       "disponible": info.find_all(class_='tddatos')[6].text,
       "hora": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[1].text,
       "dias": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[2].text,
       "edificio": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[3].text,
       "aula": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[4].text,
       "periodo": info.find(align='center').find('table').find_all('tr')[0].find_all('td')[5].text,
       "hora2": info.find(align='center').find('table').find_all('tr')[1].find_all('td')[1].text,
       "dias2": info.find(align='center').find('table').find_all('tr')[1].find_all('td')[2].text,
       "edificio2": info.find(align='center').find('table').find_all('tr')[1].find_all('td')[3].text,
       "aula2": info.find(align='center').find('table').find_all('tr')[1].find_all('td')[4].text,
       "periodo2": info.find(align='center').find('table').find_all('tr')[1].find_all('td')[5].text,
       "maestro": info.find_all(class_='tddatos')[7].find_all(class_='tdprofesor')[1].text
            }
    lista.append(reg)

def capturar_optativa(pos):
    reg = {
        "nrc": contenido[pos].find_all('td')[0].text,
        "clave": contenido[pos].find_all('td')[1].text,
        "materia": contenido[pos].find_all('td')[2].text,
        "seccion": contenido[pos].find_all('td')[3].text,
        "creditos": contenido[pos].find_all('td')[4].text,
        "cupos": contenido[pos].find_all('td')[5].text,
        "disponible": contenido[pos].find_all('td')[6].text

    }
    # print(reg)
    lista.append(reg)



#           PARA INCO,INNI,INBI, INRO
i = 0
iter = 3
while i < len(contenido):
    if(iter==1):
        verif = contenido[i].find_all('td')
        l=0
        for g in verif:
            l = l+1

        if(l==9):
            # optativa o especializante
            capturar_optativa(i)
            iter = 1
        else:
            # materia normal
            iter=0
    else:
        aux = contenido[i + 2].find_all('td')
        no_td = 0
        for j in aux:
            no_td = no_td + 1

        print('pos: ', i)
        if no_td > 6:
            # optativa
            capturar_optativa(i)
            print('hola')
            iter = 1
        elif no_td == 6:
            # doble horario
            iter = 4
            captura2(i)
        elif no_td == 2:
            # un horario
            iter = 3
            captura1(i)
        print('td: ', no_td)
    i = i + iter

with open('INCO.json', 'a') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent=4)







#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#       PARA INCE
# i = 0
# iter = 3
# while i < len(contenido):
#     if i==1500:
#         reg = {
#             "nrc": contenido[i].find_all(class_='tddatos')[0].text,
#             "clave": contenido[i].find_all(class_='tddatos')[1].text,
#             "materia": contenido[i].find_all(class_='tddatos')[2].text,
#             "seccion": contenido[i].find_all(class_='tddatos')[3].text,
#             "creditos": contenido[i].find_all(class_='tddatos')[4].text,
#             "cupos": contenido[i].find_all(class_='tddatos')[5].text,
#             "disponible": contenido[i].find_all(class_='tddatos')[6].text,
#             "hora": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[1].text,
#             "dias": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[2].text,
#             "edificio": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[3].text,
#             "aula": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[4].text,
#             "periodo": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[5].text,
#             "maestro": contenido[i].find_all(class_='tddatos')[7].find_all(class_='tdprofesor')[1].text,
#             "maestro2": contenido[i].find_all(class_='tddatos')[7].find_all(class_='tdprofesor')[3].text
#                 }
#         lista.append(reg)
#         iter =4
#     else:
#
#        if (iter == 1):
#            verif = contenido[i].find_all('td')
#            l = 0
#            for g in verif:
#                l = l + 1
#
#            if (l == 9):
#
#                # optativa o especializante
#                capturar_optativa(i)
#                iter = 1
#            else:
#               # materia normal
#               iter = 0
#        else:
#            aux = contenido[i + 2].find_all('td')
#            no_td = 0
#            for j in aux:
#                no_td = no_td + 1
#
#            print('pos: ', i)
#            if no_td > 6:
#               # optativa
#               capturar_optativa(i)
#               print('hola')
#               iter = 1
#            elif no_td == 6:
#               # doble horario
#               iter = 4
#               captura2(i)
#            elif no_td == 2:
#               # un horario
#               iter = 3
#               captura1(i)
#            print('td: ', no_td)
#     i = i + iter
#
# with open('INCE.json', 'a') as archivo:
#     json.dump(lista, archivo, sort_keys=False, indent=4)
#
# print(contenido[1500])









# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#       PARA IGFO
# i = 0
# iter = 3
# while i < len(contenido):
#     if(i==22):
#         reg = {
#             "nrc": contenido[i].find_all(class_='tddatos')[0].text,
#             "clave": contenido[i].find_all(class_='tddatos')[1].text,
#             "materia": contenido[i].find_all(class_='tddatos')[2].text,
#             "seccion": contenido[i].find_all(class_='tddatos')[3].text,
#             "creditos": contenido[i].find_all(class_='tddatos')[4].text,
#             "cupos": contenido[i].find_all(class_='tddatos')[5].text,
#             "disponible": contenido[i].find_all(class_='tddatos')[6].text,
#             "hora": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[1].text,
#             "dias": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[2].text,
#             "edificio": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[3].text,
#             "aula": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[4].text,
#             "periodo": contenido[i].find(align='center').find('table').find_all('tr')[0].find_all('td')[5].text,
#             "hora2": contenido[i].find(align='center').find('table').find_all('tr')[1].find_all('td')[1].text,
#             "dias2": contenido[i].find(align='center').find('table').find_all('tr')[1].find_all('td')[2].text,
#             "edificio2": contenido[i].find(align='center').find('table').find_all('tr')[1].find_all('td')[3].text,
#             "aula2": contenido[i].find(align='center').find('table').find_all('tr')[1].find_all('td')[4].text,
#             "periodo2": contenido[i].find(align='center').find('table').find_all('tr')[1].find_all('td')[5].text,
#             "hora3": contenido[i].find(align='center').find('table').find_all('tr')[2].find_all('td')[1].text,
#             "dias3": contenido[i].find(align='center').find('table').find_all('tr')[2].find_all('td')[2].text,
#             "edificio3": contenido[i].find(align='center').find('table').find_all('tr')[2].find_all('td')[3].text,
#             "aula3": contenido[i].find(align='center').find('table').find_all('tr')[2].find_all('td')[4].text,
#             "periodo3": contenido[i].find(align='center').find('table').find_all('tr')[2].find_all('td')[5].text,
#             "maestro": contenido[i].find_all(class_='tddatos')[7].find_all(class_='tdprofesor')[1].text
#         }
#         lista.append(reg)
#         iter =5
#     else:
#         if (iter == 1):
#             verif = contenido[i].find_all('td')
#             l = 0
#             for g in verif:
#                 l = l + 1
#
#             if (l == 9):
#                 # optativa o especializante
#                 capturar_optativa(i)
#                 iter = 1
#             else:
#                 # materia normal
#                 iter = 0
#         else:
#             aux = contenido[i + 2].find_all('td')
#             no_td = 0
#             for j in aux:
#                 no_td = no_td + 1
#
#             print('pos: ', i)
#             if no_td > 6:
#                 # optativa
#                 capturar_optativa(i)
#                 print('hola')
#                 iter = 1
#             elif no_td == 6:
#                 # doble horario
#                 iter = 4
#                 captura2(i)
#             elif no_td == 2:
#                 # un horario
#                 iter = 3
#                 captura1(i)
#             print('td: ', no_td)
#
#
#     i = i + iter
#
# with open('IGFO.json', 'w') as archivo:
#     json.dump(lista, archivo, sort_keys=False, indent=4)
#
#
# print(contenido[22])