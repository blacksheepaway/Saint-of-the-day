import requests
from bs4 import BeautifulSoup
import tempfile
import PySimpleGUI as sg
import re

# Encontrar e separar a frase que tem o texto alvo
def remove_sentence_with_text(text, target):
    # Divide o texto em frases usando regex
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    target_index = -1

    # Percorre as frases e encontra a primeira que contenha o texto alvo
    for i, sentence in enumerate(sentences):
        if target in sentence:
            target_index = i
            break

    # Se encontrou a frase com o texto alvo, retire ela do nome
    if target_index != -1:
        sentences.pop(target_index)
    
    # Junta as frases novamente em um único texto
    new_text = ' '.join(sentences)
    return new_text

#Função do santo do dia
def get_saint_of_the_day():
    url = "https://santo.cancaonova.com/santo/sao-jose-moscati/?sDia=12&sMes=04&sAno=2023"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontra o elemento h1 com a classe entry-title para obter o nome do santo
    saint_name_full = soup.find('h1', {'class': 'entry-title'}).text.strip()
    
    # Extrai a primeira parte do nome do santo antes da vírgula
    saint_name = re.split(',|:', saint_name_full, 1)[0].strip()

    # Encontra a tag a contendo a tag img com a classe com 'wp-image-'
    saint_image_a_tag = soup.find('a', {'href': re.compile('^https://img.cancaonova.com')})

    if saint_image_a_tag:
        # Encontra a tag img dentro da tag a
        saint_image_tag = saint_image_a_tag.find('img', {'class': re.compile('wp-image-')})
    else:
        # Se não encontrou a tag a, procurar pela tag img
        saint_image_tag = soup.find('img', {'class': re.compile('wp-image-')})

    if saint_image_tag:
        saint_image_url = saint_image_tag['src']
    else:
        saint_image_url = None
        print("Error: Saint image tag not found.")


    # Separa a legenda da imagem
    saint_image_caption = soup.find('p', {'class': 'wp-caption-text'}).text.strip()

    # 'html_content' contem o HTML que queremos analisar
    old_description_div = soup.find('div', {'class': 'entry-content', 'class': 'content-santo'})
    # Encontra todos os elementos <p> dentro da div
    all_description_paragraphs = old_description_div.find_all('p')

    # Procura os parágrafos até encontrar uma string específica
    target_string = f"{saint_name}, rogai por nós!"
    selected_paragraphs = []

    for paragraph in all_description_paragraphs:
        text = paragraph.text.strip()
        
        if target_string in text:
            # Adiciona apenas parte do parágrafo até a target_string
            selected_paragraphs.append(text.split(target_string)[0] + target_string)
            break
        else:
            selected_paragraphs.append(text)

    # Remove a frase que contém a legenda da imagem de cada parágrafo e junta os parágrafos modificados com duas quebras de linha
    saint_description = '\n\n'.join(remove_sentence_with_text(p, saint_image_caption) for p in selected_paragraphs)

    # Faz download da imagem para um arquivo temporário
    response = requests.get(saint_image_url, stream=True)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        saint_image_path = f.name

    # Extrai a data do dia, mês e ano
    dia = soup.find('span', {'id': 'dia-calendar'}).text.strip()
    mes = soup.find('span', {'id': 'mes-calendar'}).text.strip()
    ano = soup.find('span', {'id': 'ano-calendar'}).text.strip()
    date_text = f"{dia} {mes} {ano}"

    # Cria o layout do popup
    layout = [
        [sg.Text(date_text, font=('Arial', 16), justification='center')],
        [sg.Text(saint_name, font=('Arial', 24), justification='center')],
        [sg.Image(saint_image_path, size=(300, 300), pad=((0, 0), (0, 0)))],
        [sg.Text(saint_image_caption, font=('Arial', 12))],
        [sg.Multiline(saint_description, size=(60, 10), font=('Arial', 12))],
        [sg.Button('Fechar', size=(10, 1), pad=((0, 0), (10, 0)), button_color=('white', 'red'))],
        [sg.Text(target_string)]
    ]


    # Cria o popup
    window = sg.Window('Saint of the Day', layout, element_justification='center')

    # Mostra o popup e espera um botão ser pressionado
    event, values = window.read()

    # Fecha a janela
    window.close()

get_saint_of_the_day()

#Para trasformar esse script em .exe, instalar o pyinstaller
    #pip install pyinstaller
#A partir dai, transformar o script
    #pyinstaller --onefile SOTD.py    
