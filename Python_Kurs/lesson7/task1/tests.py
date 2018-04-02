from test_helper import run_common_tests, failed, get_answer_placeholders, passed


def test_window():
    window = get_answer_placeholders()[0]
    if "fun" in window:
        passed()
    else:
        failed("Nenne die Funktion fun")


def test_window1():
    window = get_answer_placeholders()[0]
    if "def " in window:
        passed()
    else:
        failed("Benutze def für die Definition der Funktion")


def test_column():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Vergesse nicht : am Ende")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_column()
    test_window1()
