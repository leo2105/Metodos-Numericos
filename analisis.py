#importacion los metodo hechos en python
import metodos
import Gauss
import GaussJordan
import L1U_Crout
import LU1_Crout
import LU_Doolittle
import Cholesky
import LDMt
import LDLt
import ParlettReid
import Aasen
import GrammSchmidt
import funciones
import time
#Lectura de Datos
opcion = 1
A = funciones.leerMat("matrizA.csv")
m=len(A[0])
n = len(A)
B = funciones.leerVect("vectorB.csv")
if m!=n:
	print " La matriz A no es cuadrada"
	opcion = 12
#menu
while(opcion!=12):
	funciones.limpiaPantalla()
	print "\n -------------------------------------------------" 
	print " Sistema de Ecuaciones del Problema de Circulacion" 
	print " -------------------------------------------------" 
	funciones.imprimeSistema(A,B,n)
	print "\n Epsilon maquina: %.60f" %(funciones.epsilonMaq())
	opcion = funciones.menu()
	funciones.limpiaPantalla()
	tiempoSimetriza = 0
	inicio = time.clock()
	if opcion < 1 or opcion >12:
		print "\n\n\n Opcion no valida!, "+str(opcion)+" no esta en lista"
	else:
		solLU1,solL1U,solLUD,solLDLt,solLDMt=[],[],[],[],[]
		solChol,solPar,solGram,solAas=[],[],[],[]
		solGauss,solGJ=0,0
		if opcion == 1:
			solGauss = Gauss.gauss(A,B,n)
			print "\n Solucion: " +str(solGauss)
		elif opcion == 2:
			solGJ = GaussJordan.gaussJordan(A,B,n)
			print "\n Solucion: "+str(solGJ)
		elif opcion == 3:
			solL1U =L1U_Crout.metodoL1U(A,B,n)
			print "\n Solucion Ax = b -> LUx = b -> Ux = y -> Ly = b:"
			print " En Ly=b, y: "+str(solL1U[0])
			print " En Ux=y, x: "+str(solL1U[1])
		elif opcion == 4:
			solLU1 =LU1_Crout.metodoLU1(A,B,n)
			print "\n Solucion Ax = b -> LUx = b -> Ux = y -> Ly = b:"
			print " En Ly=b, y: "+str(solLU1[0])
			print " En Ux=y, x: "+str(solLU1[1])
		elif opcion == 5 :
			solLUD =LU_Doolittle.metodoDoolittle(A,B,n)
			print "\n Solucion Ax = b -> LUx = b -> Ux = y -> Ly = b:"
			print " En Ly=b, y: "+str(solLUD[0])
			print " En Ux=y, x: "+str(solLUD[1])
		elif opcion == 6:
			solLDMt = LDMt.LDMt(A,B,n)
			print "\n Solucion: "
			print " En L.z=b, tenemos z: "+str(solLDMt[0])
			print " En D.y=z, tenemos y: "+str(solLDMt[1])
			print " En Mt.x=y, tenemos x: "+str(solLDMt[2])
		elif opcion == 7:
			if funciones.esSimetrica(A,n):
				solLDLt = LDLt.LDLt(A,B,n)
				print "\n Solucion: "
				print " En L.z=b, tenemos z: "+str(solLDLt[0])
				print " En D.y=z, tenemos y: "+str(solLDLt[1])
				print " En Mt.x=y, tenemos x: "+str(solLDLt[2])
			else:
				tim1=time.clock()
				C,d = funciones.simetSistema(A,B,n)
				tiempoSimetriza=time.clock()-tim1
				solLDLt = LDLt.LDLt(C,d,n)
				print " En L.z=b, tenemos z: "+str(solLDLt[0])
				print " En D.y=z, tenemos y: "+str(solLDLt[1])
				print " En Lt.x=y, tenemos x: "+str(solLDLt[2])
		elif opcion ==8:
			if funciones.esSimetrica(A,n):
				solChol = Cholesky.metodoCholesky(A,B,n)
				print "\n Solucion: "
				print " En G.y=b' tenemos y: "+str(solChol[0])
				print " En Gt.x=y tenemos x: "+str(solChol[1])
			else:
				tim1=time.clock()
				C,d = funciones.simetSistema(A,B,n)
				tiempoSimetriza=time.clock()-tim1
				solChol = Cholesky.metodoCholesky(C,d,n)
				print "\n Solucion: "
				print " En G.y=b' tenemos y: "+str(solChol[0])
				print " En Gt.x=y tenemos x: "+str(solChol[1])
		elif opcion ==9:
			solPar = ParlettReid.metodoParlet(A,B,n)
			print " Mediante las operaciones: L.z=P.b, T.w=z, Lt.y=w ->x=Pt.y"
			print "\n Solucion: "
			print " Tenemos x: "+str(solPar)
		elif opcion ==10:
			if funciones.esSimetrica(A,n):
				solAas = Aasen.metodoAasen(A,B,n)
				print " Mediante las operaciones: L.z=P.b, T.w=z, Lt.y=w ->x=Pt.y"
				print "\n Solucion: "
				print " Tenemos x: "+str(solAas)
			else:
				tim1=time.clock()
				C,d = funciones.simetSistema(A,B,n)
				tiempoSimetriza=time.clock()-tim1
				solAas = Aasen.metodoAasen(C,d,n)
				print " Mediante las operaciones: L.z=P.b, T.w=z, Lt.y=w ->x=Pt.y"
				print "\n Solucion: "
				print " Tenemos x: "+str(solAas)
		elif opcion ==11:
			solGram =GrammSchmidt.metodoGramm(A,B,n)
			print "\n Solucion por el metodo Gramm Sschmidt:"
			print " y: "+str(solGram[0])
			print " x: "+str(solGram[1])
		elif opcion ==12:
			print "\n\n Adios....."
			print "\n\n---------------------------"
			print "\n\n by. Oscar Huarcaya Canal"
			print "\n\n---------------------------"
	fin = time.clock()-tiempoSimetriza
	print "\n Tiempo de ejecucion: %.15f" %(fin-inicio)
	raw_input("\n\n Presione la tecla ENTER para continuar....")