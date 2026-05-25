import os

with open(file='remover.txt', mode='r', encoding='utf-8') as fp:
    for name in fp.readlines():
        name = name.strip()
        if not name: continue
        try:
            os.remove(f'dataset/images/train/{name}.jpg')
            os.remove(f'dataset/labels/train/{name}.txt')
        except Exception as e:
            print(f'Erro ao remover {name}: {e}')
