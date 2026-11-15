# Liquid Glass Optical Effects — 可选液态玻璃视觉技术

> **定位**：通用 Web 视觉能力，不是 MauForma 的默认审美、UI 组件库或 Apple 原生视觉的等价实现。仅在用户要求液态/玻璃质感、已确认的品牌方向适用，或方案对比后获得授权时采用。以可读性、性能和可降级的业务交互为先。

## 1. 四层光学模型：理解原理，不把 blur 当折射

| 层 | 视觉职责 | 典型实现 | 应调参数 | 排查问题 |
| --- | --- | --- | --- | --- |
| **透明（transmission）** | 让底下图像/线条透出，形成材质基础 | 半透明背景、单层色调/饱和度 | tint、alpha | 太不透明会像实色卡片；太透明会降低文本对比 |
| **折射（refraction）** | 通过背景采样坐标偏移，让曲面边缘的直线/文字变弯 | 变形贴图 + SVG `feDisplacementMap` 接入 backdrop（实验路径）；或 WebGL shader | edge falloff、strength/`scale`、法线方向 | 只有 blur、没有像素偏移，就仍然是磨砂而非折射 |
| **高光（specular / Fresnel-like）** | 亮暗边缘不均匀，暗示曲率和光源 | 方向性径向/线性渐变、mask/overlay；需要时 shader 法线与视角计算 | light direction、intensity、falloff | 一圈等亮白描边像普通边框；不要把 CSS 渐变自称严格菲涅尔模型 |
| **阴影（elevation）** | 让面板与背景分开，强调悬浮层级 | 柔和 box-shadow / drop-shadow | y-offset、blur、spread、opacity | 多层阴影太强会显脏或降低对比 |

**可选背景模糊**：少量 `backdrop-filter: blur(...)` 能缓和噪声，但不是四层之一，也不是折射。模糊过强会吃掉原本应辨认的边缘弯曲；任何情况下都不把模糊当作已经完成 refraction 的证据。

### 为什么背景会弯？

理想化近似：平坦中心 `offset≈0`，越接近圆角矩形边缘，模拟“曲面”的方向与坡度越明显，背景取样位置产生 X/Y 偏移。这个解释是**设计和渲染近似**，不是对真实玻璃光线追踪或原生系统渲染管线的完整物理描述。

SVG 的 `feDisplacementMap` 可用贴图 `in2` 的两条通道分别控制源图 `in` 的横纵位移。以 `xChannelSelector="R"`、`yChannelSelector="G"` 为例：

```text
output(x, y) = source(
  x + scale * (R(x, y) / 255 - 0.5),
  y + scale * (G(x, y) / 255 - 0.5)
)
```

中性通道值约 127.5（8-bit 常用 128）对应近零偏移；通道偏离中值越远，位移越明显。`scale` 是对贴图信号的幅度乘子：固定贴图下可以调整强度而无需重新计算整个贴图；**形状、尺寸或边缘坡度变化时仍需重新生成贴图**。依据：<https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap>。

## 2. 实现流程（按优先级选择）

### A. 低成本近似：跨浏览器视觉材质基线

1. 让真实内容处于正常 DOM、可选择/可操作。
2. 用独立视觉层渲染半透明 tint；可选轻 blur；叠加**方向不同的高光**与柔和外阴影。
3. 设置真实 `focus-visible`、hover、selected、disabled，避免为装饰牺牲对比度。
4. **标注为 glass-like / translucent fallback**，不宣称已经有真正背景折射。

典型层级（概念结构，不是跨项目开箱即用组件）：

```html
<div class="glass-surface">
  <div class="glass-tint" aria-hidden="true"></div>
  <div class="glass-highlight" aria-hidden="true"></div>
  <div class="glass-content">可读的真实控件与文字</div>
</div>
```

```css
.glass-surface {
  position: relative; isolation: isolate; overflow: hidden; border-radius: var(--glass-radius);
  box-shadow: 0 12px 35px rgb(0 0 0 / .16);
  background: rgb(255 255 255 / .12);
}
.glass-tint, .glass-highlight { position:absolute; inset:0; pointer-events:none; }
.glass-tint { background: rgb(255 255 255 / .06); backdrop-filter: blur(4px); }
.glass-highlight {
  border: 1px solid rgb(255 255 255 / .5);
  border-radius: inherit;
  background: linear-gradient(135deg, rgb(255 255 255 / .25), transparent 40%, rgb(0 0 0 / .08));
}
.glass-content { position: relative; z-index: 1; }
```

上面的 highlight 是方向性**近似**，没有计算真实 Fresnel 反射；`border` 仅用于表现边界，不是光学证明。只向现有成熟组件库的 **surface / overlay / theme slot** 增加效果，不手写取代 Select、Dialog、Popover、Keyboard 等交互原语。

### B. 实验性 Web 光学折射：Canvas 位移图 + SVG Filter + CSS

1. 获得待显示形状尺寸和圆角。使用 rounded-rectangle signed-distance function 或边缘法线近似，在画布逐像素生成偏移（中心接近 0，边缘更强）；R 编码 X、G 编码 Y、B 可保持中性、A=255。
2. 输出位移贴图的 Canvas PNG / Blob URL；将其用 SVG `feImage`（或等价 SVG 图像输入）作为 `in2`，`feDisplacementMap in="SourceGraphic" in2="map" xChannelSelector="R" yChannelSelector="G"`。调整 `scale` 得到不同强度。
3. 仅在目标浏览器**真实像素结果证明** `backdrop-filter: url(#...)` 能把该滤镜用于背景时启用；不可以把 `CSS.supports("backdrop-filter", "url(#...)")` 等同于实际折射支持。
4. 重算时机：控件宽高或圆角改变；通过 `ResizeObserver` 节流重建，避免每一帧生成 `ImageData`。切换 scale 不必重建位移图。对象 URL、SVG filter 实例与观察器在卸载时回收；多实例 filter ID 必须唯一。
5. 背景内容要足够丰富、存在文字/条纹等可观测参照；在纯色背景上无法仅凭肉眼判断折射是否生效。
6. 圆角/边缘反射/高光和阴影独立开关调试；当折射不可用时，直接回退到 A，不能让控件消失或留下黑色矩形。

**注意“滤镜作用对象”**：对元素使用 `filter:url(#...)` 改变其**自身绘制结果**，并不等于扭曲它背后的页面；只有 SVG 滤镜真正参与 backdrop 采样，才能呈现透镜背景弯曲。仅 `feDisplacementMap` 本身跨浏览器广泛可用，不能推出这条 CSS 与 SVG 背景组合也可用。

### C. 高保真路线：WebGL / GLSL（明确需要时）

需要动态曲率、RGB 色散、跟随指针/触摸的高频变形、不同半径与立体材质，可用 WebGL shader 处理受控场景采样；但：

- shader 不能神奇读取任意 DOM 后方像素。应主动设计“可采样的背景”：独立 Canvas/纹理、预渲染图像或合理的背景捕获方案；权限、跨域内容与更新同步要审查。
- 原生 RGB 分离偏移会增加采样与性能成本，视频所述轻量 SVG 示例**未实现色散**；不要在没有真实实现的情况下宣称“苹果同款动态液态玻璃”。
- 按项目 GPU / DPR / 面积和滚动场景测性能，优先少量焦点控件，不让全屏 WebGL 特效成为产品默认背景。
- 服务端渲染项目只在客户端挂载图形层；组件卸载时销毁 texture、program、canvas/renderer 和订阅。业务操作仍在 DOM 中、可键盘操作。

## 3. 组件迁移与视觉角色

| 形状/使用场景 | 可适用的玻璃层 | 不建议 |
| --- | --- | --- |
| 胶囊搜索栏、工具条 | 小面积玻璃底与边缘高光，可选弱折射 | 把真实输入框重写为 Canvas，导致输入法/焦点丢失 |
| 圆形滑块旋钮、按钮点 | 限定范围的阴影、高光与透光 | 状态色只靠高光强弱区分 |
| 播放器操作区、悬浮操作岛 | 局部焦点层与有限阴影、明确景深 | 全屏玻璃遮挡字幕与控制文字 |
| 通知浮层、活动卡片 | 受控透明与必要 blur；多背景测试对比 | 所有数据卡片默认变玻璃、持续 GPU 合成 |
| 密集表单、文档阅读、表格 | 通常保持普通实体表面 | 每一行加折射、给正文背后持续扭曲 |

**与 Component Library First 并存**：先选定原有 UI 组件来源（Button/Select/Popover/Dialog），再在库支持的 theme slot 或外围装饰层做玻璃；不要复制库内部 DOM、破坏原生表单和弹层几何。

## 4. 浏览器兼容与可靠降级（不可简化）

| 能力 | 判断 | 策略 |
| --- | --- | --- |
| 半透明背景、渐变高光与阴影 | CSS 基础能力 | 基础材质层 |
| `backdrop-filter: blur(...)` | 现代主流浏览器广泛支持，仍有版本/设备差异 | 可选，不支持时使用可读的半透明/实色背景 |
| SVG `feDisplacementMap` 用于 SVG 图像自身 | 已广泛支持 | 与 backdrop 兼容**不是一回事** |
| `backdrop-filter: url(#svgFilter)` 与背景折射链路 | 不可按所有浏览器已支持来承诺；WebKit、Firefox 存在兼容问题 | **实验性增强**，目标浏览器真实取样测试后启用 |
| WebGL shader | 需可控背景纹理、GPU 和生命周期 | 作为高保真可选路线，失败回退静态材质 |

避免在 `@supports` 判定成功后就隐藏 fallback。**实际像素/视觉回归测试**：在对照条纹或字母背景下分别截图关闭折射与开启折射，测是否真的发生位移；分别检查 Chromium、Safari/WebKit、Firefox，或对支持矩阵中未测项明确 `NOT TESTED`。

官方参考与兼容问题：
- MDN：<https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter>
- MDN：<https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap>
- WebKit：<https://bugs.webkit.org/show_bug.cgi?id=245510>
- WebKit：<https://bugs.webkit.org/show_bug.cgi?id=297770>
- 浏览器兼容性讨论：<https://github.com/mdn/browser-compat-data/issues/24110>

## 5. 无障碍、性能、安全和第一版验收

- **可读性优先**：高光/折射不能让前景标题、输入值、占位文字、图标、报错、焦点环看不清；检查亮/暗主题、高对比模式、对比度及变化背景上的最差情况。需要时用更实的内容背景，不为坚持“全通透”牺牲文字。
- **减少动效**：`prefers-reduced-motion` 下关闭循环/跟随指针的折射动画，静态材质可保留；禁用过渡也不影响真实状态。
- **资源预算**：限制效果面积、重绘频率、Canvas 贴图尺寸、DPR、SVG filter 数量；后台/不可见时停止高频刷新。不要默认在每个导航项、表格行、弹窗、卡片上叠复杂滤镜。
- **触控与键盘**：所有装饰层 `pointer-events:none`，保持语义 DOM、触控目标、弹层堆叠与焦点控制。
- **跨浏览器状态**：滤镜与资源失败时不能出现黑底/透明不可读；SSR hydration 不闪烁。原有库的 CSS 层次和 overlay portal 要实测。
- **验收等级**：`DEMO ONLY` 是样例页演示；`STATIC CHECK` 是源码检查；`VERIFIED` 仅指目标路由、目标浏览器实际验证；`NOT TESTED` 不得写成兼容。

### Gate：何时启用？

1. 用户或已确认视觉方向是否确实需要光学玻璃？否则保持常规表面。
2. 具体组件的业务职责、尺寸与背景纹理是否适合折射？若纯色背景或密集数据页，跳过复杂实现。
3. 已有主组件库是否提供 surface 插槽/主题扩展？先用其结构，不造新交互。
4. 是否有**普通可读材质 fallback**、目标浏览器测试与性能预算？不具备就只做 A。
5. 四层是否能**单独开关**复验？避免把 blur、高光、背景扭曲混成一个不可调 CSS 黑盒。

附带的原创教学演示 `assets/liquid-glass-layer-lab.html` 允许逐层观察半透明、折射开关、高光、阴影和模糊；演示不代表任何真实产品或任何浏览器都支持 SVG backdrop 折射。所有视觉效果应保持可撤销、按场景使用。

**学习素材溯源**：四层模型与基础实现顺序依据用户提供的液态玻璃教学视频文字提取，独立整理为通用 Web 设计知识；SVG 通道公式、CSS 规范及浏览器限制另以 MDN、WebKit 与兼容性记录核对。此文不包含项目特定截图或业务内容。
