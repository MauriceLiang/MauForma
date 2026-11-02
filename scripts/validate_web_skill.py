#!/usr/bin/env python3
"""Validates this Skill's Web scope, file links, and basic framework coverage."""
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
required = [
 'SKILL.md','references/framework-support-matrix.md',
 'references/framework-vue-nuxt.md','references/framework-react-next.md',
 'references/framework-other-web.md','references/stack-guide-11-items.md',
 'references/animation-engine-selection.md','references/animation-integration-lifecycle.md',
 'references/ai-frontend-prompt-policy.md','references/quality-antipatterns-by-page-type.md',
 'examples/prompt-library-web.md','assets/framework-decision.json',
 'examples/blueprints/vue/UiButton.vue','examples/blueprints/react/UiButton.tsx',
 'assets/motion-effects.json','assets/motion-gallery.html',
 'references/creative-component-libraries.md','references/enterprise-ui-library-guide.md',
 'examples/creative-library-recipes-react-vue.md','assets/creative-effects-gallery.html'
]
errors=[]
for path in required:
 if not (root/path).is_file(): errors.append(f'File missing: {path}')
dec=json.loads((root/'assets/framework-decision.json').read_text('utf-8'))
for n in ['vue3','nuxt','react','next','svelte','sveltekit','angular','solid','astro','vanilla']:
 if n not in dec['supported']: errors.append(f'Framework unsupported: {n}')
for md in root.rglob('*.md'):
 source=md.read_text('utf-8')
 for path in re.findall(r'(?<![\w/])(?:references|examples|assets|scripts)/[a-zA-Z0-9_./-]+\.(?:md|css|html|json|vue|tsx|py)',source):
  path=path.rstrip('.,;')
  if not (root/path).exists(): errors.append(f'Broken link in {md.relative_to(root)}: {path}')
motion=json.loads((root/'assets/motion-effects.json').read_text('utf-8'))
print('Motion JSON root:',type(motion).__name__)
print('Web frameworks:', ', '.join(dec['supported']))
print('Required files:',len(required))
print('Errors:',len(errors))
for e in errors[:40]: print(' -',e)
sys.exit(1 if errors else 0)
