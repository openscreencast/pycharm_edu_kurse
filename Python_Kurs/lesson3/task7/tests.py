from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, "first_half") and file.first_half == '''\nEs ist eine wirklich lange Zeichenkette (String)\nTriple-quoted''':
        passed()
    else:
        failed("Erinnere dich an Slicing.")

def test_value_python3():
    import sys
    if sys.version[0] != "3":
        passed()
        return
    try:
        import_task_file()
        passed()
    except TypeError:
        failed("/ Operator gibt float in Python3 zurück. Benutze die int() Funktion für die Umwandlung in integer (int).")

def test_window():
    window = get_answer_placeholders()[0]
    if "phrase" in window and "len" in window:
        passed()
    else:
        failed("Erinnere dich an Slicing.")


if __name__ == '__main__':
    test_value_python3()
    run_common_tests()

    test_value()
    test_window()
