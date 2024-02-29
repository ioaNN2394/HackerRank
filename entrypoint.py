def print_rangoli(size):
    
    width = 4 * size - 3
    alpha = "abcdefghijklmnopqrstuvwxyz"[0:size]

    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))


if __name__ == '__main__':

    while True:
        try:
            n = int(input("Digite el tamaño del rangoli: "))

            if 1<= n <= 26:
            
                print_rangoli(n)
                break
            else:
                print("El numero ingresado esta fuera del rango permitido")
        except ValueError:
            print("No permitido, vuelva a intentarlo")
