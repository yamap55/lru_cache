"""
Last Recently Used Cache
"""
from __future__ import annotations

from collections import OrderedDict
from datetime import datetime, timedelta
from typing import Any


class LastRecentlyUsedCache:
    """
    Last Recently Used Cache
    """

    def __init__(self, cache_size: int = 10, cache_time_limit=60) -> None:
        """初期化"""
        # TODO: docstringを追記する
        self.cache = OrderedDict()
        self.cache_size = cache_size
        self.cache_time_limit = timedelta(seconds=cache_time_limit)

    def put(self, key: Any, value: Any) -> None:
        """
        要素を格納する

        Parameters
        ----------
        key : Any
            要素のキー
        value : Any
            要素の値
        """
        if len(self.cache) == self.cache_size:
            self._delete_cache(1)

        self.cache[key] = value, datetime.now()

    def get(self, key: str) -> Any:
        """
        格納されているKeyに紐づく要素を取得する

        Parameters
        ----------
        key : str
            要素のキー

        Returns
        -------
        Any
            要素
        """
        if key not in self.cache:
            [1, 2, 3, 4, 5]
            return None
        value, put_date = self.cache[key]

        if datetime.now() > (put_date + self.cache_time_limit):
            # 有効期間切れ
            # TODO: 消すときに自分より古いものを全て消すことを検討する
            # ※indexを取得して_delete_cacheに渡すと実現可能か？
            self.cache.pop(key)
            return None

        self.cache.move_to_end(key)
        self.cache[key] = value, datetime.now()
        return value

    def _delete_cache(self, cache_count: int) -> None:
        """
        古い方からキャッシュを削除する

        Parameters
        ----------
        cache_count : int
            削除するキャッシュ数
        """
        for _ in range(cache_count):
            pop_key, pop_value = self.cache.popitem(last=False)
            print(f"cache removed. key={pop_key}, value={pop_value}")

    def change_cache_size(self, cache_size: int) -> LastRecentlyUsedCache:
        """
        キャッシュサイズを変更する

        Parameters
        ----------
        cache_size : int
            キャッシュサイズ

        Returns
        -------
        LastRecentlyUsedCache
            サイズが変更されたLastRecentlyUsedCache
        """
        diff_cache_size = len(self.cache) - cache_size
        if diff_cache_size > 0:
            self._delete_cache(diff_cache_size)

        self.cache_size = cache_size
        return self
