from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "import " in window:
        passed()
    else:
        failed("Benutze das import-Schlüsselwort")


def test_window1():
    window = get_answer_placeholders()[0]
    if "my_module" in window:
        passed()
    else:
        failed("Importiere my_module")


def test_window2():
    window = get_answer_placeholders()[0]
    if "my_module.py" in window:
        failed("Benutze nicht die Dateiendung")
    else:
        passed()


def test_window3():
    window = get_answer_placeholders()[1]
    if "my_module" in window and "hello_world(" in window:
        passed()
    else:
        failed("Benutze my_module.hello_world um die Funktion hello_world aufzurufen")

if __name__ == '__main__':
    run_common_tests()
    test_window1()
    test_window()
    test_window2()
    test_window3()
