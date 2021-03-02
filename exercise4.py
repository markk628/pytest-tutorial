import pytest

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

# if __name__ == "__main__":
#     result1 = extract_position('|error| numerical calculations could not converge.')
#     print(result1)
#     result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
#     print(result2)

@pytest.fixture
def average():
    return "|update| the positron location in the particle accelerator is x:21.432"

@pytest.fixture
def null():
    return None

@pytest.fixture
def error():
    return "|error| numerical calculations could not converge."

def test_extract_positio_average(average):
    assert extract_position(average) == "21.432"

def test_extract_position_null(null):
    assert extract_position(null) == None

def test_extract_position_error(error):
    assert extract_position(error) == None