# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/thegreatest/PyFolder/Khpi/PY_dev/kurs2sem2/lab6/gui.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/thegreatest/PyFolder/Khpi/PY_dev/kurs2sem2/lab6/Brackets_Icon.svg.png'],
)
app = BUNDLE(
    exe,
    name='gui.app',
    icon='/Users/thegreatest/PyFolder/Khpi/PY_dev/kurs2sem2/lab6/Brackets_Icon.svg.png',
    bundle_identifier=None,
)
