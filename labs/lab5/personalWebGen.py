def main():
    # name = str(input("Enter your name: "))
    # description = str(input("Enter a description: "))

    with open("./boilerplate.html", "r") as input_file:
        lines = input_file.readlines()

        for i in range(0, len(lines)):
            if lines[i].startswith("  <body>"):
                name = str(input("Enter your name: "))
                description = str(input("Enter a description: "))
                resulting_html = f"""
                <h1>{name}</h1>
                <center>{description}</center>
                </body>
                """
                lines[i] = lines[i][0:8] + resulting_html

    with open("index.html", "w") as output_file:
        output_file.writelines(lines)


if __name__ == "__main__":
    main()
