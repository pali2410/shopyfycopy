export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // 1. Try to fetch the requested static asset
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

    // 2. If missing JS module, try fetching from /scripts/ or return empty JS module (200 OK)
    if (pathname.endsWith('.js') || pathname.endsWith('.mjs')) {
      const filename = pathname.substring(pathname.lastIndexOf('/') + 1);
      const scriptUrl = new URL('/scripts/' + filename, url.origin);
      const scriptResp = await env.ASSETS.fetch(new Request(scriptUrl));
      if (scriptResp.status < 400) return scriptResp;

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
