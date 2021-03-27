def primN(n): #Verificador de números primos!
    primo = True
    for i in range (2, n):
        if n%i ==0:
            primo = False
            break
    if primo:
        return True
        
    else:
        return False

def primB(k):#criador da lista de Números primos ou não
        verif=primN(k)#Verificaçao se o número é primo ou não
        if verif== True:
            print('Esse número é primo!\nOs números primos até ele são:')
        else:
            print ('Esse número não é primo! \nMas os Números primos até ele são: ')
        print('1')  
        for i in range(2,k+1):#independente se ele for, mostrar todos que são primos até ele
            primo = primN(i)
            if primo == True:
                print(i)
        

def main():#Função onde o programa roda e se pergunta qual o número até onde vai ser rodado
   primB((int(input('insira o número para se verificar: '))))

main()
