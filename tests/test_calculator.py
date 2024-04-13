from my_python_template.calculator import my_sum


def test_my_sum_one_plus_one_is_two():
    assert my_sum(1, 1) == 2


def test_my_sum_one_plus_one_is_not_three():
    assert my_sum(1, 1) != 3
