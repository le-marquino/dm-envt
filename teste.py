import pandas as pd
import json


# Função para extrair valores de coverImageUrls
def get_cover_url(url_dict, size):
    return url_dict.get(size, None)

# Lê o conteúdo do arquivo JSON
with open('input.json', 'r') as json_file:
    data = json.load(json_file)

# Converte o JSON para um DataFrame do Pandas
df = pd.json_normalize(data)

# Criar tabelas CSV

# Tabela Item
item_columns = ['id', 'itemUuid', 'slug', 'title', 'subTitle', 'description',
                'itemType', 'itemTypeName', 'publishedAt', 'updatedAt',
                'madeAvailableAt', 'contributorUsername', 'fileName']
item_df = df[item_columns]

# Tabela Tag
tags_data = []
for idx, row in df.iterrows():
    itemUuid = row['itemUuid']
    for tag in row['tags']:
        tags_data.append({'itemUuid': itemUuid, 'tag': tag})
tag_df = pd.DataFrame(tags_data)

# Tabela Category
categories_data = []
for idx, row in df.iterrows():
    itemUuid = row['itemUuid']
    for category in row['categories']:
        categories_data.append({'itemUuid': itemUuid, 'category': category})
category_df = pd.DataFrame(categories_data)

# Salva os DataFrames em arquivos CSV
item_df.to_csv('item.csv', index=False)
tag_df.to_csv('tag.csv', index=False)
category_df.to_csv('category.csv', index=False)


# Tabela ItemAttribute
item_attr_columns = ['itemUuid', 'itemAttributes.presentationTemplatesApplicationsSupported',
                     'itemAttributes.hasDocumentation', 'itemAttributes.presentationTemplatesFileTypes',
                     'itemAttributes.dimensions.unit', 'itemAttributes.dimensions.width',
                     'itemAttributes.dimensions.height']
item_attr_df = df[item_attr_columns]

# Tabela PreviewImage
preview_images_data = []
for idx, row in df.iterrows():
    itemUuid = row['itemUuid']
    for preview_image in row['previewImagesUrls']:
        preview_images_data.append({
            'itemUuid': itemUuid,
            'tn120x80': preview_image.get('tn120x80', None),
            'w632': preview_image.get('w632', None),
            'w2740': preview_image.get('w2740', None)
        })
preview_images_df = pd.DataFrame(preview_images_data)

# Salva os DataFrames em arquivos CSV
item_df.to_csv('item.csv', index=False)
tag_df.to_csv('tag.csv', index=False)
category_df.to_csv('category.csv', index=False)
item_attr_df.to_csv('item_attribute.csv', index=False)
preview_images_df.to_csv('preview_image.csv', index=False)
