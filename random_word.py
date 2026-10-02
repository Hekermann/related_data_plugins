import requests as r
from rich.console import Console
from rich.table import Table
from rich.text import Text
from bs4 import BeautifulSoup
import os
from tinydb import TinyDB, Query

console = Console()

db = TinyDB("data/db.json", indent=4)
all_data = db.all()
get_data = [i["title"] for i in all_data]

User = Query()


def api_random_search():
    _url = "https://random-word-api.herokuapp.com/word?number=1"
    
    response = r.get(_url)
    data = response.json()
    word = data["word"]
    url = "https://relatedwords.io/" + word
    response = r.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    extract_title = soup.find_all("div", {"class": "word-ctn"})

    with console.status("Grabbing words... ", spinner="dots"):
        for i in extract_title:
            if i.text.strip() in get_data:
                console.print(f" [[bold red]-[/bold red]] {i.text.strip()}")
                continue
            else:
                console.print(f" [[bold green]+[/bold green]] {i.text.strip()}")
                db.insert({"title": i.text.strip()})
    print("Saved itmes to db | PRESS ENTER TO EXIT")
    os.system("pause >nul")
    os.system("cls")
    return