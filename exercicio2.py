#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    resposta = []
    for i in lista:
        if resposta != []:
            resposta.append(resposta[-1] + i)
        else:
            resposta.append(i)
    return resposta
        
        





# Teste a sua função aqui (caso ache necessário)

cumulativo([2, 3, 4, 5])









