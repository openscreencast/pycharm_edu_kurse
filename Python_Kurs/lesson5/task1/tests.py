from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "name" in window and "John" in window and "and" in window and "23" in window:
        passed()
    else:
        failed("Benutze das and-Schlüsselwort und den != Operator")


if __name__ == '__main__':
    run_common_tests("Benutze das and-Schlüsselwort und den != Operator")
    test_window()
