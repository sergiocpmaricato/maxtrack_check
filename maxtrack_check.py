from sys import argv
from sys import exit
from time import sleep
from requests import get

# Versão 1.1

# Cores para a mensagem de erro.
class ErroColor:
    ERRO = '\033[91m'
    FIM = '\033[0m'
    OK = '\033[1;92m'

try:
    ID_CLIENT = argv[1]
    ID_MODULOS = argv[2:]

except:
    # Verificando se o parâmetro foi passado.
    print(ErroColor.ERRO + 'Parâmetro ausente' + ErroColor.FIM)
    print('Informe o ID do cliente e dos módulos.')
    print('Exemplo: {} [ID do cliente] [IDs dos módulos]'.format(
        argv[0]))
    exit(1)


if len(ID_MODULOS) > 1:
    print(f'Iniciando pesquisa em {len(ID_MODULOS)} modulos.')
else:
    print(f'Iniciando pesquisa em {len(ID_MODULOS)} modulo.')


while True:
    try:    
        mirror_primario = get('http://50.30.39.2:' + ID_CLIENT + '06/')
        sleep(1)
        mirror_secundario = get(
            'http://85.25.19.214:' + ID_CLIENT + '06/')
        sleep(1)

    except:
        print(ErroColor.ERRO + 'Erro ao carregar a pagina, tentando novamente.' + ErroColor.FIM)
    for ID_MODULO in ID_MODULOS:
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