import time

def incluir(lista1): #Função que insire os dados na lista pré existente
    Lista1 = lista1
    t = tuple()
    nome = str(input('Insira o nome da pessoa: '))
    nome =nome.lower()
    nome = nome.capitalize()
    email = str(input('Insira um email: '))
    dia = str(input('Insira o dia do aniversário: '))
    mes = str(input('Insira o mês do aniversário: '))
    t = nome,email,dia,mes
    Lista1.append(t)
    return(Lista1)

def consultar(lista1): # função Consulta na lista por nome de aniversariante
    q = lista1
    y = str(input('insira o nome para consultar: '))
    y = y.lower()
    y =y.capitalize()
    for nome,email,dia,mes in q:
        if y == nome:
            print('Email da pessoa',email,'Dia do aniversário: ',dia, 'Mês do aniversário: ',mes)
        else:
            pass
        
def Consultar_data(lista1): #Função que Consulta pela data do aniversário
    q = lista1
    y = str(input('insira o dia do aniversário: '))
    u = str(input('insira o mês do aniversário: '))
    for nome,email,dia,mes in q:
        if y == dia and u ==mes:
            print('Nome da pessoa',nome,'Email da pessoa',email)
        else:
            pass

def listar(lista1): #Função que demonstra a lista de dados inseridos ou pré existentes
    o = lista1
    print(o)


def menu(): #Função Menu, aqui é onde o programa roda o laço, escolhi manter aqui e não na função main, por conta de organização
    
    lista1 =[('gabriel', 'gabriel@xyz.com.br', '01', '11'), ('Joana','Joana@xyza.com.br','09','12'),('Luciano','Luciano@xyz.com.br','12','01')]
    print('''
                Essas são as opções:
                (1) - Inserir um novo nome
                (2) - Consultar por nome
                (3) - Consultar por data
                (4) - Listar todos os nomes inseridos
                (0) - Encerra o programa
                ''')
    escolha = str(input('Insira sua escolha: '))
    time.sleep(0.1)
    while escolha !='0':
        if escolha == '1':
            z = incluir(lista1)
        else:
            z = lista1
            
        if escolha == '2':
            consultar(z)
        elif escolha == '3':
            Consultar_data(z)
        elif escolha == '4':
            listar(z)
        escolha =str(input('Insira sua escolha: '))
    print('Obrigado por utilizar o programa!')


def main(): #função que roda o menu.
    print('Bem-vindo ao programa')
    time.sleep(0.1)
    a = str(input('Deseja Iniciar? S/N: '))
    time.sleep(0.1)
    a = a.lower()
    if a=='s':
        time.sleep(0.1)
        menu()
    else:
        print('Obrigado por usar o programa!')


main()
    
    
