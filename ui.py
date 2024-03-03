from constants import (
    INVALID_INPUT_SELECTION_ERROR,
    OPERATION_CANCELED_BY_USER,
    PICK_ENTRY_EXPLANATION_TEXT,
    PROMPT_USER_FOR_ENTRY_NUMBER,
)


def print_article_selection_choices(results):
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result['title']}")


def get_user_selection(options):
    while True:
        user_input = input(PROMPT_USER_FOR_ENTRY_NUMBER)

        if user_input.lower() == "exit":
            print(OPERATION_CANCELED_BY_USER)
            return None

        try:
            choice = int(user_input)
            if not 1 <= choice <= len(options):
                raise ValueError
        except ValueError:
            print(INVALID_INPUT_SELECTION_ERROR)
            continue

        return options[choice - 1]["title"]


def prompt_user_for_selection(search_results):
    print(PICK_ENTRY_EXPLANATION_TEXT)
    print_article_selection_choices(search_results)
    return get_user_selection(search_results)
