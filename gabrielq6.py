import random

def lista_de_nomes(): #Função que gera o dicionario
    l = []
    t =tuple()
    dmenor ={}
    dmaior={}

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
        t = email,dia,mes
        dmenor={a:t}
        dmaior.update(dmenor)
    
        
    return(dmaior) #retorna um dicionario com 100 valores
   
def vericador(): #Verifica e imprime se no dicionario existe algum aniversariante
    l = lista_de_nomes()
    z = []
    da = int(input('Insira o dia de hoje: '))
    me = int(input('Insira o mês de hoje: '))
    print('Lista de aniversariantes')
    for i in l.items():
       if da ==i[1][1] and me==i[1][2]:
           z.append(i[0])
    o = ','.join(z)
    if len(z)!=0:
        print ('lista de aniversariantes do dia:',o)
    else:
        print('Não há aniversariantes na data mencionada.')

           

def main():# função onde o programa roda
    print('Será que alguém faz aniversário hoje??')
    vericador()
    
main()
