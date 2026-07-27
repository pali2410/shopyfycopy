export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // 1. Try fetching exact static asset requested
    let response = await env.ASSETS.fetch(request);

    // If static asset exists (200, 304, etc.)
    if (response.status < 400) {
      const isHtml = pathname === '/' || pathname.endsWith('.html') || pathname.includes('/editions/') || (response.headers.get('content-type') || '').includes('text/html');
      if (isHtml) {
        const freshHeaders = new Headers(response.headers);
        freshHeaders.set('Content-Type', 'text/html; charset=utf-8');
        freshHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
        return new Response(response.body, { status: response.status, headers: freshHeaders });
      }
      return response;
    }

    // 2. If missing JS or MJS module file
    if (pathname.endsWith('.js') || pathname.endsWith('.mjs')) {
      const rawFilename = pathname.substring(pathname.lastIndexOf('/') + 1);
      const decodedFilename = decodeURIComponent(rawFilename);

      // Try /scripts/
      const scriptUrl = new URL('/scripts/' + decodedFilename, url.origin);
      let scriptResp = await env.ASSETS.fetch(new Request(scriptUrl));
      if (scriptResp.status < 400) return scriptResp;

      // Try raw_site cdn assets path
      const cdnUrl = new URL('/raw_site/cdn.shopify.com/oxygen-v2/47215/49013/102837/4002246/assets/' + decodedFilename, url.origin);
      let cdnResp = await env.ASSETS.fetch(new Request(cdnUrl));
      if (cdnResp.status < 400) return cdnResp;

      // Safe JS module fallback with 200 OK
      return new Response('export default {};', {
        status: 200,
        headers: {
          'Content-Type': 'application/javascript; charset=utf-8',
          'Cache-Control': 'no-cache, no-store, must-revalidate'
        }
      });
    }

    // 3. If missing CSS, return empty CSS with 200 OK
    if (pathname.endsWith('.css')) {
      return new Response('', {
        status: 200,
        headers: {
          'Content-Type': 'text/css; charset=utf-8',
          'Cache-Control': 'no-cache'
        }
      });
    }

    // 4. SPA Fallback for HTML Page Routes (/editions/winter2026, etc.): Fetch /index.html and return STATUS 200 OK!
    const indexUrl = new URL('/index.html', url.origin);
    const indexResp = await env.ASSETS.fetch(new Request(indexUrl));
    const htmlHeaders = new Headers(indexResp.headers);
    htmlHeaders.set('Content-Type', 'text/html; charset=utf-8');
    htmlHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
    htmlHeaders.set('Pragma', 'no-cache');
    htmlHeaders.set('Expires', '0');

    return new Response(indexResp.body, {
      status: 200,
      headers: htmlHeaders
    });
  }
};
