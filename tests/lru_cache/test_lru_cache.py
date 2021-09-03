from lru_cache.lru_cache import LastRecentlyUsedCashe


def test_put():
    lru = LastRecentlyUsedCashe()
    lru.put("a", "dataA")

    assert True


def test_get():
    lru = LastRecentlyUsedCashe()
    lru.put("a", "dataA")

    actual = lru.get("a")
    expected = "dataA"
    assert actual == expected
