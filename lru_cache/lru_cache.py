"""
Last Recently Used Cache
"""
from __future__ import annotations

from collections import OrderedDict
from typing import Any


class LastRecentlyUsedCache:
    """
    Last Recently Used Cache
    """

    def __init__(self, cache_size: int = 10) -> None:
        """初期化"""
        self.cache = OrderedDict()
        self.cache_size = cache_size

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

        self.cache[key] = value

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
            return None

        self.cache.move_to_end(key)
        return self.cache[key]

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
