# Anime.js 可组合视觉动效配方全集（v3.0 收录）

此表由 MauForma 按官方能力**独立整理**，不是 Anime.js 官方对“内置特效”的命名。Anime.js 没有一个有限的、可穷尽的动画样式清单，属性、曲线和时间轴可组合出无限效果。此处收录 **114 种明确描述的可选动效配方**。

**A** = 高频业务可用（仍按需）；**B** = 条件适用；**C** = 展示/创意为主、默认不选。每项都明确视觉表现、适用情景、避雷以及对应的官方功能。

**执行要求**：先选动效的交互意图，再匹配配方；无理由不添加动画；一次界面最多一个显著动画焦点；保证可中断、可撤销、首屏正常显示、尊重减少动态效果偏好。

## 入场与退场（12 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `fade-in` / 透明淡入 | 元素从透明变清晰，无位移 | 轻量内容出现、异步结果 | 主体内容依赖脚本才可见 | `animate opacity [0,1]` | A |
| `fade-out` / 透明淡出 | 元素逐渐消失 | 关闭提示、次级元素撤出 | 隐藏重要错误后无法追回 | `animate opacity [1,0]` | A |
| `rise-in` / 下方轻浮入 | 内容轻微上移并淡入 | 卡片分组、欢迎页 | 频繁刷新的表格行 | `animate y [12,0] + opacity` | A |
| `drop-in` / 上方轻落入 | 内容从上方少量下移就位 | 顶部浮层、工具条 | 过大位移遮挡信息 | `animate y [-10,0] + opacity` | A |
| `slide-left` / 左侧滑入 | 元素由左侧平移进入 | 抽屉、小导航 | 整页切换不符合导航方向 | `animate x [-20,0]` | B |
| `slide-right` / 右侧滑入 | 元素由右侧平移进入 | 侧边面板、向前导航 | RTL/返回方向不匹配 | `animate x [20,0]` | B |
| `zoom-in` / 轻缩放出现 | 从略小尺寸放大到原位 | 空状态插画、轻提示 | 表格行或长正文 | `animate scale [.97,1]` | B |
| `zoom-out` / 轻缩小消退 | 缩小且逐渐透明 | 小浮层关闭 | 主内容布局位移 | `animate scale [1,.97]+opacity` | B |
| `blur-reveal` / 模糊清晰 | 轻微模糊迅速变清晰 | 品牌展示、欢迎页 | 文本阅读密集、低端设备 | `animate filter blur + opacity` | C |
| `clip-reveal` / 裁切揭示 | 内容从可见范围逐步露出 | 图片封面、图表进入 | 重要信息被裁切或阅读受阻 | `animate clipPath` | C |
| `mask-wipe` / 遮罩擦除 | 遮罩从一侧扫过以展示元素 | 展厅、视觉叙事 | 后台数据行加载 | `animate CSS mask/clipPath` | C |
| `sequential-cards` / 卡片错峰入场 | 多卡片依次淡入上浮 | 首次仪表盘加载、作品列表 | 100+ 行表格每次进入 | `animate + stagger delay` | B |

## 悬停与按压（11 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `hover-lift` / 悬停轻抬 | 卡片上移 2–4px | 可点击的展示卡片 | 不可点击的卡片 | `animate y -3` | A |
| `hover-shadow` / 悬停阴影增强 | 阴影柔和变强 | 可点击卡片 | 每处装饰造成噪音 | `animate boxShadow` | A |
| `hover-scale` / 悬停微放大 | 控件轻微变大 | 展示封面、图标按钮 | 工具表格中的所有文本 | `animate scale 1.02` | B |
| `hover-tint` / 悬停色调切换 | 背景色或文字色渐变 | 按钮、导航项 | 降低文本对比度 | `animate backgroundColor/color` | A |
| `press-down` / 按压反馈 | 按钮按下轻缩小 | 主按钮、触摸目标 | 没有焦点/禁用状态 | `animate scale [.98,1]` | A |
| `magnetic` / 磁吸跟随 | 按钮轻度追随光标 | 作品集 CTA、营销场景 | 无触摸替代或易误点击 | `createAnimatable x/y` | C |
| `pointer-tilt` / 指针倾斜 | 卡片随鼠标轻微旋转 | 视觉作品展示 | 业务表单、易眩晕场景 | `createAnimatable rotateX/rotateY` | C |
| `icon-nudge` / 图标轻推 | 箭头在 hover 时右移几像素 | 跳转链接、下一步 | 无方向性的图标 | `animate x 4` | A |
| `icon-rotate` / 图标旋转 | 操作图标旋转一定角度 | 刷新、展开 | 无语义的无限转动 | `animate rotate` | B |
| `underline-grow` / 底线延伸 | 链接底线从左到右扩展 | 文本链接 | 影响行高造成跳动 | `animate width/scaleX` | B |
| `focus-ring` / 焦点强调 | 聚焦环淡入并保持 | 键盘可用输入控件 | 只给鼠标 hover 不给键盘 | `animate shadow/opacity` | A |

## 状态与反馈（12 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `success-check` / 成功勾选 | 成功图标轻弹出 | 保存完成、提交成功 | 错误提交却显示成功 | `animate scale/opacity` | A |
| `error-shake` / 错误短摇 | 控件左右轻摇 1–2 次 | 明确错误且附文字说明 | 持续摇晃或引发眩晕 | `animate keyframes x` | B |
| `warning-pulse` / 警告短脉冲 | 状态点或边框单次强调 | 有限度的风险提醒 | 长期红色闪烁 | `animate scale/opacity` | B |
| `toast-enter` / 通知滑入 | Toast 从边缘淡入就位 | 操作反馈 | 盖住关键操作且无退出 | `animate opacity+y` | A |
| `toast-dismiss` / 通知离场 | Toast 快速渐隐移出 | 定时关闭通知 | 错误消息自动过快消失 | `animate opacity+y` | A |
| `skeleton-shimmer` / 骨架扫光 | 低对比亮带缓慢移动 | 等待不确定内容 | 高速强闪烁、替代实际进度 | `animate backgroundPosition` | B |
| `progress-fill` / 进度推进 | 进度条随真实数值伸长 | 上传、下载、构建 | 伪造进度百分比 | `animate width/scaleX` | A |
| `spinner` / 加载旋转 | 小型指示器循环旋转 | 未知时长的小范围等待 | 整页永远转圈 | `animate rotate loop` | A |
| `heartbeat` / 状态轻跳 | 元素短暂放大回归 | 轻提醒、同步完成 | 持续吸引注意力 | `animate scale keyframes` | B |
| `switch-thumb` / 开关滑块 | 滑块随开关状态左右移动 | Toggle/Segmented | 色彩是唯一状态标识 | `animate x` | A |
| `counter-change` / 数字平滑变化 | 数字逐帧更新到真实值 | 计数器、用量、统计指标 | 改变实际数值语义 | `animate JS Object property` | B |
| `badge-bump` / 徽标轻弹 | 未读数更新时短促放大 | 消息数、通知数 | 不断闪烁干扰任务 | `animate scale keyframes` | B |

## 导航与切换（10 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `tab-indicator` / 标签指示条移动 | 下划线跟随选中项滑动 | Tabs | 焦点状态丢失 | `animate x/width` | A |
| `nav-highlight` / 导航高亮过渡 | 背景浅色块移动到当前项 | 侧边栏导航 | 用位移造成导航跳动 | `animate x/y/opacity` | A |
| `breadcrumb-transition` / 面包屑更新 | 新层级轻度淡入 | 层级较深的工具 | 变成横幅标题占用空间 | `animate opacity` | B |
| `accordion-open` / 折叠展开 | 详情内容随高度展开 | 帮助内容、配置分组 | 让跳转藏在动画后 | `createLayout 或 height + opacity` | A |
| `accordion-close` / 折叠收起 | 内容平滑压缩消失 | 设置组收起 | 退出前无法保存 | `createLayout 或 height + opacity` | A |
| `menu-pop` / 菜单弹出 | 从触发点小幅缩放并淡入 | 下拉菜单、操作菜单 | 弹跳很明显、菜单无法键盘操作 | `animate scale+opacity` | A |
| `page-crossfade` / 页面交叉淡变 | 旧内容淡出、新内容淡入 | 静态作品页面转场 | 表单焦点/滚动丢失 | `createTimeline + opacity` | B |
| `stepper-advance` / 步骤推进 | 当前步骤高亮过渡并连接进度 | 多步骤表单 | 未完成步骤被误标完成 | `timeline + color/width` | A |
| `shared-element` / 共享元素转场 | 同一元素在列表和详情间延续位置 | 图库、图片详情 | 操作密集页面动线复杂 | `createLayout / shared element logic` | C |
| `sidebar-expand` / 侧栏展开 | 菜单宽度变化，内容平滑重排 | 可折叠侧栏 | 图标和文本在过程中无法读 | `createLayout update` | B |

## 浮层与容器（8 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `dialog-enter` / 对话框入场 | 遮罩淡入、弹窗微缩放就位 | 确认、编辑对话框 | 弹窗首次无法聚焦 | `createTimeline opacity+scale` | A |
| `dialog-exit` / 对话框退出 | 弹窗与遮罩快速渐隐 | 关闭对话框 | 动画阻塞表单保存 | `createTimeline opacity+scale` | A |
| `drawer-enter` / 抽屉滑入 | 面板从侧边进入 | 编辑侧栏、详情预览 | 窄屏超出或遮挡退出按钮 | `animate translateX` | A |
| `popover-enter` / 气泡浮层出现 | 小位移和透明度变化 | 筛选、辅助信息 | 需要 hover 才能操作 | `animate opacity+y` | A |
| `tooltip-enter` / 工具提示淡入 | 简短文字透明度变清晰 | 解释图标控件 | 替代可见标签或关键信息 | `animate opacity` | A |
| `context-menu` / 右键菜单轻现 | 菜单从操作点微缩放出现 | 文件管理器、开发工具 | 平台右键习惯被打破 | `animate scale+opacity` | A |
| `bottom-sheet` / 底部面板拉起 | 底部面板上滑进入 | 移动端筛选与操作 | 桌面端强行使用底部弹层 | `animate y [100%,0]` | B |
| `modal-backdrop` / 背景遮罩过渡 | 背景遮罩逐渐加深 | Dialog、Drawer | 遮罩过深或闪烁 | `animate opacity` | A |

## 文字与排版（10 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `line-reveal` / 逐行揭示 | 文本按行逐一上移出现 | 叙事页、品牌首页 | 密集业务说明文档 | `splitText lines + stagger` | C |
| `word-reveal` / 逐词揭示 | 单词先后出现 | 英文标题、品牌介绍 | 长篇中文逐词变慢 | `splitText words + stagger` | C |
| `char-reveal` / 逐字揭示 | 每个字符依次显现 | 短标题、标语 | 表格数据和长篇正文 | `splitText chars + stagger` | C |
| `text-scramble` / 字符乱码解锁 | 随机字符逐步变成原文 | 展示型数字科技标题 | 关键数值、敏感数据、可读性 | `scrambleText innerHTML` | C |
| `typewriter` / 打字揭示 | 文字按顺序逐字符增加 | 聊天演示、代码教学 | 用户真的需要快速读取全文 | `splitText 或文本更新+timer` | B |
| `headline-color` / 标题颜色渐变 | 标题从一种主题色过渡另一种 | 活动主视觉 | 后台功能标题 | `animate color` | C |
| `split-words-rise` / 分词上浮 | 短句各词依次上移并淡入 | 作品介绍、宣传短句 | 操作说明反复播放 | `splitText words + animate y` | C |
| `number-roll` / 数值滚动 | 数字由旧值渐变到实际新值 | KPI、配额、计量 | 伪造数据、造成单位混淆 | `animate object + onUpdate` | B |
| `text-highlight` / 重点语句着色 | 文本重点逐步强调 | 教学标注、选中关键词 | 焦点颜色不足 | `animate color/backgroundColor` | B |
| `cursor-blink` / 输入光标闪烁 | 光标周期性明暗切换 | 终端模拟、演示 | 真实输入框叠加假光标 | `animate opacity loop` | C |

## 数据与图表（10 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `chart-bars-grow` / 柱形增长 | 图表柱条从基线增长到数据值 | 初次展示统计图 | 每次筛选都从零增长 | `animate scaleY` | B |
| `chart-line-draw` / 折线绘制 | 折线路径沿数据点渐次出现 | 首次展示趋势图 | 更新数据时遮蔽关键数值 | `svg.createDrawable` | B |
| `donut-progress` / 环形进度 | 圆环描边沿周长增加 | 真实进度、资源监视 | 用装饰环替代数值和单位 | `svg.createDrawable/dashoffset` | B |
| `chart-point-pop` / 数据点弹出 | 关键散点轻度放大出现 | 数据图高亮 | 数千点逐一动画 | `animate scale+stagger` | B |
| `chart-crossfilter` / 交叉筛选过渡 | 筛选后保留数据位置平滑调整 | 数据看板、报表 | 数值先动画后加载数据 | `createLayout / animate values` | B |
| `chart-hover-focus` / 悬停数据强调 | 当前数据提高亮度，其他淡化 | 图表 hover | 无法键盘获取对应数值 | `animate opacity` | A |
| `count-up` / 数字计数 | 计量从前值过渡到真实值 | 仪表盘摘要 | 无来源地制造增长 | `animate object value` | B |
| `metric-delta` / 指标变化提示 | 变化值短促着色后恢复 | 实时状态、监控 | 持续闪烁影响注意力 | `animate color` | B |
| `heatmap-wave` / 热力图波纹 | 格点按位置错峰出现 | 展示型热力图 | 监控数据实时刷屏 | `stagger grid/from` | C |
| `filter-reorder` / 筛选重排 | 元素平滑移动到新列表位置 | 看板、卡片库 | 虚拟长列表大量计算 | `createLayout update` | B |

## 布局与响应（8 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `list-grid` / 列表网格切换 | 卡片在两种布局间移动 | 文件、图片库、项目看板 | 数万项同时进行 DOM 动画 | `createLayout update` | B |
| `sort-move` / 排序位置变化 | 条目移动到最新排序位置 | 看板小列表 | 表格大量行复杂动效 | `createLayout update` | B |
| `expand-card` / 卡片展开 | 卡片扩展为包含更多信息的布局 | 概览转详情 | 布局跳动严重 | `createLayout update` | B |
| `collapse-panel` / 容器收缩 | 侧边信息区收起 | 工作台、设置面板 | 反复重排导致掉帧 | `createLayout update` | B |
| `responsive-reflow` / 响应式重排 | 屏幕变化时元素平滑重新定位 | 图集、概览看板 | 视口调整持续抖动 | `createScope + createLayout` | C |
| `drag-sort-settle` / 拖拽排序归位 | 释放后其余项平顺补位 | 任务看板、清单排序 | 变更未持久化却显示成功 | `createDraggable + createLayout` | B |
| `card-flip` / 卡片翻面 | 卡片沿 Y 轴旋转显示背面 | 学习卡片、作品展示 | 财务信息、后台主要任务 | `animate rotateY` | C |
| `masonry-reflow` / 瀑布流归位 | 不同尺寸项目平滑重排 | 图片集、作品页 | 无限滚动中频繁全量动画 | `createLayout update` | C |

## 滚动与叙事（10 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `scroll-reveal` / 滚动揭示 | 进入视口时轻淡入 | 介绍页段落 | 后台滚动时不断打断阅读 | `onScroll + animate` | B |
| `scroll-scrub` / 滚动进度同步 | 滚动位置决定动画进度 | 长篇叙事、交互作品 | 用户滚动被劫持 | `onScroll sync` | C |
| `scroll-progress` / 阅读进度条 | 页面滚动进度映射为条形 | 文章、长文档 | 与任务进度混淆 | `onScroll + JS value` | B |
| `parallax` / 视差移动 | 不同图层以不同速度移动 | 展示型 Hero、景深视觉 | 表单、容易头晕 | `onScroll + y` | C |
| `sticky-stage` / 粘性场景 | 固定局部区域逐步切换内容 | 产品演示、故事介绍 | 强制滚动与键盘导航不友好 | `onScroll + timeline + CSS sticky` | C |
| `scrub-svg` / 随滚动路径描画 | 滚动越深路径显示越多 | 路线、时间线故事 | 后台流程图频繁缩放 | `onScroll + createDrawable` | C |
| `section-color` / 章节背景变色 | 滚到不同段落更换场景背景 | 作品网站 | 导致文字对比度波动 | `onScroll + backgroundColor` | C |
| `horizontal-reveal` / 水平揭示 | 横向项目随进度逐个露出 | 作品条带、里程碑 | 普通列表需要水平滚动 | `onScroll + x` | C |
| `stagger-scroll` / 滚动进入错峰 | 网格元素进入视口时依次出现 | 画廊、作品集 | 大规模数据网格 | `onScroll + stagger` | C |
| `scroll-snap-feedback` / 滚动区间反馈 | 章节切换时状态条渐变 | 长页章节导航 | 强制拦截原生滚动 | `onScroll + tabs indicator` | B |

## SVG 与图形（8 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `svg-line-draw` / SVG 描边绘制 | 线条由起点逐段描出 | 品牌 Logo、流程示意 | 无语义装饰覆盖信息 | `createDrawable draw` | B |
| `svg-line-erase` / SVG 路径擦除 | 已经显示的线段逐步消失 | 场景转场、演示动画 | 业务关键线段隐藏 | `createDrawable draw` | C |
| `svg-morph` / 形状变形 | 图形轮廓平滑过渡成另一轮廓 | 品牌、状态图标 | 具象图标失去可识别性 | `morphTo path d` | C |
| `svg-motion-path` / 路径运动 | 目标沿预设 SVG 曲线路径移动 | 流程示意、导览动画 | 实际地图位置与路径不匹配 | `createMotionPath` | C |
| `svg-dash-flow` / 路径虚线流动 | 虚线沿路径持续前进 | 网络流量、连接示意 | 持续高对比闪动 | `animate strokeDashoffset` | C |
| `svg-gauge` / 仪表盘指针 | 指针沿角度变化到真实指标 | 可视化仪表 | 数值颜色含义不明确 | `animate rotate` | B |
| `svg-orbit` / 图形绕行 | 图形沿环形/曲线轨迹往复 | 品牌加载、教育动画 | 功能页面无意义运动 | `createMotionPath/rotate` | C |
| `svg-gradient` / SVG 色彩渐变 | 渐变色值或节点位置缓慢变换 | 展示图形 | 影响文字对比度 | `animate SVG attrs/CSS vars` | C |

## 拖拽与物理（7 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `free-drag` / 自由拖拽 | 元素随指针移动 | 画布节点、看板 | 无法键盘操作 | `createDraggable` | B |
| `axis-drag` / 轴向拖拽 | 元素只能水平或垂直移动 | 滑块、分隔条 | 影响系统滚动手势 | `createDraggable x/y` | B |
| `snap-drag` / 网格吸附 | 释放后自动吸附到格点 | 流程图、设计器 | 未经提示的意外位置改变 | `createDraggable snap` | B |
| `spring-release` / 松手弹性归位 | 释放拖拽后以弹簧阻尼收敛 | 趣味控件、画布 | 高弹跳影响定位精度 | `createDraggable releaseEase:spring` | C |
| `inertial-flick` / 甩动惯性 | 快速拖动后物体继续移动再减速 | 可探索面板 | 文件管理误操作 | `createDraggable velocity/release` | C |
| `drag-boundary` / 边界回弹 | 物体到边缘有柔和回弹 | 可拖拽画布 | 阻挡主要滚动 | `createDraggable container` | C |
| `drag-to-reorder` / 拖放排序 | 拖动物件，其他对象为它腾位 | 看板、轻量清单 | 顺序改动无撤销/无键盘替代 | `createDraggable + createLayout` | B |

## 氛围与实验（8 种）

| ID / 名称 | 实际视觉表现 | 推荐场景 | 避雷 | Anime.js API 映射 | 级别 |
|---|---|---|---|---|---|
| `ambient-float` / 背景缓浮 | 大图形缓慢上下移动 | 首页装饰、展示屏 | 管理系统常驻背景 | `animate y alternate loop` | C |
| `ambient-rotate` / 背景慢旋 | 抽象图形持续缓慢旋转 | 品牌展示、空状态 | 频繁抢注意力 | `animate rotate loop` | C |
| `orbital-particles` / 粒子环绕 | 多个光点按路径缓动 | 科技演示 | 企业列表页背景 | `createMotionPath + stagger` | C |
| `wave-grid` / 波浪网格 | 格子按时间形成波浪起伏 | 数据艺术、产品介绍 | 可读性密集区 | `stagger grid + scale` | C |
| `random-dots` / 随机散点 | 点阵随机弹跳后收敛 | 创意实验 | 持续随机导致眩晕 | `random + stagger` | C |
| `elastic-logo` / 弹性 Logo | 品牌图形弹性缩放回原位 | 启动动画 | 每天打开工具都长时间播放 | `spring scale` | C |
| `loading-ripple` / 扩散波纹 | 圆环逐渐放大同时渐隐 | 轻量等待图标 | 多个波纹造成持续刺激 | `animate scale+opacity loop` | B |
| `glow-breathe` / 柔和呼吸光 | 光晕明暗缓慢变化 | 录音中、活动状态 | 用红蓝大光圈做纯装饰 | `animate opacity loop` | B |

## 适用性与证据边界

- **官方明确支持**：`animate()`、`createTimeline()`、`createAnimatable()`、`createLayout()`、`createDraggable()`、`onScroll()`、`splitText()`、`scrambleText()`、`stagger()`、SVG 工具等。详见 [animejs-official-capabilities.md](animejs-official-capabilities.md)。
- **配方自行组合**：`hover-lift`、`toast-enter`、`typewriter` 等命名**不是官方 API 名称**；它们是基于官方原语组合出的设计方案。
- `clip-path`、`filter`、某些 CSS 自定义属性和复杂 SVG 的跨浏览器支持与性能需要实机验证。
- 对 `createLayout`、SVG 形变、`onScroll`、拖拽等高级效果，先读官方专页再写具体实现；不要将示意配置直接当可复制代码。
- 组件已有 CSS transition、原生动画或框架动画时，不为使用 Anime.js 而重复安装库。

## 技术入口

- [官方文档](https://animejs.com/documentation)；[内置缓动完整清单](animejs-easing-complete.md)；[官方能力类别](animejs-official-capabilities.md)；[已核对的代码示例](../examples/animejs-v4-snippets.md)。
- `assets/motion-effects.json` 与本表同源，可供自动化工具检索。
