import json
import os.path
livros = []
with open('livros.json', 'r', encoding='utf8') as json_file:
    obj = json.loads(json_file.read())
    for i in obj:
        livros.append(i)
print(os.path.exists('livros.json'))


print(livros)