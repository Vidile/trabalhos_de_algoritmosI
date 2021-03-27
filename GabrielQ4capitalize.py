def ajeitador(): #Função que pede o nome e ajeita ele
    nome = str(input('Insira o nome: '))

    n = nome.lower()#Transforma o nome todo em minusculo
    b = n.split(sep=' ')#Transforma a string em lista e separa o nome pelos espaços
    c =[]
    f = []
    for i in b:#Para todo o nome separado pelo espaço, ele vai capitalizar a primeira letra
        p = i[0].upper
        c.append(p)
        f = i.split(sep=i[0])
    m = c+f
    print(m)   
        
         #Coloca o nome capitalizado na lista vazia C
    a = ' '.join(m)#Transforma tudo em string novamente

    print(a) #Print do novo nome formatado 


def main(): #Função onde o programa roda
    ajeitador()


main()
