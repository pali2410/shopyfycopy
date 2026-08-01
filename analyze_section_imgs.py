import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sidekick_idx = content.find('id="sidekick"')
section_text = content[sidekick_idx:sidekick_idx+5000]
imgs = re.findall(r'src="(https://cdn\.shopify\.com[^"]+)"', section_text)
print('CDN images in sidekick section:')
for img in imgs[:5]:
    print(' ', img[:150])

# animate-show-media
anim_idx = content.find('animate-show-media')
print('\nanimate-show-media at:', anim_idx)
print('Context:', content[max(0,anim_idx-50):anim_idx+200])

# Look for global-lg:hidden elements - these are mobile-specific content
mobile_els = content.count('global-lg:hidden')
desktop_els = content.count('hidden global-lg:block')
print(f'\nglobal-lg:hidden count (mobile-only elements): {mobile_els}')
print(f'hidden global-lg:block count (desktop-only elements): {desktop_els}')
