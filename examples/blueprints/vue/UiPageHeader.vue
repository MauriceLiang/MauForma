<script setup lang="ts">
withDefaults(defineProps<{
  title: string
  description?: string
  density?: 'compact' | 'comfortable'
}>(), { density: 'compact' })
</script>

<template>
  <header class="sp-page-header" :class="`sp-page-header--${density}`">
    <div class="sp-page-header__copy">
      <h1 class="sp-page-header__title">{{ title }}</h1>
      <p v-if="description" class="sp-page-header__description">{{ description }}</p>
    </div>
    <div v-if="$slots.actions" class="sp-page-header__actions"><slot name="actions" /></div>
  </header>
</template>
