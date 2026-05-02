import requests
import os

def get_apod():
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Formatação para o GitHub
    image_url = data.get("url")
    title = data.get("title")
    explanation = data.get("explanation")[:300] + "..."
    
    content = f"#### {title}\n\n<img src='{image_url}' width='400' />\n\n> {explanation}"
    return content

def update_readme(content):
    with open("README.md", "r", encoding="utf-8") as file:
        readme = file.read()

    start_tag = "<!-- NASA-APOD:START -->"
    end_tag = "<!-- NASA-APOD:END -->"
    
    new_readme = readme.split(start_tag)[0] + start_tag + "\n" + content + "\n" + end_tag + readme.split(end_tag)[1]

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_readme)

if __name__ == "__main__":
    new_content = get_apod()
    update_readme(new_content)
