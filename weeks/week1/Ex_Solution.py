# Jadon Zufall-CS 1120-100
# Aug 31 2022

def main() -> None:
    text: str = "This is my string, it contains words.  This string is a string."
    stripped_text: str = text.replace(",", "").replace(".", "")
    words: dict = {}
    for i in stripped_text.split(" "):
        w: str = i.strip().lower()
        if w == "":
            continue
        try:
            words[w] += 1
        except KeyError:
            words[w] = 1

    for i in words:
        print(f"{i} : {words[i]}")


if __name__ == "__main__":
    main()
