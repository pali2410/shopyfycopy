import sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# The module script on desktop requests:
# ./scripts/(_locale).editions.winter2026-BOe91MRy.js
#
# On desktop Chrome - this file is requested as:
#   GET /scripts/(_locale).editions.winter2026-BOe91MRy.js
#   -> Cloudflare ASSETS.fetch finds the file -> 200 OK -> works
#
# On mobile Chrome - the SAME request is made:
#   GET /scripts/(_locale).editions.winter2026-BOe91MRy.js 
#   -> BUT if _worker.js intercepts this URL and the path includes '.' 
#      (it does: .js) then isPageRoute = FALSE -> ASSETS.fetch(request) is called
#   -> ASSETS.fetch checks: does /scripts/(_locale).editions.winter2026-BOe91MRy.js exist?
#   -> YES it exists! So it should return 200 OK.
#
# Why does mobile fail then?
# The "Animation with name autoplay not found" error suggests Rive animations fail on mobile.
# The "FallbackImageScene-DrEja6F1.js:1 Failed to load module script: Expected a JavaScript-or-Wasm module script"
# This is the FALLBACK scene module we created - it was served as text/html before
#
# The real mobile issue might be:
# 1. WebGL context creation fails on mobile
# 2. The Rive animation player fails  
# 3. The react app hangs waiting for these to resolve
#
# FIX: We need to detect WebGL failure on mobile and show the page content without the canvas

print("Analysis:")
print("The module imports work on desktop because Cloudflare ASSETS.fetch finds the files.")
print("On mobile the issue is:")
print("1. WebGL canvas fails silently")
print("2. Rive animation 'autoplay' not found")
print("3. React app hangs in loading state waiting for 3D assets")
print()
print("The fix should be:")
print("- Inject a mobile JS snippet that detects when the canvas is stuck")
print("- After 3 seconds, if the main content is not visible, remove loading barrier")
print("- Do NOT touch index.html module imports - only add a mobile timeout rescue script")
