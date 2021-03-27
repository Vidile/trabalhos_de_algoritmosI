global Pilha
def cria_pilha():
    global Pilha
    Pilha =[]

def pilha_vazia(p):
    return len(p)== 0
def obter_topo(p):
    return p[len(p)-1]

def empilha(valor):
    global PL
    PL.append(valor)

def desempilha(p):
    if not pilha_vazia(p):
        return p.pop()
    return 'Pilha Vazia'

def mostrar_pilha(p):
    if not pilha_vazia(p):
        print('Topo:', end = '')
        for i in range(len(p)-1,-1,-1):
            print(p[i], end = '')
        print(' : fundo.')
