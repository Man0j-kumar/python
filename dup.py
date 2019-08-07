def test_case(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False
print(test_case([1,2,3,4]))
print(test_case([1,2,2,3,4,6,4]))