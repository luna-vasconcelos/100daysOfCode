# declaração das variáveis
pi = 3.14159
R = float(input())
A = pi * R**2

# imprimindo o resultado de diferentes formas:
# normal, com todas as casas decimais
print("A=",A)
# normal, com todas as casas decimais usando o .format
print("A = {}".format(A))
# 
print(f"A= {A:.4f}")
# 
print("A= {:.4f}".format(A))
