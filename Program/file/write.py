def write_list_with_courses(data):
    """
    records links to courses in a file
    :param data: list
    :return: None
    """
    with open("result.txt", "w") as write_file:
        if data == [] or data is None:
            write_file.write("Sorry, but program didnt search anything.")
            return None
        i = 1
        for mini_data in data:
            write_file.write("{}.".format(i))
            for key in mini_data:
                if key == "title":
                    try:
                        write_file.write(mini_data[key])
                        write_file.write(" - ")
                    except:
                        for letter in mini_data[key]:
                            try:
                                print(
                                    "Program get wrong input data so program "
                                    "change name of {} course!".format(i))
                                write_file.write(letter)
                            except:
                                pass
                        write_file.write(" - ")
                elif key == "url":
                    try:
                        write_file.write(
                            "www.udemy.com{}".format(mini_data[key]))
                    except:
                        for letter in mini_data[key]:
                            try:
                                print(
                                    "Program get wrong input data so program "
                                    "change name of {} course!".format(i))
                                write_file.write(letter)
                            except:
                                pass
            write_file.write("\n")
            i += 1
    print("Program save results in result.txt")


def special_write(data):
    """
    special write for curriculum data
    :param data: list
    :return: None
    """
    with open("result.txt", "w") as opened_file:
        if len(data) != 0:
            i = 1
            for course_data in data:
                if "url" in course_data[-1] and "title" in course_data[-1]:
                    opened_file.write("{}.".format(i))
                    opened_file.write(course_data[-1]["title"])
                    opened_file.write(" - ")
                    opened_file.write(
                        "www.udemy.com{}".format(course_data[-1]["url"]))
                    opened_file.write("\n")
                    i += 1
        else:
            opened_file.write("Sorry, but program didnt search anything.")
    print("Program save results in result.txt")
