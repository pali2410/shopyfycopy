import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Original Size:', len(content))

# Find existing script injection and remove it
script_start = content.find('/* PARAMVEER CREDIT INJECTION')
if script_start > 0:
    s_start = content.rfind('<script>', 0, script_start)
    s_end = content.find('</script>', script_start)
    if s_start >= 0 and s_end > 0:
        content = content[:s_start] + content[s_end + len('</script>'):]
        print('Removed previous credit script block')

# New script: Centered Modal Popup with Black & Off-White UI
POPUP_SCRIPT = r"""<script>
(function () {
  /* PARAMVEER CREDIT POPUP - Black & Off-White Theme */

  function injectNavPill() {
    if (document.getElementById('pz-nav-pill')) return;
    var nav = document.querySelector('nav');
    if (!nav || nav.children.length === 0) return;

    var pill = document.createElement('a');
    pill.id = 'pz-nav-pill';
    pill.href = '#';
    pill.setAttribute('aria-label', 'Recreated by Paramveer Sinh Zala');
    pill.innerHTML = '<span style="display:inline-flex;align-items:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="opacity:0.9;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/></svg>Recreated by <strong style="font-weight:600;">Paramveer</strong></span>';

    Object.assign(pill.style, {
      display: 'inline-flex',
      alignItems: 'center',
      gap: '6px',
      padding: '8px 16px',
      borderRadius: '9999px',
      fontSize: '13px',
      fontWeight: '500',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      color: '#f5f5f7',
      background: 'rgba(255, 255, 255, 0.12)',
      border: '1px solid rgba(255, 255, 255, 0.2)',
      textDecoration: 'none',
      cursor: 'pointer',
      whiteSpace: 'nowrap',
      backdropFilter: 'blur(12px)',
      WebkitBackdropFilter: 'blur(12px)',
      marginRight: '10px',
      letterSpacing: '-0.01em',
      lineHeight: '1',
      transition: 'all 0.2s ease'
    });

    pill.onmouseenter = function() {
      this.style.background = 'rgba(255, 255, 255, 0.22)';
      this.style.borderColor = 'rgba(255, 255, 255, 0.4)';
    };
    pill.onmouseleave = function() {
      this.style.background = 'rgba(255, 255, 255, 0.12)';
      this.style.borderColor = 'rgba(255, 255, 255, 0.2)';
    };

    var last = nav.children[nav.children.length - 1];
    nav.insertBefore(pill, last);

    pill.addEventListener('click', function(e) {
      e.preventDefault();
      openPopup();
    });
  }

  function injectPopupModal() {
    if (document.getElementById('pz-modal-overlay')) return;

    /* Backdrop overlay */
    var overlay = document.createElement('div');
    overlay.id = 'pz-modal-overlay';
    Object.assign(overlay.style, {
      position: 'fixed',
      top: '0',
      left: '0',
      width: '100vw',
      height: '100vh',
      zIndex: '999999',
      background: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(16px)',
      WebkitBackdropFilter: 'blur(16px)',
      display: 'none',
      alignItems: 'center',
      justifyContent: 'center',
      opacity: '0',
      transition: 'opacity 0.25s ease'
    });

    /* Modal dialog box */
    var dialog = document.createElement('div');
    dialog.id = 'pz-modal-dialog';
    dialog.innerHTML =
      '<div style="position:relative;width:100%;max-width:540px;background:#0c0c0e;border:1px solid rgba(245,245,247,0.16);border-radius:24px;padding:36px;box-shadow:0 30px 70px rgba(0,0,0,0.85);color:#f5f5f7;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,sans-serif;box-sizing:border-box;">' +
        
        /* Close button */
        '<button id="pz-modal-close" style="position:absolute;top:20px;right:20px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);color:#f5f5f7;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:18px;line-height:1;display:flex;align-items:center;justify-content:center;transition:all 0.2s;" onmouseover="this.style.background=\'rgba(255,255,255,0.18)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">&times;</button>' +
        
        /* Profile Header */
        '<div style="display:flex;align-items:center;gap:16px;margin-bottom:22px;">' +
          '<div style="width:54px;height:54px;border-radius:50%;background:#f5f5f7;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;color:#0c0c0e;flex-shrink:0;">P</div>' +
          '<div>' +
            '<h3 style="margin:0 0 4px;font-size:22px;font-weight:700;color:#f5f5f7;letter-spacing:-0.02em;">Paramveer Sinh Zala</h3>' +
            '<p style="margin:0;font-size:13px;color:#a1a1aa;font-weight:400;">Full-Stack Developer &bull; Creator of OmniRip</p>' +
          '</div>' +
        '</div>' +

        /* Story */
        '<p style="font-size:14px;line-height:1.65;color:#d4d4d8;margin:0 0 24px;font-weight:400;">' +
          'Extracted and replicated this entire <strong style="color:#f5f5f7;">Shopify Editions Winter &rsquo;26</strong> website &mdash; including 19 3D GLB models, Rive animations, KTX2 GPU textures, and 150+ feature sections &mdash; <strong style="color:#f5f5f7;">with just one prompt</strong> using OmniRip in ~20 minutes.' +
        '</p>' +

        /* Stat Grid (Black & Off-White theme) */
        '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:28px;">' +
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

        /* Action Buttons */
        '<div style="display:flex;flex-direction:column;gap:12px;">' +
          '<a href="https://www.linkedin.com/in/paramveer-sinh-zala-601114423/" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:10px;background:#f5f5f7;color:#0c0c0e;padding:14px;border-radius:9999px;font-size:14px;font-weight:600;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background=\'#e5e5e7\'" onmouseout="this.style.background=\'#f5f5f7\'">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="#0c0c0e"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>' +
            'Connect on LinkedIn' +
          '</a>' +
          '<a href="mailto:zalazalazalaparamveer113@gmail.com" style="display:flex;align-items:center;justify-content:center;gap:8px;background:rgba(255,255,255,0.06);color:#f5f5f7;padding:13px;border-radius:9999px;font-size:14px;font-weight:500;text-decoration:none;border:1px solid rgba(255,255,255,0.12);transition:all 0.2s;" onmouseover="this.style.background=\'rgba(255,255,255,0.12)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.06)\'">' +
            'zalazalazalaparamveer113@gmail.com' +
          '</a>' +
        '</div>' +
      '</div>';

    overlay.appendChild(dialog);
    document.body.appendChild(overlay);

    /* Close events */
    document.getElementById('pz-modal-close').addEventListener('click', closePopup);
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) closePopup();
    });
  }

  function openPopup() {
    injectPopupModal();
    var overlay = document.getElementById('pz-modal-overlay');
    if (!overlay) return;
    overlay.style.display = 'flex';
    setTimeout(function() {
      overlay.style.opacity = '1';
    }, 10);
  }

  function closePopup() {
    var overlay = document.getElementById('pz-modal-overlay');
    if (!overlay) return;
    overlay.style.opacity = '0';
    setTimeout(function() {
      overlay.style.display = 'none';
    }, 250);
  }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closePopup();
  });

  function checkAndInject() {
    injectNavPill();
    injectPopupModal();
  }

  var observer = new MutationObserver(checkAndInject);
  observer.observe(document.body, { childList: true, subtree: true });

  window.addEventListener('load', function() {
    checkAndInject();
    setTimeout(checkAndInject, 500);
    setTimeout(checkAndInject, 1500);
  });
})();
</script>"""

if '</body>' in content:
    content = content.replace('</body>', POPUP_SCRIPT + '\n</body>', 1)
    print('Injected Black & Off-White Popup Modal script before </body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html size:', len(content))
print('SUCCESS!')
