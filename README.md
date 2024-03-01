# HackerRank
Título: Operación de Suma de Matriz: Un Problema de Programación

Resumen: El problema de la “Operación de Suma de Matriz” es un desafío de programación que implica manipular una matriz de números enteros a través de una serie de operaciones y calcular la suma de los elementos de la matriz después de cada operación.

Descripción del problema: Se nos da una permutación de identidad de N enteros como una matriz inicial. Una permutación de identidad de N enteros es una matriz de la forma [1, 2, …, N-1, N]. Se nos pide realizar M operaciones en la matriz e informar la suma de los elementos de la matriz después de cada operación.

Cada operación consiste en un entero 〖op〗_i. Si la matriz contiene 〖op〗_i, debemos intercambiar los primeros y últimos elementos de la matriz. Si la matriz no contiene 〖op〗_i, debemos eliminar el último elemento de la matriz e insertar 〖op〗_i al final de la matriz.

Restricciones: Las restricciones del problema son las siguientes:

2 ≤ N, M ≤ 10^5
1 ≤ 〖op〗_i ≤ 5 * 10^5
Solución propuesta: La solución propuesta para este problema implica seguir los pasos descritos en el problema. Primero, inicializamos la matriz como una permutación de identidad. Luego, para cada operación, verificamos si 〖op〗_i está en la matriz. Si es así, intercambiamos los primeros y últimos elementos. Si no, eliminamos el último elemento e insertamos 〖op〗_i al final. Después de cada operación, calculamos e imprimimos la suma de los elementos de la matriz.

LINK DEL CHALLENGE:
https://www.hackerrank.com/contests/hack-the-interview-vi/challenges/maximum-sum-10-1/problem
