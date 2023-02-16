idade = int(input("Digite a sua idade"))
dinheiro = int(input('digite a quantidade de dinheiro que voce tem: '))
carteira = input('Voce tem carteira de motorista? (s/n')

if (idade >= 18 and dinheiro >= 50) or carteira == "s":
    print("VocÊ pode alugar o carro.")
else:
    print("Você não pode alugar o carro.")