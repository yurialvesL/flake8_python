from fila_normal import Filanormal
from fila_prioritaria import FilaPrioritaria


"""fila_teste = Filanormal()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamacliente(5))"""


fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(15))
print(fila_teste_2.chama_cliente(1))
print(fila_teste_2.estatistica('10/01/2022', 198, 'detail'))
