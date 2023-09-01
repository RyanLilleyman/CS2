def main():
    n = int(input("How many classees are you taking this semester?"))
    classes = {}
    teachers = {}
    meetingTimes = {}
    for i in range(n):
        print(f"Enter the {i}th course:")
        course = str(input())

        print(f"Enter the {course} room number")
        courseNumber = str(input())

        print(f"Who is the professor of {course}?")
        prof = str(input())

        print(f"What is the meeting time of {course}?")
        time = str(input())
        teachers[course] = prof
        meetingTimes[course] = time
        classes[course] = courseNumber

    for k, v in classes.items():
        print(k, v)

    for k, v in teachers.items():
        print(k, v)
    for k, v in meetingTimes.items():
        print(k, v)


if __name__ == "__main__":
    main()
