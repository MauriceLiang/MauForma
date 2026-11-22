#!/usr/bin/env node
/**
 * Mechanical closure check for a scoped, human/Agent-reviewed title-prefix audit.
 *
 * Usage:
 *   node scripts/audit_title_prefixes.mjs --url <real-url> --out before.json
 *   # Review every candidate, implement the UI change, capture the same route again:
 *   node scripts/audit_title_prefixes.mjs --url <real-url> --out after.json
 *   node scripts/validate_title_prefix_review.mjs \
 *     --before before.json --after after.json --review decisions.json
 *
 * Review format: {"decisions":[{"title_path":"...", "prefix_path":"...",
 *   "title":"...", "prefix":"...", "decision":"delete|move|merge|split|keep",
 *   "role":"...", "reason":"...", "information_loss":"...", 
 *   "placement_reason":"...", "evidence":"..."}]}
 *
 * Keep the exact locator fields from a discovered candidate. The check
 * verifies completeness and unchanged prefix relationships, NOT whether
 * the reviewer's declared meaning or browser visual quality is true.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const ACTIONS = new Set(['delete', 'move', 'merge', 'split', 'keep']);
const DISALLOWED_KEEP_ROLES = new Set(['decorative', 'redundant', 'generic_category', 'unknown', 'unreviewed']);
const GENERIC = /^(?:context|adds context|visual hierarchy|looks professional|looks premium|better ux|more polished|provides context|enhances hierarchy|说明功能|提升层次|增强层次|提供上下文|增强专业感|增加高级感|有助于理解|更美观|好看|不确定)$/i;

function nontrivial(value) {
  return typeof value === 'string' && Array.from(value.trim()).length >= 8
    && !GENERIC.test(value.trim());
}

export function titlePrefixKey(candidate) {
  return ['title_path', 'prefix_path', 'title', 'prefix']
    .map(field => typeof candidate?.[field] === 'string' ? candidate[field].trim() : '')
    .join('\u001f');
}

function collect(report, label, issues) {
  if (!report || !Array.isArray(report.candidates)) {
    issues.push(label + ': missing candidates array from rendered audit');
    return new Map();
  }
  if (report.verification !== 'NOT_VERIFIED') {
    issues.push(label + ': unexpected audit verification; scanner never certifies UI semantics');
  }
  const result = new Map();
  for (const [index, candidate] of report.candidates.entries()) {
    if (!candidate || ['title_path', 'prefix_path', 'title', 'prefix'].some(
      field => typeof candidate[field] !== 'string' || !candidate[field].trim()
    )) {
      issues.push(label + ': malformed candidate at index ' + index);
      continue;
    }
    const key = titlePrefixKey(candidate);
    if (result.has(key)) issues.push(label + ': duplicate candidate at index ' + index);
    result.set(key, candidate);
  }
  return result;
}

/**
 * @returns {{passed:boolean,status:string,issues:string[],counts:object}}
 */
export function validateTitlePrefixReview(before, after, review) {
  const issues = [];
  const beforeMap = collect(before, 'before', issues);
  const afterMap = collect(after, 'after', issues);
  const decisions = new Map();
  if (!review || !Array.isArray(review.decisions)) {
    issues.push('review: missing decisions array');
  } else {
    for (const [index, item] of review.decisions.entries()) {
      if (!item || ['title_path', 'prefix_path', 'title', 'prefix'].some(
        field => typeof item[field] !== 'string' || !item[field].trim()
      )) {
        issues.push('review: invalid locator at index ' + index);
        continue;
      }
      const key = titlePrefixKey(item);
      if (decisions.has(key)) issues.push('review: duplicate decision at index ' + index);
      decisions.set(key, item);
      if (!beforeMap.has(key) && !afterMap.has(key)) {
        issues.push('review: stale/unobserved decision for ' + item.title + ' / ' + item.prefix);
      }
    }
  }
  const allKeys = new Set([...beforeMap.keys(), ...afterMap.keys()]);
  for (const key of allKeys) {
    const candidate = afterMap.get(key) || beforeMap.get(key);
    const label = candidate.title + ' / ' + candidate.prefix;
    const item = decisions.get(key);
    if (!item) {
      issues.push('UNREVIEWED: ' + label);
      continue;
    }
    if (!ACTIONS.has(item.decision)) {
      issues.push('INVALID_DECISION: ' + label);
      continue;
    }
    if (!nontrivial(item.reason)) issues.push('MISSING_REASON: ' + label);
    if (!nontrivial(item.role)) {
      // Roles such as "step", "status" or "brand" are short but meaningful.
      if (typeof item.role !== 'string' || item.role.trim().length < 3 ||
          DISALLOWED_KEEP_ROLES.has(item.role.trim().toLowerCase()) && item.decision === 'keep') {
        issues.push('MISSING_OR_INVALID_ROLE: ' + label);
      }
    }
    const persists = afterMap.has(key);
    if (item.decision === 'keep') {
      if (DISALLOWED_KEEP_ROLES.has(String(item.role).trim().toLowerCase())) {
        issues.push('UNJUSTIFIED_KEEP_ROLE: ' + label);
      }
      if (!nontrivial(item.information_loss)) {
        issues.push('KEEP_NEEDS_INDEPENDENT_INFORMATION: ' + label);
      }
      if (!nontrivial(item.placement_reason)) {
        issues.push('KEEP_NEEDS_ABOVE_TITLE_REASON: ' + label);
      }
      if (!nontrivial(item.evidence)) {
        issues.push('KEEP_NEEDS_EVIDENCE: ' + label);
      }
      if (!persists) issues.push('STALE_KEEP_NOT_PRESENT_AFTER: ' + label);
    } else if (persists) {
      issues.push('UNRESOLVED_PREFIX_STILL_RENDERED: ' + label);
    }
  }
  return {
    passed: issues.length === 0,
    status: issues.length ? 'REVIEW_BLOCKED' : 'STATIC_REVIEW_COMPLETE_NOT_VISUALLY_VERIFIED',
    issues,
    counts: {
      before: beforeMap.size,
      after: afterMap.size,
      decisions: decisions.size,
      resolved: [...allKeys].filter(key => decisions.has(key)).length
    },
    note: 'Requires human/Agent semantic judgment and real rendered QA. This is review-completeness checking, not automatic design or behavior verification.'
  };
}

async function main() {
  const args = process.argv.slice(2);
  const options = {};
  for (let i = 0; i < args.length; i++) {
    if (!args[i].startsWith('--')) throw new Error('Unexpected argument: ' + args[i]);
    options[args[i].slice(2)] = args[++i];
  }
  if (!options.before || !options.after || !options.review) {
    throw new Error('Usage: --before before.json --after after.json --review decisions.json [--out summary.json]');
  }
  const load = filename => JSON.parse(fs.readFileSync(path.resolve(filename), 'utf8'));
  const result = validateTitlePrefixReview(load(options.before), load(options.after), load(options.review));
  if (options.out) fs.writeFileSync(path.resolve(options.out), JSON.stringify(result, null, 2) + '\n');
  process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  if (!result.passed) process.exitCode = 1;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url))
  main().catch(error => { console.error(error.message); process.exitCode = 2; });
