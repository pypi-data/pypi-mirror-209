"""This class defines the base machine object"""


class Machine:
    """The base machine object"""

    def __init__(self):
        """
        Create a new Machine object
        
        :return: The new machine object.
        """

        self.test = "Hello World"

    def work1(self):
        """
        Do Some work.
        
        :return: Nothing
        """
        print(self.test)

    def work2(self):
        """
        Do Some work.
        
        :return: The test string
        """
        return self.test
