# Main será usado para orquestrar os outros scripts python
# Executar o pré-processamento nas imagens
# TALVEZ, fazer o data augmentation
# rodar o treino
# rodar o test
# criar o csv final com as respostas

import preProcessImage


def main():
    preProcessImage.main()


if __name__ == '__main__':
    main()
