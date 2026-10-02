import os
from rich.console import Console
console = Console()

def more_then3():
    with open("data/db.txt", "r") as f:
        lines = f.readlines()
    
    user_input = input("remove old data? [y/n]: ")
    if user_input == "y":
        os.remove("sort/more_then3.txt")
    user_input = input("min words: ")
    with open("sort/more_then3.txt", "w", encoding="utf-8") as f:
        for line in lines:
            get_words = line.strip()
            get_words = get_words.split(" ")
            if len(get_words) > int(user_input):
                clean_line = " ".join(get_words)
                f.write(clean_line + "\n")
                console.print(" [[bold green]+[/bold green]] " + clean_line)
            else:
                continue
    print("Sorted data saved to [sort/more_then3.txt] | PRESS ENTER TO EXIT")
    os.system("pause >nul")
    os.system("cls")
    return


if __name__ == "__main__":
    more_then3()