def classify_event(url):
    """
    Takes a URL string and returns the type of user action.
    """

    url = url.lower()

    if "like" in url:
        return "LIKE"
    elif "comment" in url:
        return "COMMENT"
    elif "feed" in url or "timeline" in url:
        return "VIEW_POST"
    else:
        return "UNKNOWN"
