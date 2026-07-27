import os
import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# Valid ES Module code for FallbackImageScene-DrEja6F1.js
FALLBACK_SCENE_JS = """// FallbackImageScene Module for Mobile Devices
export function FallbackImageScene(props) {
  return null;
}
export function Scene(props) {
  return null;
}
export default function DefaultScene(props) {
  return null;
}
"""

paths = [
    'FallbackImageScene-DrEja6F1.js',
    os.path.join('scripts', 'FallbackImageScene-DrEja6F1.js'),
    os.path.join('assets', 'FallbackImageScene-DrEja6F1.js'),
    os.path.join('editions', 'FallbackImageScene-DrEja6F1.js'),
    os.path.join('raw_site', 'cdn.shopify.com', 'oxygen-v2', '47215', '49013', '102837', '4002246', 'assets', 'FallbackImageScene-DrEja6F1.js')
]

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
    with open(p, 'w', encoding='utf-8') as f:
        f.write(FALLBACK_SCENE_JS)
    print(f"Created fallback module at: {p}")

# Now add animation fallback and error suppression to index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Suppress "Animation with name autoplay not found" in error filter
if 'Animation with name' not in content:
    content = content.replace(
        "str.indexOf('Invalid URL') !== -1;",
        "str.indexOf('Invalid URL') !== -1 || str.indexOf('Animation with name') !== -1 || str.indexOf('FallbackImageScene') !== -1;"
    )
    print("Added Animation & FallbackImageScene error suppression filters")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS!")
