from src.restaurante import Restaurante

restaurante_praca = Restaurante('Restaurante da Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 8)
restaurante_praca.receber_avaliacao('Pedro', 7)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()


