# :shopping_cart: 全自動カロガチャ機 :sunglasses:
エピックセブンのカロガチャを自動で行い、聖約の栞と神秘メダルを購入するためのスクリプトです。  
カロガチャするのが大変だったので自分用に作りました。

オリジナルを[EmaOlay](https://github.com/EmaOlay/E7-Auto-Shop-Refresh)氏が作成し、
[Daniel-Fox-msu](https://github.com/Daniel-Fox-msu/E7_shop_refresher)氏がフォークしたスクリプトへ手を加えています。

## コピペ元からの主な変更点
- 日本語表示へ変更
- 85装備の検出を追加
- ロジックの調整

## 注意点
- 本スクリプトのご利用は自己責任でお願いします。  

- BlueStacksでの動作を想定しています。他エミュレーターでも動作するとは思いますが未検証です。

- 作者が普段遊んでいるウィンドウサイズに合わせた画像ファイルを用意しています。  
上手く動作しない場合はimagesフォルダへ新たに画像ファイルを用意してください。

- ウィンドウサイズに応じてスクリプト内のbutton_offset_xの値の調整が必要になります。

- BlueStacksを最前面に表示する必要があります。（バックグラウンドで動作させることはできないため、他のウィンドウに隠れていた場合は動作しません。）

- マルチディスプレイ環境に対応していません。プライマリーディスプレイでのみ動作します。（対処方法は後述）

- おまかせ周回中に実行するのはオススメしません。ラグ発生による検出漏れが発生するためです。

## 実行するまでの流れ
1. Python3.10.11をインストールしてください。  
Windows環境なら[こちら](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

2. requirements.txtに記載されているライブラリをインストールします。  
`pip install -r requirements.txt`

3. シークレットショップの画面を開き、autogarogacha.pyを実行してください。

## マルチディスプレイ環境への対応
`multi-display\__init__.py`  
このファイルを下記パスへコピペして上書きしてください。  
`C:\Users\{ユーザー名}\AppData\Local\Programs\Python\Python310\Lib\site-packages\pyscreeze\__init__.py`

もしフォルダが見当たらない場合には下記ファイルを実行すると表示されます。  
`tool\getsitepackages.py`
