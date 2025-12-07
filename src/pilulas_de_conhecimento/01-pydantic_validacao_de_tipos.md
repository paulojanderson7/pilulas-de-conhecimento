## 01. Pydantic - Validação de Tipos<br>

O Pydantic é uma biblioteca Python utilizada para validação de tipos.<br>
Quando criamos um modelo, podemos herdá-lo da classe pydantic.BaseModel e especificar os atributos e seus tipos.<br>
Dessa forma, ao criar uma instância dessa classe, o Pydantic faz uma validação dos tipos dos atributos.<br>

```python
from pydantic import BaseModel, ValidationError

class Pessoa(BaseModel):
    nome: str
    idade: int
    altura: float 

try:
    pessoa_valida = Pessoa(
        nome='João',
        idade=30,
        altura=1.74,
    )

    print(f'Pessoa válida: {pessoa_valida.nome}, {pessoa_valida.idade}, {pessoa_valida.altura}')
    #> Pessoa válida: João, 30, 1.74

    pessoa_invalida = Pessoa(
        nome='José',
        idade='trinta',
        altura='um metro e setenta',
    )
    #> Erro de validação: 2 validation errors for Pessoa
    # idade
    # Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='trinta', input_type=str]
    # altura
    # Input should be a valid number, unable to parse string as a number [type=float_parsing, input_value='um metro e setenta', input_type=str]

except ValidationError as e:
    print(f'Erro de validação: {e}')
```

**Para que é usado:**<br>
Na criação de API's é comum definir o *Schema*, ou seja, o que se espera como parâmetros de entrada daquela requisição.<br>
Com isso, ao receber uma requisição na API, o Pydantic valida os tipos dos parâmetros passados.<br>
Caso o usuário enviar um parâmetro inválido, a aplicação não quebra tentando tratar algo para a qual não foi programada.<br>
Além disso, é possivel retornar ao solicitante uma mensagem **422 Unprocessable Entity.** indicando que houve um erro de validação.