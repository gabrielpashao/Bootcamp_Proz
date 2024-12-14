def calculator():
    while True:
        print("Opções:\n")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        op = input("Digite o número da operação: ")

        if op == "0":
            print("Saindo da calculradora...")
            break
        elif op not in ["1", "2", "3", "4"]:
            print("Opção inválida.")
            continue

        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if op == "1":
            res = num1+num2
            operacao = "Soma"
        elif op == "2":
            res = num1-num2
            operacao = "Subtração"
        elif op == "3":
            res = num1*num2
            operacao = "Multiplicação"
        elif op == "4":
            if num2 != 0:
                res = num1/num2
                operacao = "Divisão"
            else:
                print("Erro: Divisão por zero!")
                continue
        
        print(f"{operacao}: {num1} {['+', '-', '*', '/'][int(op) - 1]} {num2} = {res:.2f}\n")

calculator()
            