/* Mobile Fix v6 - Clean, Non-Destructive Mobile Helper */
(function() {
  var ua = navigator.userAgent || '';
  var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(ua) ||
                 (window.matchMedia && window.matchMedia('(max-width: 900px)').matches);

  if (!isMobile) return;

  console.log('[Mobile Fix v6] Initialized');

  /* 1. Suppress Rive state machine warnings on mobile */
  var _origWarn = console.warn;
  console.warn = function() {
    var m = String(arguments[0] || '');
    if (m.indexOf('State Machine') !== -1 || m.indexOf('Animation with name') !== -1) return;
    _origWarn.apply(console, arguments);
  };

  /* 2. Surgical CSS for mobile layout visibility */
  function injectCSS() {
    if (document.getElementById('m-fix-v6')) return;
    var s = document.createElement('style');
    s.id = 'm-fix-v6';
    s.textContent =
      '.main-wrapper{opacity:1!important;visibility:visible!important;pointer-events:auto!important;}' +
      'main{opacity:1!important;visibility:visible!important;}' +
      'section{opacity:1!important;visibility:visible!important;}' +
      'section h2{opacity:1!important;visibility:visible!important;color:inherit!important;}' +
      'section h3{opacity:1!important;visibility:visible!important;}' +
      'section p{opacity:1!important;visibility:visible!important;color:inherit!important;}' +
      'section span{opacity:1!important;visibility:visible!important;}' +
      '.safe-min-h-70-svh{opacity:1!important;visibility:visible!important;}' +
      '.narrative-1{opacity:1!important;visibility:visible!important;}' +
      'canvas[data-rollout-canvas]{opacity:1!important;}' +
      'section img{opacity:1!important;visibility:visible!important;}' +
      'section .pointer-events-auto{pointer-events:auto!important;}' +
      '.animate-show-media{animation:none!important;opacity:1!important;}' +
      '.text-light{color:#ffffff!important;}' +
      '.text-dark{color:#000000!important;}' +
      '.skill-tag{opacity:1!important;visibility:visible!important;}';
    (document.head || document.documentElement).appendChild(s);
  }

  /* 3. Activate lazy content and stuck sections */
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
    var canvases = document.querySelectorAll('canvas[data-rollout-canvas]');
    for (var k = 0; k < canvases.length; k++) {
      canvases[k].style.opacity = '1';
    }
  }

  function runFixes() {
    injectCSS();
    activateSections();
  }

  if (document.head) injectCSS();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      runFixes();
      setTimeout(runFixes, 800);
      setTimeout(runFixes, 2500);
    });
  } else {
    runFixes();
    setTimeout(runFixes, 800);
    setTimeout(runFixes, 2500);
  }
})();
