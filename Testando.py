import time
def arquivo():
    arquivo = open('Banco de dados2.txt','w')
    arquivo.close()
    return arquivo

def incluir(): #Função que insire os dados e guarda no arquivo
    nome = str(input('Insira o nome da pessoa: '))
    nome =nome.lower()
    nome = nome.capitalize()
    email = str(input('Insira um email: '))
    dia = str(input('Insira o dia do aniversário: '))
    mes = str(input('Insira o mês do aniversário: '))
    arquivo = open('Banco de dados2.txt','r')
    conteudo = arquivo.readlines()
    conteudo.append('\n'+nome+','+email+','+dia+','+mes)
    arquivo = open('Banco de dados2.txt','w')
    arquivo.writelines(conteudo)
    arquivo.close()
   
    return arquivo


def consultar(): # função Consulta no arquivo por nome de aniversariante
    with open('Banco de dados2.txt') as f:
        conteudo = f.readlines()
    w =[x.strip() for x in conteudo]
    l = [tuple (x.split(',')) for x in w]
    y = str(input('insira o nome para consultar: '))
    y = y.lower()
    y =y.capitalize()
    print(l)
    for a,b,c,d in l:
        if y==a:
            print('email: ',b,'Data do aniversario: ',c,'Mês do aniversario:',d)
        else:
            pass

def Consultar_data(): #Função que Consulta pela data do aniversário
    with open('Banco de dados2.txt') as f:
        conteudo = f.readlines()
    w =[x.strip() for x in conteudo]
    l = [tuple (x.split(',')) for x in w]
    y = str(input('insira o dia do aniversário: '))
    u = str(input('insira o mês do aniversário: '))
    for a,b,c,d in l:
        if y == c and u ==d:
            print('Nome da pessoa',a,'Email da pessoa',b)
        else:
            pass
        
def listar(): #Função que demonstra a lista de dados inseridos ou pré existentes
    with open('Banco de dados2.txt') as f:
        conteudo = f.readlines()
    w =[x.strip() for x in conteudo]
    print(w)

def menu(): #Função Menu, aqui é onde o programa roda o laço, escolhi manter aqui e não na função main, por conta de organização
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
            z = incluir()   
        elif escolha == '2':
            consultar()
        elif escolha == '3':
            Consultar_data()
        elif escolha == '4':
            listar()
        else:
            print('erro')
            escolha =str(input('Insira sua escolha: '))
        escolha =str(input('Insira sua escolha: '))
    print('Obrigado por utilizar o programa!')




def main():
    print('Bem-vindo ao programa')
    time.sleep(0.1)
    c = str(input('é a primeira  vez que vocÊ usa o programa: S/N?'))
    c.lower()
    if c =='s':
        arquivo()
    else:
        pass
    
    a = str(input('Deseja Iniciar? S/N: '))
    time.sleep(0.1)
    a = a.lower()
    if a=='s':
        time.sleep(0.1)
        menu()
    else:
        print('Obrigado por usar o programa!')

main()
