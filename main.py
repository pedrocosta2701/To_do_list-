def menu():
     
     print("\n ----  Seja Bem Vindo  ----  \n"
        "\n1 - Adicionar Tarefa?\n"
        "2 - Deletar Tarefa?\n"
        "3 - Editar Tarefa?\n"
        "4 - Listar Tarefas?\n"
        "5 - Sair!\n"
     )


def add_task(tasks):

        print("    | Adicione uma nova tarefa |    \n")

        task_name = input("Qual a tarefa?")
        task_status = input("Status:(Em andamento,Pendente,Finalizada)")
        task_responsible = input("Reponsável?")

        task = {
          "name": task_name,
          "status": task_status,
          "responsible": task_responsible 
        }

        tasks.append(task)

        print(f"\n !! Tarefa {task_name} adicionada !! ")


def delete_task(tasks):
       
     if not tasks: 
          
          print("\nNenhuma tarefa cadastrada")
          return
     
     number = int(input("\nQual tarefa deseja deletar?"))

     if number <= len(tasks): 
               
          tasks.pop(number -1) 
     
          print("Tarefa deletada")
          
     else:
          print("Tarefa não cadastrada.")
          

def edit_tasks(tasks):

     if not tasks: 
          
          print("\nNenhuma tarefa cadastrada")
          return
     
     for i, task in enumerate(tasks, start=0):
          print(f"{i + 1} - {task['name']}")

     number = int(input("\nQual tarefa deseja editar"))
     
     if number <= len(tasks):

          tasks[number - 1]["name"] = input("Novo nome:")
          tasks[number - 1]["status"] = input("Novo status:")
          tasks[number - 1]["responsible"] = input("Novo responsável:")

          print("\nTarefa atualizada")

     else:
          print("Tarefa não encontrada.")

          
def list_tasks(tasks):
   
     print("\n------- TODAS AS TAREFAS -------")

     if not tasks: 
          
          print("\nNenhuma tarefa cadastrada")
          return
               
     for i, task in enumerate(tasks, start=0):
          
          print(f"\nTarefa: {i + 1}")
          print("\nNome:", task["name"])
          print("Status:", task["status"])
          print("Responsável:", task["responsible"])


def main():
        
     tasks = []

     while True:

          menu()

          option = input("Escolha uma opção:\n")

          if option == "1": 
               add_task(tasks)

          elif option == "2":
               list_tasks(tasks) 
               delete_task(tasks)
            
          elif option == "3":
               list_tasks(tasks) 
               edit_tasks(tasks)
               
          elif option == "4": 
               list_tasks(tasks)

          elif option == "5":
               print("Até logo")
               break
            
          else: 
               print("Opção inválida")

if __name__ == "__main__":
     main()

     #      switch (option)
     #      {    
     #                case "1": 
     #                     add_task(tasks)
     # }