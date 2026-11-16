# AcadStadio 最新修正版

[ZIPをダウンロード](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio_v1.72.2_BuildFix.zip)

[ビルド設定のみ](https://github.com/alz7485/TXT2/raw/refs/heads/main/downloads/AcadStadio.spec)

PyInstallerでPySide6/PyQt5が競合するエラーに対応。Tkinterアプリに不要なQtバインディング6種をspecで除外。共有環境のQtを削除する必要はありません。

置換後 python -m PyInstaller --clean --noconfirm AcadStadio.spec で再ビルド。

spec構文・除外指定・同梱データパスを検証。WindowsでのEXEビルドは未確認。前版のドロップ対策・SELECT改良も含みます。

SHA256: 1e079c8dd9d132fec5eede0ffb951073a096459e6a93e284999ba45123a621c6
