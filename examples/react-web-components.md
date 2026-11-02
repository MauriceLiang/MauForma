# React 组件契约示例

源码位于 `examples/blueprints/react/UiButton.tsx` 与 `UiPageHeader.tsx`；共用样式在 `examples/blueprints/shared/component-tokens.css`。真实项目有 shadcn/ui 或其他组件时**优先复用并调整现有组件**。

```tsx
import { UiButton } from '@/components/ui/UiButton';
import { UiPageHeader } from '@/components/composites/UiPageHeader';

export function UsersPage() {
  return (
    <main>
      <UiPageHeader title="用户管理" description="管理用户账号与访问权限" actions={<UiButton>新增用户</UiButton>} />
      {/* 在这里组合真正的 DataTable、FilterBar 与查询状态 */}
    </main>
  );
}
```

对于 Next App Router，需要事件处理的按钮组件应在适当 client boundary 下使用。组件演示页检查 keyboard focus、loading/disabled、错误态、深浅色和长文本。
