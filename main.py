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
     
     try:
     
          number = int(input("\nQual tarefa deseja deletar?"))

     except ValueError:

          print("\n Digite apenas números!")
          return
     
     if number <= len(tasks): 
               
          tasks.pop(number -1) 
     
          print("Tarefa deletada")
          
     else:
          print("Tarefa não cadastrada.")
          

def edit_tasks(tasks):

     if not tasks: 
          
          print("\nNenhuma tarefa cadastrada")
          return
     
     try:
  
          number = int(input("\nQual tarefa deseja editar ?"))

     except ValueError:

          print("\nDigite apenas números!")
          return
     
     # if number <= len(tasks):
     
     if number > 0 and number <= len(tasks):

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

          match option:

               case "1":
                    add_task(tasks)
                    continue
               
               case "2":
                    list_tasks(tasks) 
                    delete_task(tasks)
                    continue

               case "3":
                    list_tasks(tasks) 
                    edit_tasks(tasks)
                    continue
               
               case "4":
                    list_tasks(tasks)
                    continue
               
               case "5":
                    print("\nAté logo")
                    break 
               
               case _:
                    print("\nOpção inválida, tente novamente.")
                    
if __name__ == "__main__":
     main()

     #      switch (option)
     #      {    
     #                case "1": 
     #                     add_task(tasks)
     # }