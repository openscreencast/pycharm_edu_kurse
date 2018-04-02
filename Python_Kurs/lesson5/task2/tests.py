from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if " and " in window and " or " in window and " not " in window:
        passed()
    else:
        failed("Benutze 'and', 'or' und 'not'")


if __name__ == '__main__':
    run_common_tests("Benutze 'and', 'or' und 'not'")
    test_window()
