"""
Last Recently Used Cashe
"""
from typing import Any


class LastRecentlyUsedCashe:
    """
    Last Recently Used Cashe
    """

    def __init__(self) -> None:
        """初期化"""
        self.cashe = {}

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
        return self.cashe[key]
