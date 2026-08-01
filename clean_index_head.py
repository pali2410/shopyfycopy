import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove all the broken injected scripts and broken svg tags at the start of <head>
# Find starting point: <!DOCTYPE html><html lang="en" class=""><head>
start_tag = '<!DOCTYPE html><html lang="en" class=""><head>'
end_marker = '<style id="pz-mobile-styles">'

start_pos = html.find(start_tag)
end_pos = html.find(end_marker)

if start_pos != -1 and end_pos != -1:
    # Keep what was before start_tag + start_tag
    prefix = html[:start_pos + len(start_tag)]
    suffix = html[end_pos:]

    # Clean header insertion
    clean_head = """
<script>
(function() {
  /* CLEAN TITLE & SKULL FAVICON LOCK (NON-MUTATING) */
  var DESIRED_TITLE = '💀 Recreated by Paramveer | Shopify Winter 2026';
  document.title = DESIRED_TITLE;

  function ensureSkullFavicon() {
    var svgFavicon = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💀</text></svg>";
    var icon = document.querySelector("link[rel*='icon']");
    if (!icon) {
      icon = document.createElement('link');
      icon.rel = 'icon';
      icon.type = 'image/svg+xml';
      icon.href = svgFavicon;
      if (document.head) document.head.appendChild(icon);
    } else if (icon.href !== svgFavicon) {
      icon.href = svgFavicon;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureSkullFavicon);
  } else {
    ensureSkullFavicon();
  }
})();
</script>
<script>
(function() {
  // Global Error & Console Handler to suppress React SSR/Hydration Mismatch Errors
  var origConsoleError = console.error;
  var origConsoleWarn = console.warn;

  function isHydrationError(msg) {
    if (!msg) return false;
    var str = String(msg);
    return str.indexOf('Minified React error #418') !== -1 ||
           str.indexOf('Minified React error #423') !== -1 ||
           str.indexOf('Minified React error #425') !== -1 ||
           str.indexOf('Minified React error #345') !== -1 ||
           str.indexOf('Minified React error #422') !== -1 ||
           str.indexOf('Minified React error #419') !== -1 ||
           str.indexOf('error-decoder.html') !== -1 ||
           str.indexOf('hydrateRoot') !== -1 ||
           str.indexOf('hydrat') !== -1 ||
           str.indexOf('Hydrat') !== -1 ||
           str.indexOf('Text content does not match') !== -1 ||
           str.indexOf('Expected server HTML') !== -1 || str.indexOf('Failed to construct') !== -1 || str.indexOf('Invalid URL') !== -1 || str.indexOf('Animation with name') !== -1 || str.indexOf('FallbackImageScene') !== -1;
  }

  console.error = function() {
    if (arguments[0] && isHydrationError(arguments[0])) {
      return; // Suppress React hydration mismatch logs
    }
    origConsoleError.apply(console, arguments);
  };

  console.warn = function() {
    if (arguments[0] && isHydrationError(arguments[0])) {
      return; // Suppress React hydration warnings
    }
    origConsoleWarn.apply(console, arguments);
  };
})();
</script>
<meta charSet="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>💀 Recreated by Paramveer | Shopify Winter 2026</title>
<link rel="icon" type="image/svg+xml" href="/skull-favicon.svg"/>
<meta name="description" content="The commerce renaissance is here. Explore 150+ product updates across AI, retail, and more."/>
<link rel="preload stylesheet" href="./styles/tailwind-G-N6aznT.css" as="style"/>
<link rel="preconnect" href="https://cdn.shopify.com"/>
<link rel="dns-prefetch" href="https://cdn.shopify.com"/>
<link rel="preload stylesheet" href="./styles/fonts-latin-CzfLCQn_.css" as="style"/>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" />
"""
    new_html = prefix + clean_head + suffix
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESS: Cleaned up index.html header!")
else:
    print(f"ERROR: Could not find markers: start={start_pos}, end={end_pos}")
