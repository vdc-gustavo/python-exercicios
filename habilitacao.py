idade = input("Insira sua idade: ")

if (idade >= 18):
    print("Você pode tirar a carteira de habilitação!")
elif (idade >= 18 and idade <= 25):
    print("Você pode tirar a carteira de habilitação, porém o seguro será mais caro enquanto for menor de 25 anos.")
else:
    print("Você é menor de idade e não pode tirar habilitação!")

