from helloworld import hello

def test_hello(capfd):
    hello()
    out, err = capfd.readouterr()

    assert out == "Hello World\n"
    assert err is ''