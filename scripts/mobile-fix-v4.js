/* Mobile Nuclear Fix v4 - No syntax errors, no template literals */
(function() {
  var ua = navigator.userAgent || '';
  var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(ua) ||
                 (window.matchMedia && window.matchMedia('(max-width: 900px)').matches);

  if (!isMobile) return;

  console.log('[Mobile Fix v4] Applying fixes...');

  /* 1. Suppress Rive animation errors */
  var _w = console.warn;
  console.warn = function() {
    var m = String(arguments[0] || '');
    if (m.indexOf('State Machine') !== -1 || m.indexOf('Animation with name') !== -1) return;
    _w.apply(console, arguments);
  };

  /* 2. Throttle MessageChannel (React 18 scheduler infinite loop) */
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
              /* Blocked - retry later */
              setTimeout(function() { if (_handler) _handler(evt); }, 200);
              return;
            }
            if (totalMsg > 600) {
              totalMsg = 0;
              blockUntil = Date.now() + 2000;
              console.log('[Mobile Fix v4] React MessageChannel throttled for 2s');
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

  /* 3. Inject CSS !important to force content visible */
  function injectCSS() {
    if (document.getElementById('m-fix-css')) return;
    var s = document.createElement('style');
    s.id = 'm-fix-css';
    var rules = '';
    rules += '.main-wrapper{opacity:1!important;visibility:visible!important;}';
    rules += 'main{opacity:1!important;visibility:visible!important;}';
    rules += 'section{opacity:1!important;visibility:visible!important;pointer-events:auto!important;}';
    rules += 'h1,h2,h3,p,a,button{opacity:1!important;visibility:visible!important;}';
    rules += 'canvas[data-rollout-canvas]{opacity:0!important;pointer-events:none!important;}';
    rules += 'canvas[aria-hidden="true"]{display:none!important;}';
    rules += '*{transition-duration:0.001s!important;animation-duration:0.001s!important;}';
    s.textContent = rules;
    (document.head || document.documentElement).appendChild(s);
    console.log('[Mobile Fix v4] CSS injected');
  }

  /* 4. Activate stuck sections */
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
  }

  function runFixes() { injectCSS(); activateSections(); }

  /* Run immediately if DOM ready */
  if (document.head) injectCSS();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      runFixes();
      setTimeout(runFixes, 500);
      setTimeout(runFixes, 2000);
      setTimeout(runFixes, 5000);
    });
  } else {
    runFixes();
    setTimeout(runFixes, 500);
    setTimeout(runFixes, 2000);
    setTimeout(runFixes, 5000);
  }

  window.addEventListener('load', function() {
    runFixes();
    setTimeout(runFixes, 1000);
    setTimeout(runFixes, 3000);
  });
})();
