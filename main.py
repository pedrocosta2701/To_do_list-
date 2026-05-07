def main():
    tasks = []

    while True:
        print("\n--- NOVA TAREFA ---")

        name = input("Qual a tarefa? ")
        status = input("Status: ")
        responsible = input("Responsável: ")

        task = {
            "name": name,
            "status": status,
            "responsible": responsible
        }

        tasks.append(task)

        continuar = input("\nDeseja adicionar outra tarefa? (sim/não): ").strip().lower()

        if continuar != "sim":
            break

    print("\n------- TODAS AS TAREFAS -------")

    for i, task in enumerate(tasks, start=1):
        print(f"\nTarefa {i}")
        print("Nome:", task["name"])
        print("Status:", task["status"])
        print("Responsável:", task["responsible"])


if __name__ == "__main__":
    main()
