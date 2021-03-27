def arquivo():
    arquivo = open('Banco de dados2.txt','w')
    arquivo.close()
    return arquivo

def incluir(): #Função que insire os dados na lista pré existente
    Lista1 =[]
    t = tuple()
    nome = str(input('Insira o nome da pessoa: '))
    nome =nome.lower()
    nome = nome.capitalize()
    email = str(input('Insira um email: '))
    dia = str(input('Insira o dia do aniversário: '))
    mes = str(input('Insira o mês do aniversário: '))
    t = nome,email,dia,mes
    Lista1.append(t)
    list2 =','.join(Lista1)
    arquivo = open('Banco de dados2.txt','r')
    conteudo = arquivo.readlines()
    conteudo.append(list2)
    arquivo = open('Banco de dados2.txt','w')
    arquivo.writelines(conteudo)
    arquivo.close()


    return arquivo

incluir()
