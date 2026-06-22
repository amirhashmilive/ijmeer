"""
Add copy-to-clipboard buttons next to institutional email addresses
on editorial-board.html and editorial-portfolio.html.
"""

import re

BASE = r"C:\Users\hashm\Desktop\Projects\Workplace IJMEER"

# ─── Shared CSS ──────────────────────────────────────────────────────────────
COPY_CSS = """
    /* ── Email copy button ── */
    .email-copy-wrap {
      display: inline-flex; align-items: center; gap: 5px;
    }
    .copy-email-btn {
      display: inline-flex; align-items: center; justify-content: center;
      width: 22px; height: 22px;
      background: rgba(37,99,235,0.08);
      border: 1px solid rgba(37,99,235,0.2);
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px;
      color: var(--blue, #2563eb);
      padding: 0;
      line-height: 1;
      position: relative;
      transition: background 0.15s, border-color 0.15s;
      vertical-align: middle;
    }
    .copy-email-btn:hover {
      background: rgba(37,99,235,0.15);
      border-color: rgba(37,99,235,0.4);
    }
    .copy-email-btn .copy-tip {
      visibility: hidden; opacity: 0;
      position: absolute; bottom: calc(100% + 5px); left: 50%;
      transform: translateX(-50%);
      background: #1e293b; color: #fff;
      font-size: 10px; font-family: sans-serif; font-weight: 600;
      white-space: nowrap;
      padding: 2px 7px; border-radius: 3px;
      pointer-events: none;
      transition: opacity 0.15s;
    }
    .copy-email-btn.copied .copy-tip {
      visibility: visible; opacity: 1;
    }"""

# ─── Shared JS ───────────────────────────────────────────────────────────────
COPY_JS = """<script>
(function(){
  document.querySelectorAll('.copy-email-btn').forEach(function(btn){
    btn.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      var email = btn.getAttribute('data-email');
      if (!email) return;
      navigator.clipboard.writeText(email).then(function(){
        btn.classList.add('copied');
        setTimeout(function(){ btn.classList.remove('copied'); }, 1800);
      }).catch(function(){
        var ta = document.createElement('textarea');
        ta.value = email; ta.style.position='fixed'; ta.style.opacity='0';
        document.body.appendChild(ta); ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        btn.classList.add('copied');
        setTimeout(function(){ btn.classList.remove('copied'); }, 1800);
      });
    });
  });
})();
</script>"""

# ─── Copy button HTML ─────────────────────────────────────────────────────────
def copy_btn(email):
    return (f'<button class="copy-email-btn" data-email="{email}" '
            f'aria-label="Copy {email}" title="Copy email">'
            f'&#x1F4CB;<span class="copy-tip">Copied!</span></button>')

# ═══════════════════════════════════════════════════════════════════════════════
# FILE 1: editorial-board.html
# ═══════════════════════════════════════════════════════════════════════════════
path_board = BASE + r"\editorial-board.html"
with open(path_board, 'r', encoding='utf-8') as f:
    content = f.read()

# 1a. Inject CSS before closing </style> in the page-specific <style> block
css_target = '  </style>'
assert css_target in content, "CSS target not found in editorial-board.html"
content = content.replace(css_target, COPY_CSS + '\n  </style>', 1)

# 1b. Wrap each mailto anchor with email-copy-wrap + add copy button
#     Pattern: <a href="mailto:EMAIL">EMAIL</a>
def wrap_board_email(m):
    email = m.group(1)
    return (f'<span class="email-copy-wrap">'
            f'<a href="mailto:{email}">{email}</a>'
            f'{copy_btn(email)}</span>')

content = re.sub(
    r'<a href="mailto:([^"]+)">\1</a>',
    wrap_board_email,
    content
)

# 1c. Inject JS just before </body>
content = content.replace('</body>', COPY_JS + '\n</body>', 1)

with open(path_board, 'w', encoding='utf-8') as f:
    f.write(content)
print("[OK] editorial-board.html updated")

# ═══════════════════════════════════════════════════════════════════════════════
# FILE 2: editorial-portfolio.html
# ═══════════════════════════════════════════════════════════════════════════════
path_port = BASE + r"\editorial-portfolio.html"
with open(path_port, 'r', encoding='utf-8') as f:
    content = f.read()

# 2a. Inject CSS — find the last </style> inside <head>
#     The portfolio has a large <style> block; append before its closing tag
css_target = '  </style>\n</head>'
assert css_target in content, "CSS target not found in editorial-portfolio.html"
content = content.replace(css_target, COPY_CSS + '\n  </style>\n</head>', 1)

# 2b. For portfolio, email cards look like:
#     <a href="mailto:EMAIL" class="profile-link-card">
#       <div class="plc-icon" ...>✉️</div>
#       <div>
#         <div class="plc-label">Institutional Email</div>
#         <div class="plc-value">EMAIL</div>
#       </div>
#     </a>
# Strategy: add a copy button AFTER the closing </a> of the email card,
# wrapped together in a positioned container.

def wrap_portfolio_email(m):
    email = m.group(1)
    full_card = m.group(0)
    return (
        f'<div class="email-copy-wrap" style="display:flex;align-items:center;gap:6px;">'
        f'{full_card}'
        f'{copy_btn(email)}'
        f'</div>'
    )

# Match the entire mailto profile-link-card anchor for institutional emails
pattern = (
    r'<a href="mailto:([^"]+)" class="profile-link-card">'
    r'\s*<div class="plc-icon"[^>]*>✉️</div>'
    r'\s*<div>'
    r'\s*<div class="plc-label">Institutional Email</div>'
    r'\s*<div class="plc-value">[^<]+</div>'
    r'\s*</div>'
    r'\s*</a>'
)

content = re.sub(pattern, wrap_portfolio_email, content, flags=re.DOTALL)

# 2c. Inject JS before </body>
content = content.replace('</body>', COPY_JS + '\n</body>', 1)

with open(path_port, 'w', encoding='utf-8') as f:
    f.write(content)
print("[OK] editorial-portfolio.html updated")
print("\nDone. Copy buttons added to both files.")
