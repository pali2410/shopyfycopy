import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('scripts/(_locale).editions.winter2026-BOe91MRy.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all imports
imports = re.findall(r'import[^"\']*["\']([^"\']+)["\']', content)
print('IMPORTS IN BOe91MRy.js:')
for i in imports:
    print(' ', i)
