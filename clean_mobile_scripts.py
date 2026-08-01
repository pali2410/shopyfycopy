import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove ALL previous mobile fix scripts injected by us
OLD_MARKERS = [
    '/* ============================================================\n   NUCLEAR MOBILE FIX',
    '/* ============================================================\n   MOBILE RIVE INFINITE LOOP BREAKER',
    '/* MOBILE RESCUE: Force page content visible if canvas hangs */',
]
for marker in OLD_MARKERS:
    idx = html.find(marker)
    while idx > 0:
        script_start = html.rfind('<script>', 0, idx)
        script_end = html.find('</script>', idx) + len('</script>')
        if script_start > 0 and script_end > len('</script>'):
            html = html[:script_start] + html[script_end:]
            print(f'Removed script at pos {script_start}')
            idx = html.find(marker)
        else:
            break

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Cleaned old scripts. File saved.')
print('Lines now:', len(html.splitlines()))
