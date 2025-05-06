# To-Do List em Python
tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

def mostrar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

# Testando a aplicação
adicionar_tarefa("Comprar leite")
adicionar_tarefa("Estudar Python")
mostrar_tarefas()
