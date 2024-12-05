# BTC/JPY Price Fetcher

BitFlyerからBTC/JPYの価格データを取得し、CSVファイルとして保存するPythonスクリプトです。

## 機能

- BitFlyerからBTC/JPYの日次価格データを取得
- 指定した期間（デフォルト：90日）のデータを取得可能
- データをCSVファイルとして保存
- 基本的な統計情報の表示

## 必要なライブラリ

- ccxt: 暗号資産取引所のAPIを扱うためのライブラリ
- pandas: データ処理用ライブラリ

## インストール方法

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python btc_price_fetcher.py
```

## 出力データ

以下の情報を含むCSVファイルが生成されます：

- timestamp: 日時
- open: 始値
- high: 高値
- low: 安値
- close: 終値
- volume: 取引量

## 注意事項

- API制限に注意してください
- インターネット接続が必要です
- 取得したデータは参考値として扱ってください