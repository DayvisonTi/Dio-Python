def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor , combustivel)

# valido
criar_carro(modelo="Toro",ano=2020, placa="ABC-1234", marca="Fiat", motor="2.0", combustivel="Diesel")
# invalido
criar_carro("Toro",2020, "ABC-1234", marca="Fiat", motor="2.0", combustivel="Diesel")