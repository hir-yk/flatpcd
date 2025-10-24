# 📦 flatpcd: createflatfield.py

このリポジトリは、2D平面上に均一な点群データ（PCDファイル）を生成する Python スクリプト `createflatfield.py` を提供します。点群処理やセンサシミュレーション、ロボットのマッピングテストなどに活用できます。

## 🧭 概要

`createflatfield.py` は、指定された範囲と間隔に基づいて、平面上に点群を生成し `.pcd` ファイルとして保存します。生成される点群は、Z軸がすべて0のフラットなフィールドで、各点には固定の強度値（intensity）が付与されます。

## 🚀 使い方

### 実行コマンド

```bash
python createflatfield.py --origin_x 0 --origin_y 0 --range_x 100 --range_y 100 --interval 1
```

### 引数一覧

| 引数         | 型    | デフォルト | 説明 |
|--------------|--------|------------|------|
| `--origin_x` | int    | 0          | 原点のX座標（メートル） |
| `--origin_y` | int    | 0          | 原点のY座標（メートル） |
| `--range_x`  | int    | 100        | X方向の範囲（メートル） |
| `--range_y`  | int    | 100        | Y方向の範囲（メートル） |
| `--interval` | float  | 1.0        | 点間の間隔（メートル） |

## 📄 出力ファイル

- `testfile.pcd`: PCD v0.7 形式の点群ファイル
- 各点のフォーマット: `x y z intensity`
  - `x`, `y`: メートル単位の座標
  - `z`: 常に `0`
  - `intensity`: 固定値 `20`

## 🛠️ 必要なライブラリ

- Python 3.x
- NumPy

```bash
pip install numpy
```

## 📌 注意点

- 座標は内部的にミリメートル単位で処理され、出力時にメートルに変換されます。
- 出力ファイル名は固定で `testfile.pcd` です。変更したい場合はスクリプトを編集してください。

## 📚 ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。
