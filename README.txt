

O ponto de entrada do programa é o main.py
Os parâmetros para a execução do programa são:

-i ou --input, estado inicial ou arquivo contendo o estado inicial
-a ou --algorithm, algorítimo que vai ser executado
 - 0 = avalia_sucessor
 - 1 = expande (parâmetros adicional -c ou --custo)
 - BFS
 - DFS
 - A*


#executa algorítimo [BFS] para o estado que está no arquivo [input_file.txt] retorna resultados no arquivo [output_file.txt]
python3 ./src/main.py --algorithm BFS -i input_file.txt -o output_file.txt 

#executa algorítimo [avalia_sucessor] para o estado [2_3541687]
python3 ./src/main.py -a 0 -i 2_3541687

#executa algorítimo [expande] para o estado [2_3541687] com custo [0]
python3 ./src/main.py -a 1 -i 2_3541687 -c 0