estoque = [
    {"nome": "Notebook", "valor": 4500.0, "quantidade": 10, "categoria": "Informática"},
    {"nome": "Mouse", "valor": 45.90, "quantidade": 50, "categoria": "Informática"},
    {"nome": "Cadeira Gamer", "valor": 1200.0, "quantidade": 5, "categoria": "Móveis"},
    {"nome": "Monitor 24pol", "valor": 899.90, "quantidade": 8, "categoria": "Informática"},
    {"nome": "Teclado Mecânico", "valor": 350.0, "quantidade": 15, "categoria": "Informática"},
]


def ler_texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            print("Erro: este campo é obrigatório e não pode ficar vazio. Tente novamente.")
            continue
        return valor


def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = float(entrada.replace(",", "."))
        except ValueError:
            print("Erro: valor inválido. Digite um número (ex: 199.90).")
            continue

        if valor <= 0:
            print("Erro: o valor deve ser maior que zero.")
            continue

        return valor


def ler_quantidade(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            quantidade = int(entrada)
        except ValueError:
            print("Erro: quantidade inválida. Digite um número inteiro.")
            continue

        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
            continue

        return quantidade


def listar_produtos(lista_produtos):
    if not lista_produtos:
        print("\nNenhum produto cadastrado no momento.\n")
        return

    print()
    print(f"{'Nome':<20}{'Valor (R$)':<15}{'Quantidade':<15}{'Categoria':<20}")
    for produto in lista_produtos:
        print(
            f"{produto['nome']:<20}"
            f"R$ {produto['valor']:<12.2f}"
            f"{produto['quantidade']:<15}"
            f"{produto['categoria']:<20}"
        )
    print()


def cadastrar_produto(lista_produtos):
    print("\nCadastro de novo produto")
    nome = ler_texto_obrigatorio("Nome do produto: ")
    valor = ler_valor("Valor do produto: ")
    quantidade = ler_quantidade("Quantidade em estoque: ")
    categoria = ler_texto_obrigatorio("Categoria do produto: ")

    novo_produto = {
        "nome": nome,
        "valor": valor,
        "quantidade": quantidade,
        "categoria": categoria,
    }

    lista_produtos.append(novo_produto)
    print(f"\nProduto '{nome}' cadastrado com sucesso!\n")


def buscar_produto(lista_produtos):
    nome_buscado = ler_texto_obrigatorio("\nDigite o nome do produto que deseja buscar: ")

    encontrados = [
        produto for produto in lista_produtos
        if produto["nome"].lower() == nome_buscado.lower()
    ]

    if not encontrados:
        print(f"\nProduto '{nome_buscado}' não encontrado no estoque.\n")
        return

    print("\nProduto(s) encontrado(s):")
    listar_produtos(encontrados)


def buscar_produtos_por_categoria(lista_produtos):
    categoria_buscada = ler_texto_obrigatorio("\nDigite a categoria que deseja buscar: ")

    encontrados = [
        produto for produto in lista_produtos
        if produto["categoria"].lower() == categoria_buscada.lower()
    ]

    if not encontrados:
        print(f"\nCategoria '{categoria_buscada}' não encontrada no estoque.\n")
        return

    print(f"\nProduto(s) da categoria '{categoria_buscada}':")
    listar_produtos(encontrados)


def encontrar_categoria_maior_valor_total(lista_produtos):
    if not lista_produtos:
        print("\nNão há produtos cadastrados para analisar as categorias.\n")
        return

    totais_por_categoria = {}

    for produto in lista_produtos:
        categoria = produto["categoria"]
        valor_total_produto = produto["valor"] * produto["quantidade"]
        totais_por_categoria[categoria] = totais_por_categoria.get(categoria, 0) + valor_total_produto

    categoria_maior_valor = max(totais_por_categoria, key=totais_por_categoria.get)
    maior_valor_total = totais_por_categoria[categoria_maior_valor]

    print("\nValor total por categoria")
    for categoria, valor_total in totais_por_categoria.items():
        print(f"{categoria}: R$ {valor_total:.2f}")

    print("\nCategoria com maior valor total em estoque")
    print(f"Categoria: {categoria_maior_valor}")
    print(f"Valor total: R$ {maior_valor_total:.2f}")
    print()


def analisar_estoque(lista_produtos):
    if not lista_produtos:
        print("\nNão há produtos cadastrados para gerar a análise.\n")
        return

    total_produtos = len(lista_produtos)
    valor_total_estoque = sum(p["valor"] * p["quantidade"] for p in lista_produtos)
    total_itens = sum(p["quantidade"] for p in lista_produtos)

    produto_maior_valor = max(lista_produtos, key=lambda p: p["valor"])
    produto_menor_quantidade = min(lista_produtos, key=lambda p: p["quantidade"])

    print("\nAnálise do estoque")
    print(f"Quantidade de produtos cadastrados: {total_produtos}")
    print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")
    print(f"Produto com maior valor: {produto_maior_valor['nome']} (R$ {produto_maior_valor['valor']:.2f})")
    print(f"Produto com menor quantidade: {produto_menor_quantidade['nome']} ({produto_menor_quantidade['quantidade']} unid.)")
    print(f"Quantidade total de itens em estoque: {total_itens}")
    print()


def ordenar_produtos_por_valor(lista_produtos):
    lista_ordenada = sorted(lista_produtos, key=lambda p: p["valor"])
    print("\nProdutos ordenados por valor.")
    listar_produtos(lista_ordenada)
    return lista_ordenada


OPCOES_MENU = (
    "1  Listar produtos",
    "2  Cadastrar produto",
    "3  Buscar produto por nome",
    "4  Buscar produtos por categoria",
    "5  Exibir análise do estoque",
    "6  Ordenar produtos por valor",
    "7  Exibir categoria com maior valor total",
    "8  Sair",
)


def exibir_menu(opcoes_menu):
    print("\nMENU PRINCIPAL")
    for opcao in opcoes_menu:
        print(opcao)
    print()


def main():
    while True:
        exibir_menu(OPCOES_MENU)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos(estoque)

        elif opcao == "2":
            cadastrar_produto(estoque)

        elif opcao == "3":
            buscar_produto(estoque)

        elif opcao == "4":
            buscar_produtos_por_categoria(estoque)

        elif opcao == "5":
            analisar_estoque(estoque)

        elif opcao == "6":
            ordenar_produtos_por_valor(estoque)

        elif opcao == "7":
            encontrar_categoria_maior_valor_total(estoque)

        elif opcao == "8":
            print("\nEncerrando o sistema de controle de estoque.")
            break

        else:
            continue


if __name__ == "__main__":
    main()
