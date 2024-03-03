import sys
from constants import FETCH_ERROR, NO_RESULTS_FOUND_ERROR
from wiki_api import fetch_wiki_articles, fetch_wiki_summary
from ui import prompt_user_for_selection


def args_to_string(input):
    return " ".join(input[1:])


def fetch_and_print_summary(topic):
    summary = fetch_wiki_summary(topic)
    print(summary if summary else FETCH_ERROR)


def find_articles(topic):
    search_results = fetch_wiki_articles(topic)
    if search_results:
        selected_topic = prompt_user_for_selection(search_results[1:])
        if selected_topic:
            fetch_and_print_summary(selected_topic)
    else:
        print(NO_RESULTS_FOUND_ERROR)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = args_to_string(sys.argv)
        summary = fetch_wiki_summary(topic)
        if summary:
            print(summary)

        else:
            find_articles(topic)
    else:
        print("Usage: wiki <TOPIC_NAME>")
