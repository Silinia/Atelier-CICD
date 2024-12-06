import markdown
import os

rev = 0
events = []

def prepare_pages():
    html_to_write = []
    image_to_write = []
    image_path = "/events/"
    files = os.listdir('events')
    files.sort()
    for file in files:
        if file.endswith('.md'):
            with open(f'events/{file}', 'r') as f:
                text = f.read()
                html = markdown.markdown(text)
                html_to_write.append(html)

        if file.endswith('.webp'):
            link = f'<img src="{os.path.dirname(image_path)+ "/" + file}" alt="image">'
            image_to_write.append(link)

    with open('Pages/accueil.html', 'w+') as f:
        for i in range(len(html_to_write)):
            f.write((image_to_write[i] if image_to_write[i] else ''))
            f.write((html_to_write[i] if html_to_write[i] else ''))

    for i in range(0, len(html_to_write)): 
        with open(f'Pages/Events/Evenement-{i+1}.html', 'w+') as f:
            f.write((image_to_write[i] if image_to_write[i] else ''))
            f.write((html_to_write[i] if html_to_write[i] else ''))

prepare_pages()
