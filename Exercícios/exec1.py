def func_fibonnaci(n):
    var_loop = True
    var_fibonnaci = [0, 1]  # Inicia a sequência com 0 e 1 em uma Lista
    while var_loop:
        prox_num = var_fibonnaci[-1] + var_fibonnaci[-2] # Soma dos números anteriores
        if prox_num > n:
            var_loop = False # Quebra o looping pra não fazer fibonnaci infinito
        var_fibonnaci.append(prox_num) # Adiciona o número a lista
    return var_fibonnaci

def pertence(num):
    var_fibonnaci = func_fibonnaci(num)  # Gera a sequência até o número informado
    return num in var_fibonnaci


if __name__ == "__main__": # Executando as funções
    try: 
        prova_num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: ")) # Pegando o número informado já transformando em inteiro (Nota: se colocar uma String vai dar erro)
    
        if pertence(prova_num):
            print(f"O número {prova_num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {prova_num} não pertence à sequência de Fibonacci.")
    except:
        print("Por favor informar um número.")