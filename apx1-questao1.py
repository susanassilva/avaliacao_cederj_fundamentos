#Subprogramas
def menorNumero(valores):
    valorMenor = valores[0]
    for k in valores:
        if k < valorMenor:
            valorMenor = k
    return valorMenor

def maiorNumero(valores):
    valorMaior = valores[0]
    for j in valores:
        if j > valorMaior:
            valorMaior = j
    return valorMaior

def totalNumeros(valores):
    j = 0
    total = 0
    while j < len(valores):
        total += valores[j] 
        j+=1
    return total


#ProgramaPrincipal
resultado = 0 
qtd = 0
tamanho = 0 
inserir = input()
while inserir != "":
    numeros = list(map(float, inserir.split()))
    resultado += totalNumeros(numeros)
    menor = menorNumero(numeros)
    maior = maiorNumero(numeros)
    print(f'Menor: {menor}, Maior: {maior}')
    tamanho += len(numeros)  
    inserir = input()
    qtd += 1
    
print(f'Quantidade de Números Lidos {tamanho}')
media = resultado / tamanho
if qtd == 0:
    print('Nenhum Número Foi Lido. Portanto, não existe média!!!')
else: 
    print(f'Média dos Números Lidos: {round(media, 2)}')
