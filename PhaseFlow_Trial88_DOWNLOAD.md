# PhaseFlow Trial88 ダウンロード

[PhaseFlow Trial88 ソース版ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/PhaseFlow_Trial88_onedir_source.zip)

- ファイル名：`PhaseFlow_Trial88_onedir_source.zip`
- サイズ：6,900,747 バイト
- [SHA-256確認用ファイル](downloads/PhaseFlow_Trial88_onedir_source.zip.sha256)

## 主な変更

- 項目編集を「項目プリセット」「項目マスタ」のタブに整理。
- プリセットの検索・内容プレビュー、マスタの検索・種別絞り込み・複製を追加。
- 単位時間を役割ごとの数値入力に変更。色・期間の表示プレビューを追加。
- Trial86の保存復旧・読込エラー表示、Trial87のボタンアイコンと配置改善を継承。

## 使い方

1. ZIPをダウンロードし、展開します。
2. Windowsで `PhaseFlow_Trial88/build_onedir.bat` を実行すると、`dist/PhaseFlow/PhaseFlow.exe` を作成できます（Pythonが必要です）。
3. 配布時は `dist/PhaseFlow` フォルダ全体を配布してください。
4. 既存データは従来どおりEXE隣の `data` フォルダで使用します。

このZIPはソース版です。Windows用EXEは含まれていません。画面例はZIP内の `previews`、変更内容は `Trial88_変更内容.txt` を参照してください。

Linuxのモデル・GUIテスト96件が成功。新UIの配置チェックは表示倍率150％・200％でも成功しました。Windows実機・SMB上での動作確認は未実施です。

SHA-256: `f25ec7f8b4b980d622d6eae2a5f69f1b598bdf992b5cf36637f13789a75ccd6f`
