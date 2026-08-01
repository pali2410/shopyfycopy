import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

SUPER_LINK_INTERCEPTOR = """
<script>
(function() {
  /* BULLETPROOF EXTERNAL LINK & BUTTON INTERCEPTOR */

  // 1. Intercept window.open calls to external URLs
  var origWindowOpen = window.open;
  window.open = function(url, target, features) {
    if (typeof url === 'string') {
      if (url.indexOf('linkedin.com/in/paramveer') !== -1 || url.indexOf('github.com/pali2410') !== -1) {
        return origWindowOpen.apply(window, arguments);
      }
      if (url.startsWith('http') || url.startsWith('//') || url.indexOf('shopify') !== -1) {
        console.log('[Link Interceptor] Prevented window.open to:', url);
        return null;
      }
    }
    return origWindowOpen.apply(window, arguments);
  };

  // 2. Intercept click events on links, buttons, and elements with data-href/data-url
  document.addEventListener('click', function(e) {
    var target = e.target;
    while (target && target !== document && target !== document.body) {
      var id = target.id || '';
      var href = target.getAttribute('href') || target.getAttribute('data-href') || target.getAttribute('data-url') || target.getAttribute('action') || '';
      var tag = (target.tagName || '').toUpperCase();

      // Allow our own custom branding links
      if (id.startsWith('pz-') || href.indexOf('linkedin.com/in/paramveer') !== -1 || href.indexOf('github.com/pali2410') !== -1) {
        return;
      }

      // Check if element or ancestor is external link / button
      var isExternal = href.startsWith('http://') || 
                         href.startsWith('https://') || 
                         href.startsWith('mailto:') || 
                         href.startsWith('//') || 
                         href.indexOf('shopify.com') !== -1 || 
                         href.indexOf('shopify') !== -1;

      // Check button text for external actions like "Start for free" or "Shopify.com"
      var text = (target.innerText || target.textContent || '').trim().toLowerCase();
      var isExternalButton = text.indexOf('start for free') !== -1 || 
                              text.indexOf('shopify.com') !== -1 || 
                              text.indexOf('try for free') !== -1;

      if (isExternal || (tag === 'BUTTON' && isExternalButton) || (tag === 'A' && isExternalButton)) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.log('[Link Interceptor] Intercepted click on:', tag, href || text);
        return false;
      }

      target = target.parentNode;
    }
  }, true);
})();
</script>
"""

# Replace existing link interceptor
start_marker = '/* GLOBAL RUNTIME EXTERNAL LINK INTERCEPTOR */'
if start_marker in html:
    script_start = html.rfind('<script>', 0, html.find(start_marker))
    script_end = html.find('</script>', html.find(start_marker)) + len('</script>')
    if script_start != -1 and script_end != -1:
        html = html[:script_start] + SUPER_LINK_INTERCEPTOR + html[script_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("SUCCESS: Upgraded link interceptor in index.html!")
    else:
        print("ERROR: Script tags around marker not found")
else:
    print("Marker not found, inserting after SafeURL polyfill...")
    insert_pos = html.find('window.URL = SafeURL;\n})();\n</script>')
    if insert_pos != -1:
        insert_at = insert_pos + len('window.URL = SafeURL;\n})();\n</script>')
        html = html[:insert_at] + '\n' + SUPER_LINK_INTERCEPTOR + html[insert_at:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("SUCCESS: Inserted super link interceptor!")
