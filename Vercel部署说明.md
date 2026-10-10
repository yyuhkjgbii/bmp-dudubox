# 在 Vercel 上部署（bmp.dudubox.top 子域 + 每车牌一路径）

## 最终效果

- 站点首页（车牌索引）：`https://bmp.dudubox.top/`
- 单个车牌页面：`https://bmp.dudubox.top/pages/ars1688/`
- 另一个：`https://bmp.dudubox.top/pages/bo39476/`

## 部署步骤（两种方式任选其一）

### 方式 A：网页拖拽上传（最简单，无需装任何东西）

1. 打开 https://vercel.com ，用 GitHub / GitLab / 邮箱 注册登录
2. 点击右上角 **「Add New」→「Project」**
3. 在 Import 页面，选 **「Deploy without Git」/ 或直接把 `bmp-dudubox` 文件夹拖进去**
4. Vercel 会自动识别为静态站点，直接点 **Deploy**
5. 部署完成后会得到一个免费域名，形如 `https://bmp-dudubox-xxxx.vercel.app`

### 方式 B：命令行（推荐，方便以后批量更新）

```bash
# 1. 安装 Vercel CLI
npm i -g vercel

# 2. 进入项目目录
cd bmp-dudubox

# 3. 首次部署（会提示登录 + 是否链接到已有项目）
vercel

# 4. 之后每次改完 data.json 重新生成后，一条命令上线
vercel --prod
```

## 绑定自己的域名 bmp.dudubox.top

1. 在 Vercel 项目页 → **Settings → Domains**
2. 输入 `bmp.dudubox.top`，点 **Add**
3. Vercel 会给你一条记录，去 dudubox.top 的 DNS 服务商处添加：
   - 类型：**CNAME**
   - 主机记录（Name）：`bmp`
   - 记录值（Value）：`cname.vercel-dns.com`
4. 保存后等几分钟，Vercel 会自动签发 HTTPS 证书，显示 Valid 即成功

## 批量生成新网页

1. 编辑 `data.json`，加一条（填 车牌 / 姓名 / 入网时间 / 防伪文字 / 目录）
2. 运行 `python build.py` 重新生成
3. 重新部署（方式 A 重新拖拽；方式 B 跑 `vercel --prod`）

新网页自动获得路径：`https://bmp.dudubox.top/pages/<目录>/`

## 注意事项

- **DNS 解析**：`bmp.dudubox.top` 这个子域要在 dudubox.top 的 DNS 处加 CNAME 记录，记录值填 `cname.vercel-dns.com`（Vercel 域名绑定页会明确给出，以页面显示为准）
- **备案**：Vercel 服务器在境外，**不需要 ICP 备案**，这是相比腾讯云国内节点的优势（.top 域名无需备案即可用）
- **访问速度**：境外节点，国内访问速度一般，如追求国内速度建议仍用腾讯云/EdgeOne，但需备案
- `vercel.json` 里的 `trailingSlash: true` 保证 `/pages/ars1688/` 这种带斜杠路径能正常访问
