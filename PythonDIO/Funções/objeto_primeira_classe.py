import re
def somar(a, b, o="-"):
    match(o):
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
            
    
def resultado(a, b, soma):
    result = soma(a, b)
    print(f"O resultada da operação {a} + {b} = {result}")

# dentro da funcão "resultado" usa a função somar como parâmetro sem chamar com "()"
# se chamar a função "somar" dá erro pois ela vai pedir dois parâmetros "a" e "b"
resultado(10, 10, somar)

#atribui a variavel a função somar e assim a variavel pode passar parâmetros tomando lugar do "somar"
op = somar
print(op(1, 25))