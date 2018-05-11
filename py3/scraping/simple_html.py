from bs4 import BeautifulSoup

SIMPLE_HTML = """<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>"""

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    print(simple_soup.find('h1').string)


def find_list_items():
    li_tags = simple_soup.find_all('li')
    print([li.string for li in li_tags])


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph)


def other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph)


find_list_items()
find_subtitle()
other_paragraph()
