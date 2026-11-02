#!/usr/bin/env python3
"""Static consistency check for SPUI original motion recipe metadata."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'assets/motion-effects.json').read_text())
effects=data['effects']
assert len(effects)==114, f'Expected 114 recipes, got {len(effects)}'
assert len({x['id'] for x in effects})==len(effects), 'Duplicate IDs'
assert len(set(x['category'] for x in effects))==12, 'Expected 12 effect categories'
required={'id','category','name','effect','good_for','avoid','animejs_mapping','tier','preview','classification'}
for x in effects:
    assert required<=set(x),f'Missing keys: {x}'
    assert x['tier'] in ('A','B','C'),x['id']
    assert all(x[k] for k in required),x['id']
full=(root/'references/animejs-motion-recipes.md').read_text()
for x in effects:
    assert f'`{x["id"]}`' in full, x['id']
eases=(root/'references/animejs-easing-complete.md').read_text()
for family in ['Quad','Cubic','Quart','Quint','Sine','Expo','Circ','Bounce','Back','Elastic']:
    for prefix in ['in','out','inOut','outIn']:
        assert f'`{prefix}{family}`' in eases
for ease in ['linear','in','out','inOut','outIn']:
    assert f'`{ease}`' in eases
html=(root/'assets/motion-gallery.html').read_text()
for item in effects:
    assert f'"id":"{item["id"]}"' in html, item['id']
print('PASS: 114 recipes, 12 categories, 45 built-in ease names, metadata/markdown/gallery sync')
