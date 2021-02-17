import sys
import logging

from argument_parser import Arguments
from expand import expand_node
from node import Node
from sucessor import get_successor_states


# Exercicio 01
def run_successor_states_function(arguments: Arguments):
    successor_states = get_successor_states(arguments.initial_state)

    to_print = ""
    for successor_state in successor_states:
        to_print += "(" + successor_state + "," + successor_states[successor_state] + ") "

    print(to_print.strip())


# Exercicio 02
# refatorar o nó tem que se  expandir por conta, talvez a função expand_node possa ser passada para dentro do nó
def run_expand_nodes_function(arguments: Arguments):
    to_expand_node = Node(arguments.initial_state, None, arguments.initial_state_cost, [])
    expanded_nodes = expand_node(to_expand_node)

    to_print = ""
    for expanded_node in expanded_nodes:
        to_print += "(" + expanded_node.action + "," + expanded_node.state + "," \
                    + str(expanded_node.cost) + "," + expanded_node.predecessor.state + ") "

    print(to_print.strip())


# Exercicio 03
# a) BFS
def run_bfs_algorithm(arguments: Arguments):
    pass


# b) DFS
def run_dfs_algorithm(arguments: Arguments):
    pass


# c) A* (distancia Hamming)
def run_astar_h1_algorithm(arguments: Arguments):
    pass


# d) A* (distancia Manhattan)
def run_astar_h2_algorithm(arguments: Arguments):
    pass


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
    main(parsed_arguments)  # <-- Rodamos a funcao main com eles

    logging.info("Execution finished")  # <-- Ao final, informamos que a execucao terminou
