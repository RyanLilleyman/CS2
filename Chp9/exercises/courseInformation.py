def main():
    n = int(input("How many classees are you taking this semester?"))
    for i in range(n):
        classes = {}
        print(f"Enter the {i}th course:")
        course = str(input())
        print(f"Enter the {course} room number")
        courseNumber = str(input())

        classes[course] = courseNumber


if __name__ == "__main__":
    main()
