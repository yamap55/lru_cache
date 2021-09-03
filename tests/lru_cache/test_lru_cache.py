from lru_cache.lru_cache import LastRecentlyUsedCashe


def test_put():
    lru = LastRecentlyUsedCashe()
    lru.put("a", "dataA")
    assert True
