from Tarea_Func_3 import sum_digits_list
import pytest

def test_sum_digit_list_with_large_numbers_return_correct_results(capsys):
    #arrange
    list_input = [25639, 256398, 55555, 15236985, 1236589, 88888999]
    #act
    sum_digits_list(list_input)
    #assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "The sum of the digits in the list is 105700165"


def test_sum_digit_list_with_negative_large_numbers_return_correct_results(capsys):
    #arrange
    list_input = [-25639, -256398, -55555, -15236985, -1236589, -88888999]
    #act
    sum_digits_list(list_input)
    #assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "The sum of the digits in the list is -105700165"



def test_sum_digit_list_with_empty_list_return_correct_results(capsys):
    #arrange
    list_input = []
    #act
    sum_digits_list(list_input)
    #assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "The sum of the digits in the list is 0"