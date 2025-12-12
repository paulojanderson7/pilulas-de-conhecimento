lista = ['maçã', 'abacate', 'abacaxi']

iterador = iter(lista)

print(iterador)

print(next(iterador))
#> <list_iterator object at 0x77bca1e90040>

print(next(iterador))
#> maçã

print(next(iterador))
#> abacate

print(next(iterador))
#> abacaxi

print(next(iterador))
#> Traceback ... StopIteration
