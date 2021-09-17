"""
Last Recently Used Cashe
"""
from typing import Any


class LastRecentlyUsedCashe:
    """
    Last Recently Used Cashe
    """

    def __init__(self, cache_size: int = 10) -> None:
        """初期化"""
        self.cashe = {}
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
        self.cashe[key] = value

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
        if key in self.cashe:
            return self.cashe[key]
        return None
