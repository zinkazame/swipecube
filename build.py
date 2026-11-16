#!/usr/bin/env python3
"""Builds the two outputs from src/game.html:
   www/index.html  - standalone, Three.js inlined, works offline (used by the Android app)
   dist/artifact.html - page body for the hosted web version (Three.js from cdnjs)
"""
import pathlib

root = pathlib.Path(__file__).parent
src = (root / "src" / "game.html").read_text()
three = (root / "src" / "three.min.js").read_text()
assert "</script" not in three.lower()

marker = "<script>\n(function () {"
i = src.index(marker)
head_part, rest = src[: src.index('<div id="app">')], src[src.index('<div id="app">'):]
body_before, game_js = src[src.index('<div id="app">'): i], src[i:]

standalone = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">\n'
    '<meta name="theme-color" content="#0e1117">\n'
    + head_part + "</head>\n<body>\n" + body_before
    + "<script>" + three + "</script>\n" + game_js + "\n</body>\n</html>\n"
)
(root / "www").mkdir(exist_ok=True)
(root / "www" / "index.html").write_text(standalone)

cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n'
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "artifact.html").write_text(head_part + body_before + cdn + game_js)
print("built", len(standalone) // 1024, "KB standalone")
