# AcadStadio 1.72.4-beta109

[最新ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.4_SimpleSelectTrial109.zip)

SELECTをプレビューだけのシンプルな画面に整理しました。クリックで選択・解除、ドラッグで囲んで選択、Shift＋ドラッグで一括解除し、「選択を確定」で完了。座標・式・条件一覧・保存方式は表示せず、安全な点参照を内部で自動生成します。選択数、元に戻す、すべて解除を表示し、プレビューを全幅にしました。

囲みは各対象図形への参照として保存。旧版の範囲・除外条件も互換保持します。最大100条件、安全な参照点のない図形を確定しない制約は継続。

コア522件・実Tk 8.6/Xorgの関連GUI26件・スモーク成功。Windows/AutoCAD実機・SCR実行・EXEビルドは未実施。

前版の点参照入力フロー、SELECT作成・削除時の保護、ドロップ対策、Qtビルド設定も含みます。Pythonソース版。解凍してrequirements.txtをインストールし、python src/main.pyで起動。

SHA256: f139ddcd3a557c00d931f027188dbc374199807b27dbb985402c4d14fa2d482a
