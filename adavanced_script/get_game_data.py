import os # Permite interagir com o sistema operativo (ficheiros, diretórios, variáveis de ambiente)
import json # ler e escrever dados no formato JSON
import shutil # disponibiliza operações (copiar, mover, apagar) sobre ficheiros e pastas
from subprocess import PIPE, run # permite executar comandos externos e comunicar com outros processos
import sys # permite acessar a linha de comandos 

def find_all_game_dirs(source):
    pass

def main(source, target_dir):
    cwd = os.getcwd() #obtem o diretório a partir do qual este script foi executado (current working dir)
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target_dir)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must only pass a source and a target directory!")
    
    source, target_dir = args[1:]
    main(source, target_dir)
