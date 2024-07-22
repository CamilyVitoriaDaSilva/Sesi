conjunto = {1,1,1,1,1,1,2,3,4,5,6,7}
#não mostra números repetidos
print (conjunto)
#criar um conjunto vazio
meu_conjunto = set ()
print(meu_conjunto)
#remover item do conjunto
conjunto.remove(2)
print (conjunto)
#verificando um elemento no conjunto
meu_conjunto = {7,8,9}
print("tem o 7 no conjunto:",7 in meu_conjunto)# retorna verdadeiro ou falso
print("tem o 10 no conjunto:",10 in meu_conjunto)# retornar falso
#operação com conjunto - UNIÃO
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
uniao =  conjunto01 | conjunto02
print("União do 1 com o 2",uniao)
#operação com conjunto - INTERSEÇÃO
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
intersecao =  conjunto01 & conjunto02
print("intersecao do 1 com 2:",intersecao)
#operação com conjunto - deferença 
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
diferenca =  conjunto01 - conjunto02
print("diferença (o que esta no conjunto 1 ):",diferenca)
#operação com conjunto - SIMETRICA
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
simetrica =  conjunto01 ^ conjunto02
print("simetria dos dois conjuntos",simetrica)
#len() retorna número de intes
#clear() limpa
#copy() copia
#operação com conjunto - LEN
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
len = len(conjunto01)
print("retornar números de itens",len)
#operação com conjunto - CLEAR
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
clear =  conjunto01.clear(clear)
print("conjunto usando clear",clear)



