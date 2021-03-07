# -*- coding: utf-8 -*-
import eel
import sys
import socket
@eel.expose
def jsFunc(values):
    return()
# 定数
ENTRY_POINT = 'index.html'
CHROME_ARGS = [
    '--incognit',  # シークレットモード
    '--disable-http-cache',  # キャッシュ無効
    '--disable-plugins',  # プラグイン無効
    '--disable-extensions',  # 拡張機能無効
    '--disable-dev-tools',  # デベロッパーツールを無効にする
]
ALLOW_EXTENSIONS = ['.html', '.css', '.js', '.ico']



def start():  # 画面生成
    eel.init('web')
    eel.start('index.html',size=(500,500))
start()
def exit():  # 終了時の処理
    sys.exit(0)
exit()