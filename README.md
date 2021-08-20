# LRU Cache

本リポジトリは TDD のお題である「LRU Cache」の Python 実装になります。

## 参考

- https://www.slideshare.net/t_wada/tddbc-exercise
- https://image.slidesharecdn.com/tddbcexercise-110919222207-phpapp01/95/tddbc-5-728.jpg?cb=1316471500

## 環境詳細

- Python : 3.9.6

### 事前準備

- Docker インストール
- VS Code インストール
- VS Code の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone

### 開発手順

1. VS Code 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナー image の取得や作成が行われる
5. 起動したら開発可能

## ユニットテスト実行

```
pytest
```
