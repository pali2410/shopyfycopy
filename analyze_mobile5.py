import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the inline module script content at position 1065941
mod_pos = 1065941
tag_end = content.find('>', mod_pos)
script_start = tag_end + 1
script_end = content.find('</script>', script_start)
print('MODULE SCRIPT CONTENT:')
print(content[script_start:script_start+3000])

# Find all data-autoplay animations
anim = re.findall(r'autoplay["\']?[^>]*>', content[:1070000])
print('\nAUTOPLAY REFS:', len(anim))

# find animation name references that could fail on mobile
anim2 = re.findall(r'animation["\'][^"\']+["\']', content[:1070000])
print('\nANIMATION REFS (first 10):')
for a in anim2[:10]:
    print(a)
