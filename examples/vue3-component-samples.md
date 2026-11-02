# Vue 3 组件先行：最小代码样例（与现有 Reka UI 兼容的外围样式层）

下列仅说明 API 和样式复用方式，**不是要求项目放弃已有 Reka UI / Radix 原语**。要处理 Dialog、Popover、Select、Tabs、Tooltip 等复杂组件时，优先包装现有可访问 primitive，不要用自制 div 还原键盘和焦点逻辑。

## UiButton.vue

```vue
<script setup lang="ts">
withDefaults(defineProps<{
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger'
  size?: 'default' | 'sm'
  loading?: boolean
  disabled?: boolean
  type?: 'button' | 'submit' | 'reset'
}>(), {
  variant: 'secondary', size: 'default',
  type: 'button', loading: false, disabled: false
})
</script>

<template>
  <button
    :type="type"
    class="ui-button"
    :class="[
      `ui-button--${variant}`,
      size === 'sm' && 'ui-button--sm'
    ]"
    :disabled="disabled || loading"
    :aria-busy="loading || undefined"
  >
    <span v-if="loading" aria-hidden="true">…</span>
    <slot v-if="!loading" />
    <span v-else>处理中</span>
  </button>
</template>
```

从组件使用处**仅控制 variant/size/disabled/loading**，不传入随意的颜色或圆角。异步请求的结束、错误与防重复提交由调用层管理；按钮负责一致的交互状态显示。

## UiField.vue

```vue
<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{
  id: string
  label: string
  modelValue: string
  hint?: string
  error?: string
  required?: boolean
  disabled?: boolean
}>()
const emit = defineEmits<{ 'update:modelValue': [value: string] }>()
const describedBy = computed(() => [
  props.hint ? `${props.id}-hint` : '',
  props.error ? `${props.id}-error` : ''
].filter(Boolean).join(' ') || undefined)
</script>

<template>
  <div class="ui-field">
    <label class="ui-label" :for="id">{{ label }}</label>
    <input
      :id="id" class="ui-input" type="text"
      :value="modelValue"
      :disabled="disabled"
      :required="required"
      :aria-invalid="error ? true : undefined"
      :aria-describedby="describedBy"
      @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    />
    <p v-if="hint" :id="`${id}-hint`" class="ui-hint">{{ hint }}</p>
    <p v-if="error" :id="`${id}-error`" class="ui-error">{{ error }}</p>
  </div>
</template>
```

## 业务页面如何调用

```vue
<template>
  <UiPanel>
    <UiField v-model="projectName" id="project-name" label="项目名称" :error="nameError" />
    <UiButton variant="primary" :loading="saving" @click="saveProject">保存</UiButton>
    <UiButton variant="secondary" @click="cancel">取消</UiButton>
  </UiPanel>
</template>
```

要点：业务页面不写 `.save-button`、`.cancel-button` 的外观；按钮变体、焦点、圆角和主题由公共组件统一管理。实际使用时按项目文件结构导入组件并实现业务函数。


## UiPageHeader.vue：功能页共享标题模式（新增 v2.1）

```vue
<script setup lang="ts">
withDefaults(defineProps<{
  title: string
  description?: string
  breadcrumbs?: Array<{ label: string; to?: string }>
  density?: 'compact' | 'comfortable'
}>(), { density: 'compact' })
</script>

<template>
  <header class="ui-page-header" :class="`ui-page-header--${density}`">
    <nav v-if="breadcrumbs?.length" aria-label="面包屑导航" class="ui-page-header__breadcrumbs">
      <template v-for="(crumb, i) in breadcrumbs" :key="`${i}-${crumb.label}`">
        <span v-if="i > 0" aria-hidden="true">/</span>
        <a v-if="crumb.to" :href="crumb.to">{{ crumb.label }}</a>
        <span v-else :aria-current="i === breadcrumbs.length - 1 ? 'page' : undefined">{{ crumb.label }}</span>
      </template>
    </nav>
    <div class="ui-page-header__main">
      <div class="ui-page-header__copy">
        <h1>{{ title }}</h1>
        <p v-if="description">{{ description }}</p>
      </div>
      <div v-if="$slots.actions" class="ui-page-header__actions"><slot name="actions" /></div>
    </div>
  </header>
</template>

<style scoped>
.ui-page-header { margin-bottom: var(--spui-space-6, 24px); }
.ui-page-header__breadcrumbs { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:12px; font-size:12px; color:var(--spui-text-muted); }
.ui-page-header__main { display:flex; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; gap:12px 20px; }
.ui-page-header__copy { min-width:0; flex:1 1 220px; }
.ui-page-header h1 { margin:0; font-size:clamp(24px,2.6vw,30px); line-height:1.25; letter-spacing:-.035em; color:var(--spui-text); }
.ui-page-header p { margin:6px 0 0; font-size:13px; line-height:1.6; color:var(--spui-text-soft); }
.ui-page-header__actions { display:flex; flex-wrap:wrap; align-items:center; gap:8px; }
.ui-page-header--comfortable h1 { font-size:clamp(28px,3.2vw,36px); }
</style>
```

仅作为模式示例：真实项目应沿用已有路由链接组件（例如 RouterLink）和真实 token 命名，并避免在已有父级 H1 时重复输出 H1。没有必要的描述就不要传 `description`，绝不能自动生成英文眉题/宣传口号。
