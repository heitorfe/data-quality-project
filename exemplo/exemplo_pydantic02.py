from pydantic import BaseModel, PositiveInt, validate_call # type: ignore


class NumeroPositivo(BaseModel):
    numero: PositiveInt
    
@validate_call   # liga o validador
def soma_numeros_positivos(x: NumeroPositivo, y:NumeroPositivo) -> NumeroPositivo:
    return x + y

print(soma_numeros_positivos(4, 5))
print(soma_numeros_positivos(4, -5))
print(soma_numeros_positivos(-4, 5))
