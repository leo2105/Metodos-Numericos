NumericalAnalysis
=================

Package about methods in Numerical Analysis for solving linear equations also can to handle machine numbers.

Sobre el programa
-----------------

El archivo MachineNumer.py contiene métodos para generar números de máquina indicandole ciertos parámetros.

El archivo LinearEquation.py contiene métodos para resolver ecuaciones lineales.

Finalmente el archivo Main.py muestra un menú con el acceso a ambos programas.

Cómo ejecutar el programa
------------------------

Guardar los tres archivos MachineNumber.py, LinearSolver.py y Main.py en una misma carpeta, luego 
dentro esa carpeta ejecutar el archivo Main.py.

Por ejemplo si usamos la terminal, nos dirigimos a la carpeta de los archivos y luego ejecutamos:

python Main.py

Cómo usarlo
-------------

Para el manejo de números de maquina se necesitan parámetros como mantisa, base y las cotas del exponente 
de la base, el mismo programa indica los pasos.

Para resolver ecuaciones lineales necesitamos la matriz y el vector independiente, también en ciertos 
casos se necesita confirmar el tipo de resolución: con pivotacion parcial, total o sin pivotación.

Por hacer
---------

Agregar nuevos métodos lineales y mejorar los existentes, por ejemplo:

- Metodo de Parlett y Reid
- Metodo de Aasen
- Completar el tema de condicionamiento

Agregar los metodos no lineales.

Básicamente agregar otro que falte y obviamente mejorar los existentes en busca de bugs.

Si alguien quiere aportar solo haga un fork del project :).

