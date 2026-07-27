import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
print('Total href attributes in index.html:', len(hrefs))

external_shopify = [h for h in hrefs if 'shopify.com' in h]
print('External shopify.com hrefs found:', len(external_shopify))

for h in set(external_shopify):
    print('  -', h)
