class URL:
    """
    class that represents url class
    have methods:
        add_category() - add to url category of course
        add_subcategory() - add to url subcategory of course
        price() - add to url price
        is_affiliate_agreed() - add to url true or false depend on affiliate
        agreed
        is_fixed_priced_deals_agreed() -  add to url true or false depend on
        price
        is_percentage_deals_agreed() - add to url true or false depend on price
        language() - add to url setting language
        has_simple_quiz() -  add to url true or false depend on simple quiz
        has_closed_caption() -  add to url true or false depend on closed
        caption
        has_coding_exercises() - add to url true or false depend on ident
        url() - return url that represent courses list
        instructional_level() - check what is level of course
        ordering() - check what order has course
    """

    def __init__(self):
        self.__url = "https://www.udemy.com/api-2.0/courses/?page_size=100"
        self.__curriculum_url = "https://www.udemy.com/api-2.0/courses/{}\
/public-curriculum-items/?page_size=100"

    def add_category(self, text):
        """
        add to url category of course
        :param text: str
        :return: None
        """
        if " & " in text:
            i = 0
            new_text = ""
            while i <= len(text) - 1:
                try:
                    if text[i] == " " and text[i + 1] == "&" and text[
                        i + 2] == " ":
                        new_text += "+%26+"
                        i += 3
                    else:
                        new_text += text[i]
                        i += 1
                except:
                    break
        try:
            self.__url += "&category={}".format(new_text)
        except:
            self.__url += "&category={}".format(text)

    def add_subcategory(self, text):
        """
        add to url subcategory of course
        :param text: str
        :return: None
        """
        if " & " in text:
            i = 0
            new_text = ""
            while i <= len(text) - 1:
                try:
                    if text[i] == " " and text[i + 1] == "&" and text[
                        i + 2] == " ":
                        new_text += "+%26+"
                        i += 3
                    else:
                        new_text += text[i]
                        i += 1
                except:
                    break
        try:
            self.__url += "&subcategory={}".format(new_text)
        except:
            self.__url += "&subcategory={}".format(text)

    def price(self, ident):
        """
        add to url price
        :param ident: bool
        :return: None
        """
        if ident:
            self.__url += "&price=price-paid"
        else:
            self.__url += "&price=price-free"

    def is_affiliate_agreed(self, ident):
        """
        add to url true or false depend on affiliate
        :param ident: bool
        :return: None
        """
        self.__url += "&is_affiliate_agreed={}".format(ident)

    def is_fixed_priced_deals_agreed(self, ident):
        """
        add to url true or false depend on price
        :param ident: bool
        :return: None
        """
        self.__url += "&is_fixed_priced_deals_agreed={}".format(ident)

    def is_percentage_deals_agreed(self, ident):
        """
        add to url true or false depend on price
        :param ident: bool
        :return: None
        """
        self.__url += "&is_percentage_deals_agreed={}".format(ident)

    def language(self, text):
        """
        add to url setting language
        :param text: str
        :return: None
        """
        self.__url += "&language={}".format(text)

    def has_simple_quiz(self, ident):
        """
        add to url true or false depend on simple quiz
        :param ident: bool
        :return: None
        """
        self.__url += "&has_closed_caption={}".format(ident)

    def has_closed_caption(self, ident):
        """
        add to url true or false depend on closed caption
        :param ident: bool
        :return: None
        """
        self.__url += "&has_coding_exercises={}".format(ident)

    def has_coding_exercises(self, ident):
        """
        add to url true or false depend on ident
        :param ident: bool
        :return: None
        """
        self.__url += "&has_simple_quiz={}".format(ident)

    def instructional_level(self, text):
        """
        check what is level of course
        :param text: str
        :return: None
        """
        if " & " in text:
            i = 0
            new_text = ""
            while i <= len(text) - 1:
                try:
                    if text[i] == " " and text[i + 1] == "&" and text[
                        i + 2] == " ":
                        new_text += "+%26+"
                        i += 3
                    else:
                        new_text += text[i]
                        i += 1
                except:
                    break
        try:
            self.__url += "&instructional_level=".format(new_text)
        except:
            self.__url += "&instructional_level=".format(text)

    def ordering(self, text):
        """
        check what order has course
        :param text: str
        :return: str
        """
        if " & " in text:
            i = 0
            new_text = ""
            while i <= len(text) - 1:
                try:
                    if text[i] == " " and text[i + 1] == "&" and text[
                        i + 2] == " ":
                        new_text += "+%26+"
                        i += 3
                    else:
                        new_text += text[i]
                        i += 1
                except:
                    break
        try:
            self.__url += "&ordering={}".format(new_text)
        except:
            self.__url += "&ordering={}".format(text)

    def url(self):
        """
        return url
        :return: str
        """
        return self.__url


class curriculum_url():
    """
    class that represent curriculum url.Have methods:
        curriculum_url() - return url that represents curriculum list
    """

    def __init__(self, id):
        self.__curriculum_url = "https://www.udemy.com/api-2.0/courses/{}\
/public-curriculum-items/?page_size=100".format(id)

    def currric_url(self):
        """
        return url that represents curriculum list
        :return: str
        """
        return self.__curriculum_url
