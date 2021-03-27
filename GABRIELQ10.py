class conta: #Classe conta corrente
    def __init__(self,numero,saldo):#Geradora
        self.numero = numero
        self.saldo =0
    def saque(self,saldo): #Modulo para realizar saques
        saldo = saldo
        a = float(input('Insira o valor a ser sacado: '))
        if a>saldo:
            ValueError
            print('Impossivel realizar esse saque, tente novamente.')
            return saldo
        else:
            u = saldo - a
            print('O valor sacado foi de: ',a,'Em sua conta restam: ',u)
            return u
    def deposito(self,saldo):#Modulo que realiza deposito
        saldo = saldo
        a = float(input('Insira o valor a ser depositado: '))
        saldo = saldo +a
        print(saldo)
        return saldo
a =conta(numero = '3213123',saldo =0)#conta que usamos de prova

def menu():#menu do caixa
    print('''
            1 Sacar
            2 Depositar
            3 encerrar
            4 mostrar saldo
                     ''')
    w = str(input('Insira sua opção: '))
    
    b = a.saldo
    
    while w != '3':
        if w =='1':
            b = a.saque(b)
        if w =='2':
            b = a.deposito(b)
            print('Obrigado pelo deposito!')
        if w =='4':
            print(b)
        w = str(input('Insira sua opção: '))
    print('Obrigado por usar nossos serviços')

def main():#função onde o programa roda
    menu()


main()
