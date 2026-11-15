// BountyBot ($BNTY) — makefun-coin-promo-01 entry (Node 22, standard library only).
//
// The entry is the coin itself: an agent launches BountyBot on pump.fun, and
// LAUNCH.json at this repository's root names the coin's mint and the signature
// of the transaction that created it. This program's only job is to hand that
// file to the grader: it copies LAUNCH.json into the output directory, where
// the gate reads it. Nothing written here is judged — the coin's logo
// (logo.png), name, ticker, description and links live on pump.fun, and the
// house reads them from there.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// Read LAUNCH.json once first: a missing file, bad JSON, or a file without
// the two keys the gate looks for is a loud failure here instead of a
// silent copy of a broken entry. The copy itself is byte for byte, so the
// two runs still write identical output.
const launchPath = join(BOT_DIR, 'LAUNCH.json');
let launch: unknown;
try {
  launch = JSON.parse(readFileSync(launchPath, 'utf8'));
} catch (err) {
  console.error(`LAUNCH.json could not be read from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
if (
  typeof launch !== 'object' ||
  launch === null ||
  typeof (launch as Record<string, unknown>).mint !== 'string' ||
  typeof (launch as Record<string, unknown>).create_signature !== 'string'
) {
  console.error('LAUNCH.json must be a JSON object with string "mint" and "create_signature" fields.');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(launchPath, join(OUTPUT_DIR, 'LAUNCH.json'));
} catch (err) {
  console.error(`Could not copy LAUNCH.json from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
