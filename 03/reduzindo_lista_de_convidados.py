"""
3.7 - Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa.
"""

people = ["Molly", "Taiãma", "Nena", "Rita", "Daniela", "Laura", "Baltazar"]
print(people)

print("Cadê a minha mesa? Só tem espaço para dois convidados.")

baltazar = people.pop()
print("Foi mal, " + baltazar + ". O jantar não vai rolar, não entregaram a minha mesa. ¯\_(ツ)_/¯")
laura = people.pop()
print("Foi mal, " + laura + ". O jantar não vai rolar, não entregaram a minha mesa. ¯\_(ツ)_/¯")
daniela = people.pop()
print("Foi mal, " + daniela + ". O jantar não vai rolar, não entregaram a minha mesa. ¯\_(ツ)_/¯")
rita = people.pop()
print("Foi mal, " + rita + ". O jantar não vai rolar, não entregaram a minha mesa. ¯\_(ツ)_/¯")
nena = people.pop()
print("Foi mal, " + nena + ". O jantar não vai rolar, não entregaram a minha mesa. ¯\_(ツ)_/¯")

print(people)

print("Bora jantar, " + people[-1] + ".")
print("Bora jantar, " + people[0] + ".")

del people[-1]
del people[0]

print(people)