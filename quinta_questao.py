string = "ola mundo"

string_invertida = string[::-1]
#Slicing da string de forma decrescente, começando do fim até o ínicio
#O primeiro ":" indica que não foi definido um valor de início, então começa do final da string.
# - O segundo ":" também não define o valor de fim, então vai até o início da string.
# - O "-1" indica que a string será reconstruída de forma inversa.
print(string_invertida)