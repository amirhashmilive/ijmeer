/* ============================================================
   IJMEER — components.js  (v3 — Premium Edition)
   Injects header + footer into all pages.
   ============================================================ */
(function () {
  'use strict';

  const S = 'https://docs.google.com/forms/d/e/1FAIpQLSeLAeEVTKRf18Qks4Z_QXDYWUPiNAZirDUKz_TWLBIiiMMPtw/viewform?usp=publish-editor';



  /* ────────────────────────────────────────────────────────────
     HEADER
  ──────────────────────────────────────────────────────────── */
  const HEADER = `
<header class="site-header" id="site-header" role="banner">
  <div class="container header-inner">
    <a href="index.html" class="brand" aria-label="IJMEER Home">
      <div class="brand-mark" aria-hidden="true">IJ</div>
      <div class="brand-text">
        <span class="brand-name">IJMEER</span>
        <span class="brand-sub">Open Access Journal</span>
      </div>
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Main navigation">
      <div class="nav-item"><a href="journal.html" class="nav-link">Journal</a></div>
      <div class="nav-item"><a href="editorial-board.html" class="nav-link">Editorial Board</a></div>
      <div class="nav-item"><a href="authors.html" class="nav-link">Authors</a></div>
      <div class="nav-item"><a href="peer-review.html" class="nav-link">Peer Review</a></div>
      <div class="nav-item transition-all"><a href="archive.html" class="nav-link">Archives</a></div>
      <div class="nav-item"><a href="citations.html" class="nav-link">Citations</a></div>
      <div class="nav-item"><a href="contact.html" class="nav-link">Contact</a></div>
    </nav>

    <div class="header-actions">
      <a href="${S}" class="btn-submit desktop-only" target="_blank" rel="noopener" id="nav-submit-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
        Submit
      </a>
      <button class="mobile-menu-toggle" aria-label="Open menu">☰</button>
    </div>
  </div>

  <div class="overlay"></div>

  <nav class="mobile-nav">
    <button class="close-menu" aria-label="Close menu">&times;</button>
    <ul>
      <li><a href="journal.html">Journal</a></li>
      <li><a href="editorial-board.html">Editorial Board</a></li>
      <li><a href="authors.html">Authors</a></li>
      <li><a href="peer-review.html">Peer Review</a></li>
      <li><a href="archive.html">Archives</a></li>
      <li><a href="citations.html">Citations</a></li>
      <li style="margin-top: 30px;"><a href="${S}" class="submit-btn" target="_blank" rel="noopener">Submit Manuscript</a></li>
    </ul>
  </nav>
</header>`;

  /* ────────────────────────────────────────────────────────────
     FOOTER
  ──────────────────────────────────────────────────────────── */
  const FOOTER = `
<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <!-- Brand column -->
      <div class="footer-brand">
        <a href="index.html" class="brand" style="margin-bottom:16px;" aria-label="IJMEER Home">
          <div class="brand-mark">IJ</div>
          <div class="brand-text">
            <span class="brand-name">IJMEER</span>
            <span class="brand-sub">Open Access Journal</span>
          </div>
        </a>
        <p class="footer-desc">INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY EXPLICATION AND EMERGING RESEARCH (IJMEER).</p>
        <div style="margin-top:20px;">
          <div style="font-size:0.82rem;font-weight:700;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">
            Publisher: <a href="https://www.meerfoundation.co.in/" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">Meer Foundation</a>
          </div>
          <div style="font-size:0.82rem;color:rgba(255,255,255,0.7);line-height:1.7;">
            Address: House No. 103, Housing Board Colony, Hatkeshar, Dhamtari – 493773, Chhattisgarh, India
          </div>
        </div>
        <div style="margin-top:16px;">
          <div style="font-size:0.72rem;font-weight:700;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">Contact IJMEER</div>
          <div style="font-size:0.82rem;color:rgba(255,255,255,0.7);line-height:1.7;">
            Email: <a href="mailto:ijmeerj@gmail.com" style="color:inherit;">ijmeerj@gmail.com</a><br>
            Email: <a href="mailto:editor@ijmeer.com" style="color:inherit;">editor@ijmeer.com</a>
          </div>
        </div>
        <div class="social-links" style="margin-top:36px;" aria-label="Social media links">
          <a href="https://facebook.com/ijmeerj" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="IJMEER on Facebook">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
          <a href="https://instagram.com/ijmeerj" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="IJMEER on Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          </a>
          <a href="https://twitter.com/ijmeerj" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="IJMEER on X (Twitter)">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
          </a>
          <a href="https://linkedin.com/company/ijmeerj" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="IJMEER on LinkedIn">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
          </a>
          <a href="https://youtube.com/@ijmeerj" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="IJMEER on YouTube">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon fill="white" points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02"/></svg>
          </a>
          <a href="https://chat.whatsapp.com/EpVXdvvrbKc9HlyXKDfftB" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Join IJMEER WhatsApp Community">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a6.98 6.98 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.09.537 4.056 1.475 5.768L0 24l6.395-1.682A11.942 11.942 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.802 9.802 0 0 1-5.092-1.424l-.364-.216-3.78.994.99-3.696-.236-.38A9.808 9.808 0 0 1 2.182 12c0-5.42 4.398-9.818 9.818-9.818 5.42 0 9.818 4.398 9.818 9.818 0 5.42-4.398 9.818-9.818 9.818z"/></svg>
          </a>
        </div>
      </div>

      <!-- Journal column -->
      <div>
        <h3 class="footer-head">Journal</h3>
        <nav class="footer-links" aria-label="Journal links">
          <a href="journal.html">About IJMEER</a>
          <a href="editorial-board.html">Editorial Board</a>
          <a href="journal.html#book-reviews">Book Reviews</a>
          <a href="journal.html#indexing">Indexing</a>
          <a href="archive.html">Archives</a>
          <a href="citations.html">Articles &amp; Citations</a>
          <a href="library.html">Library Access</a>
        </nav>
      </div>

      <!-- Author Resources column -->
      <div>
        <h3 class="footer-head">Authors</h3>
        <nav class="footer-links" aria-label="Author resources">
          <a href="${S}" target="_blank" rel="noopener">Submit Paper</a>
          <a href="authors.html">Author Instructions</a>
          <a href="authors.html#preparing">Preparing Materials</a>
          <a href="authors.html#fees">Fees &amp; Pricing</a>
          <a href="authors.html#agreement">Publishing Agreement</a>
          <a href="authors.html#impact">Post-Publication</a>
        </nav>
      </div>

      <!-- Policies column -->
      <div>
        <h3 class="footer-head">Policies &amp; Contact</h3>
        <nav class="footer-links" aria-label="Policy and contact links">
          <a href="open-access-options.html">Open Access</a>
          <a href="publishing-ethics.html">Publishing Ethics</a>
          <a href="research-transparency.html">Transparency</a>
          <a href="rights-permissions.html">Rights &amp; Permissions</a>
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="contact.html">Contact Us</a>
        </nav>
      </div>
    </div>

    <div class="footer-bottom">
      <p>
        &copy; <span data-year></span> IJMEER. Published by
        <a href="https://www.meerfoundation.co.in/" target="_blank" rel="noopener noreferrer">Meer Foundation</a>.
        All rights reserved. &nbsp;|&nbsp; ISSN (Print): XXXX-XXXX &nbsp;|&nbsp; ISSN (Online): XXXX-XXXX &nbsp;|&nbsp; Since 2025
      </p>
    </div>
  </div>
</footer>
<div id="toast-container" class="toast-container" aria-live="polite" aria-atomic="false"></div>
<button id="scroll-top" aria-label="Scroll to top of page" title="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="18 15 12 9 6 15"/></svg>
</button>`;

  /* ────────────────────────────────────────────────────────────
     INJECT HTML
  ──────────────────────────────────────────────────────────── */
  function inject(id, html, position = 'before') {
    const placeholder = document.getElementById(id);
    if (!placeholder) return;
    const tmp = document.createElement('div');
    tmp.innerHTML = html;
    const parent = placeholder.parentNode;
    while (tmp.firstChild) {
      if (position === 'before') parent.insertBefore(tmp.firstChild, placeholder);
      else parent.insertBefore(tmp.firstChild, placeholder.nextSibling);
    }
    placeholder.remove();
  }

  inject('site-header-inject', HEADER);
  inject('site-footer-inject', FOOTER);

  // Notify core.js that the header is now in the DOM so it can bind mobile menu
  document.dispatchEvent(new CustomEvent('headerInjected'));

  /* ────────────────────────────────────────────────────────────
     TOAST NOTIFICATION UTILITY
  ──────────────────────────────────────────────────────────── */
  window.showToast = function(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const icon = type === 'success'
      ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>'
      : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>';
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.style.borderLeftColor = type === 'success' ? 'var(--emerald)' : 'var(--gold)';
    toast.innerHTML = `${icon}<span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
  };

})();
