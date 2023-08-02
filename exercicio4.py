#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    for i in lista:
        record = 0
        for j in lista:
            if i == j and record != 0:
                return True
            elif i == j and record == 0:
                record += 1






# Teste a sua função aqui (caso ache necessário)










