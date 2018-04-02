from test_helper import test_is_not_empty, test_answer_placeholders_text_deleted, passed, failed, import_task_file


def test_is_identifier():
    try:
        import_task_file()
    except NameError:
        passed()
        return
    except SyntaxError:
        failed("ungültigen Bezeichner verwendet")
        return
    failed("Unbestimmte Variable verwenden")


if __name__ == '__main__':
    error_text = "Du solltest hier eine undefinierte Variable eingeben."

    test_is_not_empty()
    test_answer_placeholders_text_deleted(error_text)
    test_is_identifier()
