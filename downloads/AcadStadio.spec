# Optional Windows build: pyinstaller --clean --noconfirm AcadStadio.spec
# Build on Windows; cross-compilation from Linux is not supported.
from pathlib import Path
base=Path(SPECPATH)
# This is a Tkinter application. Optional DXF/rendering dependencies can pull
# Qt hooks from a shared build environment; never bundle Qt into this app.
QT_EXCLUDES = ['PyQt5', 'PyQt6', 'PySide2', 'PySide6', 'shiboken2', 'shiboken6']
a=Analysis([str(base/'AcadStadio.pyw')],pathex=[str(base/'src')],
           binaries=[],datas=[(str(base/'assets'),'assets'),(str(base/'docs'),'docs'),(str(base/'examples'),'examples')],
           hiddenimports=['openpyxl','ezdxf','ezdxf.addons','ezdxf.math'],hookspath=[],hooksconfig={},runtime_hooks=[],excludes=QT_EXCLUDES,noarchive=False)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,[],exclude_binaries=True,name='AcadStadio',debug=False,
        bootloader_ignore_signals=False,strip=False,upx=False,console=False,
        icon=str(base/'assets'/'acadstadio.ico'))
coll=COLLECT(exe,a.binaries,a.datas,strip=False,upx=False,name='AcadStadio')
