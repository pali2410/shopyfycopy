/* Mobile Fix v5 - Surgical fixes: scroll + images + text + section content */
(function() {
  var ua = navigator.userAgent || '';
  var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(ua) ||
                 (window.matchMedia && window.matchMedia('(max-width: 900px)').matches);

  if (!isMobile) return;

  console.log('[Mobile Fix v5] Applying surgical mobile fixes...');

  /* 1. Suppress Rive state machine errors that trigger React infinite loops */
  var _origWarn = console.warn;
  console.warn = function() {
    var m = String(arguments[0] || '');
    if (m.indexOf('State Machine') !== -1 || m.indexOf('Animation with name') !== -1) return;
    _origWarn.apply(console, arguments);
  };

  /* 2. Throttle MessageChannel (React 18 scheduler for infinite loop) */
  var _MC = window.MessageChannel;
  if (_MC) {
    var totalMsg = 0;
    var blockUntil = 0;
    window.MessageChannel = function() {
      var mc = new _MC();
      var _handler = null;
      Object.defineProperty(mc.port1, 'onmessage', {
        set: function(fn) {
          _handler = function(evt) {
            totalMsg++;
            var now = Date.now();
            if (now < blockUntil) {
              setTimeout(function() { if (_handler) _handler(evt); }, 200);
              return;
            }
            if (totalMsg > 600) {
              totalMsg = 0;
              blockUntil = Date.now() + 2000;
              console.log('[Mobile Fix v5] React scheduler throttled');
            }
            fn.call(mc.port1, evt);
          };
        },
        get: function() { return _handler; },
        configurable: true
      });
      return mc;
    };
  }

  /* 3. Inject SURGICAL CSS - only fix what is actually invisible, keep 3D canvases working */
  function injectCSS() {
    if (document.getElementById('m-fix-v5')) return;
    var s = document.createElement('style');
    s.id = 'm-fix-v5';
    s.textContent =
      /* Force main wrapper and sections visible */
      '.main-wrapper{opacity:1!important;visibility:visible!important;pointer-events:auto!important;}' +
      'main{opacity:1!important;visibility:visible!important;}' +
      'section{opacity:1!important;visibility:visible!important;}' +
      /* Section text content always visible */
      'section h2{opacity:1!important;visibility:visible!important;color:inherit!important;}' +
      'section h3{opacity:1!important;visibility:visible!important;}' +
      'section p{opacity:1!important;visibility:visible!important;color:inherit!important;}' +
      'section span{opacity:1!important;visibility:visible!important;}' +
      /* Force section text panels (sidebars) visible */
      '.safe-min-h-70-svh{opacity:1!important;visibility:visible!important;}' +
      '.narrative-1{opacity:1!important;visibility:visible!important;}' +
      /* Force rollout canvas to show (remove initial opacity-0) */
      'canvas[data-rollout-canvas]{opacity:1!important;}' +
      /* Force lazy images to load eagerly on mobile */
      'section img{opacity:1!important;visibility:visible!important;}' +
      /* Allow scrolling - enable pointer events where needed */
      'section .pointer-events-auto{pointer-events:auto!important;}' +
      /* Show animate-show-media elements immediately */
      '.animate-show-media{animation:none!important;opacity:1!important;}' +
      /* Text colors for dark sections */
      '.text-light{color:#ffffff!important;}' +
      '.text-dark{color:#000000!important;}' +
      /* Make skill tags visible */
      '.skill-tag{opacity:1!important;visibility:visible!important;}';
    (document.head || document.documentElement).appendChild(s);
    console.log('[Mobile Fix v5] CSS injected');
  }

  /* 4. Force all lazy images to load eagerly */
  function forceLoadImages() {
    var imgs = document.querySelectorAll('img[loading="lazy"]');
    for (var i = 0; i < imgs.length; i++) {
      imgs[i].loading = 'eager';
      if (imgs[i].dataset.src) {
        imgs[i].src = imgs[i].dataset.src;
      }
    }
  }

  /* 5. Activate all stuck sections */
  function activateSections() {
    var stuck = document.querySelectorAll('[data-initiated="false"]');
    for (var i = 0; i < stuck.length; i++) {
      stuck[i].setAttribute('data-initiated', 'true');
      stuck[i].setAttribute('data-scrolled', 'true');
      stuck[i].setAttribute('data-sidebar-ready', 'true');
      stuck[i].setAttribute('data-sidebar-loaded', 'true');
    }
    var idle = document.querySelectorAll('[data-state="idle"]');
    for (var j = 0; j < idle.length; j++) {
      idle[j].setAttribute('data-state', 'active');
    }
    /* Show rollout canvas */
    var canvases = document.querySelectorAll('canvas[data-rollout-canvas]');
    for (var k = 0; k < canvases.length; k++) {
      canvases[k].style.opacity = '1';
    }
  }

  function runFixes() {
    injectCSS();
    activateSections();
    forceLoadImages();
  }

  /* Inject CSS immediately */
  if (document.head) injectCSS();

  /* Run on DOMContentLoaded */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      runFixes();
      setTimeout(runFixes, 500);
      setTimeout(runFixes, 1500);
      setTimeout(runFixes, 3500);
    });
  } else {
    runFixes();
    setTimeout(runFixes, 500);
    setTimeout(runFixes, 1500);
    setTimeout(runFixes, 3500);
  }

  window.addEventListener('load', function() {
    runFixes();
    setTimeout(runFixes, 1000);
    setTimeout(runFixes, 3000);
  });

})();
