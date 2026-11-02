# 动画引擎与组件生命周期：适用于所有 Web 框架

## 不可违反的技术安全线

- **DOM 所有权**：Vue/React/Svelte/Angular 管理 DOM 渲染。命令式引擎只能在组件挂载后按 `ref` 或作用域目标操作，不应跨组件 query 全站 `.card` 然后控制任意元素。
- **清理**：组件销毁、路由切换、弹窗关闭、依赖变化时停止/回收时间轴、事件监听、Observers、ScrollTrigger、Rive/Lottie 运行实例。
- **SSR**：服务端不能直接引用 `window/document`。动画在客户端 hook 中启动；首屏 HTML 应当在无 JS 动画时正常可见。
- **冲突**：不要同时由 Tailwind transition、Motion、Anime.js 操纵同一元素的 `transform/opacity`；若组合，需要明确属性所有权与嵌套层。
- **性能**：优先 `transform/opacity`，谨慎频繁更改 `width/height/top/left`、SVG path、blur 和大面积 box-shadow。避免大量强制同步测量布局。
- **无障碍**：遵守 `prefers-reduced-motion`，允许暂停循环动效，动画不能阻止键盘焦点。需要延迟功能状态的操作必须按语义进行而不是依赖动画的 onComplete。
- **测试**：快速打开/关闭、滚动中卸载、路由跳转、组件重挂载、长列表、低端机、动画依赖失效、减少动效偏好。

## Vue 3

- 先使用 `<Transition>`/`<TransitionGroup>`。
- 命令式动画在 `onMounted` 中创建，作用于单个 `ref<HTMLElement | null>`。
- `onUnmounted` / `onScopeDispose` 取消/还原；依赖改变时停止旧动画。
- Nuxt 在客户端挂载后运行，或通过官方 `<ClientOnly>` 方案处理复杂 DOM 引擎。

## React / Next.js

- 对 DOM 的命令式动画放在 `useEffect` / 按需 `useLayoutEffect`，返回 cleanup；不要在 render 内操作 DOM。
- React StrictMode 开发环境可能模拟挂载/清理以暴露副作用；正确 cleanup 应当幂等。
- Next App Router 的交互组件放在 client boundary，DOM 动画不要在 Server Component 模块顶层执行。
- 纯声明式组件动效（Motion）应遵循自己的 presence/layout 协议；不要把动画对象暴露为全局变量。

## Astro / 内容型页面

- Islands 仅在需要交互的位置加载，避免整个站点变成客户端渲染。
- 原生 CSS / WAAPI 优先，复杂动画尽量采用 IntersectionObserver 只在视口内激活。

## 验收示例

- 关闭弹窗后没有继续触发 toast 或更新已卸载组件。
- 浏览器减少动效时弹窗仍立即可交互，主要文字即刻可见。
- 快速点开关闭十次不会叠加十个监听器。
- 列表筛选不会把数据重排动画误当数据真实值变化。
