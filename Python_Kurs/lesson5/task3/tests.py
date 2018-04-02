from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Vergesse nicht : am Ende")


def test_len():
    window = get_answer_placeholders()[0]
    if "len" in window:
        passed()
    elif "not" in window:
        passed()
    else:
        failed("Benutze die Funktion len()")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_len()
