import json


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

