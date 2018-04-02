from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "my_object" in window and "variable1" in window:
        passed()
    else:
        failed("Benutze my_object.variable1 für den Zugriff")

def test_window1():
    window = get_answer_placeholders()[0]
    if "my_object " in window or "my_object." in window:
        passed()
    else:
        failed("Benutze my_object.variable1 für den Zugriff")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
