## 02. Pydantic - Serialização

Serialização é o processo de converter objetos em memória para uma representção em strings ou bytes.

Isso é muito comum para permitir um armazenamento, ou transmissão dos dados que compoem esse objeto.

No Pydantic a serialização significa converter modelos Pydantic para uma representação em dicionário ou em strings compatíveis com o formato JSON.

A forma mais comum de fazer isso é por meio do método model_dump():

```python
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
# nesse caso o resultado é um dicionário (dict).

print(p.model_dump_json())
#> {"nome":"João","idade":30,"altura":1.74}
# nesse caso o resultado é uma sting JSON.
```

**Para que é usado:**<br>
Quando nossa aplicação vai interajir com outras aplicações ou sistemas externos é comum enviar dados em um formato universal como o JSON.<br>

Sem o Pydantic seria necessário fazer essas conversões de forma manual para cada tipo de dado que seria enviado para sistemas externos, inclusive para tipos como `datetime`, `enum` entre outros.