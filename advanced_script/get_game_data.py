import os # Permite interagir com o sistema operativo (ficheiros, diretórios, variáveis de ambiente)
import json # ler e escrever dados no formato JSON
import shutil # disponibiliza operações (copiar, mover, apagar) sobre ficheiros e pastas
from subprocess import PIPE, run # permite executar comandos externos e comunicar com outros processos
import sys # permite acessar a linha de comandos 

GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break

    return game_paths

def get_name_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    
    return new_names

def create_target_dir(target):
    if not os.path.exists(target):
        os.mkdir(target)

def copy_and_overwrite(source, file_path):
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
    shutil.copytree(source, file_path)

def make_json_metadata_file(path, game_dirs):
    data = {
        "gameNames": game_dirs,
        "numOfGames": len(game_dirs)
    }
    
    with open(path, "w") as f:
        json.dump(data, f)
    

def main(source, target_dir):
    cwd = os.getcwd() #obtem o diretório a partir do qual este script é executado (current working dir)
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target_dir)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_paths(game_paths, "_game")
    
    create_target_dir(target_path)
    
    for src, dest in zip(game_paths, new_game_dirs):
        file_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, file_path)

    json_path = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must only pass a source and a target directory!")
    
    source, target_dir = args[1:]
    main(source, target_dir)
