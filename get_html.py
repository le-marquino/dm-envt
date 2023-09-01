import requests

def fetch_raw_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except requests.HTTPError as http_err:
        print(f"Erro HTTP ao acessar {url}: {http_err}")
    except Exception as err:
        print(f"Outro erro ocorrido ao acessar {url}: {err}")
    return None

def save_to_file(filename, content):
    with open(filename + ".txt", "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    url_map = {
        "alexdndz": "https://elements.envato.com/user/alexdndz/graphic-templates",
        # ... todos os outros mapeamentos de nomes para URLs ...
        "SuperSonic_Studio": "https://elements.envato.com/user/SuperSonic_Studio"
    }

    for name, url in url_map.items():
        raw_html = fetch_raw_html(url)
        if raw_html:
            save_to_file(name, raw_html)
            print(f"Conteúdo salvo em {name}.txt")
