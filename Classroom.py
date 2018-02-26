# module with class Classroom
# writed Zenovii Popenyuk


class Classroom():
    """
    class Classroom
    have parameter number capacity equimpent
    have function:
        is_larger():
            return classroom is larger than another classroom
        equipment_differences():
            return equipment that is in our room but isn`t in another
    """
    def __init__(self, number='001', capacity=0, equimpent=[]):
        """
        (string, int, list)
        """
        self.number = number
        self.capacity = capacity
        self.equimpent = equimpent

    def __str__(self):
        """
        if you want to print classroom this function will be used
        :return str
        """
        print_sentence = 'Classroom {} has a capacity of {} persons and has the following equipment: {}\
            .'.format(self.number, self.capacity, ", ".join(self.equimpent))
        return print_sentence

    def is_larger(self, another_self):
        """
        Calculate is classroom is larger or no
        :param another_self: Classroom
        :return: bool
        """
        if self.capacity > another_self.capacity:
            return True
        return False

    def equipment_differences(self, another_self):
        """
        Make list of equipment that is in our room and isn`t in another
        :param another_self: Classroom
        :return: list
        """
        lst = []
        for equimpents in self.equimpent:
            if equimpents not in another_self.equimpent:
                lst.append(equimpents)
        return lst

    def __repr__(self):
        sentence = 'Classroom({}, {}, {})'.format(self.number,\
                               self.capacity, self.equimpent)
        return sentence


