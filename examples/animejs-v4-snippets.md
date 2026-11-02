# Anime.js v4.5.0 可直接复用的核心实现示例

安装 `npm install animejs@4.5.0`。代码示例面向 ES Modules；按项目构建工具处理打包和生命周期。下列示例采用官网已经明确支持的入口。**代码片段需放入存在对应元素的环境**；组件卸载及重复触发由项目添加清理。高级场景的生产集成还需实测。

## 1. 卡片顺序淡入上浮（首页/展示型）

```js
import { animate, stagger } from 'animejs';

animate('.work-card', {
  opacity: [0, 1],
  y: [16, 0],
  delay: stagger(70),
  duration: 440,
  ease: 'outCubic',
});
```

避免在 CSS 中永久把内容设为 `opacity: 0`。对于 SSR / JS 加载失败，保持内容默认可见，渐入只作为增强。

## 2. 小按钮按压反馈（任务型）

```js
import { animate } from 'animejs';
const button = document.querySelector('.save-button');
if (button) button.addEventListener('pointerdown', () => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  animate(button, { scale: [1, .98, 1], duration: 150, ease: 'outCubic' });
});
```

## 3. 数字更新（真实数值）

```js
import { animate } from 'animejs';
const node = document.querySelector('[data-value]');
const current = Number(node?.textContent || 0);
const nextValue = 42; // Replace with ACTUAL data, not hardcoded mock in production.
const counter = { value: current };
if (node) animate(counter, {
  value: nextValue,
  duration: 500,
  ease: 'outCubic',
  onUpdate: () => { node.textContent = String(Math.round(counter.value)); },
});
```

## 4. Timeline 同步与分步

```js
import { createTimeline } from 'animejs';
createTimeline({ defaults: { duration: 200, ease: 'outCubic' } })
  .add('.dialog-backdrop', { opacity: [0, 1] }, 0)
  .add('.dialog-panel', { opacity: [0, 1], y: [12, 0] }, 40);
```

## 5. 自动布局切换（列表 / 网格）

```js
import { createLayout } from 'animejs';
const root = document.querySelector('.items-layout');
if (root) {
  const layout = createLayout(root);
  document.querySelector('.view-toggle')?.addEventListener('click', () => {
    layout.update(({ root }) => root.classList.toggle('is-grid'));
  });
}
```

## 6. 滚动关联（只用于叙事）

```js
import { animate, onScroll } from 'animejs';
animate('.story-art', {
  y: [-20, 0],
  opacity: [0.6, 1],
  autoplay: onScroll({ sync: true }),
});
```

## 7. SVG 线条绘制

```js
import { animate, svg } from 'animejs';
animate(svg.createDrawable('.brand-path'), {
  draw: ['0 0', '0 1'],
  duration: 900,
  ease: 'inOutCubic',
});
```

## 8. SVG 路径变形

```js
import { animate, svg } from 'animejs';
animate('.source-path', {
  d: svg.morphTo('.target-path'),
  duration: 700,
  ease: 'inOutCubic',
});
```

## 9. SVG 曲线运动

```js
import { animate, svg } from 'animejs';
animate('.moving-dot', {
  ...svg.createMotionPath('.motion-path'),
  duration: 1500,
  ease: 'inOutCubic',
});
```

## 10. 文字逐字出现

```js
import { animate, stagger, splitText } from 'animejs';
const { chars } = splitText('.story-title', { words: false, chars: true });
animate(chars, { opacity: [0, 1], y: [10, 0], delay: stagger(28), duration: 340, ease: 'outCubic' });
```

## 11. 字符扰动揭示（装饰型，避免敏感数值）

```js
import { animate, scrambleText } from 'animejs';
animate('.tech-slogan', { innerHTML: scrambleText(), duration: 1100 });
```

`innerHTML` 是 Anime.js 官网 `scrambleText()` 的目标属性；不要自行对不可信字符串进行未转义的 innerHTML 拼接。

## 12. 自由拖拽

```js
import { createDraggable } from 'animejs';
createDraggable('.canvas-node');
```

## 13. 带轻量回弹的弹簧

```js
import { animate, spring } from 'animejs';
animate('.feedback-icon', { scale: [0.9, 1], ease: spring({ bounce: .15, duration: 300 }) });
```

官网说明春天曲线计算的 settling duration 会覆盖普通动画 `duration`；使用感知时间参数。不要用于频繁高密度表格操作。

## 14. 高频光标跟随

```js
import { createAnimatable } from 'animejs';
const follower = createAnimatable('.pointer-dot', { x: 180, y: 180, ease: 'outCubic' });
const area = document.querySelector('.demo-area');
area?.addEventListener('pointermove', e => {
  const rect = area.getBoundingClientRect();
  follower.x(e.clientX - rect.left);
  follower.y(e.clientY - rect.top);
});
```

## 15. 响应式 / reduced-motion 作用域

```js
import { createScope, animate } from 'animejs';
const scope = createScope({ mediaQueries: { reduced: '(prefers-reduced-motion: reduce)' } });
scope.add(({ matches }) => {
  if (matches.reduced) return; // Keep content visible in CSS by default.
  animate('.decorative-orb', { y: [-6, 6], alternate: true, loop: true, duration: 1200 });
});
// In the framework component's unmount cleanup: scope.revert();
```

## 16. 网格错峰效果

```js
import { animate, stagger } from 'animejs';
animate('.grid-dot', {
  scale: stagger([.75, 1.1], { grid: [6, 6], from: 'center' }),
  delay: stagger(40, { grid: [6, 6], from: 'center' }),
  duration: 400,
  ease: 'inOutCubic',
});
```

## 官方参考

- <https://animejs.com/documentation>
- <https://animejs.com/documentation/animation>
- <https://animejs.com/documentation/layout>
- <https://animejs.com/documentation/svg>
- <https://animejs.com/documentation/text>
- <https://animejs.com/documentation/easings>
