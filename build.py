# -*- coding: utf-8 -*-
"""
RFID 车管信息页批量生成脚本
读取 data.json，批量生成每个车牌的独立网页 + 站点首页索引。
用法：python build.py
"""
import json
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, "data.json")
TEMPLATE_FILE = os.path.join(BASE, "template.html")
PAGES_DIR = os.path.join(BASE, "pages")
INDEX_FILE = os.path.join(BASE, "index.html")


def load_template():
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return f.read()


def render(tpl, item):
    html = tpl
    for key in ("车牌", "姓名", "入网时间", "防伪文字"):
        html = html.replace("{{%s}}" % key, str(item.get(key, "")))
    return html


def build_pages(items):
    if os.path.exists(PAGES_DIR):
        shutil.rmtree(PAGES_DIR)
    os.makedirs(PAGES_DIR, exist_ok=True)
    # 防伪底图复制到 pages/ 根，供每个子页面通过 ../a1.png 引用
    bg_src = os.path.join(BASE, "a1.png")
    if os.path.exists(bg_src):
        shutil.copy(bg_src, os.path.join(PAGES_DIR, "a1.png"))
    tpl = load_template()
    for item in items:
        folder = item.get("目录") or item.get("车牌")
        if not folder:
            print("[跳过] 缺少目录字段:", item)
            continue
        d = os.path.join(PAGES_DIR, folder)
        os.makedirs(d, exist_ok=True)
        html = render(tpl, item)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("[生成] pages/%s/index.html  <-  %s / %s" % (folder, item.get("姓名"), item.get("车牌")))


def build_index(items):
    """生成站点首页：所有车牌链接列表"""
    links = []
    for item in items:
        folder = item.get("目录") or item.get("车牌")
        links.append(
            '<li><a href="pages/%s/">%s（%s）</a></li>'
            % (folder, item.get("车牌"), item.get("姓名"))
        )
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>车管系统信息页索引</title>
<style>
body{font-family:'Microsoft YaHei',sans-serif;max-width:640px;margin:40px auto;padding:0 20px;}
h1{font-size:22px;color:#303133;}
ul{list-style:none;padding:0;}
li{margin:10px 0;}
a{display:block;padding:14px 16px;background:#f5f7fa;border-radius:8px;color:#303133;text-decoration:none;border:1px solid #e4e7ed;}
a:hover{background:#ecf5ff;color:#409eff;}
</style>
</head>
<body>
<h1>车管系统信息页索引</h1>
<ul>
%s
</ul>
</body>
</html>""" % "\n".join(links)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("[生成] index.html（站点首页索引）")


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        items = json.load(f)
    build_pages(items)
    build_index(items)
    print("\n完成！共 %d 个网页。" % len(items))
    print("把整个 bmp-dudubox/ 目录上传到腾讯云 Pages / EdgeOne Pages 即可。")


if __name__ == "__main__":
    main()
