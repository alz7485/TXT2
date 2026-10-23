from pathlib import Path
import hashlib

folder = Path(__file__).resolve().parent
name = "Yohaku_v0.9.0_transfer"
parts = sorted(folder.glob(name + ".part*"))
if not parts:
    raise SystemExit("分割ファイルが見つかりません。")
output = folder / (name + ".txt")
with output.open("wb") as dst:
    for part in parts:
        dst.write(part.read_bytes())
print("復元完了:", output.name)
print("SHA256:", hashlib.sha256(output.read_bytes()).hexdigest())
