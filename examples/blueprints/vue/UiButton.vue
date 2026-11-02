<script setup lang="ts">
withDefaults(defineProps<{
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger'
  size?: 'sm' | 'md'
  loading?: boolean
  disabled?: boolean
  type?: 'button' | 'submit' | 'reset'
}>(), {
  variant: 'primary', size: 'md', loading: false, disabled: false, type: 'button',
})
</script>

<template>
  <button
    class="sp-button"
    :class="[`sp-button--${variant}`, `sp-button--${size}`]"
    :type="type"
    :disabled="disabled || loading"
    :aria-busy="loading ? 'true' : undefined"
  >
    <span v-if="loading" class="sp-button__spinner" aria-hidden="true" />
    <slot />
  </button>
</template>
