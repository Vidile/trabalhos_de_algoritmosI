def palin(n):
    
    if n == n[::-1]:
        return True


def main():
    n = str(input('insira a palavra: '))
    n = n.upper()
    palin(n)
    if palin(n) == True:
        print('É palindromo')
    else:
        print('Não é palindromo')


main()


