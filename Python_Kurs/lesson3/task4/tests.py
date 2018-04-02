from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, "exclamation") and file.exclamation == "!":
        passed()
    else:
        failed("Benutze den -1-Index um das letzte Zeichen zu erhalten.")


def test_negative_index():
    window = get_answer_placeholders()[0]
    if "-" in window:
        passed()
    else:
        failed("Benutze den negativen Index")

if __name__ == '__main__':
    run_common_tests()

    test_negative_index()
    test_value()
