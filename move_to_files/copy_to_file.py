import os
import shutil

caminho_original = '/home/lucasrejanio/Documentos/Estudos/Python/move_to_files/caminho_original'
caminho_novo = '/home/lucasrejanio/Documentos/Estudos/Python/move_to_files/caminho_novo'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe!')

for root, dirs, file in os.walk(caminho_original):
    for file in file:
        old_file_path = os.path.join(root,file)
        new_file_path = os.path.join(caminho_novo, file)

        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo {file} copiado com sucesso!')


for root, dirs, file in os.walk(caminho_original):
    for file in file:
        old_file_path = os.path.join(root,file)
        new_file_path = os.path.join(caminho_original, file)
        print(f'Arquivo {file} removido com sucesso!')

        os.remove(new_file_path)