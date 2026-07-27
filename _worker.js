export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // A. Intercept Page Routes (/editions/winter2026, /) -> serve /index.html with Status 200 OK
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
        return new Response(indexResp.body, { status: 200, headers: htmlHeaders });
      } catch (err) {}
    }

    // B. Remap legacy URL-encoded parentheses filenames to safe names
    // e.g. %28_locale%29.editions.winter2026-BOe91MRy.js -> locale-editions-winter2026-BOe91MRy.js
    const decodedPath = decodeURIComponent(pathname);
    if (decodedPath.includes('(_locale).editions.winter2026')) {
      const safePath = decodedPath.replace(
        '(_locale).editions.winter2026',
        'locale-editions-winter2026'
      );
      try {
        const safeUrl = new URL(safePath, url.origin);
        const safeResp = await env.ASSETS.fetch(safeUrl);
        if (safeResp.status < 400) {
          const jsHeaders = new Headers(safeResp.headers);
          jsHeaders.set('Content-Type', 'application/javascript; charset=utf-8');
          return new Response(safeResp.body, { status: 200, headers: jsHeaders });
        }
      } catch (e) {}
    }

    // C. Try static asset lookup
    let response = await env.ASSETS.fetch(request);
    if (response.status < 400) return response;

    // D. Asset fallbacks for JS chunks
    if (pathname.endsWith('.js') || pathname.endsWith('.mjs')) {
      const rawFilename = pathname.substring(pathname.lastIndexOf('/') + 1);
      const decodedFilename = decodeURIComponent(rawFilename);

      try {
        const scriptResp = await env.ASSETS.fetch(new URL('/scripts/' + decodedFilename, url.origin));
        if (scriptResp.status < 400) return scriptResp;
      } catch (e) {}

      // Try with safe name (no parentheses)
      const safeFilename = decodedFilename.replace('(_locale).editions.winter2026', 'locale-editions-winter2026');
      try {
        const safeResp = await env.ASSETS.fetch(new URL('/scripts/' + safeFilename, url.origin));
        if (safeResp.status < 400) return safeResp;
      } catch (e) {}

      return new Response('export default {};', {
        status: 200,
        headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'no-cache' }
      });
    }

    if (pathname.endsWith('.css')) {
      return new Response('', { status: 200, headers: { 'Content-Type': 'text/css; charset=utf-8' } });
    }

    // E. Final SPA fallback (Status 200 OK)
    try {
      const indexUrl = new URL('/index.html', url.origin);
      const fallbackResp = await env.ASSETS.fetch(indexUrl);
      return new Response(fallbackResp.body, {
        status: 200,
        headers: {
          'Content-Type': 'text/html; charset=utf-8',
          'Cache-Control': 'no-cache, no-store, must-revalidate'
        }
      });
    } catch (e) {
      return new Response('Site loading...', { status: 200, headers: { 'Content-Type': 'text/html' } });
    }
  }
};
