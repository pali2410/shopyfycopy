import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the sidekick section content - what's inside it
sidekick_idx = content.find('id="sidekick"')
print('SIDEKICK SECTION (first 2000 chars):')
print(content[sidekick_idx:sidekick_idx+2000])
