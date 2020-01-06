#!/usr/bin/python3
import sys
import requests
from time import sleep

# Cores para a mensagem de erro.


class ErroColor:
    ERRO = '\033[91m'
    FIM = '\033[0m'
    OK = '\033[1;92m'


try:
    ID_MODULO = sys.argv[2]
    ID_CLIENT = sys.argv[1]

except:

    # Verificando se o parâmetro foi passado.
    print(ErroColor.ERRO + 'Parâmetro ausente' + ErroColor.FIM)
    print('Informe o ID do módulo.')
    print('Exemplo: {} [ID do cliente ] [ID do módulo]'.format(
        sys.argv[0]))
    sys.exit()


while True:
    mirror_primario = requests.get('http://50.30.39.2:' + ID_CLIENT + '06/')
    mirror_secundario = requests.get(
        'http://85.25.19.214:' + ID_CLIENT + '06/')

    if ID_MODULO in mirror_primario.text:
        print(f'O modulo {ID_MODULO} está' + ErroColor.OK +
              ' Online ' + ErroColor.FIM + 'no Mirror Primário.')
    elif ID_MODULO in mirror_secundario.text:
        print(f'O modulo {ID_MODULO} está' + ErroColor.OK +
              ' Online ' + ErroColor.FIM + 'no Mirror Secundário.')
    else:
        print(f'O modulo {ID_MODULO} parece estar' +
              ErroColor.ERRO + ' Offline.' + ErroColor.FIM)
    sleep(5)
