# Maxine’s Notes

基于 Jekyll 的中英双语个人博客。采用项目内 `skills/maxine-blog/SKILL.md` 中定义的红白 UI 和内容规范。

## 本地预览

安装 Ruby 与 Bundler 后，在项目根目录运行：

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

打开终端输出的本地地址；根路径会进入 `/zh/`，英文首页为 `/en/`。

生产构建及链接检查：

```sh
bundle exec jekyll build
python3 scripts/check_site.py
```

GitHub Pages 可继续使用现有 Jekyll 分支构建方式，无需切换托管服务。项目使用共享 Liquid 模板，不依赖自定义插件。修改文件不会自动提交或推送；推送到 Pages 配置的发布分支后由 GitHub 构建。实际分支与发布目录以仓库 Settings → Pages 为准。

## GitLab Pages 发布

仓库包含 `.gitlab-ci.yml`，推送到 GitLab 默认分支后自动构建并发布 `_site/`。
流水线通过 `CI_PAGES_URL` 自动设置站点地址和子路径，不修改 GitHub Pages 的默认配置。
构建成功后在 GitLab 的 Deploy → Pages 查看实际网址。

## 写一篇文章

中文文件存入 `_posts/zh/YYYY-MM-DD-article-slug.md`，英文存入 `_posts/en/`。推荐复制以下模板，日期改成实际发布日期（Asia/Shanghai），不填未来时间：

```yaml
---
layout: post
title: "文章标题"
description: "简短说明读者能从这篇文章获得什么。"
date: 2026-11-25 10:00:00 +0800
lang: zh-CN
translation_key: article-slug
permalink: /zh/posts/article-slug/
categories: [learning]
tags: [writing]
featured: false
---
```

正文使用 Markdown。教程截图、照片或封面可放在 `assets/images/posts/article-slug/`。封面可选，配置 `image` 和 `image_alt`；无需为每篇文章制作封面。

- 分类选一个：`tools`、`learning`、`reflections`。
- 标签最多三个。
- 英文版使用相同 `translation_key`，设置 `lang: en` 和 `/en/posts/article-slug/`。
- 两种语言文件各自有实际发布日期；允许先发布单一语言。系统只链接已存在的译文。
- 实质更新时填写 `updated`；译文可记录 `source_lang` 和 `translated_from_revision`，以便同步修改。
- 未完成的文章放 `_drafts/`；普通构建不发布草稿。

## 页面与交互

- 首页、博客、关于页均有独立中英文入口。
- 博客按语言列出文章，分类筛选支持 URL 参数和浏览器前进／后退；禁用 JavaScript 时仍可阅读完整列表与归档。
- 长文有至少三个二级标题时，浏览器自动生成目录；手机默认折叠。
- 中文和英文 RSS 为 `/zh/feed.xml`、`/en/feed.xml`；旧 `/feed.xml` 保留为全站订阅。
- `/sitemap.xml` 只列出公开内容页面。旧 `/about/`、`/archive/`、`/posts/hello-world/` 与原 NoteGPT 路径通过静态跳转保持可访问。
- 首页在当前语言文章超过五篇且配置了 `featured: true` 后显示精选区。项目、评论、搜索等按实际内容需要再扩展。

## 维护位置

- `assets/css/main.css`：色彩 token、共享样式和响应式布局。
- `assets/js/main.js`：分类筛选与文章目录。
- `_data/translations.json`：中英文界面文案。
- `_data/categories.json`：分类标识与本地化名称。
- `_layouts/`、`_includes/`：共享页面与组件。
- `AGENTS.md`、`skills/maxine-blog/`：后续创作与开发规范，已排除在网站构建输出之外。

原 NoteGPT 英文教程保留 HTML 正文并迁入 `_posts/en/`，以保留原始链接和段落；新文章优先采用 Markdown。
