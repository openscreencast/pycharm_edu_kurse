from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if file.number == 12.0:
        passed()
    else:
        failed("Benutze den += Operator")


def test_window():
    window = get_answer_placeholders()[0]
    if "+=" in window:
        passed()
    else:
        failed("Benutze den += Operator")


if __name__ == '__main__':
    run_common_tests("Du solltest die Datei ändern")
    test_value()
    test_window()
