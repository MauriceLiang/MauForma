# React / Next：可复用组件与性能审查补充

参考 Vercel Composition Patterns 与 React Best Practices 的设计意图；具体 API 以项目 React/Next 版本和已安装原语为准，不照抄其它版本实现。

## 组件结构与 API

- 避免巨型组件一串 §isCompact/isDark/isPrimary/isEditable§ 等互斥布尔参数；用明确的 §variant/size§ 枚举或 compound components 表达角色。
- 复合组件由共享 Provider 管跨子组件的状态，边界清楚；对简单按钮不滥用复杂 Context。
- 独立展示层与数据/业务逻辑：§components/ui§ 负责一致的外观、焦点/键盘和基础状态；业务字段、权限、API 归 feature 层。
- 受控/非受控模式在组件 API 中明确；不要把渲染 prop、children 和 context 混得无法追踪。
- 将变体、状态、键盘行为做成可运行的组件展示或测试用例，稳定后再铺业务页面。
- React 19 规则不能直接作用于 React 18；适配 Next SSR / RSC，client component 只在需要交互时声明。

## 性能排序

1. **实际感知问题**：网络请求瀑布、服务端串行阻塞、数据重复拉取；
2. **包体积**：非首屏重特效动态加载，避免把全站动画引擎塞进每个页面；
3. **渲染稳定性**：不必要的全树状态传播、无意义重复渲染、大列表虚拟化；
4. **最后才考虑微优化**：不要为每个纯文本元素添加 memo。

## 与视觉规则联动

- 强动效集中在高价值视区；避免动画库与 React 状态管理同时改同一 DOM 属性。
- 组件卸载清理动画、观察器与计时器。
- SSR 时避免在 render 中读取 browser-only API；优化图片加载与合理降级。
- 不把可访问性问题推给三方库默认解决；检查焦点与键盘。

## PR 验收

输出复用组件映射、变体与状态证据、版本/依赖变化、瓶颈定位与实际测试。**未测性能只能给风险预测，不可声称优化成功**。

官方参考：https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns
https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
