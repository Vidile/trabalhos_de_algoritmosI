def Arq(): #Função que abre lê e salva o conteudo do arquivo em formato de lista
    meu_arquivo = open('Ano novo.txt','r')
    conteudo = meu_arquivo.readlines()
    meu_arquivo.close()
    return conteudo

def leitor(a):#Função que lê o arquivo e faz as operações com suas letras
    cont = 0
    contes =0
    contM =0
    b = a
    b =''.join(b)#Transforma a lista em uma string novamente
    for i in b:
        a = ord(i)
        if a in range(65,91):#Percorre a string em busca das letras maiusculas
            cont= cont+1
    for i in b:
        a =ord(i)
        if a in range(97,123):#Percorre a string em busca das letras minuculas
            contM= contM+1
    for i in b:
        if i==chr(32):#Percorre a string em busca dos espaços vazios
            contes +=1
    
            
   
    print('Número de espaços vazios: ',contes,
          '\nNúmero de Letras Maiusculas: ',cont,
          '\nNúmero de letras Minusculas; ',contM)
    
def main(): #Função onde se rodam as outras 
    a = Arq()
    leitor(a)

main() 
