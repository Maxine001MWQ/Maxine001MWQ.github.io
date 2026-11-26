"""Validate built pages, local links, bilingual pairs and feeds using only Python stdlib."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET
import re
import os

site_url = urlparse(os.environ.get('CI_PAGES_URL', 'https://maxine001mwq.github.io'))
baseurl = site_url.path.rstrip('/')

root = Path('_site')
assert root.is_dir(), 'Build the Jekyll site first.'

class Page(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.file, self.lang, self.canonical = file, None, None
        self.links, self.alternates, self.ids = [], {}, set()
        self.h1 = 0
        self.redirect = False
        self.feed(file.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'h1': self.h1 += 1
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh': self.redirect = True
        if a.get('id'):
            assert a['id'] not in self.ids, f'Duplicate ID: {self.file}: {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a['href']
        if tag == 'link' and a.get('hreflang'): self.alternates[a['hreflang']] = a['href']
        for attr in ('href', 'src'):
            if a.get(attr): self.links.append(a[attr])

def resolve(url, source=None):
    parts = urlparse(url)
    if parts.scheme and parts.scheme not in ('http', 'https'): return None
    if parts.netloc and parts.netloc != site_url.netloc: return None
    path = unquote(parts.path)
    if baseurl and path.startswith('/'):
        assert path == baseurl or path.startswith(baseurl + '/'), f'Link outside site base path: {url}'
        path = path[len(baseurl):] or '/'
    target = root / path.lstrip('/') if path.startswith('/') else (source.parent / path if source else root / path)
    if not path and source: target = source
    if target.is_dir(): target = target / 'index.html'
    return target

verification_files = set()
for source in Path('.').glob('google*.html'):
    if re.fullmatch(r'google[0-9a-f]+\.html', source.name):
        built = root / source.name
        assert built.exists(), f'Missing Google verification file: {source}'
        assert source.read_text().strip() == f'google-site-verification: {source.name}', f'Invalid verification content: {source}'
        assert built.read_bytes() == source.read_bytes(), f'Changed verification file: {source}'
        verification_files.add(built)
pages = {file: Page(file) for file in root.rglob('*.html') if file not in verification_files}
legacy = root / 'how-to-turn-scattered-career-notes-into-a-resume-with-notegpt/index.html'
assert legacy.exists(), 'Missing legacy English article URL'
pages[legacy] = Page(legacy)
for file, page in pages.items():
    assert page.lang in ('zh-CN', 'en'), f'Missing language: {file}'
    assert page.canonical, f'Missing canonical: {file}'
    if page.redirect:
        target = resolve(page.canonical)
        assert target in pages and not pages[target].redirect, f'Invalid or chained redirect: {file}'
    elif '/zh/' in str(file) or '/en/' in str(file):
        assert page.h1 == 1, f'Expected one main heading: {file}'
    for link in page.links:
        target = resolve(link, file)
        if target is None: continue
        assert target.exists(), f'Broken local link: {file}: {link}'
        fragment = unquote(urlparse(link).fragment)
        if fragment and target in pages:
            assert fragment in pages[target].ids, f'Broken anchor: {file}: {link}'
    for lang, url in page.alternates.items():
        target = resolve(url)
        assert target in pages and pages[target].lang == lang, f'Wrong alternate: {file}: {url}'
        assert pages[target].alternates.get(page.lang) == page.canonical, f'Non-reciprocal alternate: {file}'
for lang in ('zh', 'en'):
    feed = ET.parse(root / lang / 'feed.xml')
    for link in feed.findall('./channel/item/link'):
        assert f'/{lang}/posts/' in link.text and resolve(link.text).exists(), f'Wrong RSS language: {link.text}'
sitemap = ET.parse(root / 'sitemap.xml')
for loc in sitemap.findall('.//{*}loc'):
    assert resolve(loc.text).exists(), f'Broken sitemap URL: {loc.text}'
assert not (root / 'skills').exists() and not (root / 'AGENTS.md').exists()
print(f'Validated {len(pages)} pages: local links, anchors, reciprocal language links, RSS, sitemap and excluded instructions.')
