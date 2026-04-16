from analyzer import classify_event

def test_like():
    assert classify_event("/api/likePost") == "LIKE"


def test_comment():
    assert classify_event("/api/comment") == "COMMENT"


def test_view():
    assert classify_event("/api/feed") == "VIEW_POST"


def test_unknown():
    assert classify_event("/api/randomEndpoint") == "UNKNOWN"
