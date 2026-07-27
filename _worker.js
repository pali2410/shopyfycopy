export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;
    const decodedPath = decodeURIComponent(pathname);

    // Check if the request is for a static asset (has extension like .js, .css, .wasm, etc.)
    const isAsset = /\.(js|css|wasm|woff2|woff|ttf|otf|json|png|jpg|jpeg|gif|svg|hdr|glb|gltf|mp3|ico)$/i.test(decodedPath);

    // A. Static Asset Requests
    if (isAsset) {
      // 1. Try direct asset lookup from ASSETS binding
      try {
        let response = await env.ASSETS.fetch(request);
        if (response.status < 400) return response;
      } catch(e) {}

      // 2. Extract base filename (handles relative asset fetches under /editions/winter2026/...)
      const rawFilename = decodedPath.substring(decodedPath.lastIndexOf('/') + 1);

      // 3. Try looking up in /scripts/ or root /
      const searchPaths = [
        '/' + rawFilename,
        '/scripts/' + rawFilename,
        '/' + rawFilename.replace('(_locale).editions.winter2026', 'locale-editions-winter2026'),
        '/scripts/' + rawFilename.replace('(_locale).editions.winter2026', 'locale-editions-winter2026')
      ];

      for (const sp of searchPaths) {
        try {
          const altResp = await env.ASSETS.fetch(new URL(sp, url.origin));
          if (altResp.status < 400) {
            const mime = rawFilename.endsWith('.js') ? 'application/javascript; charset=utf-8' :
                         rawFilename.endsWith('.css') ? 'text/css; charset=utf-8' : altResp.headers.get('Content-Type');
            const h = new Headers(altResp.headers);
            if (mime) h.set('Content-Type', mime);
            return new Response(altResp.body, { status: 200, headers: h });
          }
        } catch(e) {}
      }

      // 4. Fallback for JS / CSS assets to prevent blank screens & strict MIME type errors
      if (rawFilename.endsWith('.js')) {
        return new Response('export default {};', {
          status: 200,
          headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'no-cache' }
        });
      }
      if (rawFilename.endsWith('.css')) {
        return new Response('', {
          status: 200,
          headers: { 'Content-Type': 'text/css; charset=utf-8' }
        });
      }

      // Return 404 for missing non-essential assets
      return new Response('Asset not found', { status: 404 });
    }

    // B. Page Routes (/editions/winter2026, /, /editions/...) -> Serve /index.html with 200 OK
    try {
      const indexUrl = new URL('/index.html', url.origin);
      const indexResp = await env.ASSETS.fetch(indexUrl);
      const htmlHeaders = new Headers(indexResp.headers);
      htmlHeaders.set('Content-Type', 'text/html; charset=utf-8');
      htmlHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
      htmlHeaders.set('Pragma', 'no-cache');
      htmlHeaders.set('Expires', '0');
      return new Response(indexResp.body, { status: 200, headers: htmlHeaders });
    } catch (err) {
      return new Response('Loading...', { status: 200, headers: { 'Content-Type': 'text/html' } });
    }
  }
};
