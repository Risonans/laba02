from my_lib import *
import pytest

#Тест фибоначчи
class fibonacci_numbers:
    #Тестируем программу на корректный ввод и вывод
    def test_on_correct_fib(self):
        assert fibonnaci(4) == [0, 1, 1, 2]

    #Тестируем на некорректный ввод
    def test_on_incorrect_fib(self):
        with pytest.raises(TypeError):
            fibonnaci("23sdgf")

#Тест сортировки пузырьком
class bubble_sort:
    #Тестируем корректный ввод и вывод
    @pytest.mark.parametrize("a, b, expected_result", [([3, 2, 1, 7], 1, [1, 2, 3, 7]),
                                                       ([3, 2, 1, 7], 2, [7, 3, 2, 1])])
    def test_on_correct_bubble(a, b, expected_result):
        assert bubble(a, b) == expected_result

    #Тестируем некорректный ввод
    def test_on_incorrect_bubble(self):
        with pytest.raises(TypeError):
            bubble(231,[])

#Тест калькулятора
class test_calculator:
    #Проверка калькулятора с корректным вводом
    @pytest.mark.parametrize("a, b, c, expected_result", [(1, 2, '+', 3),
                                                          (2, 1, '-', 1),
                                                          (2, 3, '*', 6),
                                                          (9, 3, '/', 3)])
    def test_on_correct_calc(a, b, c, expected_result):
        assert calculator(a, b, c) == expected_result

    #Проверка калькулятора с некорректным вводом
    def test_on_incorrect_calc(self):
        assert calculator('1',2, "+") == "Неверно заданы параметры"