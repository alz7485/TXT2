# AcadStadio 1.72.7-beta112

[最新ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.7_LayoutFlowTrial112.zip)

レイアウト作成をプレビュータブの「＋」へ統一。LAYOUTの新規追加を外し、モデルブロックではVIEWPORTの追加を無効にしました。空のレイアウトフォルダもSCRで作成します。旧保存データのLAYOUTは互換保持します。

システム変数はSYSVARS／SYSVARの共通設定。レイアウトごとの専用変数UI・用紙／印刷設定UIは未実装です。詳細は同梱docs/LAYOUT_COMMANDS.md。

コア528件・実Tk 8.6/Xorgの関連GUI18件・スモーク成功。Windows/AutoCAD実機・SCR実行・EXEビルドは未実施。

モデルとレイアウトの独立視点、SELECT簡素化、100件超対応、点参照入力フロー、ドロップ対策、Qtビルド設定も含みます。Pythonソース版。解凍してrequirements.txtをインストールし、python src/main.pyで起動。

SHA256: bfcc88bcdf4c58d9ed55a5f13bc0d2446fe9d7ad96b523d8c463ac12cea625ab
