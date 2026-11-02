# 其他网页框架适配：Svelte / Angular / Solid / Astro / Vanilla

**统一的是设计原则与组件契约，不是源代码。** 先复用项目已有组件，再考虑以下候选库。

## Svelte / SvelteKit

- **核心**：Svelte 组件/响应式模型，SvelteKit 提供 Web 应用路由/服务端能力。
- **组件**：Bits UI 提供无样式、键盘/焦点管理的 headless primitives；shadcn-svelte 提供可维护的 UI 层。一个项目优先确定主组件系统。
- **动画**：先用 Svelte 内置 `transition`/`animate`/CSS；复杂 DOM 使用 Anime.js/GSAP/Motion JS，销毁时清理。
- **数据**：SvelteKit `load`/actions 适用于服务端流转；全局状态遵循当前项目存储模式，避免无意义地引入 React Zustand。
- **避雷**：不要复制 React TSX 或 Vue `<script setup>` 到 Svelte 组件。
- 来源：https://svelte.dev/docs/svelte/overview 、https://bits-ui.com/docs/introduction

## Angular

- **核心**：组件、模板、依赖注入、Signals/RxJS 与 Angular Router，适用于大型结构化前端。
- **组件**：Angular CDK（基础行为）、Angular Material 或 PrimeNG / NG-ZORRO；尽量一个主视觉系统。
- **动画**：优先 CSS / 平台能力以及项目采用的 Angular 动画方案；复杂动画引入 Anime.js/GSAP 时要处理组件生命周期与检测成本。
- **数据**：HttpClient + service/缓存；按项目已有库/Signals/RxJS 架构实现。
- **避雷**：不要在 Angular 中调用 React hooks，不在模板中重造已有 ARIA 交互。
- 来源：https://angular.dev/overview 、https://material.angular.dev/ 、https://primeng.org/

## Solid / SolidStart

- **核心**：细粒度 Signals、组合式 UI。框架的状态与渲染模型不同于 React，不把 React hook 教程照抄过去。
- **组件**：Kobalte 或 Ark UI 原语；将 Token、variant 与 focus 统一到自有组件包装层。
- **动画**：CSS/WAAPI、Anime.js、GSAP；确认 Solid 响应与 DOM 更新边界。
- **避雷**：不要因为 JSX 相似就把 React hook/useState 当 Solid API。
- 来源：https://www.solidjs.com/ 、https://kobalte.dev/

## Astro

- **核心**：内容优先、静态/服务端 HTML；需要交互的局部才水合成 Island。
- **组件**：Astro 原生组件、已有 CSS 设计系统；需要时插入 React、Vue、Svelte、Solid 等官方框架集成。
- **动画**：CSS / WAAPI 优先，重型动画只在特定 Island 加载，尊重 `prefers-reduced-motion`。
- **避雷**：不能为一个静态首页把所有内容都变成 React Client Island。
- 来源：https://docs.astro.build/en/guides/framework-components/

## 纯 HTML / CSS / JS

- **核心**：语义 HTML + CSS Tokens + ES modules；复杂可复用 UI 可考虑 Web Components，但不必“为了现代”引入大框架。
- **组件**：适量 `<template>`、ES module 与 Web Components；Dialog/Popover 优先利用正确的原生语义，确保焦点处理。
- **动画**：CSS、Web Animations API、Anime.js/GSAP 按需。保持内容不依赖 JS 动画才可见。
- **避雷**：不要在没有卸载/清理的条件下无限注册监听器，不要把网页全部做成透明初始状态。

## 全部框架通用的最低验收标准

语义 HTML、可访问焦点、键盘/触摸、浅/深色、窄屏、不重复造组件、组件状态、真实 API 反馈、无动效回退和性能观察。后台的 PageHeader 规则不是营销 Hero 页的绝对限制。
