import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find script type=module
mod_scripts = [(m.start(), m.group()) for m in re.finditer(r'<script[^>]+type=["\']module["\'][^>]*>', content)]
print('MODULE SCRIPT TAGS:')
for pos, tag in mod_scripts[:10]:
    print(f'  [{pos}] {tag}')
    # Also show src
    src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
    if src_m:
        print(f'    SRC: {src_m.group(1)}')

# Find all script tags in first 2000 chars after <head>
head_idx = content.find('<head')
print('\nFIRST 2000 CHARS OF HEAD:')
print(content[head_idx:head_idx+2000])

# Find canvas element
canvas_idx = content.find('<canvas')
print('\nCANVAS AT:', canvas_idx)
if canvas_idx > 0:
    print(content[canvas_idx:canvas_idx+300])
