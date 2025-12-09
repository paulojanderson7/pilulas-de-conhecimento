from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    idade: int
    altura: float 

p = Pessoa(nome='João', idade=30, altura=1.74)

print(p)
#> nome='João' idade=30 altura=1.74

print(p.model_dump())
#> {'nome': 'João', 'idade': 30, 'altura': 1.74}
# nesse caso o resultado é um dicionário Python.

print(p.model_dump_json())
#> {"nome":"João","idade":30,"altura":1.74}
# nesse caso o resultado é uma sting JSON.