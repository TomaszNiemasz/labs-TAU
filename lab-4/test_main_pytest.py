import pytest
from main import add, sub, root, factorial

test_data_add = [(1, 2, 3), (10, 5, 15), (-5, 6, 1)]
test_data_add_type = [(1, 'true', 3), (7.5, 5, 13)]
# test_data_add_value = [(-32767, 32767, 0), (5, 10, 15), (-2147483647, 2147483647, 0)]
test_data_sub = [(2, 2, 0), (-8, -2, -6), (2, -7, 9)]
test_data_sub_type = [(2, 1.7, 0), ('two', -7, 9)]
# test_data_sub_value = [(-32767, 32767, -65534), (5, 10, -5), (-2147483647, 2147483647, -4294967294)]
test_data_factorial = [(1, 1), (0, 1)]
test_data_factorial_type = [(3 + 8j, 1), ('zero', 1)]
test_data_factorial_value = [(-3, 1), (-1, None)]
test_data_root = [(27, 3, 3.0), (4, 2, 2.0), (1, 8, 1.0)]
test_data_root_type = [(25.5, 3, 3.0), ('two', 4, 2.0)]
test_data_root_value = [(-27, 2, 3.0), (-2, 4, 0.5)]


@pytest.mark.parametrize("num1, num2, result", test_data_add)
def test_add(num1, num2, result):
    assert add(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", test_data_add_type)
def test_add_type(num1, num2, result):
    with pytest.raises(TypeError):
        assert add(num1, num2) == result


# @pytest.mark.parametrize("num1, num2, result", test_data_add_value)
# def test_add_value(num1, num2, result):
#     with pytest.raises(ValueError):
#         assert add(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", test_data_sub)
def test_sub(num1, num2, result):
    assert sub(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", test_data_sub_type)
def test_sub_type(num1, num2, result):
    with pytest.raises(TypeError):
        assert sub(num1, num2) == result


# @pytest.mark.parametrize("num1, num2, result", test_data_sub_value)
# def test_sub_value(num1, num2, result):
#     with pytest.raises(ValueError):
#         assert sub(num1, num2) == result


@pytest.mark.parametrize("num1, result", test_data_factorial)
def test_factorial(num1, result):
    assert factorial(num1) == result


@pytest.mark.parametrize("num1, result", test_data_factorial_type)
def test_factorial_type(num1, result):
    with pytest.raises(TypeError):
        assert factorial(num1) == result


@pytest.mark.parametrize("num1, result", test_data_factorial_value)
def test_factorial_value(num1, result):
    with pytest.raises(ValueError):
        assert factorial(num1) == result


@pytest.mark.parametrize("num1, num2, result", test_data_root)
def test_root(num1, num2, result):
    assert root(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", test_data_root_type)
def test_root_type(num1, num2, result):
    with pytest.raises(TypeError):
        assert root(num1, num2) == result


@pytest.mark.parametrize("num1, num2, result", test_data_root_value)
def test_root_value(num1, num2, result):
    with pytest.raises(ValueError):
        assert root(num1, num2) == result


if __name__ == "__main__":
    pytest.main()
