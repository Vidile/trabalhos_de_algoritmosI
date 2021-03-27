def Arq(): #Função que abre lê e salva o conteudo do arquivo em formato de lista
    meu_arquivo = open('Ano novo.txt','r')
    conteudo = meu_arquivo.readlines()
    meu_arquivo.close()
    return conteudo

def leitor(a):#Função que lê o arquivo e faz as operações com suas letras
    cont = 0
    contes =0
    contM =0
    contA = 0
    contA1 = 0
    contB1 = 0
    contC1 = 0
    contD1 = 0
    contE1 = 0
    contF1 = 0
    contG1 = 0
    contH1 = 0
    contI1 = 0
    contJ1 = 0
    contK1 = 0
    contL1 = 0
    contM1 = 0
    contN1 = 0
    contO1 = 0
    contP1 = 0
    contQ1 = 0
    contR1 = 0
    contS1 = 0
    contT1 = 0
    contU1 = 0
    contV1 = 0
    contW1 = 0
    contX1 = 0
    contY1 = 0
    contZ1 = 0 
    contB = 0
    contC = 0
    contD = 0
    contE = 0
    contF = 0
    contG = 0
    contH = 0
    contI = 0
    contJ = 0
    contK = 0
    contL= 0
    contN = 0
    contO = 0
    contP = 0
    contQ = 0
    contR = 0
    contS = 0
    contT = 0
    contU = 0
    contV = 0
    contW = 0
    contX = 0
    contY = 0
    contZ =0
    l =[]
    z = []
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
    for i in b:
        if i =='a':
            contA = contA+1
        if i =='A':
            contA1 = contA1+1
        elif i =='b':
            contB = contB+1
        elif i =='B':
            contB1 = contB1+1
        elif i =='c':
            contC = contC+1
        elif i =='C':
            contC1 = contC1+1
        elif i =='d':
            contD = contD+1
        elif i =='D':
            contD1 = contD1+1
        elif i =='e':
            contE = contE+1
        elif i =='E':
            contE1 = contE1+1
        elif i =='F':
            contF= contF+1
        elif i =='f':
            contF1 = contF1+1
        elif i =='g':
            contG = contG+1
        elif i =='G':
            contG1 = contG1+1
        elif i =='h':
            contH = contH+1
        elif i =='H':
            contH1 = contH1+1
        elif i =='I':
            contI = contI+1
        elif i =='i':
            contI1 = contI1+1
        elif i =='J':
            contJ = contJ+1
        elif i =='j':
            contJ1 = contJ1+1
        elif i =='K':
            contK = contK+1
        elif i =='k':
            contK1 = contK1+1
        elif i =='L':
            contL = contL+1
        elif i =='l':
            contL1 = contL1+1
        elif i =='M':
            contM = contM+1
        elif i =='m':
            contM1 = contM1+1
        elif i =='n':
            contN = contN+1
        elif i =='N':
            contN1 = contN1+1
        elif i =='O':
            contO = contO+1
        elif i =='o':
            contO1 = contO1+1
        elif i =='p':
            contP = contP+1
        elif i =='P':
            contP1 = contP1+1
        elif i =='Q':
            contQ = contQ+1
        elif i =='q':
            contQ1 = contQ1+1
        elif i =='r':
            contR = contR+1
        elif i =='R':
            contR1 = contR1+1
        elif i =='S':
            contS = contS+1
        elif i =='s':
            contS1 = contS1+1
        elif i =='T':
            contT = contT+1
        elif i =='t':
            contT1 = contT1+1
        elif i =='U':
            contU = contU+1
        elif i =='u':
            contU1 = contU1+1
        elif i =='V':
            contV = contV+1
        elif i =='v':
            contV1 = contV1+1
        elif i =='w':
            contW = contW+1
        elif i =='W':
            contW1 = contW1+1
        elif i =='x':
            contX = contX+1
        elif i =='X':
            contX1 = contX1+1
        elif i =='Y':
            contY = contY+1
        elif i =='y':
            contY1 = contY1+1
        elif i =='z':
            contZ = contZ+1
        elif i =='Z':
            contZ1 = cont1+1
      
    print('número de a minuscula: ',contA,
          'numero de A maiusculo: ',contA1,'número de B minuscula: ',contB,
          'numero de B maiusculo: ',contB,'número de C minuscula: ',contC,
          'numero de C maiusculo: ',contC1,'número de D minuscula: ',contD,
          'numero de D maiusculo: ',contD1,'número de E minuscula: ',contE,
          'numero de E maiusculo: ',contE1,'número de F minuscula: ',contF1,
          'numero de F maiusculo: ',contF,'número de G minuscula: ',contG,
          'numero de G maiusculo: ',contG1,'número de H minuscula: ',contH,
          'numero de H maiusculo: ',contH1,'número de I minuscula: ',contI,
          'numero de I maiusculo: ',contI1,'número de J minuscula: ',contJ1,
          'numero de J maiusculo: ',contJ,'número de K minuscula: ',contK1,
          'numero de K maiusculo: ',contK,'número de L minuscula: ',contL1,
          'numero de L maiusculo: ',contL,'número de M minuscula: ',contM1,
          'numero de M maiusculo: ',contM,'número de N minuscula: ',contN1,
          'numero de N maiusculo: ',contN,'número de O minuscula: ',contO1,
          'numero de O maiusculo: ',contO1,'número de P minuscula: ',contP1,
          'numero de P maiusculo: ',contP1,'número de Q minuscula: ',contQ1,
          'numero de Q maiusculo: ',contQ,'número de R minuscula: ',contR,
          'numero de R maiusculo: ',contR1,'número de S minuscula: ',contS1,
          'numero de S maiusculo: ',contS,'número de T minuscula: ',contT1,
          'numero de T maiusculo: ',contT,'número de U minuscula: ',contU1,
          'numero de U maiusculo: ',contU,'número de V minuscula: ',contV1,
          'numero de V maiusculo: ',contV,'número de W minuscula: ',contW,
          'numero de W maiusculo: ',contW1,'número de X minuscula: ',contX,
          'numero de X maiusculo: ',contX1,'número de Y minuscula: ',contY1,
          'numero de Y maiusculo: ',contY,'número de Z minuscula: ',contZ,
          'numero de Z maiusculo: ',contZ1,)
    
    

    
    print('Número de espaços vazios: ',contes,
          '\nNúmero de Letras Maiusculas: ',cont,
          '\nNúmero de letras Minusculas; ',contM)
def main(): #Função onde se rodam as outras e gera o 
    a = Arq()
    leitor(a)

main() 
