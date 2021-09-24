import pytest

from lru_cache.lru_cache import LastRecentlyUsedCache


def test_put():
    lru = LastRecentlyUsedCache()
    lru.put("a", "dataA")

    assert True


class TestGet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lru = LastRecentlyUsedCache(cache_size=2)
        self.lru.put("first_key", "data_1")
        self.lru.put("second_key", "data_2")

    def test_normal(self):
        actual = self.lru.get("first_key")
        expected = "data_1"
        assert actual == expected

    def test_change_cache_order(self):
        self.lru.get("first_key")
        self.lru.put("third_key", "data_3")

        actual = self.lru.get("second_key")
        assert actual is None

        # 念のため本来消えるはずであったキャッシュが残っている事を確認
        actual_first = self.lru.get("first_key")
        expected_first = "data_1"
        assert actual_first == expected_first


class TestGetReturnNone:
    def test_get_not_exist_key(self):
        lru = LastRecentlyUsedCache()

        actual = lru.get("NotExistKey")
        expected = None

        assert actual == expected

    def test_exceed_cache_size(self):
        # キャッシュサイズが指定値を超えた時にgetできないこと
        lru = LastRecentlyUsedCache(cache_size=1)

        lru.put("old_key", "old_data")
        lru.put("new_key", "new_data")

        actual = lru.get("old_key")
        expected = None

        assert actual == expected
