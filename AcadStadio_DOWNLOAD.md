# AcadStadio 1.73.0-beta113

[最新ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.73.0_PolylineEditTrial113.zip)

SELECTの後へ「PEDIT · ポリライン編集」を追加できます。ポリライン化／結合／閉じる／結合して閉じるを選択。線分と円弧の混在を曲率を保持して1本にまとめ、プレビューとSCRへ反映します。曲線の中点、後続のコピー・分解にも対応。サンプルはexamples/polyline_edit_arc_project.json、手順と制約はdocs/POLYLINE_EDIT.md。

未接続・分岐・異なる属性・3D形状・連続線の部分選択などは自動で処理せず拒否します。結合許容差による微小な調整はプレビューとCADで差が出る場合があります。

コア539件・実Tk/Xorgの関連GUI13件・スモーク成功。Windows/AutoCAD実機、実PEDIT操作、UNDOロールバック、EXEビルドは未確認です。

以前のSELECT簡素化と100件超対応、モデル／レイアウト視点、レイアウト作成フロー、点参照入力、ドロップ／ビルド対策も含みます。Pythonソース版。解凍後requirements.txtをインストールし、python src/main.pyで起動。

SHA256: 2a47431cbef9f9c6dd880cdd220ae94a646913952dd3b361d6a38126dac19ed5
