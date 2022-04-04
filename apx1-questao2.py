#Subprogramas
def escrever(qtd):
    for ind in range(qtd):
        nome = str(input('Digite seu nome Completo: ')).strip()
        nomeLista = nome.split()
        sobrenome = nomeLista[len(nomeLista)-1]
        nomeCompleto = nomeLista[0] + ' ' + sobrenome
        print(nomeCompleto)
    
#Programa principal
quantidadeDeNomes = int(input('Digite a quantidade de nomes que deseja imprimir: '))
escrever(quantidadeDeNomes)

