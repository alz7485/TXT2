# Trial108との統合

## 比較した版

- 添付：AcadStadio_v1.72.3_PointAxisFlowTrial108.zip
- こちらの直前版：AcadStadio_v1.72.2_SafeExclude.zip
- 共通の元：Trial107（整理版ZIP内の原本ソースと比較）

## 添付から取り込んだ変更

- macro_editor.pyの2か所：点参照確定後のaxis状態を引き継ぐ。Xの後はY、それ以外は次点XYへ。
- theme.pyのAPP_VERSION：1.72.3-beta108。
- test_gui_point_continuation.py：3頂点のXY連続入力など。
- test_gui_inline_point_reference.py：ボタン・Enter・テンキーEnter・右クリックから次点XYへ進む検証。

Trial108はSELECT新機能を含まないため、全ファイルの上書きはせず、共通版との差分を取り込みました。

## 維持したこちら側の変更

SELECTの＋／−・安全な点参照除外・外接範囲参照・作成制限・削除時処理、DXF／DWGドロップ対策、Qtビルド競合対策。対象のソースとspecは直前版とのバイト一致を確認しました。

## 統合時に追加した修正・検証

- block_browser.py：Treeviewのindentが15pなど単位付きでも、winfo_pixelsでピクセルへ変換。実Tkの起動テストで発見。
- test_gui_safe_exclusion.py：実エディタで除外を点参照化→最大最小XY変換→確定→コンパイルまで検証。
- 過去資料の再膨張を防ぐため、添付の長いREADME・ログ履歴は再取り込みせず、この資料へ統合点を集約。

詳細な結果はVALIDATION.md。Windows実機での確認は別途必要です。
