import getopt
import os
import sys

class Arguments:

    def __init__(self, argv):
        self.__argv = argv[1:]  # <-- Desconsidera o indice 0 pois eh o file name
        self.initial_state = ''
        self.initial_state_cost = 0
        self.algorithm = ''
        self.input_file = ''
        self.output_file = ''
        self.log_level = 0
        self.path_dirname = os.path.dirname(argv[0])

        self.try_parse()

    def try_parse(self):
        try:
            opts, args = getopt.getopt( # <-- C-style parser
                self.__argv,    # <-- Lista de argumentos
                "hi:o:a:c:l:",  # <-- Ordem dos argumentos
                ["input=", "ofile=", "algorithm=", "cost=", "log="] # <-- Versao longa dos parametros
            )
        except getopt.GetoptError:
            print('test.py -h for help')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print('test.py -i <initial_state | initial_state_file.txt> -o <output_moves_file.txt>')
                sys.exit()

            elif opt in ("-i", "--input"):      # <-- O input pode ser:
                if arg.endswith(".txt"):        # <-- a) Um arquivo de texto
                    self.input_file = arg
                else:                           # <-- b) Uma string de estado inicial
                    self.initial_state = arg

            elif opt in ("-o", "--ofile"):
                self.output_file = arg

            elif opt in ("-a", "--algorithm"):
                self.algorithm = arg

            elif opt in ("-c", "--cost"):
                self.initial_state_cost = arg

            elif opt in ("-l", "--log"):
                self.log_level = arg

