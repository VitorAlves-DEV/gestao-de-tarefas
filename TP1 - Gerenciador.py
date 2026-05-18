# TESTE DE PERFOMANCE 1 - GESTÃO DE TAREFAS
# Funcionalidades do Programa:

# Adicionar Tarefa: Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
# Listar Tarefas: Mostrar todas as tarefas pendentes na lista, enumerando-as.
# Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída.
# Remover Tarefa: Dar ao usuário a opção de remover uma tarefa da lista.
# Detalhes da Implementação:

# Utilize loops (for e/ou while) para apresentar um menu de opções ao usuário e realizar operações repetidas.
# Manipule uma lista para armazenar e gerenciar as tarefas, incluindo adicionar, listar, marcar como concluída e remover tarefas.
# Crie funções para cada funcionalidade do sistema (adicionar, listar, marcar como concluída, remover), utilizando argumentos, parâmetros por palavra-chave, parâmetros padrão e retorno de valores.
# Documente cada função utilizando DocStrings para descrever seu propósito, uso e parâmetros.

def adicionar_tarefas(tarefas, nome_tarefa):
    """
    Adiciona uma nova tarefa à lista de tarefas pendentes.

    Parâmetros:
    tarefas (list): A lista de tarefas pendentes.
    nome_tarefa (str): O nome da tarefa a ser adicionada.

    Retorna:
    None
    """
    tarefa = {
        "Tarefa": nome_tarefa,
        "Concluída" : False
        }
    
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return
    
    
def listar_tarefas(tarefas):
    """
    Lista todas as tarefas pendentes.

    Parâmetros:
    tarefas (list): A lista de tarefas pendentes.

    Retorna:
    None
    """
    if not tarefas:
        print("Nenhuma tarefa pendente.")
        return
    else:
        print("Tarefas Pendentes:")
        for index, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["Concluída"] else "Pendente"
            nome_tarefa = tarefa["Tarefa"]
            print(f"{index}. {nome_tarefa} - {status}")
        return
               
def marcar_concluida(tarefas, numero_tarefa):
    """
    Marca uma tarefa específica como concluída.

    Parâmetros:
    tarefas (list): A lista de tarefas pendentes.
    numero_tarefa (int): O número da tarefa a ser marcada como concluída.

    Retorna:
    None
    """
    if 1 <= numero_tarefa <= len(tarefas):
        tarefas[numero_tarefa - 1]["Concluída"] = True
        print(f"Tarefa '{tarefas[numero_tarefa - 1]['Tarefa']}' marcada como concluída!")
    else:
        print("Número da tarefa inválido.")    
        
    return

def remover_tarefa(tarefas, numero_tarefa):
    """
    Remove uma tarefa da lista de tarefas pendentes.

    Parâmetros:
    tarefas (list): A lista de tarefas pendentes.
    numero_tarefa (int): O número da tarefa a ser removida.

    Retorna:
    None
    """
    if 1 <= numero_tarefa <= len(tarefas):
        tarefa_removida = tarefas.pop(numero_tarefa - 1)
        print(f"Tarefa '{tarefa_removida['Tarefa']}' removida com sucesso!")
    else:
        print("Número da tarefa inválido.")
    
    return
        
                
tarefas = []

while True: 
    print("\nGestão de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Digite '5' ou 'sair' para encerrar o programa.")

    escolha = input("Escolha uma opção (1-5): ")
    
    if escolha == '1':
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefas(tarefas, nome_tarefa)
    elif escolha == '2': 
        listar_tarefas(tarefas)
    elif escolha == '3':
        numero_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
        marcar_concluida(tarefas, numero_tarefa)
    elif escolha == '4':
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
        remover_tarefa(tarefas, numero_tarefa)
    elif escolha.lower().strip() == 'sair' or escolha == '5':
        print("Encerrando o programa. Até mais!")
        break
    else: 
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")