def test_upper():
    assert "hola".upper() == "HOLA"


def test_lower():
    assert "MUNDO".lower() == "mundo"


def test_capitalize():
    assert "python".capitalize() == "Python"


def test_title():
    assert "aprende python".title() == "Aprende Python"


def test_swapcase():
    assert "PyThOn".swapcase() == "pYtHoN"


def test_strip():
    assert "  hola  ".strip() == "hola"


def test_lstrip():
    assert "  hola".lstrip() == "hola"


def test_rstrip():
    assert "hola  ".rstrip() == "hola"


def test_replace():
    assert "Python es divertido".replace("divertido", "potente") == "Python es potente"


def test_find():
    assert "aprende python".find("py") == 8


def test_count():
    assert "banana".count("a") == 3


def test_startswith():
    assert "archivo.py".startswith("archivo")


def test_endswith():
    assert "archivo.py".endswith(".py")


def test_isalpha():
    assert "python".isalpha()


def test_isdigit():
    assert "12345".isdigit()


def test_isalnum():
    assert "abc123".isalnum()


def test_isspace():
    assert "   ".isspace()


def test_islower():
    assert "python".islower()


def test_isupper():
    assert "PYTHON".isupper()


def test_zfill():
    assert "42".zfill(5) == "00042"


def test_center():
    assert "hola".center(10, "-") == "---hola---"


def test_ljust():
    assert "hola".ljust(10, ".") == "hola......"


def test_rjust():
    assert "hola".rjust(10, ".") == "......hola"


def test_split():
    assert "uno, dos, tres".split(", ") == ["uno", "dos", "tres"]


def test_join():
    assert " ".join(["python", "es", "genial"]) == "python es genial"


def test_splitlines():
    assert "uno\ndos\ntres".splitlines() == ["uno", "dos", "tres"]


def test_strip_char():
    assert "---hola---".strip("-") == "hola"


def test_index():
    assert "python".index("thon") == 2


def test_format():
    name = "Juan"
    assert f"Hola, {name}" == "Hola, Juan"


def test_fstring():
    nombre = "Juan"
    assert f"Hola, {nombre}" == "Hola, Juan"


def test_expandtabs():
    assert "hola\tpython".expandtabs() == "hola    python"


def test_rfind():
    assert "banana".rfind("a") == 5


def test_rindex():
    assert "banana".rindex("a") == 5


def test_partition():
    assert "hola mundo".partition(" ") == ("hola", " ", "mundo")


def test_rpartition():
    assert "hola mundo mundo".rpartition(" ") == ("hola mundo", " ", "mundo")


def test_casefold():
    assert "MUNDO".casefold() == "mundo"


def test_get_item():
    assert "python"[0] == "p"
    assert "python"[-1] == "n"
    assert "python"[1:3] == "yt"
    assert "python"[:3] == "pyt"
    assert "python"[3:] == "hon"


def test_concat():
    assert "hola" + " " + "mundo" == "hola mundo"


def test_repeat():
    assert "python " * 3 == "python python python "


def test_len():
    assert len("python") == 6
