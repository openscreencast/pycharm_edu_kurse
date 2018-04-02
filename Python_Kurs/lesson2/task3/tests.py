from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_type_used():
    window = get_answer_placeholders()[0]
    if "type" in window and "float_number" in window:
        passed()
    else:
        failed("Nutze die type() Funktion")

if __name__ == '__main__':
    run_common_tests()
    test_type_used()
