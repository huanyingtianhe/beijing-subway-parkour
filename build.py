# Inline game.js (with lines.json from map.amap.com/subway) into page.html's game <script>,
# then write index.html and play.html: the same page as a complete standalone document
# (index.html is what static hosts such as Vercel serve at the site root).
import pathlib
root = pathlib.Path(__file__).parent
game = (root/'game.js').read_text(encoding='utf-8').replace('/*__DATA__*/', (root/'lines.json').read_text(encoding='utf-8'))
html = (root/'page.html').read_text(encoding='utf-8')
start = html.index('three.min.js"></script>') + len('three.min.js"></script>')
i = html.index('<script>', start); j = html.index('</script>', i)
html = html[:i] + '<script>\n' + game + '</script>' + html[j+len('</script>'):]
(root/'page.html').write_text(html, encoding='utf-8')
head = ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n')
for out in ('index.html', 'play.html'):
    (root/out).write_text(head + html + '\n</body>\n</html>\n', encoding='utf-8')
print('built', len(html))
