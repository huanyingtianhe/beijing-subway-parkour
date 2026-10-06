# Inline game.js (with lines.json from map.amap.com/subway) into index.html's game <script>,
# then write play.html: the same page as a complete standalone document for opening straight from disk.
import pathlib
root = pathlib.Path(__file__).parent
game = (root/'game.js').read_text(encoding='utf-8').replace('/*__DATA__*/', (root/'lines.json').read_text(encoding='utf-8'))
html = (root/'index.html').read_text(encoding='utf-8')
start = html.index('three.min.js"></script>') + len('three.min.js"></script>')
i = html.index('<script>', start); j = html.index('</script>', i)
html = html[:i] + '<script>\n' + game + '</script>' + html[j+len('</script>'):]
(root/'index.html').write_text(html, encoding='utf-8')
head = ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n')
(root/'play.html').write_text(head + html + '\n</body>\n</html>\n', encoding='utf-8')
print('built', len(html))
