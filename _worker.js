export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // A. Intercept Page Routes (/editions/winter2026, /editions/spring2026, /) and fetch /index.html cleanly
    const isPageRoute = pathname === '/' || pathname.includes('/editions/') || !pathname.includes('.');

    if (isPageRoute) {
      try {
        const indexUrl = new URL('/index.html', url.origin);
        const indexResp = await env.ASSETS.fetch(indexUrl);
        const htmlHeaders = new Headers(indexResp.headers);
        htmlHeaders.set('Content-Type', 'text/html; charset=utf-8');
        htmlHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
        htmlHeaders.set('Pragma', 'no-cache');
        htmlHeaders.set('Expires', '0');

        return new Response(indexResp.body, {
          status: 200,
          headers: htmlHeaders
        });
      } catch (err) {
        // Fallthrough if fetch fails
      }
    }

    // B. Static Asset Lookup
    let response = await env.ASSETS.fetch(request);
    if (response.status < 400) return response;

    // C. Asset Fallbacks for JS chunks
    if (pathname.endsWith('.js') || pathname.endsWith('.mjs')) {
      const rawFilename = pathname.substring(pathname.lastIndexOf('/') + 1);
      const decodedFilename = decodeURIComponent(rawFilename);

      try {
        const scriptResp = await env.ASSETS.fetch(new URL('/scripts/' + decodedFilename, url.origin));
        if (scriptResp.status < 400) return scriptResp;
      } catch (e) {}

      try {
        const cdnResp = await env.ASSETS.fetch(new URL('/raw_site/cdn.shopify.com/oxygen-v2/47215/49013/102837/4002246/assets/' + decodedFilename, url.origin));
        if (cdnResp.status < 400) return cdnResp;
      } catch (e) {}

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

    // D. Final SPA fallback to /index.html (Status 200 OK)
    const indexUrl = new URL('/index.html', url.origin);
    const fallbackResp = await env.ASSETS.fetch(indexUrl);
    const finalHeaders = new Headers(fallbackResp.headers);
    finalHeaders.set('Content-Type', 'text/html; charset=utf-8');
    finalHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');

    return new Response(fallbackResp.body, {
      status: 200,
      headers: finalHeaders
    });
  }
};
