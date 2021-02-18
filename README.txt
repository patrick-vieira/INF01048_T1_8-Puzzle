

O ponto de entrada do programa é o main.py
Os parâmetros para a execução do programa são:

-i ou --input, estado inicial ou arquivo contendo o estado inicial
-a ou --algorithm, algorítimo que vai ser executado
 - successor = avalia_sucessor
 - expand = expande (parâmetros adicional -c ou --custo)
 - BFS
 - DFS
 - A1
 - A2


#executa algorítimo [BFS] para o estado que está no arquivo [input_file.txt] retorna resultados no arquivo [output_file.txt]
python3 ./src/main.py --algorithm BFS -i input_file.txt -o output_file.txt 

#executa algorítimo [avalia_sucessor] para o estado [2_3541687]
python3 ./src/main.py -a successor -i 2_3541687

#executa algorítimo [expande] para o estado [2_3541687] com custo [0]
python3 ./src/main.py -a expand -i 2_3541687 -c 0








##
Considerações. usar recursão pode causar problema por causa da profundidade
RecursionError: maximum recursion depth exceeded while calling a Python object

    def get_path_nodes(self):
        path = [self]
        self.__get_path(path)
        path.reverse()
        return path

    def __get_path(self, curr_path: list) -> list:
        if self.predecessor is not None:  # <-- Se ha um antecessor
            curr_path.append(self.predecessor)  # <-- Adicionamos ele no caminho
            return self.predecessor.__get_path(curr_path)
        else:  # <-- se não tem predecessor é o início
            return curr_path

uma alternativa simples e barata foi alterar a fução recursiva pelo loop ;)

    def __get_path_sem_recursao(self, path: list, node):
        pred = node.predecessor

        while pred:
            path.append(pred)
            pred = pred.predecessor