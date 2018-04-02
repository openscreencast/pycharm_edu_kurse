from test_helper import run_common_tests, failed, get_answer_placeholders, passed


def test_window():
    window = get_answer_placeholders()[0]
    if "square" in window and "def " in window:
        passed()
    else:
        failed("Nenne die Funktion square")


def test_column():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Vergesse nicht : am Ende")

if __name__ == '__main__':
    run_common_tests()
    test_column()
    test_window()
