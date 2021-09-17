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


class TestGetReturnNone:
    def test_exceed_cache_size(self):
        # キャッシュサイズが指定値を超えた時にgetできないこと
        lru = LastRecentlyUsedCashe(size=1)
        lru.put("a", "dataA")
        lru.put("b", "dataB")

        actual = lru.get("a")
        expected = None

        assert actual == expected
