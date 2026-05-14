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

def list_tasks(tasks):
   
     print("\n------- TODAS AS TAREFAS -------")

     if not tasks: 
          
          print("Nenhuma tarefa cadastrada")
          return
               
     for i, task in enumerate(tasks, start=0):

          print(f"\nTarefa: {i}")
          print("\nNome:", task["name"])
          print("\nStatus:", task["status"])
          print("\nResponsável:", task["responsible"])

def delete_task(tasks):
       
     if not tasks: 
          
          print("Nenhuma tarefa cadastrada")
          return
     
     for i, task in enumerate(tasks, start=0):
     
          print(f"\nTarefa {i}")
          print("Nome:", task["name"])
     
     number = int(input("\nQual tarefa deseja deletar?"))

     if number <= len(tasks): #(len) numerar a lista 
               
          tasks.pop(number) #(pop) Funçao para deletar o index da lista 
               
          print("Tarefa deletada")
          
     else:
          print("Tarefa não cadastrada.")
          

def main():
        
     tasks = []


     while True:

          menu()

          option = input("Escolha uma opção:\n")

          if option == "1": 
               add_task(tasks)

          elif option == "2":
               delete_task(tasks)
            
          elif option == "4": 
               list_tasks(tasks)

          elif option == "5":
               print("Até logo")
               break
            
          else: 
               print("Opção inválida")

if __name__ == "__main__":
     main()