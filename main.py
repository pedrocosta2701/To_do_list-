def main():
    tasks = []

    while True:

        print("\n======= Seja Bem Vindo =======\n"
        "\n1 - Adicionar Tarefa.\n" 
        "2 - Deletar Tarefa.\n" 
        "3 - Editar Tarefa.\n" 
        "4 - Listar Tarefas.\n"
        "5 - Sair!\n")

        option = input("Escolha uma opção:")

        if option == "1": 

            print("\n--- NOVA TAREFA ---")

            name = input("Qual a tarefa? ")
            status = input("Status: ")
            responsible = input("Responsável:")

            task = {
                "name": name,
                "status": status,
                "responsible": responsible
            }

            tasks.append(task)

            continuar = input("\nDeseja adicionar outra tarefa? (sim/não): ").strip().lower()

            if continuar != "sim":
                break

        if option == "4": 

            print("\n------- TODAS AS TAREFAS -------")

            for i, task in enumerate(tasks, start=1):
                print(f"\nTarefa {i}")
                print("Nome:", task["name"])
                print("Status:", task["status"])
                print("Responsável:", task["responsible"])


if __name__ == "__main__":
    main()

    # numero 1 está funcioando perfeitamente porém na linha 31 ainda está errado a solicitaçao ao usuário, precisa concertar
    # numero 4 está lisantando certinho as atividades que foram criadas porém ele ainda está imprimindo na tela o menu novamente, precisa ser concertado. 
    