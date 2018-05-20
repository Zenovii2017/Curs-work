import time
import json
import requests
from Data.oauth import oauth
from greetings.greetings_with_user import breaktime
import sys
from URL.url import URL


def get_courses_list(url):
    """
    get courses list from udemy api with link
    :param url: str
    :return: list
    """
    data = oauth()
    r = requests.get(url, headers=data)
    response = json.loads(r.text)

    try:
        returned_list = response["results"]
    except:
        print("Wait 50 seconds, because program cant make more than 10")
        print("requests per 50 seconds")
        sys.exit()
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
        print("You input something wrong!")
        sys.exit()
    return returned_list


def get_curriculum_items(id):
    """
    get information about course from udemy api
    :param id: int
    :return: list
    """
    try:
        url = URL().curriculum_url().format(id)
        data = oauth()
        return json.loads(requests.get(url, headers=data).text)
    except:
        print("Wait 50 seconds")
