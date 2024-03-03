from fetch import fetch
from constants import (
    EXPANDING_SEARCH_TEST,
    NO_SPECIFIC_ENTRY_FOUND_ERROR,
    SEARCH_URL,
    SUMMARY_BASE_URL,
)


def fetch_wiki_articles(topic):
    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json",
        "srlimit": 10,
    }
    print(EXPANDING_SEARCH_TEST)
    response_data = fetch(SEARCH_URL, params, "articles")
    return response_data.get("query", {}).get("search", []) if response_data else []


def fetch_wiki_summary(topic):
    summary_url = f"{SUMMARY_BASE_URL}{topic.replace(' ', '_')}"
    response_data = fetch(summary_url, fetchType="article summary")
    if response_data and response_data.get("type") != "disambiguation":
        return response_data.get("extract", "Summary not available.")
    print(NO_SPECIFIC_ENTRY_FOUND_ERROR)
    return None
