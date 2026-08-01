import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# Verify index.html has original imports back
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '(_locale).editions.winter2026-BOe91MRy.js' in content:
    print('GOOD: Original parenthesized filename is RESTORED in index.html')
elif 'locale-editions-winter2026-BOe91MRy.js' in content:
    print('BAD: Renamed file still in index.html - needs manual fix')
else:
    print('UNKNOWN: cannot find import in index.html')

# Confirm the import line
import re
mod_idx = content.find('(_locale).editions.winter2026')
print('Import context:', content[max(0,mod_idx-30):mod_idx+80])
