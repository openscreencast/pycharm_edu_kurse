from test_helper import run_common_tests, passed, failed, get_answer_placeholders, import_task_file, get_file_output


def test_window1():
    windows = get_answer_placeholders()

    if windows[1].isdigit():
        passed()
        return
    else:
        output = get_file_output()
        if len(output) > 1:
            import re

            p = re.compile("Ich bin (\d*) Jahre alt.")
            if p.match(output[1]) is not None:
                passed()
                return
    failed("Zifferausgabe")


def test_window():
    windows = get_answer_placeholders()

    if windows[0] == "%d":
        passed()
    else:
        failed("Benutze %d als Symbol")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
