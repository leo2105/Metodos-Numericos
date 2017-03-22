"""Paquete que calcula los Numeros de Maquina (o Machine Numbers) para cierto tipo de maquina, 
	su cantidad, aproximaciones y errores .

	Por ejemplo si se trabaja con la maquina: MARC-32 se tienen las siguientes definiciones:


	Un numero en una maquina binaria en una notacion cientifica normalizada:
	x = +-(t) x 2^e, similarmente  x = +-(0.a1 a2 a3 ... at) x 2^e
	donde:

	x es un numero real.
	t es la mantisa. 1/2 <= t < 1, si x != 0.
	e es el exponente de la base 2, L <= e <= U, e es un entero.
	a1 = 1, ai E {0, 1} para i != 1.

	De los 32 bits de la MARC-32 se distribuyen en:

	1 bit - signo del numero real x.
	1 bit - signo del exponente e.
	7 bits - exponente( para su valor absoluto)
	23 bits - para la mantisa(valor absoluto de t)

	Entonces si un numero puede ser representado siguiendo estos parametros, ie, solo 7 bits
	para |e| y 24 bits para |t| (se gana un bit mas ya que a1 ya es 1) entonces es un numero de
	maquina en la MARC-32(puede haber distintas configuraciones para otro tipo de maquina).

	Como ejemplo, 1/10 = 0.1 no es un numero de maquina en la MARC-32, ya que 0.1 en base 2 
	es un numero periodico( 0.0001 1001 1001 ... ), ie, tiene mas de 24 bits de mantisa 
	y para que sea un numero de maquina en la MARC-32 se tendria que redondear o truncar 
	a 24 bits de mantisa, y buscar el numero de maquina, f(x), mas cercano a x.
	
   Definiciones en el programa:
   t : mantisa.
   b : base. 
   L : cota inferior del exponente de la base.
   U : cota superior del exponente de la base.
   MN : Numero de maquina

   Nota: Las funciones y las variables estan en ingles, y los comentarios en espanol.	
"""
from math import fabs
from sys import exit


def inputParam():
	"""Ingreso de los parametros para crear el conjunto de numeros de maquina"""

	t = int(raw_input('Ingrese la mantisa t:'))
	b = int(raw_input('Ingrese la base b:'))
	L = int(raw_input('Ingrese la cota inferior L:'))
	U = int(raw_input('Ingrese la cota superior U:'))

	# if(b < 2 or t <= 0 or L > U or type(t + b + L + U) != type(1)):
	# 	exit('Revise sus parametros: base > 2, mantisa > 0, L > U, y'\
	# 			+ ' los valores deben ser enteros')

	return t, b, L, U

def countMN(t, b, L, U):
	"""Funcion que calcula la cantidad de Numeros de Maquina en base a los
	   parametros. """ 

	if(b < 2 or t <= 0 or L > U or type(t + b + L + U) != type(1)):
		exit('Revise sus parametros: base > 2, mantisa > 0, L > U, y'\
			 	 + ' los valores deben ser enteros')   

	return (2 * (b-1) * ((b)**(t-1)) * (U-L+1) + 1)			

def setMN(t, b, L, U):
	"""Funcion que calcula los Numeros de Maquina en base a los parametros."""

	if(b < 2 or t <= 0 or L > U or type(t + b + L + U) != type(1)):
		exit('Revise sus parametros: base > 2, mantisa > 0, L > U, y'\
			 	 + ' los valores deben ser enteros')	 		

	#matrix[b**(t-1)][U-L+1]
	row = (b)**(t-1)
	col = (U-L+1)
	matrix = [([0] * col) for i in range(row)]
	for i in range(row):
		for j in range(col):
			#formula general de un elemento de la matriz
			matrix[i][j] =  (b**j * (b**(t-1) + i)) / float((b**t * b**abs(L)))
	
	return matrix

def showFraction(t, b, L, U):
	"""Funcion que muestra el conjunto de numeros en base 10 en funcion
		 a los parametros"""

	matrix = setMN(t, b, L, U)
	denom = b**t * b**abs(L)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			#A cada elemento de la matriz lo multiplico por el denominador para 
			#obtener el numerador, luego muestro este numero dividido el denominador.
			matrix[i][j] = '+-' + str(int(matrix[i][j] * (denom))) + '/' + str(denom)
	for i in range(len(matrix)):
		print str(matrix[i][:]) + '\n'

	#Nota: Segun el conjunto el valor 0 esta implicito.			

def showSetB(t, b, L, U):
	"""Funcion que muestra el conjunto de numeros en base 2 en funcion
			 a los parametros"""

	matrix = setMN(t, b, L, U)
	denom = b**t * b**abs(L)
	for i in range(len(matrix)):
		temp = '+-' + str(base10ToBaseB(int(matrix[i][0] * (denom)), b))
								
		for j in range(len(matrix[0])):
			#A cada elemento de la matriz lo multiplico por el denominador para 
			#obtener el numerador, luego muestro este numero divido el denominador.
			matrix[i][j] = temp + 'x' + '(' + str(b) + '^' + str(L + j) + ')';
				
	for i in range(len(matrix)):
		print str(matrix[i][:]) + '\n'	

	#Nota: Segun el conjunto el valor 0 esta implicito.

def base10ToBaseB(n, b):
	"""Funcion que convierte un numero de base 10 a base b"""

	if(b < 2): 
		exit('Valor de base incorrecto: base >= 2')

	if(n == 1):
		return '1'

	else:
		string = ''
		while(n/b != 0):
			temp = n % b
			n /= b
			string += str(temp)

	return (string + str(n))[::-1]

def aproxMN(t, b, L, U, x):
	"""Funcion que dado un parametro calcula el valor mas proximo a un numero
		 de maquina"""

	matrix = setMN(t, b, L, U)
	minimum = fabs(x - matrix[0][0])
	machineNumber = 0  #fl(x): numero de maquina mas cercano a x.
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			temp = fabs(x - matrix[i][j])
			if(temp < minimum):
				minimum = temp
				machineNumber = matrix[i][j]

	return machineNumber

def absoluteError(t, b, L, U, x):
	"""Funcion que calcula el error absoluto: |x - x*|"""
	
	return fabs(x - aproxMN(t, b, L, U, x))

def relativeError(t, b, L, U, x):
	"""Funcion que calcula el error relativo: (|x - x*| / |x|)"""

	return (absoluteError(t, b, L, U, x) / (fabs(x))) * 100 
				
def menu():
	print "\t\t\t  Bienvenidos al Programa de"
	print "\t\t\tGeneracion de Numeros de Maquina"
	opc = 1
	while(opc):
		print "Elija la funcion a usar:\n"
		print """
			0.  Definiciones.
			1.  Mostrar el conjunto en base B.
			2.  Mostrar el conjunto como fraccion.
			3.  Cantidad de numeros de maquina.
			4.  Error absoluto para un x dado.
			5.  Error relativo para un x dado.
			6.  Valor mas proximo a un MN para un x dado.
			7.  Salir
			  """
		opc = input('Ingrese opcion\n')
		if type(opc) != type(1):
			print 'Debe ingresar un valor entero, vuela a intentarlo'
			continue
		if opc == 7:
			exit('Gracias por usar el programa')
		if opc < 0 or opc >= 8:
			print 'Opcion incorrecta'
			continue
		if opc == 0:
			print __doc__
			opc = 1
			continue		
		#ingreso de los paramatros
		t, b, L, U = inputParam()
		if opc == 1:
			showSetB(t, b, L, U)

		elif opc == 2:
			showFraction(t, b, L, U)	

		elif opc == 3:
			print countMN(t, b, L, U)	

		elif opc == 4:
			x = float(raw_input('Ingrese el valor de x: '))
			print ('Error absoluto: {0}%').format(absoluteError(t, b, L, U, x))	

		elif opc == 5:
			x = float(raw_input('Ingrese el valor de x: '))
			print ('Error relativo: {0}%').format(relativeError(t, b, L, U, x))	

		elif opc == 6:
			x = float(raw_input('Ingrese el valor de x: '))
			print aproxMN(t, b, L, U, x)	

		print 'Resultado obtenido con exito'		

