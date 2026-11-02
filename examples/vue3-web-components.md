# Vue 3 组件契约示例

源码位于 `examples/blueprints/vue/UiButton.vue` 与 `UiPageHeader.vue`，共享 CSS 在 `examples/blueprints/shared/component-tokens.css`。这些是**最低复杂度参考实现**，不是完全独立的 UI 框架。已有 Reka UI/shadcn-vue/Element Plus 项目优先改造已有同名组件，不必复制。

```vue
<script setup lang="ts">
import UiButton from '@/components/ui/UiButton.vue'
import UiPageHeader from '@/components/composites/UiPageHeader.vue'
</script>

<template>
  <main>
    <UiPageHeader title="用户管理" description="管理用户账号与访问权限">
      <template #actions><UiButton>新增用户</UiButton></template>
    </UiPageHeader>
    <!-- 在这里组合真正的 DataTable、FilterBar 和 API 状态 -->
  </main>
</template>
```

通过组件展示页检验尺寸、变体、loading/disabled、深浅色、focus-visible、长文本。不在页面中写 `.my-user-page button { border-radius: 22px; }` 覆盖统一按钮外观。
