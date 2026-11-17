# AcadStadio 1.72.3-beta108 統合版

[最新ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.3_MergedTrial108.zip)

[統合内容の詳細](downloads/AcadStadio_MERGE_Trial108.md)

添付のPointAxisFlowTrial108から、点参照確定後のX→同じ点Y→次点XY、XY→次点XYのフロー修正を取り込みました。SELECTの＋／−選択、安全な点参照除外、最大最小XY点参照、作成制限・削除処理、ドロップ対策とQtビルド設定を保持。Treeviewの単位付きindentも標準変換で処理します。

コア522件、実Tk/Xorgの関連GUI37件、スモーク成功。全GUI一括・Windows/AutoCAD実機・SCR実行・EXEビルドは未実施。

Pythonソース版。解凍してrequirements.txtをインストールし、python src/main.pyで起動。Windows用ビルドは同梱EXE_BUILD_ONEDIR.mdを参照してください。

SHA256: 2dc185dfe1da6c652eb2bf0fefc1589f4e811c7b37a45ce33b95720de7dcfe29
