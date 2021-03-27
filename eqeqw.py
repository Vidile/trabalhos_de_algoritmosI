import random

def lista_de_nomes(): #Função que gera a lista de tuplas de maneira randomica
    l = []
    t =tuple()

    for i in range (1,101):#For que gera os dias e os meses
        mes = random.randint(1,12)
        if mes ==2:
            dia = random.randint(1,28)
        elif mes == 4 or mes == 6 or mes == 9:
            dia =random.randint(1,30)
        else:
            dia = random.randint(1,31)
        o =[]    
        for i in range(0,10):# for que gera os nomes
           
            nome =random.randint(97,122)
            nome_real = chr(nome)
            o.append(nome_real)


        
        a ='' .join(o)
        email = a+'@xyz.com.br'
        t = a,email,dia,mes 
        l.append(t)
        
    return(l) #retorna uma lista de 100 tuplas
   
def vericador(): #Verifica se na lista existe algum aniversariante
    l = lista_de_nomes()
    da = int(input('Insira o dia de hoje: '))
    me = int(input('Insira o mês de hoje: '))
    print('Lista de aniversariantes')
    print(l)
    for a,email,dia,mes in l:
       if da ==dia and me==mes:
           print ('Nome da pessoa:',a,'Email da pessoa: ',email)
       else:
           pass

           

def main():# programa onde o programa roda
    print('Será que alguém faz aniversário hoje??')
    vericador()
    
main()
