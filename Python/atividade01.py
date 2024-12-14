def calculator(num1, num2, op):
  match op:
    case 1:
      res = num1 + num2
      return res
    case 2:
      res = num1 - num2
      return res
    case 3:
      res = num1 * num2
      return res
    case 4:
      if num2 != 0:
        res = num1 / num2
        return res
      else:
        res = "Erro: Divisão por 0"
        return res
    case _:
      res = 0
      return res

print(calculator(10, 5, 1))
print(calculator(10, 5, 2))
print(calculator(10, 5, 3))
print(calculator(10, 5, 4))
print(calculator(10, 5, 5))