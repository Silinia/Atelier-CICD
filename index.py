import markdown
import os

rev = 0
events = []

def prepare_pages():
    html_to_write = []
    image_to_write = []
    
    files = os.listdir('events')
    files.sort()
    for file in files:
        file_path = os.path.join('events', file)
        if file.endswith('.md'):
            with open(file_path, 'r') as f:
                text = f.read()
                html = markdown.markdown(text)
                html_to_write.append(html)

        if file.endswith('.webp'):
            link = f'<img src="{os.path.join("events", file)}" alt="image">'
            image_to_write.append(link)

    with open('Pages/index.html', 'w+') as f:
        for i in range(len(html_to_write)):
            f.write((image_to_write[i] if image_to_write[i] else ''))
            f.write((html_to_write[i] if html_to_write[i] else ''))
            f.write('<br>')
            f.write(f'<a href=/Pages/Evenement-{i+1}.html>Voir l\'événement</a>')
            f.write('<br>')

    for i in range(0, len(html_to_write)): 
        with open(f'Pages/Events/Evenement-{i+1}.html', 'w+') as f:
            f.write((image_to_write[i] if image_to_write[i] else ''))
            f.write((html_to_write[i] if html_to_write[i] else ''))
            f.write('<br>')

prepare_pages()
