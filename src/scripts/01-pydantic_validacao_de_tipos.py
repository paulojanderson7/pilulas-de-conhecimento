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