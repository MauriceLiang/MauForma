# Vue 3 / Nuxt：组件分工与响应式边界

参考 vuejs-ai 的 Vue Best Practices 思想，实际实现要遵循项目 Vue/Nuxt 版本和 Options API 既有约束。

## 默认架构

- 新 Vue 3 组件通常用 `<script setup lang="ts">` + SFC；既有 Options API 大项目按明确迁移计划推进，不强制局部重写。
- Props 向下传值，Emits 向上传事件；可复用的逻辑放 composables，不把所有东西堆进全局 Pinia。
- `ref/computed` 保持单一数据来源；避免滥用 watcher 形成状态回写循环，避免把 derivable state 再单独存。
- 共享基础 `UiButton/UiField/UiDialog` 聚焦视觉与行为原语；列表加载、权限、业务查询在页面 feature 层。
- 组件公共 API 说明 Props/Emits/Slots/错误与加载状态，并有可验证展示；不要以多页面复制 CSS 代替共享组件。
- 数据密集组件的优化优先真实瓶颈；Vue 大列表渲染/异步组件/缓存只有在有证据时采用。

## 工程边界

Nuxt SSR 不在顶层访问 document/window；命令式动画在 mounted 后运行，卸载时清理。Vue Transition 优先处理简单显示隐藏；更复杂的动效按 `references/animation-engine-selection.md` 选库。

UI 主库已有 Element Plus/Ant Design Vue/Reka 等先继承，不强制迁移。使用 Vue 官方生态的测试方案验证组件状态和键盘、焦点、触摸交互。

## 质量门槛

- 所有 Props/Emits 类型与默认值有明确意义；
- 没有循环 watcher 和不必要的跨组件事件总线；
- 空、错误、加载、禁用有演示和测试；
- 构图遵循 Master 与当前页面 override，而不是每个 Vue 页面自创一套主色。

参考：https://github.com/vuejs-ai/skills/tree/main/skills/vue-best-practices
