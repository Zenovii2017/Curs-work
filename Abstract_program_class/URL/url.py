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
        language() - add to url setting language
        has_simple_quiz() -  add to url true or false depend on simple quiz
        has_closed_caption() -  add to url true or false depend on closed
        caption
        has_coding_exercises() -
        url() - return url that represent courses list
        curriculum_url() - return url that represents curriculum list
        instructional_level() - check what is level of course
        ordering() - check what order has course
    """

    def __init__(self):
        self.__url = "https://www.udemy.com/api-2.0/courses/?page_size=100"
        self.__curriculum_url = "https://www.udemy.com/api-2.0/courses/{}\
/public-curriculum-items/?page_size=100"

    def add_category(self, text):
        raise NotImplementedError

    def add_subcategory(self, text):
        raise NotImplementedError

    def price(self, text):
        raise NotImplementedError

    def is_affiliate_agreed(self, variable):
        raise NotImplementedError

    def is_fixed_priced_deals_agreed(self, variable):
        raise NotImplementedError

    def is_percentage_deals_agreed(self, variable):
        raise NotImplementedError

    def language(self, text):
        raise NotImplementedError

    def has_simple_quiz(self, variable):
        raise NotImplementedError

    def has_closed_caption(self, variable):
        raise NotImplementedError

    def has_coding_exercises(self, variable):
        raise NotImplementedError

    def instructional_level(self, variable):
        raise NotImplementedError

    def ordering(self, variable):
        raise NotImplementedError

    def url(self):
        return self.__url

    def curriculum_url(self):
        return self.__curriculum_url
