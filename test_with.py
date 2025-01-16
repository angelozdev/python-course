def test_using_resource():
    with open("./poem.txt") as poem:
        print(poem.readlines())
        assert poem.name == "./poem.txt"
        assert poem.closed == False

    assert poem.closed == True
