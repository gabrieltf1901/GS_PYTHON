import json
from datetime import datetime
import secrets


def salvar_dados_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)


def carregar_dados_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def cadastrar_usuario():
    usuarios = carregar_dados_usuarios()

    while True:
        nome_usuario = input("Digite seu nome de usuário: ")
        if nome_usuario not in usuarios:
            break
        else:
            print("Nome de usuário já existe. Tente novamente.")

    nome_completo = input("Digite seu nome completo: ")
    genero = input("Digite seu gênero: ")
    senha = input("Digite sua senha: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    cep = input("Digite seu CEP: ")
    endereco = input("Digite seu endereço: ")
    cpf = input("Digite seu CPF: ")
    rg = input("Digite seu RG: ")
    convenio = input("Digite o nome do convênio (SE APLICÁVEL): ")
    n_convenio = input("Digite o número do convênio (SE APLICÁVEL): ")

    usuarios[nome_usuario] = {
        "nome_completo": nome_completo,
        "genero": genero,
        "senha": senha,
        "telefone": telefone,
        "email": email,
        "cep": cep,
        "endereco": endereco,
        "cpf": cpf,
        "rg": rg,
        "convenio": convenio,
        "n_convenio": n_convenio
    }

    salvar_dados_usuarios(usuarios)
    print("Cadastro realizado com sucesso!")


def fazer_login():
    usuarios = carregar_dados_usuarios()
    tentativas = 10

    while tentativas > 0:
        id_usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if id_usuario in usuarios and usuarios[id_usuario]["senha"] == senha:
            print("Login bem-sucedido!")
            return usuarios[id_usuario]  # Retorna as informações do usuário
        else:
            tentativas -= 1
            print(f"Nome de usuário ou senha incorretos. Tentativas restantes: {tentativas}")

    print("Número máximo de tentativas alcançado. Saindo do programa.")
    return None  # Retorna None se o login falhar


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False


def agendar_consulta(usuario):
    if usuario is not None:
        while True:
            data = input("Digite a data da consulta (DD/MM/AAAA): ")
            if validar_data(data):
                break
            else:
                print("Data inválida. Tente novamente.")

        while True:
            hora = input("Digite a hora da consulta (HH:MM): ")
            if validar_hora(hora):
                break
            else:
                print("Hora inválida. Tente novamente.")

        causas = input("Digite as causas da consulta: ")
        motivos = input("Digite os motivos da consulta: ")

        # Geração de um token aleatório
        token = secrets.token_hex(20)

        usuario["token_agendamento"] = token

        # Aqui você pode usar as informações do usuário, os dados da consulta e o token conforme necessário
        print(f"Consulta agendada para {data} às {hora}.")
        print(f"Causas da consulta: {causas}")
        print(f"Motivos da consulta: {motivos}")
        print(f"Token de confirmação: {token}")
        print(f"Guarde este token pois ele é a chave de entrada para sua consulta!")
    else:
        print("Usuário não logado. Faça o login antes de agendar uma consulta.")


def realizar_consulta(usuario):
    if usuario is not None:
        token_agendamento = input("Digite o token de agendamento: ")

        # Verifica o token
        if token_agendamento == usuario.get("token_agendamento"):
            print("Aguarde que você será redirecionado para a sala virtual da NotreDame Intermédica!")
        else:
            print("Token de agendamento inválido. A consulta não pode ser realizada.")
    else:
        print("Usuário não logado. Faça o login antes de realizar uma consulta.")


def menu_principal():
    usuario_logado = None

    while True:
        print("\n===== Menu Principal =====")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Agendar consulta")
        print("4. Realizar consulta")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            usuario_logado = fazer_login()
        elif opcao == 3:
            agendar_consulta(usuario_logado)
        elif opcao == 4:
            realizar_consulta(usuario_logado)
        elif opcao == 0:
            print("Encerrando programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()