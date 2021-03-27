
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

    
def lisp(): #Função que gera a lista de números primos e a repetição
    l = []
    for i in range (2,1001): #for que gera a lista usando a função primN
        verif = primN(i)
        if verif == True:
            l.append(i)
    n = (int(input('Insira o número para verificar se é primo, 0 para encerrar: ')))
         
    while n!= 0: #repetição que vai perguntar o número até informar o 0
        if n in l:
            print ('\nEsse número é primo!')
        else:
            print('\nEsse número não é primo!')
            
        n = (int(input('\nInsira o número para verificar se é primo, 0 para encerrar: ')))
        
    print('\nObrigado por usar o programa!')

def main(): # Função onde o programa é rodado
    lisp()

main()


                



