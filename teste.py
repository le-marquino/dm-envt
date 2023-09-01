import json

# Carregar o conteúdo do arquivo .txt
with open('isometrics.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Encontrar a posição do primeiro 'itemUuid'
start_index = content.find('"items": [{') + 9
print("Start index:", start_index)

# Exibir um pequeno trecho do início do conteúdo sendo considerado
start_context = content[max(0, start_index):start_index + 50]
print("Start context:", start_context)

# Encontrar a posição de 'searchResultsCount' após o primeiro 'itemUuid'
end_index = content.find('searchResultsCount', start_index) -27
print("End index:", end_index)

# Exibir um pequeno trecho do final do conteúdo sendo considerado
end_context = content[end_index-50:end_index]
print("End context:", end_context)

# Recortar o conteúdo para incluir apenas os itens
items_data = content[start_index:end_index]
#print("Items data:", items_data)

# Converter a string JSON para um objeto Python
items_list = json.loads(items_data)

# Salvar os dados em um arquivo .json
with open('output_isometrics.json', 'w', encoding='utf-8') as json_file:
    json.dump(items_list, json_file, ensure_ascii=False, indent=4)

print("Dados salvos em output.json")
