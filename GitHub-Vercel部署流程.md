# GitHub → Vercel 部署完整流程

## 前提状态
- ✅ 本地已初始化 git 仓库，并完成首次提交（分支 main）
- ⚠️ 尚未推送到 GitHub（需你手动建仓库 + push）
- 域名 dudubox.top 已在 Cloudflare 接入（但还没加 bmp 子域记录）

## 第 1 步：在 GitHub 创建仓库

1. 打开 https://github.com/new
2. Repository name 填：`bmp-dudubox`（或任意名字）
3. 选 **Public 或 Private** 均可（Vercel 都支持）
4. **不要**勾选 "Add a README"（本地已有）
5. 点 **Create repository**

创建后会进入一个页面，记下仓库地址，形如：
`https://github.com/你的用户名/bmp-dudubox.git`

## 第 2 步：把本地代码推送到 GitHub

在 `bmp-dudubox` 目录下执行（把地址换成你自己的）：

```bash
git remote add origin https://github.com/你的用户名/bmp-dudubox.git
git push -u origin main
```

> 首次 push 会弹出 GitHub 登录窗口（或要求输入 Personal Access Token）。
> 如果用 HTTPS 且无法登录，用 Personal Access Token 代替密码：
> GitHub → Settings → Developer settings → Personal access tokens → 生成一个勾选 `repo` 权限的 token。

## 第 3 步：Vercel 关联 GitHub 自动部署

1. 打开 https://vercel.com → 登录（推荐用 GitHub 账号直接登录）
2. **Add New → Project**
3. 在 Import 列表里找到 `bmp-dudubox` 仓库 → **Import**
4. 配置页：
   - Framework Preset：选 **Other**（纯静态站点）
   - Build Command：留空
   - Output Directory：留空
5. 点 **Deploy** → 等待部署完成

## 第 4 步：绑定 bmp.dudubox.top 域名

1. Vercel 项目 → **Settings → Domains**
2. 输入 `bmp.dudubox.top` → **Add**
3. 去 Cloudflare（dudubox.top 的 DNS）加一条记录：
   - 类型：**CNAME**
   - 名称：`bmp`
   - 目标：`cname.vercel-dns.com`
   - 代理状态：**灰色云（仅 DNS）**，关闭代理
4. 等几分钟，Vercel 显示 Valid 即成功

## 第 5 步：验证

- `https://bmp.dudubox.top/` → 车牌索引首页
- `https://bmp.dudubox.top/pages/ars1688/` → 曾** / 赣ARS1688
- `https://bmp.dudubox.top/pages/bo39476/` → 张** / 赣BO39476

## 以后批量加新网页（全自动）

1. 编辑 `data.json`，加一条新记录
2. 运行 `python build.py` 重新生成
3. 提交并推送：
   ```bash
   git add -A
   git commit -m "新增车牌 xxx"
   git push
   ```
4. **Vercel 检测到 push 会自动重新部署**，无需任何手动操作

---

## 常见问题

**Q1：push 时提示没有权限 / 401？**
用 Personal Access Token 代替密码，或改用 SSH 方式。

**Q2：Vercel 绑定域名一直显示 Invalid？**
99% 是 Cloudflare 的橙色代理没关。去 Cloudflare 把 bmp 那条记录改成灰色云（仅 DNS）。

**Q3：build.py 用哪个 Python？**
任意 Python 3 即可。本机可用：
`C:/Users/dell/.workbuddy/binaries/python/versions/3.13.12/python.exe build.py`
