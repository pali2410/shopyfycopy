import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the canvas elements inside sections and understand their structure
canvas_els = re.findall(r'<canvas[^>]+>', content)
print(f'CANVAS ELEMENTS ({len(canvas_els)} total):')
for c in canvas_els[:8]:
    print(' ', c[:200])
print()

# Check what classes the canvas has - specifically for opacity-0
# The canvas starts at opacity-0 and transitions to visible when WebGL loads
# On mobile WebGL should work but Rive fails

# Find the 3D scene fallback - what happens when WebGL fails?
# FallbackImageScene component
fallback_idx = content.find('FallbackImageScene')
print('FallbackImageScene at:', fallback_idx)
if fallback_idx > 0:
    print('Context:', content[max(0,fallback_idx-100):fallback_idx+300])

# Check the canvas inside each section - what class does it have initially?
# Look for the first few canvases in sections
section_canvas = re.findall(r'<section[^>]*id="(\w+)"[^>]*>.*?<canvas([^>]*)>', content, re.DOTALL)
print('\nSECTION CANVAS CLASSES:')
for sid, cls in section_canvas[:5]:
    print(f'  Section {sid}: canvas class{cls[:100]}')
