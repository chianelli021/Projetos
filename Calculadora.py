#Calculadora

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação: ")
match operacao:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2

print(f"Resultado: {res}")

