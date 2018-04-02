from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "color" in window:
        passed()
    else:
        failed("einen color-Parameter hinzufügen")


def test_window1():
    window = get_answer_placeholders()[0]
    if "self" in window:
        passed()
    else:
        failed("den self-Parameter nicht vergessen")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
