def verificaTipo(entrada):
    tipoEntrada = type(entrada)
    transformaFloat(entrada)

def transformaFloat(entrada):
    if '..' in entrada:
        print('Há mais do que um "."')
    try: 
        output = float(entrada)
        print(output)
        conversaoMoeda(output)
        return True
    except ValueError:
        i = 0
        while i < len(entrada):
            if entrada[i].isalpha() == True:
                print(f'Você digitou errado, {entrada} não é do tipo float. \nNa posição {i+1} há o caracter {entrada[i]}.') #A posição i foi somada a 1 para o usuário se localizar caso conte de 1 até n, e não de 0 até n.
                break
            else:
                i+=1
                
def conversaoMoeda(output):
    taxa = float(input('Digite a taxa de conversão: '))
    real = output * taxa
    print(f'o valor {output} USD com a taxa de {taxa} vai para {round(real, 3)}BRL')
    verificaParcelamento(real)

def aplicaDesconto(descontado):
    valorDesconto = descontado - (descontado * 0.15)
    return (round(valorDesconto, 3))    

def verificaParcelamento(valor):
    parcelar = int(input('Em quantas vezes deseja parcelar o produto? '))
    if parcelar == 1:
        descontado = aplicaDesconto(valor)
        print(f"Você ganhou 15% de desconto, portanto, de {valor} BRL, você vai pagar {descontado} BRL")
    else: 
        print(valor)
        juros = 5/100
        resultadoFinal = (valor * ((1 + juros) ** parcelar))
        resultadoParcelas = resultadoFinal/parcelar
        print(f'Pagando em {parcelar} parcelas, e com 5% de juros ao mês, você pagará {round(resultadoParcelas, 2)} BRL por mês, sendo o total de {round(resultadoFinal, 2)}BRL')



#Programa Principal
entrada = input('Digite o valor do produto: ')
verificaTipo(entrada)
