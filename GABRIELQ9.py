import time
global Fila
def gera_fila(): #Gera a fila
    global Fila
    Fila= []
    
def fila_vazia(f): #Função que serve para ser usada como checagem da fila, auxilia outras funções
    return len(f)==0

def obter_frente(f): #Função que me diz o proximo da fila
    if not fila_vazia(f):
        print(f[0])
    else:
        print('Fila Vazia!')

def insere(valor): #Função onde os valores/senhas da fila são inseridos
    global Fila
    Fila.append(valor)

def remove(f): #Retira a primeira senha da fila
    if not fila_vazia(f):
        aux = f[0]
        del f[0]
        return aux
    else:
        print('Fila Vazia!')

def mostrar_fila(f): #Mostra a fila completa
    if not fila_vazia(f):
        print('Frente:',end='')
        for i in range(len(f)):
            print(f[i],end='')
        print(':fim.')
    else:
        print('Fila Vazia!')

def menu(): #Função Menu, aqui é onde o programa roda o laço, escolhi manter aqui e não na função main, por conta de organização
    gera_fila()
    print('''
                Essas são as opções:
                (1) - Inserir senha na fila
                (2) - Retirar senha da fila
                (3) - Ver o proximo da fila
                (4) - Listar todas senhas da fila
                (0) - Encerra o programa
                ''')
    time.sleep(0.1)
    escolha = str(input('Insira sua escolha: '))
    time.sleep(0.1)
    while escolha !='0':
        try:
            if escolha == '1':
                time.sleep(0.1)
                w = int(input('Insira a senha da fila: '))
                z = insere(w)   
            if escolha == '2':
                remove(Fila)
            elif escolha == '3':
                time.sleep(0.1)
                obter_frente(Fila)
            elif escolha == '4':
                time.sleep(0.1)
                mostrar_fila(Fila)
            time.sleep(0.1)
            escolha =str(input('Insira sua escolha: '))
        except ValueError:
            print('invalido')
            time.sleep(0.1)
            escolha =str(input('Insira sua escolha: '))

    print('''

                Obrigado por utilizar o programa!''')

def main(): #Função onde roda o menu
    print('''

                Bem-vindos a filas 2020.1!!!''')
    menu()


main()


