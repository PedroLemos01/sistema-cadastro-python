pessoas = []
proximo_id = 1


def cadastrar_pessoa():
    global proximo_id

    print("\n=== NOVO CADASTRO ===")

    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    pessoa = {
        "id": proximo_id,
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone,
        "email": email
    }

    pessoas.append(pessoa)

    print(f"\nPessoa cadastrada com sucesso!")
    print(f"ID do cadastro: {proximo_id}")

    proximo_id += 1


def listar_pessoas():
    if len(pessoas) == 0:
        print("\nNenhuma pessoa cadastrada.")
        return

    print("\n=== PESSOAS CADASTRADAS ===")

    for pessoa in pessoas:
        print(f"\nID: {pessoa['id']}")
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"CPF: {pessoa['cpf']}")
        print(f"Telefone: {pessoa['telefone']}")
        print(f"E-mail: {pessoa['email']}")


def buscar_pessoa():
    if len(pessoas) == 0:
        print("\nNenhuma pessoa cadastrada.")
        return

    try:
        id_busca = int(input("\nDigite o ID que deseja buscar: "))
    except ValueError:
        print("\nDigite um ID válido.")
        return

    for pessoa in pessoas:
        if pessoa["id"] == id_busca:
            print("\n=== PESSOA ENCONTRADA ===")
            print(f"ID: {pessoa['id']}")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Telefone: {pessoa['telefone']}")
            print(f"E-mail: {pessoa['email']}")
            return

    print("\nNenhum cadastro encontrado com esse ID.")


def editar_pessoa():
    if len(pessoas) == 0:
        print("\nNenhuma pessoa cadastrada.")
        return

    try:
        id_busca = int(input("\nDigite o ID que deseja editar: "))
    except ValueError:
        print("\nDigite um ID válido.")
        return

    for pessoa in pessoas:
        if pessoa["id"] == id_busca:
            print("\n=== EDITAR CADASTRO ===")
            print("Pressione Enter para manter o valor atual.\n")

            nome = input(f"Nome [{pessoa['nome']}]: ")
            idade = input(f"Idade [{pessoa['idade']}]: ")
            cpf = input(f"CPF [{pessoa['cpf']}]: ")
            telefone = input(f"Telefone [{pessoa['telefone']}]: ")
            email = input(f"E-mail [{pessoa['email']}]: ")

            if nome:
                pessoa["nome"] = nome

            if idade:
                pessoa["idade"] = idade

            if cpf:
                pessoa["cpf"] = cpf

            if telefone:
                pessoa["telefone"] = telefone

            if email:
                pessoa["email"] = email

            print("\nCadastro atualizado com sucesso!")
            return

    print("\nNenhum cadastro encontrado com esse ID.")


def excluir_pessoa():
    if len(pessoas) == 0:
        print("\nNenhuma pessoa cadastrada.")
        return

    try:
        id_excluir = int(input("\nDigite o ID que deseja excluir: "))
    except ValueError:
        print("\nDigite um ID válido.")
        return

    for pessoa in pessoas:
        if pessoa["id"] == id_excluir:
            print(f"\nCadastro encontrado: {pessoa['nome']}")

            confirmacao = input("Tem certeza que deseja excluir? (s/n): ")

            if confirmacao.lower() == "s":
                pessoas.remove(pessoa)
                print("\nCadastro excluído com sucesso!")
            else:
                print("\nExclusão cancelada.")

            return

    print("\nNenhum cadastro encontrado com esse ID.")


while True:
    print("\n================================")
    print("       SISTEMA DE CADASTRO")
    print("================================")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Editar cadastro")
    print("5 - Excluir cadastro")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_pessoa()

    elif opcao == "2":
        listar_pessoas()

    elif opcao == "3":
        buscar_pessoa()

    elif opcao == "4":
        editar_pessoa()

    elif opcao == "5":
        excluir_pessoa()

    elif opcao == "6":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida. Escolha uma opção de 1 a 6.")
