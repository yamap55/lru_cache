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
    def test_get_not_exist_key(self):
        lru = LastRecentlyUsedCashe()

        actual = lru.get("NotExistKey")
        expected = None

        assert actual == expected

    def test_exceed_cache_size(self):
        # キャッシュサイズが指定値を超えた時にgetできないこと
        lru = LastRecentlyUsedCashe(cache_size=1)

        lru.put("old_key", "old_data")
        lru.put("new_key", "new_data")

        actual = lru.get("old_key")
        expected = None

        assert actual == expected
