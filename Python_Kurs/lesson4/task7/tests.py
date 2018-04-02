from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "grocery_dict" in window and " in " in window:
        passed()
    else:
        failed("Benutze das in-Schlüsselwort")

def test_fish():
    window = get_answer_placeholders()[0]
    if "fish" in window:
        passed()
    else:
        failed("Prüfe ob die grocery_dict keys fish enthalten")

if __name__ == '__main__':
    run_common_tests("Benutze das in-Schlüsselwort")
    test_window()
    test_fish()
