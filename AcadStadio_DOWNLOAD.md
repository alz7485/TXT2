# AcadStadio 最新改良版

[ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.2_SelectSubtract.zip)

プレビューで＋選択／−除外してから「選択図形の最大・最小XYを点参照にする」を実行。最終選択の最小最大X/Yを表示し、各図形の外接範囲への点参照式で窓を作ります。元図形の移動や半径変更にも範囲が追従。除外条件は保存・SCR出力に反映します。

点クリックの除外位置は数値座標のため、図形移動後は除外位置も確認してください。囲む窓の内側の別図形は除外指定で調整します。

コア518件・スモーク成功。GUI実操作・Windows/AutoCAD実機は今回未確認。Pythonソース版。解凍後requirements.txtをインストールしてpython src/main.pyで起動。

前版のQtビルド修正・ドロップ対策・SELECTの作成制限と削除処理も含みます。

SHA256: 231c55883fcbe961d7ea562845d77fea34048161fd6364cbe6c429b796733a36
