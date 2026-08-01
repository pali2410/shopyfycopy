import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all script src attributes (module scripts)
mods = re.findall(r'<script[^>]+src=["\']([^"\']+)["\'][^>]*>', content)
print('MODULE SCRIPTS:')
for m in mods[:20]:
    print(m)

# Find body tag
body_idx = content.find('<body')
print('\nBODY TAG:', content[body_idx:body_idx+500])

# Find how React app mounts
app_div = content.find('id="root"')
if app_div < 0:
    app_div = content.find("id='root'")
print('\nROOT DIV:', content[app_div-20:app_div+200] if app_div > 0 else 'NOT FOUND')

# Find loading overlay / spinner
for kw in ['loading', 'spinner', 'splash', 'data-state', 'visibility:hidden', 'display:none']:
    idx = content.find(kw)
    if idx > 0:
        print(f'\n[{kw}] at {idx}:', content[max(0,idx-50):idx+200])
