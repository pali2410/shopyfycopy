export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;
    const decodedPath = decodeURIComponent(pathname);

    // 1. Identify static asset extensions
    const isAsset = /\.(js|css|wasm|woff2|woff|ttf|otf|json|png|jpg|jpeg|gif|svg|hdr|glb|gltf|mp3|ico)$/i.test(decodedPath);

    if (isAsset) {
      // Extract file basename
      const filename = decodedPath.substring(decodedPath.lastIndexOf('/') + 1);
      const safeFilename = filename.replace('(_locale).editions.winter2026', 'locale-editions-winter2026');

      // Build candidate paths in order of preference
      const candidatePaths = [
        pathname, // original exact path
        '/' + filename, // root level
        '/scripts/' + filename, // scripts folder
        '/styles/' + filename, // styles folder
        '/images/' + filename, // images folder
        '/media/' + filename, // media folder
        '/3d_models/' + filename, // 3d_models folder
        '/' + safeFilename,
        '/scripts/' + safeFilename
      ];

      for (const p of candidatePaths) {
        try {
          const assetReq = new Request(new URL(p, url.origin), request);
          const response = await env.ASSETS.fetch(assetReq);
          
          // Verify response is a valid asset (not index.html fallback)
          if (response.status < 400) {
            const contentType = response.headers.get('Content-Type') || '';
            
            // If Cloudflare returned text/html for a .js or .css file, skip it
            if (contentType.includes('text/html') && !filename.endsWith('.html')) {
              continue;
            }

            // Ensure correct Content-Type for JS and CSS files
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

      // Safe emergency fallback for missing JS / CSS to avoid breaking page load or throwing MIME errors
      if (filename.endsWith('.js')) {
        return new Response('/* Empty fallback script */\nexport default {};', {
          status: 200,
          headers: { 'Content-Type': 'application/javascript; charset=utf-8', 'Cache-Control': 'no-cache' }
        });
      }
      if (filename.endsWith('.css')) {
        return new Response('/* Empty fallback css */', {
          status: 200,
          headers: { 'Content-Type': 'text/css; charset=utf-8', 'Cache-Control': 'no-cache' }
        });
      }

      return new Response('Asset not found', { status: 404 });
    }

    // 2. Page route requests (/editions/winter2026, /, /editions/...) -> serve /index.html with status 200
    try {
      const indexReq = new Request(new URL('/index.html', url.origin), request);
      const indexResp = await env.ASSETS.fetch(indexReq);
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
