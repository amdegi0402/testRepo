import ccxt
import pandas as pd
from datetime import datetime
import time

def fetch_btc_jpy_price(days=30):
    """
    BitFlyerからBTC/JPYの価格データを取得する関数
    
    Parameters:
    -----------
    days : int
        取得する日数（デフォルト: 30日）
    
    Returns:
    --------
    pandas.DataFrame
        取得した価格データをDataFrame形式で返す
    """
    # BitFlyer取引所のインスタンスを作成
    exchange = ccxt.bitflyer()
    
    # 現在のタイムスタンプを取得
    now = exchange.milliseconds()
    
    # データを格納するリスト
    ohlcv_data = []
    
    try:
        # 指定した日数分のデータを取得
        # BitFlyerは1日の時間足データを取得（'1d'）
        ohlcv = exchange.fetch_ohlcv(
            symbol='BTC/JPY',
            timeframe='1d',
            since=now - (days * 24 * 60 * 60 * 1000),  # 日数をミリ秒に変換
            limit=days
        )
        
        # データをリストに追加
        ohlcv_data.extend(ohlcv)
        
        # API制限を考慮して少し待機
        time.sleep(exchange.rateLimit / 1000)
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None
    
    # データをDataFrameに変換
    df = pd.DataFrame(
        ohlcv_data,
        columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
    )
    
    # タイムスタンプを読みやすい形式に変換
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    return df

def save_to_csv(df, filename='btc_jpy_prices.csv'):
    """
    取得したデータをCSVファイルとして保存する関数
    
    Parameters:
    -----------
    df : pandas.DataFrame
        保存するデータフレーム
    filename : str
        保存するファイル名（デフォルト: 'btc_jpy_prices.csv'）
    """
    if df is not None:
        df.to_csv(filename, index=False)
        print(f"データを {filename} に保存しました。")
    else:
        print("保存するデータがありません。")

def main():
    """
    メイン実行関数
    - BTCの価格データを取得
    - CSVファイルとして保存
    - 基本的な情報を表示
    """
    print("BTCの価格データを取得中...")
    
    # 90日分のデータを取得
    df = fetch_btc_jpy_price(days=90)
    
    if df is not None:
        # データを保存
        save_to_csv(df)
        
        # 基本的な統計情報を表示
        print("\n基本統計情報:")
        print(f"データ期間: {df['timestamp'].min()} から {df['timestamp'].max()}")
        print(f"平均価格: ¥{df['close'].mean():,.0f}")
        print(f"最高価格: ¥{df['high'].max():,.0f}")
        print(f"最低価格: ¥{df['low'].min():,.0f}")
        
        # 価格変動の計算
        price_change = ((df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0]) * 100
        print(f"\n期間中の価格変動: {price_change:.2f}%")
    
if __name__ == "__main__":
    main()