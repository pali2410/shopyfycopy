import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Checking index.html for mobile responsiveness...')

# Check Viewport meta tag
viewport = re.findall(r'<meta[^>]*viewport[^>]*>', content, re.IGNORECASE)
print('Viewport meta tags:', viewport)

# Check mobile menu buttons
mobile_menu = re.findall(r'aria-controls=["\']mobile-menu["\']', content)
print('Mobile menu references:', len(mobile_menu))

# Check for media queries in injected custom script
print('Injected custom script length:', len(content))
