def greetings_with_user():
    """
    greetings with user.Print all information about programe for user
    :return: None
    """
    print("\nHello!\n")
    print("This program can help you search extra courses.\n")
    print("If you want know how program works, read help.txt in folder\
 Documentation.\n")


def breaktime():
    """
    says user about limitation of count request
    :return: list
    """
    print("\nProgram can send only 10 requests per 50 second.\n")
    print("Per one requests program can download data only about\
 100 courses.\n")
    print("If you can wait, program can dowload more data.\n")
    print("If not, program can check information about courses, that\
 program download.\n")
    print("Program will write this every ten times that program download\
 course.\n")
    print("Input yes, if you can wait and no or nothing if you cant wait.\n")
    return input("Your answer is: ").lower()


def choice():
    """
    says user about two ways working program
    :return: None
    """
    print("You have choice.\n")
    print("Process the received information using udemy API resources, or\
 using methods implemented by the authors of the program. Read about the\
 advantages of the analysis in help.txt.\n")
    print("If you want using udemy resources input udemy.")
    print("If you input something else, program will work on her methods\n")
    return input("Your answer is: ").lower()
