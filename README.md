# Maxine 的 GitHub 博客

## 发布
1. 创建公开仓库 `Maxine001MWQ.github.io`，初始化 README。
2. 将本压缩包解压，把里面的文件和文件夹上传到仓库根目录（不要上传 ZIP 本身或外层文件夹）。
3. Settings → Pages → Source 选择 Deploy from a branch。
4. Branch 选择 main，目录选择 /(root)，点击 Save。
5. 在 Actions 查看构建结果，成功后打开 https://maxine001mwq.github.io/ 。

## 写新文章
在仓库点 Add file → Create new file，文件名填写 `_posts/YYYY-MM-DD-英文标题.md`。
内容模板：

```markdown
---
layout: post
title: "文章标题"
date: 2026-11-18 10:00:00 +0800
categories: 教程
---

在这里写正文。
```

日期换成实际发布日期，不要填写未来时间。提交后自动构建，首页和归档会自动更新。
编辑 `_config.yml` 可修改博客名称和简介。首篇欢迎文章可直接编辑或删除。
