export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;
    const decodedPath = decodeURIComponent(pathname);

    // 1. Identify static asset requests (.js, .css, .wasm, .woff2, .json, .png, etc.)
    const isAsset = /\.(js|css|wasm|woff2|woff|ttf|otf|json|png|jpg|jpeg|gif|svg|hdr|glb|gltf|mp3|ico)$/i.test(decodedPath);

    if (isAsset) {
      const filename = decodedPath.substring(decodedPath.lastIndexOf('/') + 1);
      const safeFilename = filename.replace('(_locale).editions.winter2026', 'locale-editions-winter2026');

      // Candidate paths relative to root asset directory
      const candidatePaths = [
        pathname,
        decodedPath,
        '/' + filename,
        '/scripts/' + filename,
        '/styles/' + filename,
        '/images/' + filename,
        '/media/' + filename,
        '/' + safeFilename,
        '/scripts/' + safeFilename
      ];

      for (const cp of candidatePaths) {
        try {
          // Pass URL object with origin + candidate path directly to env.ASSETS.fetch
          const targetUrl = new URL(cp, url.origin);
          const response = await env.ASSETS.fetch(targetUrl);
          
          if (response.status < 400) {
            const contentType = response.headers.get('Content-Type') || '';
            if (contentType.includes('text/html') && !filename.endsWith('.html')) {
              continue;
            }

            const headers = new Headers(response.headers);
            if (filename.endsWith('.js')) {
              headers.set('Content-Type', 'application/javascript; charset=utf-8');
            } else if (filename.endsWith('.css')) {
              headers.set('Content-Type', 'text/css; charset=utf-8');
            } else if (filename.endsWith('.wasm')) {
              headers.set('Content-Type', 'application/wasm');
            }

            return new Response(response.body, {
              status: 200,
              headers: headers
            });
          }
        } catch (e) {}
      }

      // Safe JS fallback if chunk is dynamic or optional
      if (filename.endsWith('.js')) {
        return new Response('/* Fallback script */\nexport default {};', {
          status: 200,
          headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'no-cache' }
        });
      }
      if (filename.endsWith('.css')) {
        return new Response('/* Fallback css */', {
          status: 200,
          headers: { 'Content-Type': 'text/css; charset=utf-8', 'Cache-Control': 'no-cache' }
        });
      }

      return new Response('Asset not found', { status: 404 });
    }

    // 2. Page route requests (/editions/winter2026, /, /editions/...) -> serve /index.html with status 200
    try {
      const indexResp = await env.ASSETS.fetch(new URL('/index.html', url.origin));
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
