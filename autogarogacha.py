from time import sleep as wait
import os
import keyboard
import pyautogui


#######################################
# 環境設定
#######################################
# 購入対象アイテム
buy_covenants = True
buy_mystics = True
buy_85_red_gear = True
buy_85_purple_gear = True

# 「購入」ボタンのオフセット設定
# アイテムアイコンの右側にあるボタンをクリックするためX座標とY座標のオフセットを調整する必要あり
# 例）1920x1080の場合はbutton_offset_xを800にする
button_offset_x = 500 # 値を高くするほど右方向の位置指定となる
button_offset_y = 20 # 値を高くするほど下方向の位置指定となる

# アイテム価格
price_c = 184000
price_m = 280000

# 画像フォルダーのパス
images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
print(os.path.join(images_folder, "shop.png"))


#######################################
# メイン処理
#######################################
# フェイルセーフをONにする。画面左上にマウスを移動させると停止する
pyautogui.FAILSAFE = True

# 開始ディレイ
start_timer = 3

# カウント用の変数
c = 0
m = 0
r = 0
p = 0
g = 0
total = 0

# フラグ
scrolled = False
bought_c = False
bought_m = False
found_r = False
found_p = False

numRefreshes = input("シークレットショップを更新する回数を数字で指定してください (0 を入力すると停止操作されるまで実行され続けます)")
if numRefreshes.isdecimal():
    numRefreshes = int(numRefreshes)
else:
    print('入力エラーです！正の整数を入力してください')
    exit()

if buy_85_red_gear:
    ans_red = str(input("85エピック装備が見つかったら一時停止しますか？ (y/n)"))
    if ans_red.lower().startswith('y'):
        buy_85_red_gear = True
    else:
        buy_85_red_gear = False

if buy_85_purple_gear:
    ans_purple = str(input("85レジェンド装備が見つかったら一時停止しますか？ (y/n)"))
    if ans_purple.lower().startswith('y'):
        buy_85_purple_gear = True
    else:
        buy_85_purple_gear = False

print(f"{start_timer}秒後に開始します。")
print("停止する時はQ キーを押し続けてください...")
print("中断する時はS キーを押し続けてください...")
wait(start_timer)

# シークレットショップ
in_shop = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "shop.png"), confidence=.80)

if in_shop:

    # 更新ボタンの検出
    refresh_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "refresh_button.png"), confidence=.90)

    # スクロールエリアの取得
    scroll_area_x, scroll_area_y = refresh_button
    scroll_area_x += 200

    # 「Q」キーを押し続けると停止するようにしておく
    while not keyboard.is_pressed('q') and (buy_covenants or buy_mystics or buy_85_red_gear or buy_85_purple_gear):

        # 「S」キーを押し続けると中断するようにしておく
        if keyboard.is_pressed('s'):
            input("中断しました。再開するにはEnterキーを押してください")

        # 聖約の栞
        if buy_covenants:
            covenant = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "covenant_icon.png"), confidence=.90, grayscale=True)

            if covenant and not bought_c:
                # 当該アイテムの右側にある「購入」ボタンを押下する
                covenant_buy_button_x, covenant_buy_button_y = covenant
                pyautogui.click(int(covenant_buy_button_x) + button_offset_x, int(covenant_buy_button_y) + button_offset_y, button='left', clicks=2, interval=0.5)

                wait(0.5)

                # 確認用のボタンを検出する
                covenant_confirm_buy_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "covenant_buy_button.png"), confidence=.80, grayscale=True)

                # 確認用のボタンを検出できなかったら何回かリトライする
                retries = 0
                while covenant_confirm_buy_button is None and retries < 3:
                    pyautogui.click(int(covenant_buy_button_x) + button_offset_x, int(covenant_buy_button_y) + button_offset_y, button='left', clicks=2, interval=0.5)
                    wait(1)
                    covenant_confirm_buy_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "covenant_buy_button.png"), confidence=.80)
                    retries += 1

                # ラグなどの何らかの理由で確認用のボタンを押下できなかったらループ処理を最初からやり直す
                # こうすることで購入できなかった神秘メダルを再度検出して購入をリトライできる
                if covenant_confirm_buy_button is None:
                    continue

                # 確認用のボタンを押下する
                pyautogui.click(covenant_confirm_buy_button, button='left', clicks=2, interval=0.5)

                # アニメーションが終わるのを待つ
                wait(3)

                # フラグ処理
                bought_c = True

                # カウント処理
                c += 1
                g += price_c

        # 神秘メダルの購入処理
        if buy_mystics:
            mystic = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "mystic_icon.png"), confidence=.90, grayscale=True)

            if mystic and not bought_m:
                # 当該アイテムの右側にある「購入」ボタンを押下する
                mystic_buy_button_x, mystic_buy_button_y = mystic
                pyautogui.click(int(mystic_buy_button_x) + button_offset_x, int(mystic_buy_button_y) + button_offset_y, button='left', clicks=2, interval=0.5)

                wait(0.5)

                # 確認用のボタンを検出する
                mystic_confirm_buy_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "mystic_buy_button.png"), confidence=.80, grayscale=True)

                # 確認用のボタンを検出できなかったら何回かリトライする
                retries = 0
                while mystic_confirm_buy_button is None and retries < 3:
                    pyautogui.click(int(mystic_buy_button_x) + button_offset_x, int(mystic_buy_button_y) + button_offset_y, button='left', clicks=2, interval=0.5)
                    wait(1)
                    retries += 1
                    mystic_confirm_buy_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "mystic_buy_button.png"), confidence=.80)

                # ラグなどの何らかの理由で確認用のボタンを押下できなかったらループ処理を最初からやり直す
                # こうすることで購入できなかった神秘メダルを再度検出して購入をリトライできる
                if mystic_confirm_buy_button is None:
                    continue

                # 確認用のボタンを押下する
                pyautogui.click(mystic_confirm_buy_button, button='left', clicks=2, interval=0.5)

                # アニメーションが終わるのを待つ
                wait(3)

                # フラグ処理
                bought_m = True

                # カウント処理
                m += 1
                g += price_m

        # 85赤装備
        if buy_85_red_gear and not found_r:
            red = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "85_red_gear.png"), confidence=.92)

            if red:
                pyautogui.moveTo(red)
                input("85赤装備が見つかりましたので確認してください。続行するにはEnterキーを押下してください...")

                # フラグ処理
                found_r = True

                # カウント処理
                r += 1

        # 85紫装備
        if buy_85_purple_gear and not found_p:
            purple = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "85_purple_gear.png"), confidence=.87)

            if purple:
                pyautogui.moveTo(purple)
                input("85紫装備が見つかりましたので確認してください。続行するにはEnterキーを押下してください...")

                # フラグ処理
                found_p = True

                # カウント処理
                p += 1

        # スクロール処理
        if not scrolled:
            # スクロールダウン
            # pyautogui.click(scroll_area_x, scroll_area_y)
            # pyautogui.scroll(-10)

            # アニメーションが終わるのを待つ
            # wait(1)

            # マウススクロールよりもマウスドラッグで動かした方が早い。スクロールしすぎるとアニメーションを待機する必要が発生するため
            pyautogui.moveTo(scroll_area_x, scroll_area_y)
            pyautogui.drag(0, -250, 0.2, button='left')

            # フラグを設定
            scrolled = True

            # スクロールしたらループの先頭に戻ってアイテム検出を再度行う
            continue

        # 現在までの統計表示
        # print(f"ショップを更新します\n購入した聖約の栞: {c * 5}\n購入した神秘メダル: {m * 50}\n発見した85赤装備: {r}\n発見した85紫装備: {p}\n消費した天空石: {total * 3}")

        # 指定回数に達した際の終了判定
        if (not numRefreshes == 0) and (total >= numRefreshes):
            break

        # 「更新」ボタンを押下
        # pyautogui.click(refresh_button, button='left')
        pyautogui.click(refresh_button, button='left', clicks=2, interval=0.5)
        wait(0.5)

        # 確認用ボタンの検出
        refresh_button_confirm = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "confirm_button.png"), confidence=.90, grayscale=True)

        # 確認用のボタンを検出できなかったら何回かリトライする
        retries = 0
        while refresh_button_confirm is None and retries < 3:
            pyautogui.click(refresh_button, button='left', clicks=2, interval=0.5)
            wait(1)
            refresh_button_confirm = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "confirm_button.png"), confidence=.90)
            retries += 1

        # ラグなどの何らかの理由で確認用のボタンを押下できなかったらループ処理を最初からやり直す
        # こうすることで購入できなかった神秘メダルを再度検出して購入をリトライできる
        if refresh_button_confirm is None:
            continue

        # 確認用のボタンを押下する
        pyautogui.click(refresh_button_confirm, button='left', clicks=2, interval=0.5)

        # フラグをリセット
        scrolled = False
        bought_m = False
        bought_c = False
        found_r = False
        found_p = False

        # カウント処理
        total += 1

        # アニメーションが終わるのを待つ
        wait(1.5)

# シークレットショップが開かれていない場合
else:
    print("シークレットショップの画面が開かれていませんので終了します")

# 購入したアイテムが1件でもあるなら統計を表示
if c > 0 or m > 0 or r > 0 or p > 0 or total > 0:
    print(f"\n購入した聖約の栞: {c * 5}\n"
        f"購入した神秘メダル: {m * 50}\n"
        f"消費したゴールド: {g:,}\n"
        f"消費した天空石: {total * 3}\n"
        f"発見した85赤装備: {r}\n"
        f"発見した85紫装備: {p}\n"
    )
else:
    print("なんの成果も!!得られませんでした!!")

print("正常終了しました")
