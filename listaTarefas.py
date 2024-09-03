itens_concluidos = []
itens = []

# Adiciona uma Tarefa a lista itens
def adicionar_item():
    item = input("Insira o nome do item para adicionar à lista de tarefas: ")
    itens.append(item)
    print(f"Item '{item}' adicionado à lista de tarefas.")

# Remove uma Tarefa de uma lista selecionada
def remove_item():
    print("\nEscolha de qual lista deseja remover uma tarefa:")
    print("1. Tarefas não Finalizadas")
    print("2. Tarefas Concluídas")
    
    escolha = input("Digite o número correspondente à lista: ")

    if escolha == "1":
        lista = itens
        lista_nome = "Tarefas não Finalizadas"
    elif escolha == "2":
        lista = itens_concluidos
        lista_nome = "Tarefas Concluídas"
    else:
        print("Opção inválida. Tente novamente.")
        return

    if not lista:
        print(f"A lista '{lista_nome}' está vazia.")
        return
    
    for i, item in enumerate(lista, start=1):
        print(f"\n{i}. {lista_nome}: {item}")

    try:
        item_remove = int(input(f"\nAdicione o número da tarefa que deseja excluir de '{lista_nome}': "))

        if 1 <= item_remove <= len(lista):
            item_excluido = lista.pop(item_remove - 1)
            print(f"Tarefa '{item_excluido}' foi removida da lista '{lista_nome}'.")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Exibe as tarefas existetes nas listas
def exibir_itens():
    if not itens and not itens_concluidos:
        print("\nNenhuma tarefa na lista.")
        return
    
    for i in itens:
        print(f"Tarefas não Finalizadas: {i} ( )")
    for ic in itens_concluidos:
        print(f"Tarefas Concluídas: {ic} ( X )")

# Faz um check na tarefa concluida
def check():
    if not itens:
        print("Não há tarefas para concluir.")
        return

    for i, item in enumerate(itens, start=1):
        print(f"\n{i}. Tarefas não Finalizadas: {item} ( )")

    try:
        item_check = int(input("\nAdicione o número da tarefa que foi concluída: "))
        if 1 <= item_check <= len(itens):
            item_concluido = itens.pop(item_check - 1)
            itens_concluidos.append(item_concluido)
            print(f"Tarefa '{item_concluido}' foi movida para concluídos.")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Menu Pricipal
while True:
    try:
        opcao = int(input("\n1 - Adicionar Item \n2 - Visualizar Lista de Tarefas \n3 - Excluir Item \n4 - Marcar como Concluido \n5 - Sair \n\n"))
        if opcao == 1:
            adicionar_item()
        elif opcao == 2:
            exibir_itens()
        elif opcao == 3:
            remove_item()
        elif opcao == 4:
            check()
        elif opcao == 5:
            print("Saindo do Programa...")
            break
        else:
            print("Opção Inválida")
    except ValueError:
        print("Por favor, insira um número válido.")
