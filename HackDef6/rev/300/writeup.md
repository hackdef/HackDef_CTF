# rev-300 Zilc0d3, but nerfed

El reto consiste en un pedazo de una funcion en ILCODE que se supone exfiltra datos, pero hay que leer el ILCODE, al final tenemos un console log que imprime la flag

Al principio del reto se invoca un console.writeline con una string hardcodeada, estos para que el participante vea como es que se pasan los parametros de una funcion en ilcode

La flag se construye a partir de declaraciones de arrays de strings, funciones que convierten un numero entero en un char, una funcion suma y al final se concatena todo en una variable flag que va hacia la funcion console.writeline

El objetivo es leer el ilcode para ver las asignaciones de funciones, memoria, etc para al final juntarlo todo en una contatenacion para obtener la flag, se puede o no hacer un script de esto pero no es necesario

El programa se compilo como una app de consola en .NET framework 4.7 y con ILDASM se extrajo le ilcode de la funcion en cuestion

El source code de la app console se puede revisar en el archivo program.cs

## HINTS
1. https://en.wikipedia.org/wiki/List_of_CIL_instructions
2. CIL is a stack-based bytecode