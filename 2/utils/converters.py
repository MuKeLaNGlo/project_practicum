from bs4 import BeautifulSoup


def svg_to_html(svg_content: str, selected_option):
    if selected_option == "html":
        html_content = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SVG in HTML</title>
        </head>
        <body>
            {svg_content}
        </body>
        </html>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        html_content = soup.prettify()
        return html_content.strip()
    return None


def html_to_svg(html_content, selected_option):
    if selected_option == "svg":
        # Парсим HTML-контент с использованием BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Ищем элемент svg внутри body
        svg_element = soup.body.find('svg')

        # Возвращаем строковое представление найденного SVG
        return str(svg_element.prettify())
