# Generador de Rangoli en Python

Este programa crea un patrón de arte llamado Rangoli, que es una forma de arte popular en India. El patrón se basa en el alfabeto inglés y su tamaño puede ser especificado por el usuario.

El desafío es el siguiente: Dado un número entero `n`, el programa debe imprimir un Rangoli del alfabeto de tamaño `n`. La letra central del Rangoli es la primera letra del alfabeto, la 'a', y la letra en los bordes es la `n`-ésima letra del alfabeto (en orden alfabético).

Para resolver este desafío, el programa define una función llamada `print_rangoli(size)`. Aquí está cómo funciona cada línea de código:

1. `width = 4 * size - 3`: Esta línea calcula el ancho del Rangoli. El ancho es cuatro veces el tamaño del Rangoli menos tres.

2. `alpha = "abcdefghijklmnopqrstuvwxyz"[0:size]`: Esta línea genera una cadena de caracteres con las primeras `n` letras del alfabeto inglés.

3. `for i in list(range(size))[::-1] + list(range(1, size)):`: Este bucle for recorre una lista de números que comienza desde `n-1` hasta `0`, y luego desde `1` hasta `n-1`. Esto asegura que la primera letra del alfabeto (la 'a') esté en el centro del Rangoli, y la `n`-ésima letra esté en los bordes.

4. `print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))`: Esta línea imprime cada línea del Rangoli. Cada línea es una secuencia de letras separadas por guiones, centrada y de un ancho específico. La secuencia de letras se genera tomando las letras desde la `n`-ésima hasta la `i`-ésima en orden inverso, seguido de las letras desde la `i`-ésima hasta la `n`-ésima en orden normal.

Finalmente, el programa solicita al usuario que ingrese el tamaño del Rangoli que desea generar, y luego llama a la función `print_rangoli(size)` con el tamaño ingresado. De esta manera, el programa puede generar un Rangoli de cualquier tamaño especificado por el usuario.

Enlace a problema de HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
