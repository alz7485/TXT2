# AcadStadio 最新修正版

[ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.2_DropFix.zip)

WindowsのDXF/DWGドロップ直後のクラッシュ対策：ネイティブ受信時はファイル名のみ取得し、Tkタイマー経由で読み込み。受信コールバックの保持・画面終了時の後始末を補強しました。

コア513件・スモーク成功。Windows実機でのドロップ・クラッシュ解消は未確認。

Pythonソース版。解凍後requirements.txtをインストールし、python src/main.pyで起動。

SELECT改良も含みます。

SHA256: c5b326097ad75272f4041e2382b418ba079dc5d241803479ac5d3ff8315ea02b
