# Complete Built-in Anime.js Easing Names and Visual Behavior (v4.5.0)

**Scope:** The official Built-in eases table contains 1 linear easing + 4 Power variants + 10 families × 4 variants, totaling **45 built-in easing names**. This is the complete list of official names, excluding unbounded parameterized combinations.

| Family | Exact names | Visual effect and cautions |
| --- | --- | --- |
| Linear | `linear` | Constant speed: suited to continuous rotation/mechanical movement; usually inappropriate as the default for buttons/dialogs |
| Power | `in`, `out`, `inOut`, `outIn` | Power curves; parameterized forms such as `inOut`(3) tune motion intensity |
| Quad | `inQuad`, `outQuad`, `inOutQuad`, `outInQuad` | Soft, relatively restrained cadence; `in`/`out` determines acceleration direction |
| Cubic | `inCubic`, `outCubic`, `inOutCubic`, `outInCubic` | Clearer acceleration/deceleration; choose `in`/`out` by desired direction |
| Quart | `inQuart`, `outQuart`, `inOutQuart`, `outInQuart` | Stronger acceleration/deceleration; choose `in`/`out` by desired direction |
| Quint | `inQuint`, `outQuint`, `inOutQuint`, `outInQuint` | Pronounced acceleration/deceleration; choose `in`/`out` by desired direction |
| Sine | `inSine`, `outSine`, `inOutSine`, `outInSine` | Very gentle, natural cadence; choose `in`/`out` by desired direction |
| Expo | `inExpo`, `outExpo`, `inOutExpo`, `outInExpo` | Large speed contrast and crisp feeling; choose `in`/`out` by desired direction |
| Circ | `inCirc`, `outCirc`, `inOutCirc`, `outInCirc` | Noticeable changes `in` speed; choose `in`/`out` by desired direction |
| Bounce | `inBounce`, `outBounce`, `inOutBounce`, `outInBounce` | Several ground-contact rebounds; mostly decorative; choose `in`/`out` |
| Back | `inBack`, `outBack`, `inOutBack`, `outInBack` | Overshoots the target before returning; use sparingly; choose `in`/`out` |
| Elastic | `inElastic`, `outElastic`, `inOutElastic`, `outInElastic` | Repeated elastic oscillation, easily exaggerated; choose `in`/`out` |

## Four timing directions

- **in:** Ease-in: starts slowly, ends quickly.
- **out:** Ease-out: starts quickly, ends slowly.
- **inOut:** Ease-in-out: slow → fast → slow.
- **outIn:** Ease-out then ease-in: changes cadence around the middle.

## Six official extended easing functions and generators

| API | Visual effect | Caution |
| --- | --- | --- |
| cubicBezier(x1,y1,x2,y2) | Custom curve shaped by two control points | Reuse intentional curves instead of random control points |
| `linear`(...) | Piecewise-`linear` easing fitted through multiple points | Distinguish the function from the built-`in` string `linear` |
| steps(count, …) | Discrete stepped jumps/frame changes | Unsuitable for an interface transition that must be continuous |
| irregular(...) | Irregular micro-jitter and random-seeming rhythm | Must not produce error-like flicker or affect large amounts of body text |
| spring({bounce,duration}) | Physical elasticity controlled through perceived duration | spring affects final settling duration |
| spring({mass,stiffness,damping,velocity}) | Fine control over mass, stiffness, damping and velocity | Verify behavior on different devices and frame rates |

## Selection guidance

- **Everyday business UI:** Prefer outQuad, outCubic, outSine or inOutCubic.
- **Fast closing:** inQuad or inCubic, with short duration.
- **Brand showcase or playful controls:** Use outBack or light spring in a limited number of appropriate cases.
- **Use cautiously:** Bounce, Elastic and large overshoot; avoid repeated bouncing in dialogs, dense tables or high-frequency actions.
- **Continuous movement:** Constant-speed linear can suit a small spinner or orbital animation, but must respond to prefers-reduced-motion.

## Official sources

- https://animejs.com/documentation/easings/built-in-eases
- https://animejs.com/documentation/easings
- https://animejs.com/documentation/easings/spring
- https://animejs.com/easings/
