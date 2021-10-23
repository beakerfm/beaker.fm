# beaker.fm
A blog about hacking and some other random things.
But mostly about code :)

The focus is on minimalistic implementations and design.
Very pythonic, I know!

Hacking is about finding the easiest way to the end objective
Often its harder to get there than you think,
every now and then its easy.
Just like life!

## Local Setup
Create a Python virtual environment

```
python3 -m venv venv
```

Install the dependencies

```
pip install -r requirements.txt
```

Select the article to build with 

```
python3 build.py
```

Build a specific article with

```
python3 build.py <article-name>
```

Run a local webserver of the generated HTML

```
python3 -m http.server
```
