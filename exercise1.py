import math, pytest

def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
    li = [1,2,3,4,5]
    assert math.isclose(get_average(li), 3)

def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

def test_palindrom():
    with pytest.raises(TypeError):
        palindrome(44)