import MachineNumber
import LinearSolver

def menu():
	print "\t\t\t  Bienvenidos al Paquete de Analisis Numerico"

	flag = 1
	while flag:
		print "Elija el programa:\n"
		print """
			1.  Numeros de maquina
			2.  Resolucion de sistemas lineales.
			3.  Salir
			  """
		opc = input('Ingrese opcion\n')
		if type(opc) != type(1):
			print 'Debe ingresar un valor entero, vuelva a intentarlo'
			continue

		if opc == 1:
			MachineNumber.menu()
		elif opc == 2:
			LinearSolver.menu()
		elif opc == 3:
			print 'Gracias por usar el programa'
			flag = 0
		else:
			print 'Opcion incorrecta'	
		
	#Para sistemas windows			
	opc = raw_input('Fin del programa, presione enter')		

if __name__ == '__main__':
	menu()	

	
