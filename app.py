import os

class colors:
    cyan = '\033[1;36m'
    white = '\033[1;97m'
    yellow = '\033[1;33m'
    end = '\033[0m'
    green = '\033[92m'
    red = '\033[1;91m'

def mensagens_login_e_cadastro():
    print(colors.white + 'BEM-VINDO(A) AO VALIDADOR DE LOGIN' + colors.end)
    print(colors.yellow + '-' * 40)
    print('[1] - CADASTRAR NOVO USUÁRIO')
    print('[2] - REALIZAR LOGIN')
    print('-' * 40 + colors.end)

def recebe_opcao_digitada():
    opcao_digitada = input(
        colors.white + 'Digite alguma das opções acima:' + colors.end)
    return opcao_digitada

def recebe_usuario_senha():
    usuario = input(f'Digite o {colors.white} usuario:' + colors.end)
    senha = input(f'Digite a {colors.white} senha:' + colors.end)
    return usuario, senha

def cadastrar_usuario():
    while True:
        usuario, senha = recebe_usuario_senha()

        with open('cad_usuario.txt', 'r') as arquivo:
            for linha in arquivo:
                if usuario in linha:
                    print(colors.red + 'NOME DE USUÁRIO NÃO DISPONÍVEL' + colors.end)
                    break

            if usuario not in linha:
                    with open('cad_usuario.txt', 'a', newline='') as arquivo:

                        arquivo.write(usuario + ',' + senha + os.linesep)

                    print(colors.green +
                        'USUÁRIO CADASTRADO COM SUCESSO' + colors.end)
                    return False

def logar_usuario():
    while True:
        print('OK, REALIZE O LOGIN:\n')
        usuario, senha = recebe_usuario_senha()
        login = usuario + ',' + senha + '\n'

        with open('cad_usuario.txt', 'r') as arquivo:
            for linha in arquivo:
                if linha == login:
                    print(colors.green + 'LOGIN OK' + colors.end)
                    break

            if linha == login:
                return False

            elif linha != login:
                print(colors.red + 'VERIFIQUE AS CREDENCIAIS DIGITADAS' + colors.end)

#### CODE MAIN ####

mensagens_login_e_cadastro()
if recebe_opcao_digitada() == "1":
    cadastrar_usuario()
else:
    logar_usuario()
