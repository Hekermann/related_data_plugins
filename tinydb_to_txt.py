import tinydb
from rich.console import Console
import os

console = Console()
db = tinydb.TinyDB("data/db.json", encoding="utf-8")

def clear():
    try:
        os.remove("data/db.txt")
    except:
        return "file not found"

def to_txt():
    all_data = db.all()
    print("Converting [TinyDB] to [TXT] data/db.json > data/db.txt")
    print()

    user_inout = input("remove old file? [y/n]: ")
    if user_inout == "y":
        clear()
        print("Removed old file [PREE ENTER TO START]")
        os.system("pause >nul")
        os.system("cls")
    with console.status("Converting... ", spinner="dots"):
        for i in all_data:
            try:
                with open("data/db.txt", "a", encoding="utf-8") as f:
                        console.print(f" [[bold red]-[/bold red]] {i["title"]}")
                        f.write(i["title"] + "\n")
            except:
                console.print(f" [[bold red]-[/bold red]] {i["title"]}")
                
    console.print("Converting done", style="bold green")
    os.system("pause >nul")
    os.system("cls")
    return
            