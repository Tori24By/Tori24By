import requests
import os

def get_apod():
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    image_url = data.get("url")
    title = data.get("title")
    explanation = data.get("explanation", "")[:300] + "..."
    
    return f"#### {title}\n\n<img src='{image_url}' width='400' />\n\n> {explanation}"

def update_readme(content):
    if not os.path.exists("README.md"):
        return

    with open("README.md", "r", encoding="utf-8") as file:
        readme = file.read()
        
    start_tag = "<!-- NASA-APOD:START -->"
    end_tag = "<!-- NASA-APOD:END -->"
    
    if start_tag not in readme or end_tag not in readme:
        print("Erro: Tags não encontradas no README.md")
        exit(1)

    parts = readme.split(start_tag)
    final_parts = parts[1].split(end_tag)
    new_readme = parts[0] + start_tag + "\n" + content + "\n" + end_tag + final_parts[1]

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_readme)

if __name__ == "__main__":
    try:
        new_content = get_apod()
        update_readme(new_content)
        print("Sucesso: README atualizado com os dados da NASA.")
    except Exception as e:
        print(f"Falha na execução: {e}")
        exit(1)
