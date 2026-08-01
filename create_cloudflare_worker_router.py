import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

WORKER_JS_CONTENT = r"""export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // Attempt to fetch asset from Cloudflare static assets
    let response = await env.ASSETS.fetch(request);

    // If request failed with 404
    if (response.status === 404) {
      // 1. If requesting a JS or MJS module file, return valid JS to prevent MIME type text/html error
      if (pathname.endsWith('.js') || pathname.endsWith('.mjs')) {
        // Try searching in /scripts/ or /assets/
        const filename = pathname.substring(pathname.lastIndexOf('/') + 1);
        const scriptRetry = await env.ASSETS.fetch(new Request(new URL('/scripts/' + filename, request.url), request));
        if (scriptRetry.status === 200) return scriptRetry;

        const assetRetry = await env.ASSETS.fetch(new Request(new URL('/assets/' + filename, request.url), request));
        if (assetRetry.status === 200) return assetRetry;

        return new Response('export default {};', {
          status: 200,
          headers: {
            'Content-Type': 'application/javascript; charset=utf-8',
            'Cache-Control': 'no-cache, no-store, must-revalidate'
          }
        });
      }

      // 2. CSS files fallback
      if (pathname.endsWith('.css')) {
        return new Response('', {
          status: 200,
          headers: {
            'Content-Type': 'text/css; charset=utf-8',
            'Cache-Control': 'no-cache'
          }
        });
      }

      // 3. SPA Fallback for HTML page routes: return index.html with no-cache headers
      const htmlResp = await env.ASSETS.fetch(new Request(new URL('/index.html', request.url), request));
      const htmlHeaders = new Headers(htmlResp.headers);
      htmlHeaders.set('Content-Type', 'text/html; charset=utf-8');
      htmlHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
      htmlHeaders.set('Pragma', 'no-cache');
      htmlHeaders.set('Expires', '0');

      return new Response(htmlResp.body, {
        status: 200,
        headers: htmlHeaders
      });
    }

    // Force no-cache headers on HTML responses so mobile devices always get the newest version
    const isHtml = pathname === '/' || pathname.endsWith('.html') || pathname.includes('/editions/') || (response.headers.get('content-type') || '').includes('text/html');
    if (isHtml) {
      const freshHeaders = new Headers(response.headers);
      freshHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
      freshHeaders.set('Pragma', 'no-cache');
      freshHeaders.set('Expires', '0');
      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: freshHeaders
      });
    }

    return response;
  }
};
"""

with open('_worker.js', 'w', encoding='utf-8') as f:
    f.write(WORKER_JS_CONTENT)
print('Created _worker.js router script')

# Update wrangler.jsonc
WRANGLER_JSONC = r"""{
  "name": "shopyfycopy",
  "compatibility_date": "2026-07-26",
  "assets": {
    "directory": "."
  }
}
"""

with open('wrangler.jsonc', 'w', encoding='utf-8') as f:
    f.write(WRANGLER_JSONC)
print('Updated wrangler.jsonc to use _worker.js router')
print('SUCCESS!')
