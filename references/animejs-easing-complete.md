# Anime.js 内置缓动完整名称与视觉表现（v4.5.0）

**范围**：官方 `Built-in eases` 表包含 1 个 `linear` + 4 个 Power 变体 + 10 个家族 × 4 个变体，共 **45 个内置缓动名称**。这是完整的官方名称表（不含无限可调的参数组合）。

| 家族 | 完整名称 | 视觉效果与注意事项 |
|---|---|---|
| Linear | `linear` | 等速运行：适合持续旋转/机械运动，默认按钮/弹窗通常不宜。 |
| Power | `in`、`out`、`inOut`、`outIn` | 幂曲线，支持如 `inOut(3)`；动态强度可调。 |
| Quad | `inQuad`、`outQuad`、`inOutQuad`、`outInQuad` | 轻柔、节奏较温和；根据 in/out 选择加减速方向。 |
| Cubic | `inCubic`、`outCubic`、`inOutCubic`、`outInCubic` | 更明确的加减速；根据 in/out 选择加减速方向。 |
| Quart | `inQuart`、`outQuart`、`inOutQuart`、`outInQuart` | 偏强的加减速；根据 in/out 选择加减速方向。 |
| Quint | `inQuint`、`outQuint`、`inOutQuint`、`outInQuint` | 强加减速；根据 in/out 选择加减速方向。 |
| Sine | `inSine`、`outSine`、`inOutSine`、`outInSine` | 非常柔和、自然；根据 in/out 选择加减速方向。 |
| Expo | `inExpo`、`outExpo`、`inOutExpo`、`outInExpo` | 速度落差大，显得利落；根据 in/out 选择加减速方向。 |
| Circ | `inCirc`、`outCirc`、`inOutCirc`、`outInCirc` | 速度变化偏明显；根据 in/out 选择加减速方向。 |
| Bounce | `inBounce`、`outBounce`、`inOutBounce`、`outInBounce` | 触地后多次反弹，偏装饰；根据 in/out 选择加减速方向。 |
| Back | `inBack`、`outBack`、`inOutBack`、`outInBack` | 越过终点再返回，适度点缀；根据 in/out 选择加减速方向。 |
| Elastic | `inElastic`、`outElastic`、`inOutElastic`、`outInElastic` | 多次弹性振荡，容易夸张；根据 in/out 选择加减速方向。 |

## 4 种节奏方向

- **`in`**：缓入：开始慢，结束快。
- **`out`**：缓出：开始快，结束慢。
- **`inOut`**：双向缓动：慢→快→慢。
- **`outIn`**：先缓出再缓入：中段节奏变化。

## 6 类扩展缓动与生成器（官方）

| API | 视觉效果 | 注意 |
|---|---|---|
| `cubicBezier(x1,y1,x2,y2)` | 自定义曲线，通过两个控制点设计运动节奏 | 曲线可复用，避免随意取点 |
| `linear(...)` | 通过多点拟合线性分段缓动曲线 | 与内置字符串 `linear` 区别看清 |
| `steps(count, …)` | 阶梯式突变、逐帧跳跃 | 不适合需要连贯的界面迁移 |
| `irregular(...)` | 不规则微抖、随机感节奏 | 禁止用于错误闪烁与大量正文 |
| `spring({bounce,duration})` | 按感知时长控制物理弹性 | `spring` 会影响最终 settling duration |
| `spring({mass,stiffness,damping,velocity})` | 细调质量、刚度、阻尼、速度的物理弹簧 | 需检验不同设备和帧率 |

## 选择建议

- **业务 UI 优先**：`outQuad`、`outCubic`、`outSine` 或 `inOutCubic`。
- **快速关闭**：`inQuad` / `inCubic`，持续时间短。
- **品牌展示或趣味控件**：在少数场景选 `outBack`、轻量 `spring`。
- **谨慎使用**：`Bounce`、`Elastic`、大 overshoot，避免在模态框、密集表格、重复操作中反复弹跳。
- **持续运动**：等速 `linear` 可以用于小 spinner 或轨道动画，但必须响应 `prefers-reduced-motion`。

## 官方链接

- <https://animejs.com/documentation/easings/built-in-eases>
- <https://animejs.com/documentation/easings>
- <https://animejs.com/documentation/easings/spring>
- <https://animejs.com/easings/>
