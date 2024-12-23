import os
import sys

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab3.task1.src.task1_1 import main as task1
from lab3.task1.src.task1_2 import main as task1
from lab3.task2.src.task2 import main as task2
from lab3.task3.src.task3 import main as task3
from lab3.task4.src.task4 import main as task4
from lab3.task5.src.task5 import main as task5
from lab3.task6.src.task6 import main as task6


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task1, [path+"/task1/txtf/input.txt"]),
        "Задание №2": (task2, [path+"/task2/txtf/input.txt"]),
        "Задание №3": (task3, [path+"/task3/txtf/input.txt"]),
        "Задание №4": (task4, [path+"/task4/txtf/input.txt"]),
        "Задание №5": (task5, [path+"/task5/txtf/input.txt"]),
        "Задание №6": (task6, [path+"/task6/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('--------------------')
        print(task_name)
        print('--------------------')
        if inputs != 1:
            for input_file in inputs:
                output_file = input_file.replace("input", "output")
                task_func(input_file, output_file)
                print()
        else:
            task_func()
            print()


if __name__ == "__main__":
    main()
