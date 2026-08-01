import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('File size (chars):', len(content))

# Find body end and look at the last 3000 chars (where scripts usually are)
body_end = content.rfind('</body>')
print('\nLAST 3000 CHARS BEFORE </body>:')
print(content[max(0,body_end-3000):body_end])
