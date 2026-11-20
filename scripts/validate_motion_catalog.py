#!/usr/bin/env python3
"""Static consistency check for MauForma's extended Web motion recipe catalog."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'assets/motion-effects.json').read_text())
effects=data['effects']
assert len(effects)==123, f'Expected 123 recipes, got {len(effects)}'
assert len({x['id'] for x in effects})==len(effects), 'Duplicate IDs'
assert len(set(x['category'] for x in effects))==12, 'Expected 12 effect categories'
required={'id','category','name','effect','good_for','avoid','animejs_mapping','tier','preview','classification'}
for x in effects:
    assert required<=set(x),f'Missing keys: {x}'
    assert x['tier'] in ('A','B','C'),x['id']
    assert all(x[k] for k in required),x['id']
full=(root/'references/animejs-motion-recipes.md').read_text()
legacy_ids=set(re.findall(r'^\|\s*`([a-z0-9-]+)`\s*/',full,re.M))
assert len(legacy_ids)==114, f'Expected 114 existing documented recipes, got {len(legacy_ids)}'
all_ids={x['id'] for x in effects}
assert legacy_ids<=all_ids, f'Legacy recipes lost: {legacy_ids-all_ids}'
new_ids=all_ids-legacy_ids
assert len(new_ids)==9, f'Expected nine curated extensions, got {len(new_ids)}'
vocabulary=(root/'references/expressive-motion-vocabulary.md').read_text()
for x in effects:
    if x['id'] in new_ids:
        assert '`'+x['id']+'`' in vocabulary, x['id']
        assert all(x.get(k) for k in ('english_name','fallback')), x['id']
eases=(root/'references/animejs-easing-complete.md').read_text()
for family in ['Quad','Cubic','Quart','Quint','Sine','Expo','Circ','Bounce','Back','Elastic']:
    for prefix in ['in','out','inOut','outIn']:
        assert f'`{prefix}{family}`' in eases
for ease in ['linear','in','out','inOut','outIn']:
    assert f'`{ease}`' in eases
html=(root/'assets/motion-gallery.html').read_text()
for item in effects:
    assert f'"id":"{item["id"]}"' in html, item['id']
print('PASS: 114 preserved + 9 new = 123 recipes, 12 categories, 45 easing names, markdown/gallery sync')
