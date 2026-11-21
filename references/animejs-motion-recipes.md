# Anime.js Composable Motion Recipes — 114 Existing Patterns (v3 Catalog)

These **114 named design recipes were independently curated by MauForma from official API capabilities**, not official "built-in effects" supplied by Anime.js. No finite complete catalog of every possible Anime.js motion exists: properties, curves and timelines can compose infinitely many behaviors. The searchable extended catalog in assets/motion-effects.json has **123 recipes**: the original 114 retained here plus 9 newer mechanisms, including text shimmer/morph, image sequence, horizontal scrolling and scroll snap, **which need not use Anime.js**. Consult expressive-motion-vocabulary.md for purposeful expressive composition, not a required effect checklist.

**Tier A**: suitable for frequent working interactions when needed. **Tier B**: conditional. **Tier C**: primarily showcase/creative, not the default. Every entry states its real appearance, meaningful contexts, risks and an official API-based mapping. The recipe IDs are MauForma names, **not Anime.js API methods**.

**Implementation contract:** Start with the user's interaction intent and approved motion preference; never add motion without purpose. Normally allow **at most one prominent motion focal point in a screen**, and preserve interruption, reversal, visible first frame and prefers-reduced-motion. Do not infer that every listed recipe should be implemented.

## Entrance and Exit (12)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `fade-in` / Fade in | Element becomes visible through opacity with no spatial movement | Light content and async results | Never hide primary content until JavaScript initializes | `animate opacity [0,1]` | A |
| `fade-out` / Fade out | Element gradually becomes transparent | Dismiss notices or secondary details | Do not make important errors irretrievable | `animate opacity [1,0]` | A |
| `rise-in` / Gentle rise | Content enters with a small upward motion and fade | Welcome and limited Card groups | Not every refresh of Table rows | `animate y [12,0] + opacity` | A |
| `drop-in` / Soft drop | Element settles downward slightly from above | Top overlay and toolbar | Avoid large motion covering content | `animate y [-10,0] + opacity` | A |
| `slide-left` / Slide from left | Element translates from left into place | Drawer and local navigation | Avoid direction that conflicts with actual navigation | `animate x [-20,0]` | B |
| `slide-right` / Slide from right | Element translates from right into place | Side panel and forward navigation | Account for RTL and Back direction | `animate x [20,0]` | B |
| `zoom-in` / Subtle zoom in | Element scales from slightly smaller to full size | Empty-state illustration and quiet notices | Not dense table rows or long body copy | `animate scale [.97,1]` | B |
| `zoom-out` / Subtle zoom out | Small element scales down and fades | Dismissing a small overlay | Avoid shifting primary content geometry | `animate scale [1,.97]+opacity` | B |
| `blur-reveal` / Focus reveal | Mildly blurred content quickly sharpens | Brand showcase or welcome | Avoid reading-dense text and low-powered devices | `animate filter blur + opacity` | C |
| `clip-reveal` / Clipped reveal | Visible crop expands to reveal content | Image cover and chart introduction | Do not clip essential information | `animate clipPath` | C |
| `mask-wipe` / Mask wipe | Mask sweeps across content to uncover it | Exhibition and storytelling | Not routine admin data rows | `animate CSS mask/clipPath` | C |
| `sequential-cards` / Staggered Cards | Card siblings fade and rise in sequence | Initial dashboard or portfolio load | Not 100+ table entries on every visit | `animate + stagger delay` | B |
## Hover and Press (11)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `hover-lift` / Gentle hover lift | Card moves upward by about 2–4px | Interactive showcase Card | Do not imply a static Card is clickable | `animate y -3` | A |
| `hover-shadow` / Hover shadow | Card shadow becomes subtly stronger | Clickable content Card | Avoid decorating every region | `animate boxShadow` | A |
| `hover-scale` / Hover scale | Control enlarges slightly | Product media and icon button | Not text in every data row | `animate scale 1.02` | B |
| `hover-tint` / Hover color shift | Background or text color interpolates | Button or navigation item | Preserve text contrast | `animate backgroundColor/color` | A |
| `press-down` / Press feedback | Button contracts slightly when pressed | Primary action and touch control | Do not omit focus and disabled states | `animate scale [.98,1]` | A |
| `magnetic` / Magnetic following | Button lightly tracks the pointer | Portfolio CTA or marketing moment | Provide touch fallback and avoid accidental activation | `createAnimatable x/y` | C |
| `pointer-tilt` / Pointer tilt | Card tilts gently with mouse position | Creative media display | Avoid business forms and dizziness | `createAnimatable rotateX/rotateY` | C |
| `icon-nudge` / Directional icon nudge | Arrow moves a few pixels on hover | Next/forward navigation | Do not animate directionless icon as directional | `animate x 4` | A |
| `icon-rotate` / Icon rotation | Operation icon rotates meaningfully | Refresh and expand | Avoid arbitrary endless spinning | `animate rotate` | B |
| `underline-grow` / Underline growth | Link underline extends along text | Inline link | Preserve line height without layout jump | `animate width/scaleX` | B |
| `focus-ring` / Focus-ring emphasis | Visible keyboard focus ring appears and persists | Accessible form controls | Mouse hover is not a substitute for keyboard focus | `animate shadow/opacity` | A |
## State and Feedback (12)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `success-check` / Success check | Completion glyph enters with short scale feedback | Actual save/submit succeeded | Never show success on failed operation | `animate scale/opacity` | A |
| `error-shake` / Brief error shake | Field shakes left/right once or twice | Actual error with explanatory text | No perpetual shake or nausea | `animate keyframes x` | B |
| `warning-pulse` / One warning pulse | Status mark or border pulses once | Risk attention in moderation | Avoid continuous flashing red | `animate scale/opacity` | B |
| `toast-enter` / Toast entrance | Toast fades/translates from nearby edge | Action feedback | Must not cover action or lack dismiss/exit | `animate opacity+y` | A |
| `toast-dismiss` / Toast dismissal | Toast exits and fades promptly | Timed status dismissal | Important error must remain readable long enough | `animate opacity+y` | A |
| `skeleton-shimmer` / Loading skeleton shimmer | Low-contrast light band moves slowly | Unknown-content loading | No fast flashes or fabricated actual progress | `animate backgroundPosition` | B |
| `progress-fill` / Progress fill | Bar advances with true measured fraction | Upload/download/build | Never invent completion percentage | `animate width/scaleX` | A |
| `spinner` / Loading spinner | Small indicator loops in rotation | Short uncertain wait | Avoid permanently spinning whole page | `animate rotate loop` | A |
| `heartbeat` / Status heartbeat | One brief scale pulse returns to baseline | Minor alert or synchronization complete | No ongoing distraction | `animate scale keyframes` | B |
| `switch-thumb` / Switch thumb travel | Thumb moves with actual toggle state | Switch and segmented control | Color cannot be only state indicator | `animate x` | A |
| `counter-change` / True counter interpolation | Number updates to its real final value | Usage/statistical counter | Do not alter underlying numeric meaning | `animate JS Object property` | B |
| `badge-bump` / Badge count bump | Badge briefly enlarges when unread count changes | Notifications and message counts | Avoid repeated disruptive blinking | `animate scale keyframes` | B |
## Navigation and Switching (10)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `tab-indicator` / Tab indicator travel | Underline moves to selected Tab | Tabs | Keyboard focus must remain visible | `animate x/width` | A |
| `nav-highlight` / Navigation highlight | Selected background moves to current destination | Sidebar navigation | Do not cause nav layout movement | `animate x/y/opacity` | A |
| `breadcrumb-transition` / Breadcrumb transition | New breadcrumb level fades in subtly | Deep hierarchical tools | Do not turn path into giant banner | `animate opacity` | B |
| `accordion-open` / Accordion opening | Disclosure content expands smoothly in height | Help or configuration group | Navigation/actions must not be hidden behind delayed motion | `createLayout or height + opacity` | A |
| `accordion-close` / Accordion closing | Disclosure compresses smoothly | Collapsible Settings groups | Do not block saving/exit | `createLayout or height + opacity` | A |
| `menu-pop` / Anchored menu appearance | Menu gently scales and fades from trigger | Value select or action menu | Avoid extreme bounce or inaccessible keyboard | `animate scale+opacity` | A |
| `page-crossfade` / Page crossfade | Old content fades away while new content appears | Portfolio page transitions | Preserve form focus and scroll state | `createTimeline + opacity` | B |
| `stepper-advance` / Stepper progression | True current step emphasis moves with progress | Multi-step form | Never mark incomplete step complete | `timeline + color/width` | A |
| `shared-element` / Shared-element continuity | Same object visually travels from list to detail | Gallery and media detail | May be overly complex for dense operational tasks | `createLayout / shared element logic` | C |
| `sidebar-expand` / Sidebar expansion | Width and neighboring layout adapt smoothly | Collapsible navigation rail | Ensure icons/text remain legible during resizing | `createLayout update` | B |
## Overlay and Container (8)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `dialog-enter` / Dialog entrance | Backdrop fades as Dialog settles through subtle scale | Confirm/edit Dialog | Ensure initial focus works | `createTimeline opacity+scale` | A |
| `dialog-exit` / Dialog exit | Dialog and backdrop fade away promptly | Closing Dialog | Must not delay actual save | `createTimeline opacity+scale` | A |
| `drawer-enter` / Drawer entrance | Side panel slides from edge | Details or editing Sidebar | Avoid clipped/blocked close button on narrow view | `animate translateX` | A |
| `popover-enter` / Popover entrance | Small shift plus opacity | Filter or contextual help | Must not require hover-only interaction | `animate opacity+y` | A |
| `tooltip-enter` / Tooltip fade | Brief helper appears with opacity | Explaining an icon | Not a substitute for a real label/critical information | `animate opacity` | A |
| `context-menu` / Context menu entrance | Menu appears with tiny scale from action point | File manager and developer tool | Preserve platform context-menu expectations | `animate scale+opacity` | A |
| `bottom-sheet` / Bottom-sheet entrance | Sheet slides up from viewport bottom | Mobile filters/actions | Do not force mobile Sheet on desktop | `animate y [100%,0]` | B |
| `modal-backdrop` / Backdrop fade | Overlay dimmer gradually increases | Dialog and Drawer | Avoid excessive dimming or flashing | `animate opacity` | A |
## Text and Typography (10)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `line-reveal` / Line reveal | Text lines rise in sequence | Brand or editorial storytelling | Not lengthy operational instruction | `splitText lines + stagger` | C |
| `word-reveal` / Word reveal | Words arrive one after another | English tagline or brand text | Do not slowly reveal long Chinese prose word by word | `splitText words + stagger` | C |
| `char-reveal` / Character reveal | Short text reveals character by character | Very short title or slogan | Never tables or long paragraphs | `splitText chars + stagger` | C |
| `text-scramble` / Text decode | Temporary random glyphs resolve to original | Fictional tech promo heading | Never sensitive data or real numeric values | `scrambleText innerHTML` | C |
| `typewriter` / Typewriter | Characters append in order | Chat mock or code teaching | Do not slow text users need immediately | `splitText ortext updates+timer` | B |
| `headline-color` / Headline color transition | Heading changes brand color smoothly | Marketing Hero | Not operational PageTitle | `animate color` | C |
| `split-words-rise` / Staggered word rise | Words rise with opacity in short phrase | Portfolio introductory text | Avoid replaying operational instructions | `splitText words + animate y` | C |
| `number-roll` / True numeric roll | Old numeric metric interpolates to actual new value | KPI or quota | Never fabricate data or confuse units | `animate object + onUpdate` | B |
| `text-highlight` / Text highlight | Selected phrase gradually gets emphasis | Education or keyword match | Preserve sufficient focus contrast | `animate color/backgroundColor` | B |
| `cursor-blink` / Simulated cursor blink | Cursor periodically changes opacity | Terminal demonstration | Do not overlay fake cursor on real Input | `animate opacity loop` | C |
## Data and Charts (10)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `chart-bars-grow` / Chart bars grow | Bars rise from baseline to actual values | First display of statistics | Not every filter refresh from zero | `animate scaleY` | B |
| `chart-line-draw` / Chart line draw | Polyline reveals along data path | Initial trend chart | Do not obscure key values after updates | `svg.createDrawable` | B |
| `donut-progress` / Donut progress | Circular stroke extends with real progress | Measured progress or resource monitor | Do not replace numerical value and unit with decoration | `svg.createDrawable/dashoffset` | B |
| `chart-point-pop` / Chart point emphasis | Relevant scatter points enter with small scale | Key data points | Do not animate thousands of points individually | `animate scale+stagger` | B |
| `chart-crossfilter` / Cross-filter continuity | Remaining marks smoothly adjust position | Analytics Dashboard | Do not animate numbers before source data loads | `createLayout / animate values` | B |
| `chart-hover-focus` / Chart hover emphasis | Current mark brightens while peers recede | Chart hover | Provide keyboard access to corresponding values | `animate opacity` | A |
| `count-up` / Count-up | Number interpolates to true measured result | Dashboard summary | Never invent growth without source | `animate object value` | B |
| `metric-delta` / Metric change highlight | Changed value briefly changes color | Monitoring/live updates | Avoid persistent flashing | `animate color` | B |
| `heatmap-wave` / Heatmap wave | Grid marks enter in spatial stagger | Illustrative heatmap | Not constantly refreshing monitoring grid | `stagger grid/from` | C |
| `filter-reorder` / Filtered reorder | Items move smoothly to their new list positions | Kanban or Card gallery | Avoid costly full animation of very long virtual list | `createLayout update` | B |
## Layout and Responsiveness (8)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `list-grid` / List/Grid toggle | Items travel between list and grid positions | Files/gallery/boards | Not tens of thousands of DOM items at once | `createLayout update` | B |
| `sort-move` / Sort movement | Rows move to new sorted positions | Small boards/lists | Not massive table animation | `createLayout update` | B |
| `expand-card` / Card expansion | Card grows into detailed layout | Overview-to-detail interaction | Prevent drastic neighboring jumps | `createLayout update` | B |
| `collapse-panel` / Panel collapse | Auxiliary pane contracts smoothly | Workspace/settings panel | Avoid repeated expensive relayout | `createLayout update` | B |
| `responsive-reflow` / Responsive layout motion | Items migrate on viewport change | Gallery or overview | Avoid continuous jitter while resizing | `createScope + createLayout` | C |
| `drag-sort-settle` / Drag sort settlement | Other items flow into place after drop | Task board and list sort | Do not imply success without actual persistence | `createDraggable + createLayout` | B |
| `card-flip` / Card flip | Card rotates around Y axis to reveal reverse | Flashcard and creative showcase | Avoid primary admin or finance interaction | `animate rotateY` | C |
| `masonry-reflow` / Masonry reflow | Uneven items adjust gracefully | Portfolio/images | Avoid replaying full layout on infinite scroll | `createLayout update` | C |
## Scroll and Storytelling (10)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `scroll-reveal` / Scroll reveal | Content lightly enters on viewport intersection | Introductory text sections | Do not interrupt admin reading every scroll | `onScroll + animate` | B |
| `scroll-scrub` / Scroll-synchronized timeline | Scroll position controls effect progress | Narrative article/interactive creative | Do not hijack wheel or touch scrolling | `onScroll sync` | C |
| `scroll-progress` / Reading progress | Scroll position updates a progress bar | Long documents and articles | Do not confuse with actual task progress | `onScroll + JS value` | B |
| `parallax` / Parallax | Layers travel at different relative speeds | Creative Hero depth | Avoid forms and vestibular triggers | `onScroll + y` | C |
| `sticky-stage` / Pinned scrollytelling | Sticky object updates content by chapter | Product walkthrough or story | Avoid forced scroll and inaccessible keyboard | `onScroll + timeline + CSS sticky` | C |
| `scrub-svg` / Scroll-drawn SVG | Path stroke reveal follows scroll progress | Route or historical timeline | Not routine process diagram zoom | `onScroll + createDrawable` | C |
| `section-color` / Section color transition | Background shifts by current chapter | Portfolio narrative | Maintain readable text contrast at every point | `onScroll + backgroundColor` | C |
| `horizontal-reveal` / Horizontal content reveal | Items appear laterally along scroll progress | Portfolio strip or milestones | Not reason to force horizontal scroll on routine list | `onScroll + x` | C |
| `stagger-scroll` / Stagger on intersection | Grid siblings enter sequentially when visible | Gallery | Not massive data grid | `onScroll + stagger` | C |
| `scroll-snap-feedback` / Scroll-section feedback | Chapter indicator transitions during scroll | Long-page navigation | Do not intercept native scroll to enforce state | `onScroll + tabs indicator` | B |
## SVG and Graphics (8)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `svg-line-draw` / SVG stroke drawing | Line is traced from start to end | Logo or process illustration | Do not obscure information behind ornament | `createDrawable draw` | B |
| `svg-line-erase` / SVG line erasing | Previously drawn path disappears gradually | Scene exit or demo | Must not hide critical business paths | `createDrawable draw` | C |
| `svg-morph` / SVG path morph | Contour transforms into another shape | Brand or status symbol | Do not destroy recognizability of concrete icons | `morphTo path d` | C |
| `svg-motion-path` / SVG motion path | Object travels an SVG curve | Route/process guide | Must match true mapped position | `createMotionPath` | C |
| `svg-dash-flow` / Flowing dashed path | Dashes advance along connection line | Network link illustration | Avoid perpetual high-contrast flashing | `animate strokeDashoffset` | C |
| `svg-gauge` / SVG gauge needle | Needle rotates to true measured angle | Instrument visualization | Meaning and units must remain clear | `animate rotate` | B |
| `svg-orbit` / Orbit animation | Object follows cyclic path | Brand loading or education | Not meaningless motion on task page | `createMotionPath/rotate` | C |
| `svg-gradient` / SVG gradient transition | Gradient stops/colors shift slowly | Decorative vector | Do not compromise text contrast | `animate SVG attrs/CSS vars` | C |
## Drag and Physics (7)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `free-drag` / Free drag | Object tracks pointer across canvas | Canvas nodes and board | Must support non-pointer keyboard alternative | `createDraggable` | B |
| `axis-drag` / Axis-constrained drag | Movement restricted to X or Y | Slider/resizable divider | Preserve native scrolling gestures | `createDraggable x/y` | B |
| `snap-drag` / Snap drag | Dropped object aligns to grid | Diagram editor | Prevent unannounced unexpected placement | `createDraggable snap` | B |
| `spring-release` / Spring release | Dragged object eases with damped physical spring | Playful control or canvas | Avoid excessive bounce reducing placement accuracy | `createDraggable releaseEase:spring` | C |
| `inertial-flick` / Inertial flick | Thrown object continues then decelerates | Explorable surface | Do not cause accidental file-manager operations | `createDraggable velocity/release` | C |
| `drag-boundary` / Drag boundary recoil | Object yields near edge then settles | Draggable canvas | Do not block main scroll | `createDraggable container` | C |
| `drag-to-reorder` / Reorder by drag | Dragged item rearranges neighbors | Boards and short lists | Provide undo and keyboard alternative | `createDraggable + createLayout` | B |
## Ambient and Experimental (8)

| ID / name | Actual appearance | Suitable context | Avoid | Anime.js mapping | Tier |
| --- | --- | --- | --- | --- | --- |
| `ambient-float` / Ambient floating | Large decoration moves up/down slowly | Showcase home or display | Not persistent admin background | `animate y alternate loop` | C |
| `ambient-rotate` / Ambient rotation | Abstract shape rotates continuously and slowly | Brand showcase/empty state | Avoid constant attention theft | `animate rotate loop` | C |
| `orbital-particles` / Orbital particles | Small points travel around paths with staggering | Tech demo | Not enterprise list background | `createMotionPath + stagger` | C |
| `wave-grid` / Grid wave | Cells change scale in timed wave | Generative data art or product story | Keep away from reading-dense content | `stagger grid + scale` | C |
| `random-dots` / Random dots | Particles jump then settle unpredictably | Creative experiment | No perpetual randomness or dizziness | `random + stagger` | C |
| `elastic-logo` / Elastic Logo | Brand emblem scales with spring return | Launch introduction | Not long daily startup delays | `spring scale` | C |
| `loading-ripple` / Loading ripple | Ring grows and fades | Small pending indicator | Avoid multiple strong perpetual pulses | `animate scale+opacity loop` | B |
| `glow-breathe` / Soft glow breathing | Glow strength changes gently | Recording/live activity status | Not giant purely decorative red/blue halo | `animate opacity loop` | B |

## Applicability and evidence boundaries

- **Officially supported primitives:** animate(), createTimeline(), createAnimatable(), createLayout(), createDraggable(), onScroll(), splitText(), scrambleText(), stagger() and SVG utilities. See animejs-official-capabilities.md for exact API and version constraints.
- **MauForma-authored compositions:** hover-lift, toast-enter, typewriter and similar IDs **are not official method names**; they express patterns composed from documented primitives.
- Browser performance/support for clip-path, filters, certain custom CSS properties and complex SVG must be checked on **actual target devices**.
- Before implementing createLayout, path morphing, onScroll or draggable effects, inspect the current official focused documentation. **Mapping descriptions in this table are not copy-ready implementation code.**
- If the component already has correct native CSS/framework animation, do not install Anime.js merely to match a recipe.

## Technical references

- Official Anime.js: https://animejs.com/documentation
- Built-in easing terms: animejs-easing-complete.md
- Official API categories: animejs-official-capabilities.md
- Verified examples: ../examples/animejs-v4-snippets.md
- Machine-searchable extended catalog (same original IDs): ../assets/motion-effects.json
