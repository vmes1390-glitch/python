from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_name():
    for name in ["Erfan", "Sobhan", "Maliheh"]:
        assert hello("Erfan") == "hello, Erfan"