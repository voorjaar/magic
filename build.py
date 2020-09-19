import os
import json
import shutil
import base64

with open('url_schemes.json') as f:
    data = json.load(f)

icons = shutil.make_archive('icons', 'zip', './icons')

with open(icons, 'rb') as f:
    encoded = base64.b64encode(f.read()).decode('utf-8')

if not os.path.isdir('dist'): os.mkdir('dist')

with open('dist/magic.json', 'w', encoding='utf-8') as f:
    json.dump({
        'data': data,
        'icons': encoded
    }, f, ensure_ascii=False)

os.remove(icons)