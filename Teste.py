def ajeitador(): #Funbção que recebe o nome e o capitaliza
    nome = str(input('Insira o nome: '))
    nome = nome.lower()
    b = nome.split(sep =' ')
    o = []
    for i in b: #for que percorre todo o B transformando a inicial em maiuscula
        p = i[0]
        p = p.upper()
        m = ''.join(p+i[1:])#Onde eu junto a letra inicial agora capitalizada com o intervalo que contem o resto da palavra
        o.append(m)
        
    a = ' '.join(o)#onde o nome é formado
    print(a)

def main(): #Função que roda o programa
    ajeitador()



main()
