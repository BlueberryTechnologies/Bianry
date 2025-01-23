# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/media/joystick/TwoDrive/System Folders/Programming/Bianry/Bianry.py'],
    pathex=[],
    binaries=[],
    datas=[('/media/joystick/TwoDrive/System Folders/Programming/Bianry/lib/python3.12/site-packages/customtkinter', 'customtkinter/')],
    hiddenimports=['pyperclip'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [('v', None, 'OPTION')],
    exclude_binaries=True,
    name='BianryPackage',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BianryPackage',
)
