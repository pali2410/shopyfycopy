export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // A. Check if this is a Page Navigation / SPA Route (e.g. /editions/winter2026, /editions/spring2026, /)
    // Page routes have no file extension or contain /editions/
    const isPageRoute = pathname === '/' || pathname.includes('/editions/') || !pathname.includes('.');

    if (isPageRoute) {
      // Fetch /index.html directly from Cloudflare assets
      const indexReq = new Request(new URL('/index.html', request.url), request);
      const indexResp = await env.ASSETS.fetch(indexReq);

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

    // B. Static Asset Request (JS, CSS, PNG, GLB, WOFF2, etc.)
    let response = await env.ASSETS.fetch(request);
    if (response.status < 400) return response;

    // C. Asset Fallbacks for JS / CSS chunks if missing
    if (pathname.endsWith('.js') || pathname.endsWith('.mjs')) {
      const rawFilename = pathname.substring(pathname.lastIndexOf('/') + 1);
      const decodedFilename = decodeURIComponent(rawFilename);

      const scriptReq = new Request(new URL('/scripts/' + decodedFilename, request.url));
      let scriptResp = await env.ASSETS.fetch(scriptReq);
      if (scriptResp.status < 400) return scriptResp;

      const cdnReq = new Request(new URL('/raw_site/cdn.shopify.com/oxygen-v2/47215/49013/102837/4002246/assets/' + decodedFilename, request.url));
      let cdnResp = await env.ASSETS.fetch(cdnReq);
      if (cdnResp.status < 400) return cdnResp;

      return new Response('export default {};', {
        status: 200,
        headers: {
          'Content-Type': 'application/javascript; charset=utf-8',
          'Cache-Control': 'no-cache, no-store, must-revalidate'
        }
      });
    }

    if (pathname.endsWith('.css')) {
      return new Response('', {
        status: 200,
        headers: {
          'Content-Type': 'text/css; charset=utf-8',
          'Cache-Control': 'no-cache'
        }
      });
    }

    // Ultimate fallback for any unhandled route to index.html (200 OK)
    const indexReq = new Request(new URL('/index.html', request.url));
    const indexResp = await env.ASSETS.fetch(indexReq);
    return new Response(indexResp.body, {
      status: 200,
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      }
    });
  }
};
