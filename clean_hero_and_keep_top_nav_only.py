import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Original Size:', len(content))

# Clean previous script
script_start = content.find('/* PARAMVEER CREDIT POPUP')
if script_start > 0:
    s_start = content.rfind('<script>', 0, script_start)
    s_end = content.find('</script>', script_start)
    if s_start >= 0 and s_end > 0:
        content = content[:s_start] + content[s_end + len('</script>'):]
        print('Cleaned previous script block')

# Final Top Nav Only Script:
# - NO modifications to middle/hero section
# - "Recreated by Paramveer" pill ONLY in top navigation bar
# - Black & Off-White Popup Modal with fully working buttons (LinkedIn, GitHub, Email, Close X)

TOP_NAV_ONLY_SCRIPT = r"""<script>
(function () {
  /* PARAMVEER CREDIT POPUP - Top Navigation Only */

  function injectTopNavPill() {
    if (document.getElementById('pz-nav-pill')) return;

    var startBtn = document.querySelector('[data-component-name="start-free-trial"]') || 
                   document.querySelector('a[href*="signup"]') || 
                   document.querySelector('nav') || 
                   document.querySelector('header');

    if (!startBtn) return;

    var pill = document.createElement('a');
    pill.id = 'pz-nav-pill';
    pill.className = 'pz-trigger';
    pill.href = '#';
    pill.setAttribute('aria-label', 'Recreated by Paramveer Sinh Zala');
    pill.innerHTML = '<span style="display:inline-flex;align-items:center;gap:6px;pointer-events:none;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="opacity:0.9;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/></svg>Recreated by <strong style="font-weight:600;">Paramveer</strong></span>';

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
      background: 'rgba(255, 255, 255, 0.16)',
      border: '1px solid rgba(255, 255, 255, 0.28)',
      textDecoration: 'none',
      cursor: 'pointer',
      whiteSpace: 'nowrap',
      backdropFilter: 'blur(12px)',
      WebkitBackdropFilter: 'blur(12px)',
      marginRight: '12px',
      letterSpacing: '-0.01em',
      lineHeight: '1',
      pointerEvents: 'auto',
      position: 'relative',
      zIndex: '99999',
      transition: 'all 0.2s ease'
    });

    pill.onmouseenter = function() {
      this.style.background = 'rgba(255, 255, 255, 0.28)';
      this.style.borderColor = 'rgba(255, 255, 255, 0.5)';
    };
    pill.onmouseleave = function() {
      this.style.background = 'rgba(255, 255, 255, 0.16)';
      this.style.borderColor = 'rgba(255, 255, 255, 0.28)';
    };

    if (startBtn.parentElement && startBtn.parentElement.tagName === 'LI') {
      var li = document.createElement('li');
      li.style.display = 'inline-block';
      li.appendChild(pill);
      startBtn.parentElement.parentElement.insertBefore(li, startBtn.parentElement);
    } else if (startBtn.parentElement) {
      startBtn.parentElement.insertBefore(pill, startBtn);
    }
  }

  function injectModal() {
    if (document.getElementById('pz-modal-overlay')) return;

    var overlay = document.createElement('div');
    overlay.id = 'pz-modal-overlay';
    Object.assign(overlay.style, {
      position: 'fixed',
      top: '0',
      left: '0',
      width: '100vw',
      height: '100vh',
      zIndex: '9999999',
      background: 'rgba(0, 0, 0, 0.78)',
      backdropFilter: 'blur(16px)',
      WebkitBackdropFilter: 'blur(16px)',
      display: 'none',
      alignItems: 'center',
      justifyContent: 'center',
      opacity: '0',
      transition: 'opacity 0.25s ease'
    });

    var dialog = document.createElement('div');
    dialog.id = 'pz-modal-dialog';
    dialog.innerHTML =
      '<div style="position:relative;width:90%;max-width:520px;background:#0c0c0e;border:1px solid rgba(245,245,247,0.18);border-radius:24px;padding:36px;box-shadow:0 30px 70px rgba(0,0,0,0.85);color:#f5f5f7;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,sans-serif;box-sizing:border-box;pointer-events:auto !important;">' +
        '<button id="pz-modal-close" type="button" style="position:absolute;top:20px;right:20px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);color:#f5f5f7;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:18px;line-height:1;display:flex;align-items:center;justify-content:center;transition:all 0.2s;pointer-events:auto !important;z-index:1000;" onmouseover="this.style.background=\'rgba(255,255,255,0.18)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">&times;</button>' +
        
        '<div style="display:flex;align-items:center;gap:16px;margin-bottom:20px;">' +
          '<div style="width:52px;height:52px;border-radius:50%;background:#f5f5f7;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;color:#0c0c0e;flex-shrink:0;">P</div>' +
          '<div>' +
            '<h3 style="margin:0 0 3px;font-size:22px;font-weight:700;color:#f5f5f7;letter-spacing:-0.02em;">Paramveer Sinh Zala</h3>' +
            '<p style="margin:0;font-size:13px;color:#a1a1aa;">Full-Stack Developer &bull; Creator of OmniRip</p>' +
          '</div>' +
        '</div>' +

        '<p style="font-size:14px;line-height:1.65;color:#d4d4d8;margin:0 0 24px;font-weight:400;">' +
          'Extracted and replicated this complete <strong style="color:#f5f5f7;">Shopify Editions Winter &rsquo;26</strong> website &mdash; including 19 3D GLB models, Rive animations, KTX2 GPU textures, and 150+ feature sections &mdash; <strong style="color:#f5f5f7;">with just one prompt</strong> using OmniRip in ~20 minutes.' +
        '</p>' +

        '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:26px;">' +
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

        '<div style="display:flex;flex-direction:column;gap:12px;pointer-events:auto !important;">' +
          '<a id="pz-btn-linkedin" href="https://www.linkedin.com/in/paramveer-sinh-zala-601114423/" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:10px;background:#f5f5f7;color:#0c0c0e;padding:14px;border-radius:9999px;font-size:14px;font-weight:600;text-decoration:none;pointer-events:auto !important;cursor:pointer;transition:all 0.2s;" onmouseover="this.style.background=\'#e5e5e7\'" onmouseout="this.style.background=\'#f5f5f7\'">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="#0c0c0e"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>' +
            'Connect on LinkedIn' +
          '</a>' +
          '<a id="pz-btn-github" href="https://github.com/pali2410/shopyfycopy.git" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:10px;background:rgba(255,255,255,0.08);color:#f5f5f7;padding:13px;border-radius:9999px;font-size:14px;font-weight:600;text-decoration:none;border:1px solid rgba(255,255,255,0.16);pointer-events:auto !important;cursor:pointer;transition:all 0.2s;" onmouseover="this.style.background=\'rgba(255,255,255,0.16)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">' +
            '<svg width="18" height="18" viewBox="0 0 24 24" fill="#f5f5f7"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>' +
            'Open Source GitHub Repository' +
          '</a>' +
          '<a id="pz-btn-email" href="mailto:zalaparamveer13@gmail.com" style="display:flex;align-items:center;justify-content:center;gap:8px;background:transparent;color:#a1a1aa;padding:10px;border-radius:9999px;font-size:13px;font-weight:500;text-decoration:none;pointer-events:auto !important;cursor:pointer;transition:all 0.2s;" onmouseover="this.style.color=\'#f5f5f7\'" onmouseout="this.style.color=\'#a1a1aa\'">' +
            'zalaparamveer13@gmail.com' +
          '</a>' +
        '</div>' +
      '</div>';

    overlay.appendChild(dialog);
    document.body.appendChild(overlay);

    document.getElementById('pz-modal-close').addEventListener('click', function(e) {
      e.stopPropagation();
      closeModal();
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

    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) closeModal();
    });
  }

  function openModal() {
    injectModal();
    var overlay = document.getElementById('pz-modal-overlay');
    if (!overlay) return;
    overlay.style.display = 'flex';
    setTimeout(function() {
      overlay.style.opacity = '1';
    }, 10);
  }

  function closeModal() {
    var overlay = document.getElementById('pz-modal-overlay');
    if (!overlay) return;
    overlay.style.opacity = '0';
    setTimeout(function() {
      overlay.style.display = 'none';
    }, 250);
  }

  /* Handle Top Nav Pill Click */
  document.addEventListener('click', function (e) {
    var el = e.target;
    
    // Ignore clicks inside the modal popup
    if (el && (el.closest('#pz-modal-dialog') || el.closest('#pz-modal-overlay'))) {
      return; 
    }

    while (el && el !== document.body && el !== document.documentElement) {
      if (
        el.id === 'pz-nav-pill' ||
        (el.className && typeof el.className === 'string' && el.className.indexOf('pz-trigger') !== -1)
      ) {
        e.preventDefault();
        e.stopPropagation();
        openModal();
        return false;
      }
      el = el.parentElement;
    }
  }, true);

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
  });

  function run() {
    injectTopNavPill();
    injectModal();
  }

  var observer = new MutationObserver(run);
  observer.observe(document.body, { childList: true, subtree: true });

  window.addEventListener('load', function() {
    run();
    setTimeout(run, 300);
    setTimeout(run, 1000);
    setTimeout(run, 2500);
  });
})();
</script>"""

if '</body>' in content:
    content = content.replace('</body>', TOP_NAV_ONLY_SCRIPT + '\n</body>', 1)
    print('Injected clean top nav script before </body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html size:', len(content))
print('SUCCESS!')
