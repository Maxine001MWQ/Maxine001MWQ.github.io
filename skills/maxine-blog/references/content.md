# 内容、目录与中英双语规范

## 信息架构

主导航为：首页 Home、博客 Blog、关于 About。项目 Projects 在有真实可展示内容后加入。归档位于博客页内部，分类和标签用于内容发现；不展示空分类或占位项目。

首页包括简短个人介绍、精选文章、最新文章、主题入口与 GitHub／RSS 页脚。文章不足时只显示最新文章，避免精选重复。关于页只写用户提供或可核实的个人信息。

## 内容分类

每篇文章采用 1 个主分类、最多 3 个标签。默认分类及稳定标识：

| 标识 | 中文 | English |
| --- | --- | --- |
| tools | 工具与工作流 | Tools & Workflows |
| learning | 学习与实践 | Learning & Practice |
| reflections | 随笔与观察 | Notes & Reflections |

标签描述具体工具或主题，例如 `ai`、`notegpt`、`career`；保持稳定标识，展示名称可以本地化。系列是独立维度，有足够相关文章后再加入。分类方向可依用户实际写作调整。

## URL 与语言行为

文章 slug 优先沿用标题对应的英文小写、连字符命名。迁移已有文章时保留其原有标题 slug，不擅自缩短；已发布文章修改显示标题时不自动更改 URL。若用户要求改链接，旧地址应直接跳转至新主地址，避免多层跳转。`translation_key` 是稳定内部配对标识，不必随 URL 修改。

| 页面 | 中文 | English |
| --- | --- | --- |
| 首页 | /zh/ | /en/ |
| 博客 | /zh/blog/ | /en/blog/ |
| 关于 | /zh/about/ | /en/about/ |
| 文章 | /zh/posts/article-slug/ | /en/posts/article-slug/ |

- 根路径 `/` 默认提供中文入口，明确展示英文入口，不依据浏览器语言强制跳转。
- 两种语言各自一个文章文件，用稳定且相同的 `translation_key` 配对；同一配对内每种语言至多一个已发布版本。
- 文章内切换语言进入对应译文；无译文时显示本地化的「暂无英文版／Chinese version unavailable」等提示，另提供目标语言博客入口。不要让不存在的译文链接指向首页并伪装成译文。
- 列表、分类、搜索、上一篇／下一篇及相关文章默认过滤当前语言。跨语言内容必须清楚标记。
- 导航、按钮、分类名称、日期格式、阅读时间、空状态和错误提示均本地化。中文采用 `zh-CN`，英文采用 `en`；URL 目录使用 `zh` 和 `en`。
- 每个语言版本设置独立标题、描述、HTML lang 和指向自身的 canonical。仅为真实存在且已发布的语言版本生成互相对应、含自身的 hreflang，不将英文 canonical 指向中文。
- sitemap 收录实际发布地址；RSS 按语言划分。阅读时间计算考虑中文字符和英文词数，不对中文仅按空格分词。
- 迁移前检查旧 URL。保留 `/posts/.../` 与现有独立英文文章地址的兼容入口，使用托管平台可行的跳转方式，不承诺 GitHub Pages 原生提供 HTTP 301。

## 建议源文件结构

```text
_posts/zh/                  中文文章
_posts/en/                  英文文章
_drafts/                    草稿
_data/translations.json     界面文案与导航标签
_data/categories.json       分类标识与显示名称
_layouts/                   共享布局
_includes/                  导航、目录、语言切换等组件
assets/css/                 共享样式
assets/images/posts/<slug>/ 文章图片
zh/                         中文入口页
en/                         英文入口页
```

这是维护结构，先检查实际实现，勿仅为符合目录树创建空文件。导航结构目前位于共享布局 `_layouts/default.html`，标签来自界面文案。显式 permalink 决定发布 URL，不依赖源文件夹自动生成语言路径。

## 文章元数据

中文示例（日期替换为实际发布日期）：

```yaml
---
layout: post
title: "如何把零散的经历整理成简历"
description: "从素材整理到初稿修改的一套工作流程。"
date: 2026-11-25 10:00:00 +0800
lang: zh-CN
translation_key: career-notes-to-resume
permalink: /zh/posts/career-notes-to-resume/
categories: [tools]
tags: [ai, notegpt, career]
featured: false
---
```

文件名保持 `YYYY-MM-DD-英文slug.md`。英文版复用 translation_key，改为英文标题、描述、`lang: en` 和英文 permalink，发布日期按实际情况填写。

可选字段：`updated`（实质性更新时间）、`image`、`image_alt`、`series`、`source_lang`、`translated_from_revision`（译文所依据的原文提交或稳定版本标识）。只写有实际依据的值，模板对缺失值应合理处理。

## 写作与翻译

- 标题表达具体内容或读者收益，摘要补充信息，不照抄标题。
- 正文从问题或主要发现开始，再给方法、例子、结果和必要来源；随笔不强制套教程结构。
- 保留作者表达，避免虚构使用经历、职业背景、项目成果和数据；示例清楚标为示例。
- 图片提供有意义的 alt；图注与来源按需要填写。封面可选，不让配图成为发布前提。
- 翻译保留事实、链接和逻辑，允许自然调整语序，不要求逐段机械对齐。原文实质更新后检查译文是否需要同步。
- 允许单语言先发布；草稿不得因为配对逻辑进入公开列表、hreflang 或 sitemap。

发布前检查元数据、语言过滤、链接、标题层级、图片、译文配对及手机阅读效果。对于纯文字改动，采用与范围相称的检查。
