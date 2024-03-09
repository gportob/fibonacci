def is_perfect_square(n):
    # Função auxiliar para verificar se um número é um quadrado perfeito
    sqrt_n = int(n**0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(num):
    # Função para verificar se um número pertence à sequência de Fibonacci
    if num < 0:
        return False
    
    # Um número é um número de Fibonacci se e somente se pelo menos um dos 5 * num^2 + 4 ou 5 * num^2 - 4 é um quadrado perfeito
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

# Solicitar um número do usuário
numero = int(input("Informe um número: "))

# Verificar se o número pertence à sequência de Fibonacci
if is_fibonacci_number(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
