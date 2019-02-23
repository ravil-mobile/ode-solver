from numpy import array, zeros

from .abstract import AbstractMethod


class ExampleMethod(AbstractMethod):
    def __init__(self):
        super().__init__()


    def adjust_data_structure(self):
        self.method_data["cs"] = "testing"
        self.method_data["itercount"] = array([2, 2, 1, 1, 1, 1])
        pass
