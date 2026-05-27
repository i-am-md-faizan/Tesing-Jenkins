from app import divide

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5

if __name__ == "__main__":
    test_divide()
    print("All tests passed ✅")
