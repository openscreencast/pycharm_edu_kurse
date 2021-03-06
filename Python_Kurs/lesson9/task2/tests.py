from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_window():
    window = get_answer_placeholders()[0]
    output = get_file_output()
    if "datetime" not in window:
        failed("Benutze das datetime-Modul")
    elif len(output) > 0 and "<" not in output[0]:
        passed()
    else:
        failed("Gib das aktuelle Datum aus")

if __name__ == '__main__':
    run_common_tests()
    test_window()
