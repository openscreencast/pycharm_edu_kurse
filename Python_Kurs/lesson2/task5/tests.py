from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_division():
    file = import_task_file()
    if file.result == 4.5:
        passed()
    else:
        failed("Falsches Ergebnis")


def test_remainder():
    file = import_task_file()
    if file.remainder == 1.0:
        passed()
    else:
        failed("Falscher Restwert")


def test_windows():
    windows = get_answer_placeholders()
    if not "/" in windows[0]:
        failed("Benutze den / Operator")
        return
    if not "%" in windows[1]:
        failed("Benutze den % Operator")
        return
    if "number" in windows[0] and "number" in windows[1]:
        passed()
    else:
        failed("Benutze den gespeicherten Wert in der Variable \"number\"")


if __name__ == '__main__':
    run_common_tests("Benutze die / und % Operatoren")
    test_windows()
    test_division()
    test_remainder()
