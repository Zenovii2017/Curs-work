import time
import json
import requests
from Data.oauth import oauth
from greetings.greetings_with_user import breaktime
from URL.url import URL, curriculum_url


def get_courses_list(url):
    """
    get courses list from udemy api with link
    :param url: str
    :return: list
    """
    currenttime = time.time()
    while True:
        try:
            data = oauth()
            r = requests.get(url, headers=data)
            response = json.loads(r.text)
            break
        except:
            print("Wait 50 seconds, because program cant make more than 10")
            print("requests per 50 seconds")
            while time.time() - currenttime <= 50:
                pass
    while True:
        try:
            currenttime = time.time()
            returned_list = response["results"]
            break
        except:
            print("Wait 50 seconds, because program cant make more than 10")
            print("requests per 50 seconds")
            while time.time() - currenttime <= 50:
                pass
    times = 1
    try:
        while response["next"] is not None:
            if times != 10:
                r = requests.get(response["next"], headers=data)
                response = json.loads(r.text)
                returned_list += response["results"]
                currenttime = time.time()
                times += 1
            else:
                answer = breaktime()
                if answer == "no" or answer == "":
                    break
                else:
                    while time.time() - currenttime <= 50:
                        pass
                times = 0
    except:
        print("Program can loose some data because you input something wrong!")
        pass
    return returned_list


def get_curriculum_items(id):
    """
    get information about course from udemy api
    :param id: int
    :return: list
    """
    url = curriculum_url(id).currric_url()
    returned_list = get_courses_list(url)
    return returned_list


def cut_data(data):
    """
    cut getted data
    :param data: dict
    :return: dict
    """
    print("If you want to get courses with free price, input free, if with "
          "paid price print paid, if it didnt matter for you press Enter!")
    answer = input("You answer is: ").lower()
    returned_data = []
    if answer == "free":
        for i in data:
            if i["is_paid"] == False:
                returned_data.append(i)
    elif answer == "paid":
        for i in data:
            if i["is_paid"] == True:
                returned_data.append(i)
    while True:
        try:
            print("We can analyze only 10 courses per 50 seconds, so you must"
                  " choose, which value will be perfect for you.")
            value = int(input("How many courses you want analyze?: "))
            break
        except:
            print("You input wrong data.")
    if answer:
        return returned_data[:value]
    else:
        return data[:value]
