from datetime import datetime, timedelta

import pytest
from freezegun import freeze_time

from lru_cache.lru_cache import LastRecentlyUsedCache


class TestPut:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lru = LastRecentlyUsedCache(cache_size=1)

    def test_normal(self):
        self.lru.put("a", "dataA")

        assert True

    def test_duplicated_key(self):
        self.lru.put("duplicated_key", "")
        self.lru.put("duplicated_key", "duplicated")

        actual = self.lru.get("duplicated_key")
        expected = "duplicated"
        assert actual == expected


class TestGet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lru = LastRecentlyUsedCache(cache_size=2, cache_time_limit=60)
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

    def test_time_limit(self):
        put_time = datetime.now()
        time = put_time + timedelta(minutes=10)  # 10分経過後の時間

        with freeze_time(time):
            actual = self.lru.get("first_key")

        expected = None
        assert actual == expected

    def test_replace_time_limit(self):
        _, put_time = self.lru.cache["first_key"]
        self.lru.get("first_key")
        _, actual = self.lru.cache["first_key"]

        assert actual > put_time


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


class TestChangeCacheSize:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.lru = LastRecentlyUsedCache(cache_size=2)
        self.lru.put("old_key", "old_data")

    def test_cache_size(self):
        lru = self.lru.change_cache_size(100)
        actual = lru.cache_size
        expected = 100

        assert actual == expected

    @pytest.mark.parametrize(
        "change_cache_size",
        [1, 2, 3],
    )
    def test_unchanged_cache(self, change_cache_size):
        lru = self.lru.change_cache_size(change_cache_size)
        actual = [(k, v[0]) for k, v in lru.cache.items()]

        expected = [("old_key", "old_data")]

        assert actual == expected

    class TestChangedCache:
        @pytest.fixture(autouse=True)
        def setup(self):
            self.lru = LastRecentlyUsedCache(cache_size=3)
            self.lru.put("old_key1", "old_data1")
            self.lru.put("old_key2", "old_data2")
            self.lru.put("old_key3", "old_data3")

        def test_changed_cache(self):
            self.lru.change_cache_size(1)

            actual = [(k, v[0]) for k, v in self.lru.cache.items()]
            expected = [("old_key3", "old_data3")]

            assert actual == expected
