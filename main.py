def menu():
     
     print("\n ----  Seja Bem Vindo  ----  \n"
        "\n1 - Adicionar Tarefa.\n"
        "2 - Deletar Tarefa.\n"
        "3 - Editar Tarefa.\n"
        "4 - Listar Tarefas.\n"
        "5 - Sair!\n"
     )

def add_task(tasks):

        print("----| Adicione uma nova tarefa |----\n")

        task_name = input("Qual a tarefa:")
        task_status = input("Status:")
        task_responsible = input("Reponsável:")

        task = {
             "name": task_name,
             "status": task_status,
             "responsible": task_responsible 
        }

        tasks.append(task)

        print(f"\n Tarefa {task_name} adicionada! ")

def list_tasks(tasks):
   
        print("\n------- TODAS AS TAREFAS -------")

        if not tasks: 
             
             print("Nenhuma tarefa cadastrada")

        else:
             
            for i, task in enumerate(tasks, start=0):
                print("| ===================== |")
                print(f"\nTarefa {i}")
                print("| ===================== |")
                print("\nNome:", task["name"])
                print("| ===================== |")
                print("\nStatus:", task["status"])
                print("| ===================== |")
                print("\nResponsável:", task["responsible"])
                print("| ===================== |")

def main():
        
        tasks = []

        while True:

            menu()

            option = input("Escolha uma opção:\n")

            if option == "1": 
                 add_task(tasks)
            
            elif option == "4": 
                 list_tasks(tasks)

            elif option == "5":
                 print("Até logo")
                 break
            
            else: 
                 print("Opção inválida")

if __name__ == "__main__":
    main()