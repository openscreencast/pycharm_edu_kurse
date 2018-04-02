from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "len(" in window:
        passed()
    else:
        failed("Benutze die Funktion len()")


if __name__ == '__main__':
    run_common_tests("Benutze die Funktion len()")
    test_window()
