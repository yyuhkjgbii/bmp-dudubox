# RFID 车管信息页 - 批量生成方案

## 目录结构

```
bmp-dudubox/
├── README.md              ← 本说明
├── data.json              ← 所有网页的数据（姓名/车牌/防伪文字），改这里即可新增
├── build.py               ← 生成脚本：读取 data.json，批量产出每个网页
├── assets/                ← 公共资源（CSS/JS，所有网页共用）
│   └── RFID信息 - 车管系统_files/
├── template.html          ← 网页模板（含占位符，不要手动改）
├── index.html             ← 站点首页（自动生成的车牌列表索引）
└── pages/                 ← 生成结果：每个车牌一个目录
    ├── ars1688/
    │   └── index.html
    ├── bo39476/
    │   └── index.html
    └── ...
```

## 使用方法

1. 编辑 `data.json`，新增/修改一条记录（只需填：车牌、姓名、入网时间、防伪文字）
2. 运行 `python build.py`（会重新生成 `pages/` 和 `index.html`）
3. 把整个 `bmp-dudubox/` 目录上传到腾讯云 Pages / EdgeOne Pages，绑定域名 `bmp.dudubox.top`

每个网页的访问地址：
- `https://bmp.dudubox.top/pages/ars1688/`（或配置后省略 pages/ 前缀）

## data.json 字段说明

```json
{
  "车牌": "赣ARS1688",      // 车牌号（显示在卡片 + 水印）
  "姓名": "曾**",            // 车主姓名
  "入网时间": "2024-12-31 12:36:27",
  "防伪文字": "ARS1688",    // 防伪图片上居中显示的文字（去掉省份简称）
  "目录": "ars1688"         // 生成后的子目录名（URL 路径，建议用车牌字母数字部分）
}
```
