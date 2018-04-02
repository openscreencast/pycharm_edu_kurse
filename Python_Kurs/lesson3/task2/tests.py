from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, "ten_of_hellos") and file.ten_of_hellos == "HalloHalloHalloHalloHalloHalloHalloHalloHalloHallo":
        passed()
    else:
        failed("Benutze eine Multiplikation")

def test_window():
    window = get_answer_placeholders()[0]
    if "*" in window:
        passed()
    else:
        failed("Benutze eine Multiplikation")

if __name__ == '__main__':
    run_common_tests("Du solltest die Datei ändern")

    test_value()
    test_window()
