import os

print("Searching for FallbackImageScene-DrEja6F1.js on disk...")

for root, dirs, files in os.walk('.'):
    for f in files:
        if 'FallbackImageScene' in f:
            print("Found file:", os.path.join(root, f))
