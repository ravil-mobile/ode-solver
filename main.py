import numpy as np
from Problems.problems import Problem
from Methods.SIFIRK32_B2x2_dmpD4 import SIFIRK32_B2x2_dmpD4 as OdeMethod
#from Methods.example import ExampleMethod as OdeMethod


def main():

    #problem = Problem(time_start=0, time_end=2, tinterpol=[])
    #structure = problem.get_method_structure()
    #print(method.__bases__)
    method = OdeMethod()
    method_data = method.get_data()

    for item in method_data:
        print(f'item: {item} --> {method_data[item]}')

if __name__ == "__main__":
    main()