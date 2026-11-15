/** Optional geometry audit for *real rendered* sidebar navigation.
 *
 * To opt in, annotate the sidebar container with
 *   data-mf-selection-indicator="external" | "none"
 * and navigation controls with data-mf-nav-item.
 * In external mode the rail is a sibling of the link/button:
 *   data-mf-indicator-rail aria-hidden="true".
 *
 * This checker verifies geometry and possible edge-border anti-patterns.
 * It cannot establish overall visual beauty, product correctness, or WCAG compliance.
 */
export async function auditSidebarIndicators(page, {
  rootSelector = '[data-mf-selection-indicator]',
} = {}) {
  return page.evaluate((selector) => {
    const problems = [];
    const add = (code, message, rootIndex, itemIndex = null) => {
      problems.push({ code, message, rootIndex, itemIndex });
    };
    const rect = (el) => el.getBoundingClientRect();
    const visible = (el) => {
      if (!el) return false;
      const st = getComputedStyle(el);
      return st.display !== 'none' &&
        st.visibility !== 'hidden' &&
        Number(st.opacity) > 0.1 &&
        rect(el).width > 0 && rect(el).height > 0;
    };
    const colorVisible = (color) => {
      if (!color || color === 'transparent') return false;
      const m = color.match(/rgba?\(([^)]+)\)/);
      if (!m) return true;
      const parts = m[1].split(/[,\s/]+/).filter(Boolean);
      return parts.length < 4 || Number(parts[3]) > 0.1;
    };
    const roots = [...document.querySelectorAll(selector)];
    if (!roots.length) {
      return { passed: false, checkedRoots: 0,
        issues: [{ code: 'NO_ANNOTATED_SIDEBAR',
          message: 'No annotated sidebar found: do not claim the route was audited.',
          rootIndex: null, itemIndex: null }] };
    }
    roots.forEach((root, ri) => {
      const mode = root.dataset.mfSelectionIndicator;
      const items = [...root.querySelectorAll('[data-mf-nav-item]')];
      if (!['external', 'none'].includes(mode)) {
        add('UNKNOWN_SELECTION_MODE', 'Choose external or none in the sidebar annotation.', ri);
        return;
      }
      if (!items.length) {
        add('NO_NAV_ITEMS', 'No data-mf-nav-item was found in this sidebar.', ri);
        return;
      }
      const active = items.filter(item =>
        item.getAttribute('aria-current') === 'page' ||
        item.getAttribute('aria-pressed') === 'true'
      );
      if (active.length !== 1) {
        add('ACTIVE_COUNT', 'Exactly one current page/item is expected in this demo scope.', ri);
      }
      items.forEach((item, ii) => {
        const selected = active.includes(item);
        const style = getComputedStyle(item);
        const edgeWidth = parseFloat(style.borderInlineStartWidth) || 0;
        if (selected && edgeWidth >= 2 && colorVisible(style.borderInlineStartColor)) {
          add('ITEM_EDGE_BORDER', 'Selected item itself has a colored inline-start border.', ri, ii);
        }
        const shadow = style.boxShadow || '';
        if (selected && /\binset\b/.test(shadow) &&
          /(?:inset\s+(?:[2-9]|\d{2,})px\s+0px|inset\s+0px\s+0px\s+0px\s+(?:[2-9]|\d{2,})px)/i.test(shadow)) {
          add('INSET_EDGE_BAR', 'Selected item has an inset stripe-like shadow.', ri, ii);
        }
        // Cosmetic pseudo-elements are hard to measure from DOM alone; flag obvious
        // left-edge full-height candidates for human review.
        if (selected) {
          const pseudo = getComputedStyle(item, '::before');
          if (pseudo.content !== 'none' && pseudo.content !== 'normal' &&
              pseudo.position === 'absolute' && parseFloat(pseudo.left) <= 1 &&
              parseFloat(pseudo.height) >= rect(item).height * 0.8) {
            add('PSEUDO_EDGE_BAR_REVIEW', 'Pseudo-element hugs item left edge at near full height.', ri, ii);
          }
        }
        const row = item.parentElement;
        const rails = row ? [...row.children].filter(child =>
          child !== item && child.hasAttribute('data-mf-indicator-rail')) : [];
        const rail = rails[0] || null;
        if (mode === 'external' && !rail) {
          add('MISSING_EXTERNAL_INDICATOR',
            'External selection requires a separate sibling indicator and stable gutter.', ri, ii);
          return;
        }
        if (mode === 'none' && rails.some(visible)) {
          add('UNEXPECTED_RAIL', 'No-rail mode should not render a visible selection indicator.', ri, ii);
        }
        if (mode === 'external' && rail) {
          if (rail.getAttribute('aria-hidden') !== 'true') {
            add('DECORATION_NOT_HIDDEN', 'Decorative rail must have aria-hidden=true.', ri, ii);
          }
          if (!selected) {
            if (visible(rail)) {
              add('INACTIVE_RAIL_VISIBLE', 'Unselected item must not display an accent rail.', ri, ii);
            }
          } else if (!visible(rail)) {
            add('ACTIVE_RAIL_MISSING', 'Selected item must show its external indicator.', ri, ii);
          } else {
            const ir = rect(item), rr = rect(rail);
            const gap = ir.left - rr.right;
            if (gap < 5) {
              add('RAIL_TOUCHES_ITEM', 'Indicator must have a visible gap outside item border box.', ri, ii);
            }
            if (rr.height > ir.height * 0.72) {
              add('RAIL_TOO_TALL', 'Rail is too tall: must be a short mark, not a full-height item border.', ri, ii);
            }
            if (rr.width > 8 || rr.width < 1) {
              add('RAIL_WIDTH', 'Rail should be a narrow independent indicator.', ri, ii);
            }
            const offset = Math.abs(rr.top + rr.height / 2 - (ir.top + ir.height / 2));
            if (offset > 5) {
              add('RAIL_OFF_CENTER', 'Rail should be centered on its selected item.', ri, ii);
            }
            if (rr.left < rect(root).left - 1 || rr.right > rect(root).right + 1) {
              add('RAIL_CLIPPED', 'Rail is outside the sidebar visible bounds.', ri, ii);
            }
          }
        }
      });
    });
    return { passed: problems.length === 0, checkedRoots: roots.length, issues: problems };
  }, rootSelector);
}

async function main() {
  const [url, rootSelector] = process.argv.slice(2);
  if (!url) {
    console.error('Usage: node scripts/audit_sidebar_indicator.mjs <url> [root-selector]');
    process.exitCode = 2;
    return;
  }
  const { chromium } = await import('playwright');
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.goto(url);
    const result = await auditSidebarIndicators(page, {
      rootSelector: rootSelector || '[data-mf-selection-indicator]'
    });
    console.log(JSON.stringify(result, null, 2));
    if (!result.passed) process.exitCode = 1;
  } finally {
    await browser.close();
  }
}
if (import.meta.url === new URL('file://' + process.argv[1]).href) {
  main().catch(err => { console.error(err); process.exitCode = 1; });
}
