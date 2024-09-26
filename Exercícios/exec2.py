def contador(palavra):
    count = palavra.lower().count('a')  # Converte a string para minúsculas e conta os "as" que tem nela.
    return count

if __name__ == "__main__": # Executando a função

    string_input = input("Digite uma string para verificar a letra 'a': ")
    
    count = contador(string_input)  # Conta a letra 'a'
    
    if count > 0: # Caso tenha um A ele printa o texto abaixo
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    elif string_input.isdigit(): # Pegando possivel erro com número digitado acima.
        print("Digite uma palavra.")
    else: # Caso não tenha A ele printa o texto abaixo
        print("A letra 'a' NÃO aparece na string.")