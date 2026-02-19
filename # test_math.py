# test_math.py
def add(a, b):
    return a + b

def test_addition():
    assert add(2, 2) == 5  # ❌ This will fail! (2+2=4, not 5)
    
def test_subtraction():
    result = 10 - 3
    assert result == 8  # ❌ This will also fail! (10-3=7, not 8)
