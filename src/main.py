# Importa bibliotecas basicas necessarias
import sys
import logging

# Importa definicoes do restante do codigo fonte
from hamming_distance import get_hamming_distance
from heuristic_search import heuristic_search
from argument_parser import Arguments
from bfs import breadth_first_search
from dfs import depth_first_search
from expand import expand_node
from manhattan_distance import get_manhattan_distance
from monitor import Monitor
from node import Node
from sucessor import get_successor_states


# Exercicio 01
def run_successor_states_function(arguments: Arguments):
    successor_states = get_successor_states(arguments.initial_state)

    to_print = ""
    for successor_state in successor_states:
        to_print += "(" + successor_state + "," + successor_states[successor_state] + ") "

    print(to_print.strip())
    logging.info(to_print.strip())


# Exercicio 02
# refatorar o nó tem que se  expandir por conta, talvez a função expand_node possa ser passada para dentro do nó
def run_expand_nodes_function(arguments: Arguments):
    to_expand_node = Node(None, arguments.initial_state, arguments.initial_state_cost, [])
    expanded_nodes = expand_node(to_expand_node)

    to_print = ""
    for expanded_node in expanded_nodes:
        to_print += "(" + expanded_node.action + "," + expanded_node.state + "," \
                    + str(expanded_node.cost) + "," + expanded_node.predecessor.state + ") "

    print(to_print.strip())
    logging.info(to_print.strip())


# Exercicio 03
# a) BFS
def run_bfs_algorithm(arguments: Arguments):
    root_node = Node(  # <-- Estado Inicial:
        None,   # <-- a) State
        arguments.initial_state,  # <-- b) Action
        0,  # <-- c) Cost
        None  # <-- d) Predecessor
    )

    final_node, monitor = breadth_first_search(root_node)

    log_results(final_node, monitor)


# b) DFS
def run_dfs_algorithm(arguments: Arguments):
    root_node = Node(
        None,
        arguments.initial_state,
        0,
        None
    )

    final_node, monitor = depth_first_search(root_node)

    log_results(final_node, monitor)


# c) A* (distancia Hamming)
def run_astar_h1_algorithm(arguments: Arguments):
    run_heuristic_algorithm(arguments.initial_state, get_hamming_distance)


# d) A* (distancia Manhattan)
def run_astar_h2_algorithm(arguments: Arguments):
    run_heuristic_algorithm(arguments.initial_state, get_manhattan_distance)


def run_heuristic_algorithm(initial_state, heuristic):
    root_node = Node(
        None,
        initial_state,
        0,
        None
    )

    final_node, monitor = heuristic_search(root_node, heuristic)

    log_results(final_node, monitor)


def log_results(final_node: Node, monitor: Monitor):
    if not final_node:
        moves = []
    else:
        moves = final_node.get_path_moves()

    if (True):  # logando por enquanto, na entrega deixar em false
        logging.info("Solução tem " + str(len(moves)) + " movimentos")
        logging.info(monitor.get_results())

    to_print = ""
    for move in moves:
        to_print += move + " "

    print(to_print.strip())


# Determina qual das funcoes deve executar
def main(arguments: Arguments):
    if arguments.algorithm == 'successor':
        run_successor_states_function(arguments)
    elif arguments.algorithm == 'expand':
        run_expand_nodes_function(arguments)
    elif arguments.algorithm == "BFS":
        run_bfs_algorithm(arguments)
    elif arguments.algorithm == "DFS":
        run_dfs_algorithm(arguments)
    elif arguments.algorithm == "A1":
        run_astar_h1_algorithm(arguments)
    elif arguments.algorithm == "A2":
        run_astar_h2_algorithm(arguments)
    else:
        raise Exception("Sorry, no algorithm found for these arguments")


# Define como o log funciona
def configure_log(arguments: Arguments):
    logging.basicConfig(
        format='%(levelname)s: %(asctime)s %(message)s',  # <-- Formato das mensagens na saída
        datefmt='%m/%d/%Y %I:%M:%S %p',  # <-- Formato da data
        level=logging.getLevelName(arguments.log_level),  # <-- Info, Warning, Error etc
        filename=arguments.path_dirname + '/logs/log.log'  # <-- Onde salvar os logs
    )


# Detecta se estamos executando a main e pega os argumentos
if __name__ == "__main__":  # <-- Se o modulo rodado eh o main
    parsed_arguments = Arguments(sys.argv)  # <-- Fazemos o parsing dos argumetos
    configure_log(parsed_arguments)  # <-- Configuramos o log a partir deles

    logging.info("Execution start for state: " + parsed_arguments.initial_state + " - algoritmo: " + parsed_arguments.algorithm)  # <-- Ao final, informamos que a execucao terminou
    main(parsed_arguments)  # <-- Rodamos a funcao main com eles

    logging.info("Execution finished for state: " + parsed_arguments.initial_state)  # <-- Ao final, informamos que a execucao terminou
