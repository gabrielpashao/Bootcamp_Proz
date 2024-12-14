executar = True

while executar:
    print("Digite seu nome completo: ")
    nome_completo = input()

    while True:
        try:
            ano_nasc = int(input("Digite o ano que você nasceu: "))
            if 1922 <= ano_nasc <= 2021:
                break
            else:
                print("Erro: Ano inválido. Tente novamente.")
        except ValueError:
            print("Erro: Informe um ano válido")
    
    idade = 2024 - ano_nasc
    print(f"Nome: {nome_completo}\nIdade: {idade}")
    executar == False
   

