nome = input("Digite seu nome: ") 

ano = int( input("Digite o seu ano de nascimento: ") ) #Forma de declaração de váriavel e o seu tipo.

#saída de dados:
print(f"Olá {nome} este ano você está fazendo {2025 - ano} anos, parabéns!") #Colocar um f antes das aspas no print permite incluir  espressões dentro de uma string e que elas sejam substituidas por seus valores

if (2025 - ano) >= 18:
    print("Certo, você está autorizado a habilitação de motorista!")
else:
    print("Aguarde maior idade!")  