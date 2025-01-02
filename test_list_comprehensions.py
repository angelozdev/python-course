def test_cubes_of_odd_numbers():
    numbers: range = range(1, 12)
    assert [x**3 for x in numbers if x % 2 != 0] == [1, 27, 125, 343, 729, 1331]


def test_lowercase_vowels():
    text: str = "Life is an incredible adventure"
    result: list[str] = [x for x in text.lower() if x in "aeiou"]
    expected: list[str] = ["i", "e", "i", "a", "i", "e", "i", "e", "a", "e", "u", "e"]
    assert result == expected


def test_words_longer_than_4():
    words: list[str] = [
        "sun",
        "elephant",
        "moon",
        "dog",
        "cat",
        "lion",
        "tiger",
        "snake",
    ]
    assert [x for x in words if len(x) > 4] == ["elephant", "tiger", "snake"]


def test_transpose_matrix():
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    expected: list[list[int]] = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    assert [[row[i] for row in matrix] for i in range(3)] == expected
