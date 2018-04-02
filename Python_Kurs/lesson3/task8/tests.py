from test_helper import run_common_tests, get_answer_placeholders, passed, failed, get_file_output


def test_value():
    window = get_answer_placeholders()[0]

    first = "Der Name dieses Eises ist \\\"Sweet'n'Tasty\\\""
    second = 'Der Name dieses Eises ist "Sweet\\\'n\\\'Tasty"'

    if first in window or second in window:
        passed()
    else:
        if '\\\"Sweet' in window or 'Tasty\\\"' in window:
            failed("Es ist nicht notwendig, das doppelte Anführungszeichen in einfachen Anführungszeichen zu escapen.")
        failed("Entschuldigung, der falsche String wird ausgegeben")


def test_output():
    output = get_file_output()
    index = output.index('''\"Süß\" ist ein Eis.''')
    if index > 0:
        if len(output) > index + 2:
            failed("Ausgabe in einer Zeile")
    passed()


if __name__ == '__main__':
    run_common_tests()
    test_output()
    test_value()
