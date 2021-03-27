# Função geradora de triângulos
def Q1():
    
    a = int(input('Insira um lado: '))
    b = int(input('Insira um lado: '))
    c = int(input('Insira um lado: '))

    # Um condicional que verifica se os números formam um triângulo
    if (a+c) > b and (b+c)> a and (a+b)> c:
        
        # Cadeia de condicionais que verifica a tipagem do triângulo
        if a==c and a==b:
            print ('É um triângulo equilátero!')
        elif a==c and a!=b:
            print ('É um triângulo isósceles!')
        elif b==c and b!=a:
            print ('É um triângulo isósceles!')
        elif a==b and a!=c:
            print ('É um triângulo isósceles!')
        else:
            print ('É um triângulo escaleno!')
            
    else:
        print ('Não é um triângulo! :(')



# Função que define o local de trabalho do programa
def main():
    Q1()
# Fazer a função rodar! 
main()
