import sys
import re

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Original Size:', len(content))

# 1. Clean all existing <title> tags and set to "Paramveer Recreate"
content = re.sub(r'<title>.*?</title>', '<title>Paramveer Recreate</title>', content, flags=re.DOTALL)

# 2. Clean any old script blocks matching PARAMVEER or pz-nav-pill
while '/* PARAMVEER' in content:
    idx = content.find('/* PARAMVEER')
    s_start = content.rfind('<script>', 0, idx)
    s_end = content.find('</script>', idx)
    if s_start >= 0 and s_end > 0:
        content = content[:s_start] + content[s_end + len('</script>'):]
        print('Removed old PARAMVEER script block')
    else:
        break

while 'pz-nav-pill' in content:
    idx = content.find('pz-nav-pill')
    s_start = content.rfind('<script>', 0, idx)
    s_end = content.find('</script>', idx)
    if s_start >= 0 and s_end > 0:
        content = content[:s_start] + content[s_end + len('</script>'):]
        print('Removed old pz-nav-pill script block')
    else:
        break

# 3. Clean old favicon tags
content = re.sub(r'<link[^>]*rel="icon"[^>]*>', '', content)
content = re.sub(r'<link[^>]*rel="shortcut icon"[^>]*>', '', content)
content = re.sub(r'<link[^>]*rel="apple-touch-icon"[^>]*>', '', content)

# 4. Injected Master Head Lock Script for Title & 💀 Skull Favicon
MASTER_HEAD_LOCK = r"""<script>
(function() {
  /* MASTER TITLE & FAVICON LOCK */
  var DESIRED_TITLE = 'Paramveer Recreate';
  
  function forceTitleAndFavicon() {
    if (document.title !== DESIRED_TITLE) {
      document.title = DESIRED_TITLE;
    }
    var titleTags = document.querySelectorAll('title');
    titleTags.forEach(function(t) {
      if (t.textContent !== DESIRED_TITLE) t.textContent = DESIRED_TITLE;
    });

    var svgFavicon = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💀</text></svg>";
    var icons = document.querySelectorAll("link[rel*='icon']");
    if (icons.length === 0) {
      var l = document.createElement('link');
      l.rel = 'icon';
      l.type = 'image/svg+xml';
      l.href = svgFavicon;
      if (document.head) document.head.appendChild(l);
    } else {
      icons.forEach(function(l) {
        l.type = 'image/svg+xml';
        l.href = svgFavicon;
      });
    }
  }

  forceTitleAndFavicon();

  // MutationObserver on document.head to catch title/favicon changes by React/Remix
  var headObs = new MutationObserver(forceTitleAndFavicon);
  if (document.head) {
    headObs.observe(document.head, { childList: true, subtree: true, characterData: true });
  }

  setInterval(forceTitleAndFavicon, 300);
})();
</script>"""

if '<head>' in content:
    content = content.replace('<head>', '<head>\n' + MASTER_HEAD_LOCK, 1)
    print('Injected Master Head Lock Script into <head>')

# 5. Master Top-Center Floating Pill & Slide Panel Script
MASTER_PILL_SCRIPT = r"""<script>
(function () {
  /* MASTER TOP-CENTER FLOATING PILL & SLIDE PANEL */

  function injectOrUpdateTopCenterPill() {
    var pill = document.getElementById('pz-nav-pill');
    if (!pill) {
      pill = document.createElement('a');
      pill.id = 'pz-nav-pill';
      pill.className = 'pz-trigger';
      pill.href = '#';
      pill.setAttribute('aria-label', 'Recreated by Paramveer Sinh Zala');
      pill.innerHTML = '<span style="display:inline-flex;align-items:center;gap:6px;pointer-events:none;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="opacity:0.9;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/></svg>Recreated by <strong style="font-weight:600;">Paramveer</strong></span>';
    }

    /* FORCE TOP CENTER POSITIONING VIA !IMPORTANT INLINE STYLES */
    pill.style.cssText = 'position: fixed !important; top: 10px !important; left: 50% !important; right: auto !important; bottom: auto !important; transform: translateX(-50%) !important; z-index: 99999999 !important; display: inline-flex !important; align-items: center !important; gap: 6px !important; padding: 8px 18px !important; border-radius: 9999px !important; font-size: 13px !important; font-weight: 500 !important; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important; color: #f5f5f7 !important; background: rgba(12, 12, 14, 0.92) !important; border: 1px solid rgba(255, 255, 255, 0.32) !important; text-decoration: none !important; cursor: pointer !important; white-space: nowrap !important; backdrop-filter: blur(16px) !important; -webkit-backdrop-filter: blur(16px) !important; letter-spacing: -0.01em !important; line-height: 1 !important; pointer-events: auto !important; box-shadow: 0 8px 28px rgba(0,0,0,0.6) !important; transition: background 0.2s ease, border-color 0.2s ease !important;';

    pill.onmouseenter = function() {
      this.style.background = 'rgba(28, 28, 34, 0.98)';
      this.style.borderColor = 'rgba(255, 255, 255, 0.55)';
    };
    pill.onmouseleave = function() {
      this.style.background = 'rgba(12, 12, 14, 0.92)';
      this.style.borderColor = 'rgba(255, 255, 255, 0.32)';
    };

    if (document.body && !document.body.contains(pill)) {
      document.body.appendChild(pill);
    }
  }

  function injectSlidePanel() {
    if (document.getElementById('pz-slide-panel')) return;

    var panel = document.createElement('div');
    panel.id = 'pz-slide-panel';
    panel.innerHTML =
      '<div style="position:relative;max-width:820px;margin:0 auto;padding:36px 40px 32px;box-sizing:border-box;">' +
        '<button id="pz-panel-close" type="button" style="position:absolute;top:20px;right:24px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);color:#f5f5f7;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:18px;line-height:1;display:flex;align-items:center;justify-content:center;transition:all 0.2s;pointer-events:auto !important;z-index:1000;" onmouseover="this.style.background=\'rgba(255,255,255,0.18)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">&times;</button>' +

        '<div style="display:flex;align-items:center;gap:18px;margin-bottom:18px;">' +
          '<div style="width:52px;height:52px;border-radius:50%;background:#f5f5f7;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;color:#0c0c0e;flex-shrink:0;">P</div>' +
          '<div>' +
            '<h3 style="margin:0 0 3px;font-size:22px;font-weight:700;color:#f5f5f7;letter-spacing:-0.02em;">Paramveer Sinh Zala</h3>' +
            '<p style="margin:0;font-size:13px;color:#a1a1aa;">Full-Stack Developer &bull; Creator of OmniRip &bull; zalaparamveer13@gmail.com</p>' +
          '</div>' +
        '</div>' +

        '<p style="font-size:14.5px;line-height:1.65;color:#d4d4d8;margin:0 0 22px;font-weight:400;">' +
          'Extracted and replicated this complete <strong style="color:#f5f5f7;">Shopify Editions Winter &rsquo;26</strong> website &mdash; including 19 3D GLB models, Rive animations, KTX2 GPU textures, and 150+ feature sections &mdash; <strong style="color:#f5f5f7;">with just one prompt</strong> using OmniRip in ~20 minutes.' +
        '</p>' +

        '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:24px;">' +
          '<div style="background:#161618;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:14px 8px;text-align:center;">' +
            '<div style="font-size:24px;font-weight:700;color:#f5f5f7;line-height:1;">1</div>' +
            '<div style="font-size:10px;color:#a1a1aa;text-transform:uppercase;letter-spacing:1px;margin-top:6px;font-weight:600;">Prompt</div>' +
          '</div>' +
          '<div style="background:#161618;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:14px 8px;text-align:center;">' +
            '<div style="font-size:24px;font-weight:700;color:#f5f5f7;line-height:1;">19</div>' +
            '<div style="font-size:10px;color:#a1a1aa;text-transform:uppercase;letter-spacing:1px;margin-top:6px;font-weight:600;">3D Models</div>' +
          '</div>' +
          '<div style="background:#161618;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:14px 8px;text-align:center;">' +
            '<div style="font-size:24px;font-weight:700;color:#f5f5f7;line-height:1;">150+</div>' +
            '<div style="font-size:10px;color:#a1a1aa;text-transform:uppercase;letter-spacing:1px;margin-top:6px;font-weight:600;">Features</div>' +
          '</div>' +
          '<div style="background:#161618;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:14px 8px;text-align:center;">' +
            '<div style="font-size:24px;font-weight:700;color:#f5f5f7;line-height:1;">~20</div>' +
            '<div style="font-size:10px;color:#a1a1aa;text-transform:uppercase;letter-spacing:1px;margin-top:6px;font-weight:600;">Minutes</div>' +
          '</div>' +
        '</div>' +

        '<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">' +
          '<a id="pz-btn-linkedin" href="https://www.linkedin.com/in/paramveer-sinh-zala-601114423/" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:8px;background:#f5f5f7;color:#0c0c0e;padding:12px 24px;border-radius:9999px;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background=\'#e5e5e7\'" onmouseout="this.style.background=\'#f5f5f7\'">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="#0c0c0e"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>' +
            'Connect on LinkedIn' +
          '</a>' +
          '<a id="pz-btn-github" href="https://github.com/pali2410/shopyfycopy.git" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.08);color:#f5f5f7;padding:12px 22px;border-radius:9999px;font-size:14px;font-weight:600;text-decoration:none;border:1px solid rgba(255,255,255,0.16);transition:all 0.2s;" onmouseover="this.style.background=\'rgba(255,255,255,0.16)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">' +
            '<svg width="18" height="18" viewBox="0 0 24 24" fill="#f5f5f7"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>' +
            'Open Source GitHub Repository' +
          '</a>' +
          '<a id="pz-btn-email" href="mailto:zalaparamveer13@gmail.com" style="display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.08);color:#d4d4d8;padding:12px 22px;border-radius:9999px;font-size:14px;font-weight:500;text-decoration:none;border:1px solid rgba(255,255,255,0.14);transition:all 0.2s;" onmouseover="this.style.background=\'rgba(255,255,255,0.14)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">' +
            '&#9993; Email' +
          '</a>' +
        '</div>' +
      '</div>';

    Object.assign(panel.style, {
      position: 'fixed',
      top: '0',
      left: '0',
      right: '0',
      width: '100%',
      zIndex: '99999999',
      background: 'rgba(12, 12, 14, 0.97)',
      backdropFilter: 'blur(24px)',
      WebkitBackdropFilter: 'blur(24px)',
      borderBottom: '1px solid rgba(245, 245, 247, 0.18)',
      color: '#f5f5f7',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      transform: 'translateY(-100%)',
      transition: 'transform 0.38s cubic-bezier(0.16, 1, 0.3, 1)',
      boxShadow: '0 20px 60px rgba(0,0,0,0.85)'
    });

    if (document.body) {
      document.body.appendChild(panel);

      document.getElementById('pz-panel-close').addEventListener('click', function(e) {
        e.stopPropagation();
        closePanel();
      });

      document.getElementById('pz-btn-linkedin').addEventListener('click', function(e) {
        e.stopPropagation();
        window.open('https://www.linkedin.com/in/paramveer-sinh-zala-601114423/', '_blank');
      });

      document.getElementById('pz-btn-github').addEventListener('click', function(e) {
        e.stopPropagation();
        window.open('https://github.com/pali2410/shopyfycopy.git', '_blank');
      });

      document.getElementById('pz-btn-email').addEventListener('click', function(e) {
        e.stopPropagation();
        window.location.href = 'mailto:zalaparamveer13@gmail.com';
      });
    }
  }

  var panelOpen = false;

  function openPanel() {
    injectSlidePanel();
    var panel = document.getElementById('pz-slide-panel');
    if (!panel) return;
    panelOpen = true;
    panel.style.transform = 'translateY(0)';
  }

  function closePanel() {
    var panel = document.getElementById('pz-slide-panel');
    if (!panel) return;
    panelOpen = false;
    panel.style.transform = 'translateY(-100%)';
  }

  document.addEventListener('click', function (e) {
    var el = e.target;
    if (el && el.closest('#pz-slide-panel')) return;

    while (el && el !== document.body && el !== document.documentElement) {
      if (
        el.id === 'pz-nav-pill' ||
        (el.className && typeof el.className === 'string' && el.className.indexOf('pz-trigger') !== -1)
      ) {
        e.preventDefault();
        e.stopPropagation();
        if (panelOpen) {
          closePanel();
        } else {
          openPanel();
        }
        return false;
      }
      el = el.parentElement;
    }
  }, true);

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && panelOpen) closePanel();
  });

  function run() {
    injectOrUpdateTopCenterPill();
    injectSlidePanel();
  }

  var observer = new MutationObserver(run);
  if (document.body) {
    observer.observe(document.body, { childList: true, subtree: true });
  }

  window.addEventListener('load', function() {
    run();
    setTimeout(run, 200);
    setTimeout(run, 800);
    setTimeout(run, 2000);
  });
})();
</script>"""

if '</body>' in content:
    content = content.replace('</body>', MASTER_PILL_SCRIPT + '\n</body>', 1)
    print('Injected Master Top-Center Pill Script before </body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html size:', len(content))
print('SUCCESS!')
