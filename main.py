def menu():
       
     print("\n ----  | Menu | ----  \n"
        "\n(1) - Adicionar Tarefa \n"
        "(2) - Deletar Tarefa \n"
        "(3) - Editar Tarefa  \n"
        "(4) - Listar Tarefas \n"
        "(5) - Sair\n"
     )

def add_task(tasks):

     print(" ----  | Adicionar Tarefa |  ---- \n")

     task_name = input("Tarefa:")
     task_responsible = input("Reponsável:")
     print("Status:")
     print("\n(1) - Em Andamento")
     print("(2) - Pendente")
     print("(3) - Finalizada")
     
     status_option = input("\nSituação:")

     match status_option:
               
          case "1":
               task_status = "Em andamento"
          
          case "2":
               task_status = "Pendente"

          case "3":
               task_status = "Finalizada"

          case _:
               task_status = "Não cadastrado"

     task = {
          "name": task_name,
          "status":task_status,
          "responsible": task_responsible 
        }

     tasks.append(task)

     print(f"\n ----  | Tarefa {task_name} adicionada |  ---- ")

def delete_task(tasks):

     print("\n ----  | Deletar Tarefa |  ---- \n")

       
     if not tasks: 
          
          print("\n ----  | Nenhuma tarefa cadastrada |  ---- ")
          return
     
     try:
     
          number = int(input("\nQual tarefa deseja deletar?"))

     except ValueError:

          print("\n Caracter inválido, digite apenas número.")
          return
     
     if number <= len(tasks): 
               
          tasks.pop(number -1) 
     
          print(" ----  | \nDeletada com sucesso. |  ---- ")
          
     else:
          print(" ----  | \nTarefa não Cadastrada. |  ---- ")
          
def edit_tasks(tasks):

     print("\n ----  | Editar Tarefa |  ---- \n")

     if not tasks: 
          
          print("\n ----  | Nenhuma tarefa cadastrada |  ---- ")
          return
     
     try:
  
          number = int(input("\nQual tarefa deseja editar?"))

     except ValueError:

          print("\nCaracter inválido, digite apenas número.")
          return
     
     if number <= 0 or number > len(tasks):
          
          print(" ----  | \nTarefa não Cadastrada. |  ---- ")
          return 
     
     print("\n ----  | Qual Situação deseja editar: |  ---- \n"
          "\n(1) - Nome"
          "\n(2) - Status"
          "\n(3) - Responsável")
     
     edit_options = input("\nEscolha uma opção:")

     match edit_options:
               
          case "1":
               tasks[number - 1]["name"] = input("\nNovo Nome:")

               print("\n ----  | Cadastrada com successo. |  ----")
               
          case "2":
               print("\nNovo Status:\n")
               print("(1) - Em Andamento")
               print("(2) - Pendente")
               print("(3) - Finalizada")

               status_option = input("\nNova situação: ")
               
               match status_option:

                    case "1": 
                         tasks[number - 1]["status"] = "Em andamento"
                    case "2": 
                         tasks[number - 1]["status"] = "Pendente"
                    case "3": 
                         tasks[number - 1]["status"] = "Finalizada"
                    case _: 
                         tasks[number - 1]["status"] = "Não cadastrado"

               print("\n ----  | Cadastrada com sucesso. |  ----")
          
          case "3":
               tasks[number - 1]["responsible"] = input("Novo Responsável:")

               print("\n ----  | Cadastrada com successo. |  ----")
               return
               
          case _:
               tasks= "Não cadastrado"

def list_tasks(tasks):
   
     print("\n ----  | Listar Tarefas |  ---- \n")

     if not tasks: 
          
          print("\n ----  | Nenhuma tarefa cadastrada |  ---- ")
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
                    
               case "2":
                    list_tasks(tasks) 
                    delete_task(tasks)
                    
               case "3":
                    list_tasks(tasks)
                    edit_tasks(tasks)
                    
               case "4":
                    list_tasks(tasks)
                    
               case "5":
                    print("\n ---- | Sessão Finalizada |  ---- \n")
                    exit()
               
               case _:
                    print("\n ----| Opção inválida, tente novamente.\n |  ---- ")
                    continue

          while True:

               menu_option = input("\nDeseja abrir o menu?\n"
               "\n(1) - Sim" 
               "\n(2) - Não\n")
               
               match menu_option:
                    
                    case "1":
                         break

                    case "2": 
                         print("\n ---- | Sessão Finalizada |  ---- \n")
                         exit()

                    case _:
                         print("\n ----| Opção inválida, tente novamente.\n |  ---- ")
                         continue
                    
if __name__ == "__main__":
     main()