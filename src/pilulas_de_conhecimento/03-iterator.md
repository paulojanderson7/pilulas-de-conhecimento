## 03. Iterador e Iterável

De forma geral um Iterador é um objeto que permite acesso de forma *progressiva* aos itens que fazem parte de uma coleção Iterável de itens .

Em Python um objeto é **iterável** se tem o método .__iter__(). 
Já um **iterador** é o objeto resultado do método .__iter__() executado em um iterável.
Além disso, o **iterador** tem o método .__next__() que fornece o próximo item da sequência.  

É possível criar um iterador a partir de uma lista, tuple, dicionários (que são exemplos de coleções de itens iteráveis).
E com isso ter acesso de modo progressivo, ou *percorrer*, cada elemento dessa coleção usando o método next() 

Isso é feito da seguinte forma:

```python
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
```

**Para que é usado:**<br>
Iteradores são a base da implementação de laços (*loops*), Compreensões de lista (*list comprehensions*), expressões geradoras e outros.

Com eles é possível processar uma sequência de dados de forma eficiente, sem ter que carregar todos os itens daquela sequencia em memória de uma vez só.


**Bônus**:

Ao acessar um arquivo de texto com muitas linhas, se fizermos `list(arquivo)` o conteúdo inteiro do arquivo será carregado na memória.

Porém, se aberto corretamente, ao fazermos um `for linha in arquivo` apenas 1 linha por vez do arquivo será carregada e processada.
Por trás disso há o uso de Iteradores.  