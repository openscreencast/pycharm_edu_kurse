from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


def test_value():
    file = import_task_file()
    if hasattr(file, "length") and file.length == 12:
        passed()
    else:
        failed("nochmal zählen")

def test_window():
    window = get_answer_placeholders()[0]
    if "for " in window:
        passed()
    else:
        failed("Benutze eine for-Schleife")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_value()
