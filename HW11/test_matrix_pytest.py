import pytest
import task4


def test_is_prime():
    arr1 = task4.Matrix([[1, 2, 3], [1, 3, 4]])
    arr2 = task4.Matrix([[2, 3], [5, 6], [3, 4]])
    arr3 = task4.Matrix([[2, 3], [5, 6], [3, 4]])
    assert not arr1 == arr2, 'Матрицы arr1 и arr2 не равны'
    assert arr3 == arr2, 'Матрицы arr3 и arr2 равны'


def test_type():
    with pytest.raises(TypeError):
        task4.Matrix(1, 3)


def test_value():
    arr1 = task4.Matrix([[1, 2, 3], [1, 3, 4]])
    arr2 = task4.Matrix([[2, 3], [5, 6], [3, 4]])
    with pytest.raises(ValueError):
        arr1 + arr2


if __name__ == '__main__':
    pytest.main(['-v'])
