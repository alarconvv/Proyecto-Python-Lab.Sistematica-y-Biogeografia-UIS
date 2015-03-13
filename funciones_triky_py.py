#! /usr/bin/python
#funciones 


### va reemplazando la posicion dada por el jugador por la ficha que le corresposnde al jugados
def reemplazar(mi_lista,buscado,reemplazo):
    for i in range(0,9):
        if mi_lista[i] == buscado:
            mi_lista[i]=reemplazo
          
### uita la opcion que el anterior jugados tom\'o         
def eliminar_opciones(opciones_reales,jugador,simbolo):
    for i in range(0,9):
        if opciones_reales[i]== jugador:
            opciones_reales[i]=simbolo
           
###  busca si el juego result\'o en empate: los dos perdieron           
def no_ganador(tabla_juego,b):
  for i in range(0,9):
    if tabla_juego[i] == ' X' or tabla_juego[i] == ' O':
      b = b + 1
  return b

### Hace el juego 
def juego(tablero,fichas_jugadores,opciones_reales,visualizacion_tab):
  b=0
  lst = [0,1]*4
  for c in lst:
    if c==0:
      a=fichas_jugadores[2]
    else:
      a=fichas_jugadores[3]
    print '\n'
    print '\n'
    fichas_jugadores[c] = raw_input("Tome una posici'on: \n")
    print '\n'
    reemplazar(tablero,fichas_jugadores[c],a)
    eliminar_opciones(opciones_reales,fichas_jugadores[c],a)
    a1,b1,c1,a2,b2,c2,a3,b3,c3=tablero
    visualizacion_tab='                              {0} | {1} | {2}\n                              -------------\n                              {3} | {4} | {5}\n                              -------------\n                              {6} | {7} | {8}'.format(a1,b1,c1,a2,b2,c2,a3,b3,c3)
    tab_ju='TABLERO EN JUEGO'
    print tab_ju.center(70 ,'.')
    print '\n'
    print '\n'
    print visualizacion_tab
    b=no_ganador(tablero,b)
    if str(str(a1)+str(a2)+str(a3)) == str(' X X X') or str(str(a1)+str(a2)+str(a3)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break
    elif str(str(b1)+str(b2)+str(b3)) == str(' X X X') or str(str(b1)+str(b2)+str(b3)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break
    elif str(str(c1)+str(c2)+str(c3)) == str(' X X X') or str(str(c1)+str(c2)+str(c3)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break 
    elif str(str(a1)+str(b2)+str(c3)) == str(' X X X') or str(str(a1)+str(b2)+str(c3)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break 
    elif str(str(a1)+str(b1)+str(c1)) == str(' X X X') or str(str(a1)+str(b1)+str(c1)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break
    elif str(str(a2)+str(b2)+str(c2)) == str(' X X X') or str(str(a2)+str(b2)+str(c2)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break 
    elif str(str(a3)+str(b3)+str(c3)) == str(' X X X') or str(str(a3)+str(b3)+str(c3)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break 
    elif str(str(a3)+str(b2)+str(c1)) == str(' X X X') or str(str(a3)+str(b2)+str(c1)) == str(' O O O'):
      print ('/\/')*40
      print '\n'
      cadena='Ha ganado esta partida{0}...PUFF...SOLO SUERTE DE PRINCIPIANTE'.format(a)
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break 
    elif b > 30:
      print ('/\/')*40
      print '\n'
      cadena='Empate ... los dos perdieron ...Poco eficientes para este tipo de juegos'
      print cadena.rjust(80,' ')
      print ('/\/')*40
      print '\n'
      break 
    else: 
      print '\n'
      print '\n'
      print '\n'
      print 'Siguente turno!!!!!!, jugador con la ficha diferente a:  >>>>>>>  {0}'.format(a)
      print '\n'
      print '\n'
      op_fal='OPCIONES POR ASIGNAR'
      print op_fal.center(70 ,'.')
      print '\n'
      print opciones_reales
