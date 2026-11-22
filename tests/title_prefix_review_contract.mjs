/** Synthetic regression for the evidence-gated before/after title-prefix closure contract. */
import assert from 'node:assert/strict';
import {validateTitlePrefixReview} from '../scripts/validate_title_prefix_review.mjs';

function candidate(title, prefix, suffix = '1', level = 2) {
  return {
    title_path: '#card-' + suffix + ' > h' + level,
    prefix_path: '#card-' + suffix + ' > p',
    title, prefix, title_level: level, semantic_decision: 'UNREVIEWED'
  };
}
function report(items) {
  return {status: items.length ? 'CANDIDATES_FOR_REVIEW' : 'NO_CANDIDATES_OBSERVED',
    verification: 'NOT_VERIFIED', candidates: items};
}
function decision(item, action, overrides = {}) {
  return {
    ...item, decision: action, role: 'decorative',
    reason: 'The nearby title and product controls already make the purpose clear.',
    ...overrides
  };
}
const decorative = candidate('交互模型', '模块分类 · 外观导览');
const chapter = candidate('循环系统', '第三章 · 人体解剖', '2', 3);
const brand = candidate('Festival programme', 'CONFIRMED EVENT MOTTO', '3', 1);
const afterOnly = candidate('Reports', 'REPORT CENTER', '4', 4);

let result = validateTitlePrefixReview(report([decorative]), report([]), {
  decisions: [decision(decorative, 'delete')]
});
assert.equal(result.passed, true);
assert.equal(result.status, 'STATIC_REVIEW_COMPLETE_NOT_VISUALLY_VERIFIED');
assert.equal(result.counts.resolved, 1);

result = validateTitlePrefixReview(report([decorative]), report([decorative]), {
  decisions: [decision(decorative, 'delete')]
});
assert.equal(result.passed, false);
assert.ok(result.issues.some(x => x.includes('UNRESOLVED_PREFIX_STILL_RENDERED')));

result = validateTitlePrefixReview(report([decorative]), report([]), {decisions: []});
assert.ok(result.issues.some(x => x.includes('UNREVIEWED')));

result = validateTitlePrefixReview(report([]), report([afterOnly]), {decisions: []});
assert.ok(result.issues.some(x => x.includes('UNREVIEWED')),
  'A new pretitle introduced during implementation must be explicitly reviewed.');

result = validateTitlePrefixReview(report([chapter]), report([chapter]), {
  decisions: [decision(chapter, 'keep', {
    role: 'chapter_sequence',
    reason: 'This is the curriculum chapter number, not a decorative category label.',
    information_loss: 'Readers would lose the verified chapter position in the ordered curriculum.',
    placement_reason: 'This is the documented chapter header for the instructional sequence.',
    evidence: 'Chapter ordering is confirmed by the product curriculum and linked table of contents.'
  })]
});
assert.equal(result.passed, true, 'Legitimate chapter content can survive with explicit evidence.');

result = validateTitlePrefixReview(report([brand]), report([brand]), {
  decisions: [decision(brand, 'keep', {
    role: 'approved_brand_narrative',
    reason: 'The event brief approves a distinct editorial motto before the programme title.',
    information_loss: 'Visitors would lose the explicitly approved campaign identity and narrative.',
    placement_reason: 'The approved original composition requires the motto as a distinct introduction.',
    evidence: 'The product creative brief and approved campaign identity document.'
  })]
});
assert.equal(result.passed, true);

result = validateTitlePrefixReview(report([chapter]), report([chapter]), {
  decisions: [decision(chapter, 'keep', {
    role: 'chapter_sequence', reason: 'Provides context', information_loss: '提升层次',
    placement_reason: '增加高级感', evidence: '有助于理解'
  })]
});
assert.equal(result.passed, false);
assert.ok(result.issues.some(x => x.includes('KEEP_NEEDS_')));

result = validateTitlePrefixReview(report([decorative]), report([decorative]), {
  decisions: [decision(decorative, 'keep', {
    role: 'decorative', information_loss: 'Some supplementary context exists in the caption.',
    placement_reason: 'Above the heading creates a little extra visual hierarchy.',
    evidence: 'The reviewer has inspected the UI screenshot in the browser.'
  })]
});
assert.equal(result.passed, false);
assert.ok(result.issues.some(x => x.includes('UNJUSTIFIED_KEEP_ROLE')));

result = validateTitlePrefixReview(report([decorative]), report([]), {
  decisions: [decision(decorative, 'move')]
});
assert.equal(result.passed, true);
result = validateTitlePrefixReview(report([decorative]), report([]), {
  decisions: [decision(decorative, 'merge')]
});
assert.equal(result.passed, true);

result = validateTitlePrefixReview(report([decorative]), report([afterOnly]), {
  decisions: [decision(decorative, 'delete')]
});
assert.equal(result.passed, false, 'Deleting one pretitle must not excuse a newly introduced one.');
assert.ok(result.issues.some(x => x.includes('UNREVIEWED')));

result = validateTitlePrefixReview(report([]), report([]), {decisions: []});
assert.equal(result.passed, true);

console.log('Title-prefix review closure PASS: deletion, persistence blocker, unreviewed/new candidates, evidenced exceptions and empty page.');
