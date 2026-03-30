# Run this script in your project folder to add Privacy/Terms links to index.html and welcome.html
# Usage: python3 add_footer.py

import os

FOOTER = '''
<div style="text-align:center;padding:24px 20px;border-top:1px solid rgba(255,255,255,0.07);margin-top:40px;font-size:0.82rem;color:#9aa3b8;font-family:Barlow,sans-serif;">
  <a href="https://go.oneserv.app/privacy.html" style="color:#4f80ff;text-decoration:none;margin:0 12px;">Privacy Policy</a>
  <span style="opacity:0.3;"> · </span>
  <a href="https://go.oneserv.app/terms.html" style="color:#4f80ff;text-decoration:none;margin:0 12px;">Terms of Service</a>
  <span style="opacity:0.3;"> · </span>
  <span style="margin:0 12px;">© 2026 Consolidated Assets LLC d/b/a OneServ</span>
</div>
'''

files = ['index.html', 'welcome.html', 'thank-you.html', 'demo.html']

for filename in files:
    if not os.path.exists(filename):
        print(f"Skipping {filename} — not found")
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'Privacy Policy' in content:
        print(f"Skipping {filename} — footer already present")
        continue
    updated = content.replace('</body>', FOOTER + '</body>')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"✓ Footer added to {filename}")

print("\nDone. Push updated files to GitHub.")
