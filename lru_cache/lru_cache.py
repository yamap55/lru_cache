"""
Last Recently Used Cashe
"""
from collections import OrderedDict
from typing import Any


class LastRecentlyUsedCashe:
    """
    Last Recently Used Cashe
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
            pop_key, pop_value = self.cache.popitem(last=False)
            print(f"cache removed. key={pop_key}, value={pop_value}")

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
