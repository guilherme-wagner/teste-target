string = input("Digite a string que deseja inverter: ")

string_invertida = ""
for char in string:
    string_invertida = char + string_invertida


print(f"String original: {string}")
print(f"String invertida: {string_invertida}")
