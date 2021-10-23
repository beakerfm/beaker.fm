import markdown
from bs4 import BeautifulSoup


with open("template.html", "r") as f:
  template = f.read()

#TODO replace with markdown.readFromFile or whatever...
# this would allow for removing next two file open blocks
with open("README.md", "r") as f:
  md = f.read()
  html = markdown.markdown(md, extensions=['fenced_code', 'codehilite'])

template = template.replace("__article__", html)

soup = BeautifulSoup(template)

with open("current.html", "w") as f:
  f.write(soup.prettify())

print(html)
