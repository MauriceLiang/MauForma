# React / Vue 创意组件落地配方（真实来源 + 工程要求）

> 以下命令来自 2026-11-02 官网可查的安装示例。**只展示已核对过的组件命令与参数**；通用结构中的业务 props/路由需按实际版本复核。全部为按需复制源码，不应把示例全部安装到同一个项目。

## React 1：React Bits 一次性 Hero 标题

官方安装：https://reactbits.dev/get-started/installation

```bash
# 官方例子：TypeScript + Tailwind 版本；TS-CSS / JS-TW 等按详情页选择
npx shadcn@latest add @react-bits/SplitText-TS-TW
```

引入生成到项目的源代码组件（实际路径以 CLI 输出为准），放到营销 `Hero`，**只有被强调的短标题**应用错峰入场。背景与 CTA 不要求同时开动效。

```tsx
// 示意用法：实际导入路径/props 按生成组件文件定义调整
import SplitText from '@/components/SplitText'

export function MarketingHero() {
  return (
    <section aria-label="产品介绍" className="hero">
      <h1 className="sr-only">让复杂任务变得清晰</h1>
      <div aria-hidden="true"><SplitText text="让复杂任务变得清晰" /></div>
      <p>通过简洁的工作流集中完成日常操作。</p>
      <a href="/docs" className="ui-primary-action">了解产品</a>
    </section>
  )
}
```

可访问性备注：**不要无条件对所有拆字组件再复制一份可视/隐藏文字**，需要检查组件本身 aria 与屏幕阅读器行为，避免读屏重复。上例是“组件拆字无法正确朗读”时的兜底模式；若组件已有完整可访问文本，应删掉重复的隐藏标题。

## React 2：React Bits 柔和 Aurora 背景

官网：https://reactbits.dev/backgrounds/aurora 。可配置颜色、透明度、暂停、`dpr` 与 `mouseInteraction`；详见组件页最新 props。

- Hero 背景**不可承载文本语义**；在其上叠加文字时保证静态对比度；Canvas 出错时显示静态渐变。
- `prefers-reduced-motion` 时使用组件 `paused`（若该版本支持）或完全卸载，渲染静态背景。
- 背景视觉强度不要随业务 loading 变化而误导用户。

## Vue 1：Vue Bits 极光背景

官方 CLI 示例：https://vue-bits.dev/ 和 https://vue-bits.dev/get-started/installation

```bash
npx jsrepo add https://vue-bits.dev/r/Aurora.json
```

然后导入**安装后的本地组件路径**（路径按 CLI 输出）：

```vue
<script setup lang="ts">
import Aurora from './Aurora.vue'
</script>

<template>
  <section class="marketing-hero">
    <div class="marketing-hero__visual" aria-hidden="true">
      <Aurora :color-stops="['#171D22', '#7cff67', '#171D22']" />
    </div>
    <div class="marketing-hero__content">
      <h1>将想法变成产品</h1>
      <p>灵活的工作流程，清晰的协作体验。</p>
      <a href="/features">了解功能</a>
    </div>
  </section>
</template>

<style scoped>
.marketing-hero { position: relative; isolation: isolate; overflow: hidden; }
.marketing-hero__visual { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.marketing-hero__content { position: relative; padding: clamp(4rem, 8vw, 9rem) 1.5rem; }
@media (prefers-reduced-motion: reduce) {
  .marketing-hero__visual { display: none; }
  .marketing-hero { background: linear-gradient(125deg, #f2f5f9, #e4edf4); }
}
</style>
```

注意 SSR：若选用的背景组件在 setup 顶层使用 `window`，需先修复访问时机；Nuxt 仅在需要时用 `<ClientOnly>` 并提供相同尺寸的 SSR fallback，以避免布局抖动。

## Vue 2：Vue Bits 文本动效

官方示例：https://vue-bits.dev/get-started/installation ，以 `SplitText.vue` 为例：

```vue
<script setup lang="ts">
import SplitText from './SplitText.vue'
</script>

<template>
  <h1 class="sr-only">Hello, you!</h1>
  <div aria-hidden="true">
    <SplitText text="Hello, you!" :delay="100" :duration="0.6" />
  </div>
</template>
```

与 React 一样，首先审查组件的无障碍处理，避免屏幕阅读器读两遍。根据组件具体 `delay` 单位与版本检查参数。

## React 3：Ant Design 与创意层边界

```tsx
import { ConfigProvider, Button, Input, Table } from 'antd'

export function UserManagement() {
  return (
    <ConfigProvider theme={{ token: { colorPrimary: '#2665D9', borderRadius: 8 } }}>
      <main>
        <header className="ui-page-header">
          <h1>用户管理</h1>
          <Button type="primary">新增用户</Button>
        </header>
        <Input.Search placeholder="搜索用户" aria-label="搜索用户" />
        {/* Table: 从真实数据/请求状态导入 columns、dataSource */}
        <Table columns={[]} dataSource={[]} rowKey="id" />
      </main>
    </ConfigProvider>
  )
}
```

上面 Table 空数组只是**代码结构示意**，不是已完成的业务实现。真正交付时必须有真实 columns/dataSource、空态、权限、loading、错误与分页。

## Vue 3：Ant Design Vue 同样只负责业务基础层

```vue
<script setup lang="ts">
const theme = { token: { colorPrimary: '#2665D9', borderRadius: 8 } }
</script>

<template>
  <a-config-provider :theme="theme">
    <main>
      <header class="ui-page-header">
        <h1>用户管理</h1>
        <a-button type="primary">新增用户</a-button>
      </header>
      <!-- 使用真实数据、错误/空态和分页配置实现 a-table -->
    </main>
  </a-config-provider>
</template>
```

## 官网 + 后台同一产品的分层示例

```text
src/
  theme/
    tokens.css                  # 一处统一品牌色 / 间距 / 字体 / 阴影
  components/ui/                # UiButton, UiDialog, UiField, UiPageHeader
  components/creative/          # AuroraHero, SplitTitle, SpotlightFeatureCard
  pages/marketing/              # 可以选择性用 React Bits 或 Vue Bits
  pages/app/                    # 企业 UI 基础库，默认无需 WebGL
```

若官网用 React、后台用 Vue 也可以**只共享设计规范与 tokens 的概念**，源码按框架独立实现。不要把 React 专用 TSX 组件的源代码塞入 Vue 仓库。

## 引入后验收清单

- [ ] npm lockfile 中的新增依赖、许可证、bundle 增量有记录
- [ ] 只加载需要的单个创意组件，不全局注册整套效果
- [ ] SEO 主标题与 CTA 在动画失败时可见、可点击
- [ ] 无障碍标签不重复读字、不被 `aria-hidden` 隐去业务信息
- [ ] 手机、触摸、低性能、暗色模式与减少动态效果测试
- [ ] React effect、Vue onUnmounted、GSAP/WebGL/事件监听清理正确
- [ ] 只选一个管理 UI 主库，所有 Button/Table/Form 外观跟 Tokens 对齐
