# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/marlo/OneDrive/Desktop/backup/python/piga/pirga.py'],
    pathex=['C:/Users/marlo/OneDrive/Desktop/backup/python/piga/defendefofo/Lib/site-packages'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CuteDefender',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\marlo\\Downloads\\logo.ico'],
    contents_directory='assets_py',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CuteDefender',
)
