import sys
import logging

from argument_parser import Arguments
from expand import expand_node
from node import Node
from sucessor import get_successor_states


def run_successor_states_function(arguments: Arguments):
    successor_states = get_successor_states(arguments.initial_state)

    to_print = ""
    for successor_state in successor_states:
        to_print += "(" + successor_state + "," + successor_states[successor_state] + ") "

    print(to_print.strip())


# refatorar o nó tem que se  expandir por conta, talvez a função expand_node possa ser passada para dentro do nó
def run_expand_nodes_function(arguments: Arguments):
    to_expand_node = Node(arguments.initial_state, None, arguments.initial_state_cost, [])
    expanded_nodes = expand_node(to_expand_node)

    to_print = ""
    for expanded_node in expanded_nodes:
        to_print += "(" + expanded_node.action + "," + expanded_node.state + "," \
                    + str(expanded_node.cost) + "," + expanded_node.predecessor.state + ") "

    print(to_print.strip())


def run_bfs_algorithm(arguments: Arguments):
    pass


def main(arguments: Arguments):
    if arguments.algorithm == 'successor':
        run_successor_states_function(arguments)
    elif arguments.algorithm == 'expand':
        run_expand_nodes_function(arguments)
    elif arguments.algorithm == "BFS":
        run_bfs_algorithm(arguments)
    else:
        raise Exception("Sorry, no algorithm found for this arguments")


def configure_log(arguments: Arguments):
    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.getLevelName(arguments.log_level),
                        filename=arguments.path_dirname + '/logs/log.log')


if __name__ == "__main__":
    parsed_arguments = Arguments(sys.argv)
    configure_log(parsed_arguments)
    main(parsed_arguments)

    logging.info("Execution finished")
