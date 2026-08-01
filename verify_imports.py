import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# Find BOTH import lines in the module script section of index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Find the module script
mod_pos = content.find('type="module"')
if mod_pos < 0:
    mod_pos = content.find("type='module'")
    
tag_end = content.find('>', mod_pos)
script_start = tag_end + 1
script_end = content.find('</script>', script_start)
module_script = content[script_start:script_end]
print('FULL MODULE SCRIPT:')
print(module_script[:1500])
