# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\converter.py'],
             pathex=['C:\\Users\\Thomasb.000\\Documents\\Converter'],
             binaries=None,
             datas=[('icns\\icon.ico', 'icon')],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='1100SeriesConverter',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icns\\icon.ico')
