# AcadStadio 1.74.0-beta114

[最新ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.74.0_ViewportPreviewTrial114.zip)

レイアウトの矩形ビューポート内に、指定した表示中心・尺度でモデルの2D図形を表示します。線・円・円弧・ポリライン・文字・ハッチング・寸法などを枠内にクリップし、複数ビューポートの全体図と詳細図も表示できます。表示専用なのでCAD図形やSCRへモデルのコピーは混入しません。

新規VIEWPORTは作成画面で表示中心X/Yと尺度を指定します。サンプルはexamples/viewport_projection_project.json、手順・制約はdocs/VIEWPORT_PREVIEW.md。

コア547件・実Tk/Xorgの関連GUI14件・スモーク成功。Windows/AutoCAD実機での見た目照合・SCR実行・EXEビルドは未確認。3D、傾いた視線、ねじれ、非矩形クリップは対象外です。番号対応が不明な別コマンドでの範囲変更は、推測せず枠のみ表示へ切り替えます。

以前の円弧対応ポリライン編集、SELECT、独立視点、レイアウト作成フロー、点参照、ドロップ／ビルド対策も含みます。Pythonソース版。解凍後requirements.txtをインストールし、python src/main.pyで起動。

SHA256: 66c1085a2c6ba4d4a4003d1085ae7a7a5d96cc0baf7c0162871953066b655607
