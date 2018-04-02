from test_helper import run_common_tests, import_task_file, passed, failed, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, "animals") and "dinosaur" in file.animals and not "dino" in file.animals:
        passed()
    else:
        failed("Ersetze 'dino' durch 'dinosaur'")

def test_window():
    window = get_answer_placeholders()[0]
    if "animals" in window and "[" in window:
        passed()
    else:
        failed("Ersetze 'dino' durch 'dinosaur'")

if __name__ == '__main__':
    run_common_tests("Benutze die Indexierung und Zuweisung")
    test_value()
    test_window()
