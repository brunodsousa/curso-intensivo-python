"""
5.2 - Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e
acrescente-os em conditional_tests.py. 
Tenha pelo menos um resultado True e um False para cada um dos casos a seguir: 
• testes de igualdade e de não igualdade com strings; ok
• testes usando a função lower(); ok
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e
menor ou igual a; 
• testes usando as palavras reservadas and e or; 
• testes para verificar se um item está em uma lista; 
• testes para verificar se um item
não está em uma lista.
"""

name = "Bruno"
number = 7
list = ["cachorro", "gato", "elefante", "girafa"]

print(name == "Bruno")
print(name == "José")
print(name != "José")
print(name != "Bruno")
print(name.lower() == "bruno")
print(name.lower() != "bruno", "\n")

print(number == 7)
print(number == 14)
print(number != 21)
print(number != 7)
print(number > 2)
print(number > 28)
print(number < 42)
print(number < 5)
print(number >= 5)
print(number >= 35)
print(number <= 10)
print(number <= 5, "\n")

print(name == "Bruno" and number == 7)
print(name == "Bruno" and number != 7)
print(name.upper() == "JOSÉ" or number >= 5)
print(name.lower() == "buba" or number != 7, "\n")

print("cachorro" in list)
print("cavalo" in list)
print("cavalo" not in list)
print("cachorro" not in list)
