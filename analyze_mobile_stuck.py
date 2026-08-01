import sys
import re

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for WebGL / loading-related clues
idx = content.find('WebGLRenderer')
print("WebGLRenderer found at:", idx)

idx2 = content.find('loading')
print("loading found at:", idx2)

# Find canvas or 3D init references
idx3 = content.find('devicePixelRatio')
print("devicePixelRatio found at:", idx3)

# Check for mobile detection
idx4 = content.find('navigator.userAgent')
print("navigator.userAgent found at:", idx4)

# Check how the root div & loading spinner are set up
root_idx = content.find('<div id="root"')
print("Root div at:", root_idx)
print("Root div context:", repr(content[root_idx:root_idx+300]))

# Check for any loading screen divs
loading_idx = content.find('opacity-0')
print("opacity-0 at:", loading_idx)
print("opacity-0 context:", repr(content[max(0,loading_idx-100):loading_idx+200]))
