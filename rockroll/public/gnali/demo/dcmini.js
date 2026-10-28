/* dcmini: runtime minimo per pubblicare le demo .dc.html fuori da Claude Design.
   Supporta {{path}}, <sc-if value>, <sc-for list as>, on*="{{fn}}", <helmet>, class Component extends DCLogic. */
(function () {
  function get(scope, path) {
    path = path.trim();
    if (path === 'true') return true; if (path === 'false') return false;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path);
    if (/^'.*'$/.test(path)) return path.slice(1, -1);
    return path.split('.').reduce(function (o, k) { return o == null ? undefined : o[k]; }, scope);
  }
  var WHOLE = /^\s*\{\{([^}]+)\}\}\s*$/;
  function interp(str, scope) {
    return str.replace(/\{\{([^}]+)\}\}/g, function (_, p) { var v = get(scope, p); return v == null ? '' : String(v); });
  }
  function build(node, scope, out) {
    if (node.nodeType === 3) { out.appendChild(document.createTextNode(interp(node.nodeValue, scope))); return; }
    if (node.nodeType !== 1) return;
    var tag = (node.localName || node.tagName).toLowerCase();
    if (tag === 'sc-if') {
      var m = WHOLE.exec(node.getAttribute('value') || '');
      if (m && get(scope, m[1])) Array.prototype.forEach.call(node.childNodes, function (c) { build(c, scope, out); });
      return;
    }
    if (tag === 'sc-for') {
      var lm = WHOLE.exec(node.getAttribute('list') || ''); var as = node.getAttribute('as') || 'item';
      var list = lm ? get(scope, lm[1]) : [];
      (list || []).forEach(function (item, i) {
        var s = Object.create(scope); s[as] = item; s.$index = i;
        Array.prototype.forEach.call(node.childNodes, function (c) { build(c, s, out); });
      });
      return;
    }
    var SVG = {svg:1,circle:1,line:1,path:1,rect:1,polyline:1,polygon:1,g:1,ellipse:1};
    var el = (SVG[tag] || node.namespaceURI === 'http://www.w3.org/2000/svg') ? document.createElementNS('http://www.w3.org/2000/svg', tag) : document.createElement(tag);
    for (var i = 0; i < node.attributes.length; i++) {
      var a = node.attributes[i], name = a.name, val = a.value;
      if (/^hint-/.test(name)) continue;
      var w = WHOLE.exec(val);
      if (/^on[a-z]+$/i.test(name) && w) {
        var fn = get(scope, w[1]);
        if (typeof fn === 'function') {
          var ev = name.slice(2).toLowerCase();
          if (ev === 'change' && (tag === 'input' || tag === 'textarea')) ev = 'input';
          el.addEventListener(ev, (function (f) { return function (e) { if (window.__dcRestoring) return; f(e); }; })(fn));
        }
        continue;
      }
      if (name === 'value' && (tag === 'input' || tag === 'textarea')) { el.value = interp(val, scope); el.setAttribute('value', el.value); continue; }
      el.setAttribute(name, interp(val, scope));
    }
    if (tag === 'form') el.addEventListener('submit', function (e) { e.preventDefault(); });
    Array.prototype.forEach.call(node.childNodes, function (c) { build(c, scope, el); });
    out.appendChild(el);
  }
  window.DCLogic = function () { this.props = {}; this.state = null; };
  window.DCLogic.prototype.setState = function (o) { this.state = Object.assign({}, this.state, typeof o === 'function' ? o(this.state) : o); window.__dcRender(); };
  window.DCLogic.prototype.forceUpdate = function () { window.__dcRender(); };
  document.addEventListener('DOMContentLoaded', function () {
    var src = document.querySelector('script[type="text/x-dc-tpl"]'); if (!src) return;
    var xml = new DOMParser().parseFromString('<root xmlns="http://www.w3.org/1999/xhtml">' + src.textContent + '</root>', 'application/xml');
    if (xml.getElementsByTagName('parsererror').length) { document.body.textContent = 'Errore nel template: ' + xml.getElementsByTagName('parsererror')[0].textContent; return; }
    var tpl = xml.documentElement;
    var helmet = tpl.getElementsByTagName('helmet')[0];
    if (helmet) { Array.prototype.slice.call(helmet.childNodes).forEach(function (c) { var f = document.createDocumentFragment(); build(c, {}, f); while (f.firstChild) document.head.appendChild(f.firstChild); }); helmet.parentNode.removeChild(helmet); }
    var x = document.createElement('div');
    document.body.insertBefore(x, src);
    var code = document.querySelector('script[data-dc-script]').textContent;
    var Comp = new Function(code + '\n;return Component;')();
    var inst = new Comp(); if (!inst.props) inst.props = {};
    var root = document.createElement('div'); root.id = 'dc-root'; x.replaceWith(root);
    window.__dcRender = function () {
      var act = document.activeElement, key = null, caret = null;
      if (act && root.contains(act) && (act.tagName === 'INPUT' || act.tagName === 'TEXTAREA')) {
        key = Array.prototype.indexOf.call(root.querySelectorAll('input,textarea'), act); try { caret = act.selectionStart; } catch (e) {}
      }
      var vals = inst.renderVals(); var frag = document.createDocumentFragment();
      Array.prototype.forEach.call(tpl.childNodes, function (c) { build(c, vals, frag); });
      root.innerHTML = ''; root.appendChild(frag);
      if (key != null && key >= 0) { var n = root.querySelectorAll('input,textarea')[key]; if (n) { window.__dcRestoring = true; n.focus(); window.__dcRestoring = false; try { if (caret != null) n.setSelectionRange(caret, caret); } catch (e) {} } }
    };
    window.__dcRender();
  });
})();
