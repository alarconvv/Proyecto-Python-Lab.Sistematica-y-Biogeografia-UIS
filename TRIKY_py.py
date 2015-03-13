! /usr/bin/python

# defina un objeto de inicio

class parametros_inicio():
  tablero = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
  a1,b1,c1,a2,b2,c2,a3,b3,c3 = tablero
  fichas_jugadores = ['jugadorA','jugadorB',' X',' O']
  visualizacion_tab = '                              {0} | {1} | {2}\n                              -------------\n                              {3} | {4} | {5}\n                              -------------\n                              {6} | {7} | {8}'.format(a1,b1,c1,a2,b2,c2,a3,b3,c3)
  opciones_juego = '\n{0}: Izquierda Superior \t{1}: Centro Superior\t{2}: Derecha Superior\n{3}: Izquierda Centre\t{4}: Centro centro\t{5}: Derecha Centro\n{6}: Izquierda Inferior\t{7}: Centro Inferior\t{8}: Derecha Inferior'.format(a1,b1,c1,a2,b2,c2,a3,b3,c3)
  opciones_reales = [a1,b1,c1,a2,b2,c2,a3,b3,c3]

# importe las funciones

from funciones_triky_py import *


###########################################
#Saludo de entrada
###########################################

saludo='   Bienvenido al mundo del TR!KY-py   '

print '\n'
print '\n'
print '\n'
print ('/\/')*40

print saludo.center(120 ,'.')

print ('/\/')*40
print '\n'
print '\n'
print '\n'

#############################################
#Reglas de juego
#############################################

print 'REGLAS DE JUEGO'
print '\n'

print '1. Si programan sin testing, hay tabla '
print '2. Si no comentan el c\'odigo, hay tabla'
print '3. Si no respetan los standares, hay tabla'
print '4. Si sequejan del lenguaje, hay tabla'
print '5. Si preguntan boludeces, hay tabla'
print '6. Si cuelgan el servidor, hay tabla'
print '7. Si reportan el mismo error 2 veces, hay tabla'
print '8. Si no respetan los standares, hay tabla'
print '9. Si eres bayesiano, hay tabla'
print '10. Si tiene que datar..no me importa, hay tabla'
print '10. Y Si no juega TR!KY-py, hay tabla'

print '\n'
print '\n'
print '\n'

#############################################
#Asignaci\'on de par\'ametros 
#############################################

# llamando al objeto anteriormente creado

inicio = parametros_inicio

# mostrar el tablero de inicio

table = 'TABLERO DE PARTIDA'

print table.center(70 ,'.')
print '\n'

print inicio.visualizacion_tab
print '\n'
print '\n'
print '\n'

# opciones para acceder alas fichas del tablero

op_ju = 'OPCIONES DE JUEGO'

print op_ju.center(70 ,'.')
print '\n'

print inicio.opciones_juego
print '\n'
print '\n'
print '\n'

# la opciones que tien para empezar

op_re='OPCIONES DE INICIO DE PARTIDA'

print op_re.center(70 ,'.')
print '\n'

print inicio.opciones_reales

# funcion juego, tiene todos los bucles de juego

juego(inicio.tablero,inicio.fichas_jugadores,inicio.opciones_reales,inicio.visualizacion_tab)

# si finaliza el juego podr\'ia volver a comenzar'

Partida= raw_input("Otra Partida? conteste si o no \n")

if Partida == 'si':

  execfile("TRIKY_py.py")

else:

  print '\n'
  print '\n'
  mess='MALOS PERDEDORES...ADIOS'

  print ('/\/')*40
  print '\n'

  print mess.center(70 ,'.')
  print '\n'
  
  print ('/\/')*40
  print '\n'
  print '\n'
  print '\n'
  quit()


  
 

