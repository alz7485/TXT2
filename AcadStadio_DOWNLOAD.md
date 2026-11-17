# AcadStadio 1.72.6-beta111

[最新ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.6_SpaceViewTrial111.zip)

モデルと各レイアウトで視点を個別に保持。レイアウト作成後にモデルへ戻ったときの表示ずれを修正しました。空レイアウトで変更したズーム・表示位置も保持します。

コア525件、実Tk 8.6/Xorgの関連GUI14件、スモーク成功。モデル・空レイアウトを3往復して図面座標の画面位置が復元されることを確認。Windows/AutoCAD実機・SCR実行・EXEビルドは未実施。

以前のSELECT簡素化、100件超対応、点参照入力フロー、ドロップ対策、Qtビルド設定も含みます。Pythonソース版。解凍してrequirements.txtをインストールし、python src/main.pyで起動。

SHA256: 5ba27c6e97001a41ad8f66e668243192e428432668cfdeddea2db5d1730f950f
