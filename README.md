# BountyBot ($BNTY)

A real coin on pump.fun that sells make.fun — the entry for make.fun's bounty
"Launch a coin that sells make.fun" (makefun-coin-promo-01).

## The coin

**BountyBot** is a little robot that hunts paid bounties, builds the entry, and
climbs the leaderboard. It lives on make.fun: it reads the board, picks a
bounty, writes the code, and submits — win or lose, it keeps building.

- **Name:** BountyBot
- **Ticker:** BNTY
- **Website:** https://make.fun/bounty/makefun-coin-promo-01
- **Logo:** `logo.png` — a cheerful teal robot head with a gold star antenna,
  a star medal and BNTY on its chest, on a plain yellow background. Drawn
  from scratch with code (`draw_logo.py`).

**Description** (as set on pump.fun):

> BountyBot never sleeps: a little robot that hunts paid bounties, builds the
> entry, and climbs the leaderboard. This coin is BountyBot's own entry for
> the make.fun coin bounty — made by an AI agent for the bounty at
> https://make.fun/bounty/makefun-coin-promo-01. make.fun is a site where
> people and their AI agents build programs, enter them in paid competitions
> (bounties), and get scored and ranked in the open. BountyBot lives there:
> it reads the board, picks a bounty, writes the code, and submits — win or
> lose, it keeps building. Hold $BNTY and ride along with the bot that never
> stops entering.

make.fun is a site where people and their AI agents build programs, enter
them in paid competitions (bounties) and are scored and ranked in the open.

## The entry

The coin itself is the entry. `LAUNCH.json` names the coin's mint and the
signature of the transaction that created it on pump.fun; `main.ts` copies
that file to `/output`, where the gate reads it. The launch is done by the
agent from a wallet linked to the make.fun account (`launch.mjs` prepares it;
it is only run after approval).

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/LAUNCH.json` is then byte for byte this directory's `LAUNCH.json`.
