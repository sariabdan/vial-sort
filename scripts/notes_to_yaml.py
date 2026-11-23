#!/usr/bin/env python3
"""Turn the operator's notes from an arm test into the yaml build_data.py scores that model from.

    ~/lerobot/.venv/bin/python scripts/notes_to_yaml.py notes/A_16000.txt --model plain-bagel
    ~/lerobot/.venv/bin/python scripts/notes_to_yaml.py notes/A_16000.txt --model plain-bagel --force

A notes file is one line per move, as typed at the robot: "<n>: <source> <destination>: <what happened>",
e.g. "2: R3 L3: put in slot 2". Other lines (a header such as "A 16000: plain bagel") are skipped. A number
used twice gets a "b" the second time (25, 25b), as on the Docs pages.

What happened is read with a few rules, on the part after the last "then" (the final result):
didn't/couldn't grasp or grab -> no_grasp; success -> placed; stuck -> never_let_go; in front / behind / missed
placing / missed drop / dropped -> drop_missed at the asked slot, off_slot anywhere else; put / placed / went /
going for slot N -> off_slot at N; "same as" (and nothing else) -> the previous note's result. A line none of
these read stops the script, so nothing is guessed.

Reads models.yaml (the model's run) and src/data/rollouts.json (its recorded takes, in order). Each note gets
the takes of its move: restarts fold into the move, and build_data.py puts the note's result on the last take.
Writes notes/<same name>.yaml next to the notes; edit it by hand to fix a reading (it is not overwritten
without --force), then re-run scripts/build_data.py.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

SITE = Path(__file__).resolve().parents[1]

LINE = re.compile(r"^\s*(\d+)\s*:\s*([LR][1-6]|bin)\s+([LR][1-6]|bin)\s*:\s*(.*?)\s*$", re.I)
NO_GRASP = re.compile(r"\b(?:didn'?t|couldn'?t|did not|could not|won'?t)\s+(?:\w+\s+)?(?:grasp|grab|grip|pick)"
                      r"|\bmissed (?:the )?(?:pickup|pick up|grasp)|\bno grasp", re.I)
WRONG_VIAL = re.compile(r"\bwrong vial", re.I)
SUCCESS = re.compile(r"\bsucce(?:ss|ed)", re.I)
STUCK = re.compile(r"\bstuck\b|\bnever let go|\bdidn'?t let go|\bdid not let go", re.I)
DROP = re.compile(r"\bin fron|\bbehind\b|\bmissed plac|\bmissed (?:the )?drop|\bdropped\b", re.I)
SLOT = re.compile(r"\bslot\s*(\d)|\b(\d)(?:st|nd|rd|th)\s+slot", re.I)
BETWEEN = re.compile(r"\bbetween (?:slot )?(\d)\D{1,12}?(\d)", re.I)
SAME = re.compile(r"\bsame as\b", re.I)
RETRY = re.compile(r"\bat first\b|\bretr(?:y|ied)\b|\bran it twice\b|\bsecond try\b", re.I)

# outcome -> what it means, for the yaml's header and the printout
OUTCOMES = {
    "placed": "the vial ended in the asked slot",
    "drop_missed": "let go at the asked slot, the vial ended beside it (in front, behind, on the rack)",
    "off_slot": "let go at another slot (ended says which)",
    "never_let_go": "carried the vial and never let go",
    "no_grasp": "never picked the asked vial up",
    "wrong_vial": "picked up another vial",
}


def slot_of(m):
    return int(m.group(1) or m.group(2))


def read(src, dst, text, prev):
    """(outcome, ended, retried) of one note; None when no rule reads it."""
    final = re.split(r"\bthen\b", text, flags=re.I)[-1]
    before = text[: len(text) - len(final)]
    retried = bool(RETRY.search(text) or NO_GRASP.search(before) or WRONG_VIAL.search(before))
    rack = dst[0] if dst != "bin" else None

    def at(n):
        if rack is None:
            return None
        return f"{rack}{n}"

    if NO_GRASP.search(final):
        return "no_grasp", "source", retried
    if WRONG_VIAL.search(final):
        return "wrong_vial", "source", retried
    if SUCCESS.search(final):
        return "placed", dst, retried
    if STUCK.search(final):
        b = BETWEEN.search(final)
        return "never_let_go", (f"{at(b.group(1))}/{at(b.group(2))}" if b and rack else None), retried
    d = DROP.search(final)
    if d:
        s = SLOT.search(final, d.end()) or SLOT.search(final)
        ended = at(slot_of(s)) if s else dst
        if ended is None:
            return None
        return ("drop_missed" if ended == dst else "off_slot"), ended, retried
    s = SLOT.search(final)
    if s and rack:
        ended = at(slot_of(s))
        return ("placed" if ended == dst else "off_slot"), ended, retried
    if SAME.search(final) and prev:
        if prev["move"] == f"{src}->{dst}":
            return prev["outcome"], prev["ended"], retried
        if prev["outcome"] in ("no_grasp", "wrong_vial"):
            return prev["outcome"], "source", retried
    return None


def parse(path):
    notes, seen = [], Counter()
    for k, line in enumerate(path.read_text().splitlines(), 1):
        m = LINE.match(line)
        if not m:
            if line.strip() and re.match(r"^\s*\d+\s*:", line):
                sys.exit(f"{path}:{k}: starts like a move but doesn't read as '<n>: <source> <destination>: ...':\n  {line}")
            continue
        n, src, dst, text = m.groups()
        src, dst = (x.upper() if x.lower() != "bin" else "bin" for x in (src, dst))
        seen[n] += 1
        label = n + ("" if seen[n] == 1 else "bcdefgh"[seen[n] - 2])
        got = read(src, dst, text, notes[-1] if notes else None)
        if got is None:
            sys.exit(f"{path}:{k}: can't tell what happened in #{label} {src} -> {dst}: {text!r}\n"
                     f"  Reword the line, or write the yaml entry for it by hand.")
        outcome, ended, retried = got
        notes.append({"n": label, "move": f"{src}->{dst}", "outcome": outcome, "ended": ended,
                      "retried": retried, "note": text})
    if not notes:
        sys.exit(f"{path}: no '<n>: <source> <destination>: ...' lines")
    return notes


def takes_of(model, only):
    models = yaml.safe_load((SITE / "models.yaml").read_text())["models"]
    m = next((x for x in models if x["id"] == model), None)
    if m is None:
        sys.exit(f"no model {model!r} in models.yaml (ids: {', '.join(x['id'] for x in models)})")
    sessions = [s for s in json.loads((SITE / "src/data/rollouts.json").read_text())["sessions"] if s["run"] == m["run"]]
    if only:
        missing = set(only) - {s["name"] for s in sessions}
        if missing:
            sys.exit(f"not sessions of {model} ({m['run']}) in rollouts.json: {', '.join(sorted(missing))}")
        sessions = [s for s in sessions if s["name"] in only]
    if not sessions:
        sys.exit(f"rollouts.json has no sessions of {model} ({m['run']}): run scripts/build_data.py first")
    sessions.sort(key=lambda s: s["name"].split("_")[-2:])  # <step>[_tag]_<day>_<time>: by day and time
    return [s["name"] for s in sessions], [(t["id"], t["move"]) for s in sessions
                                          for t in sorted(s["takes"], key=lambda t: t["take"])]


def align(notes, takes):
    """Give every recorded take to a note of the same move, in order. A take stays on the current note while the
    move is the same, moves on to the next note with another move when that one matches, and goes back to one of the
    two notes before when it repeats their move (a pair of moves run twice). Notes in a row with the same move share
    their takes, one each, the extras on the last."""
    got = [[] for _ in notes]
    p = 0
    for tid, mv in takes:
        nxt = next((q for q in range(p + 1, len(notes)) if notes[q]["move"] != notes[p]["move"]), None)
        if notes[p]["move"] == mv:
            got[p].append(tid)
        elif nxt is not None and notes[nxt]["move"] == mv:  # past any notes repeating the current move
            p = nxt
            got[p].append(tid)
        else:
            back = next((q for q in (p - 1, p - 2) if q >= 0 and notes[q]["move"] == mv), None)
            if back is None:
                near = ", ".join(f"#{notes[q]['n']} {notes[q]['move']}" for q in range(max(0, p - 1), min(len(notes), p + 2)))
                sys.exit(f"take {tid} asked {mv}, which matches no note near here ({near}).\n"
                         f"  Was a move left out of the notes, or typed with another slot?")
            got[back].append(tid)
    order = {tid: i for i, (tid, _) in enumerate(takes)}
    i = 0
    while i < len(notes):
        j = i
        while j + 1 < len(notes) and notes[j + 1]["move"] == notes[i]["move"]:
            j += 1
        if j > i:
            pool = sorted((t for q in range(i, j + 1) for t in got[q]), key=order.get)
            for q in range(i, j):
                got[q] = pool[q - i: q - i + 1]
            got[j] = pool[j - i:]
        i = j + 1
    empty = [f"#{n['n']} {n['move']}" for n, g in zip(notes, got) if not g]
    if empty:
        sys.exit(f"no recorded take for {', '.join(empty)}: a move noted but not recorded, or the recording is in "
                 f"another session (--sessions)")
    for n, g in zip(notes, got):
        n["takes"] = g
    return notes


def q(s):
    return "null" if s is None else json.dumps(s, ensure_ascii=False)


def dump(path, model, sessions, notes):
    out = [f"# Written by scripts/notes_to_yaml.py from {path.relative_to(SITE)}: the operator's notes, one entry per noted move.",
           "# scripts/build_data.py scores these sessions from this file: one rollout per move, the result on its last take,",
           "# earlier takes counted as restarts. Fix a misreading here by hand; re-running the script needs --force.",
           "#",
           "# outcome:",
           *[f"#   {k:<13} {v}" for k, v in OUTCOMES.items()],
           "# ended: where the vial ended (a slot, bin, source = it never left, A/B = stuck between two slots, null = unknown)",
           "# retried: the note says it took more than one try",
           f"model: {model}",
           f"source: {path.relative_to(SITE)}",
           f"sessions: [{', '.join(q(s) for s in sessions)}]",
           "moves:"]
    for n in notes:
        out += [f"  - n: {q(n['n'])}",
                f"    move: {n['move']}",
                f"    outcome: {n['outcome']}",
                f"    ended: {n['ended'] or 'null'}",
                f"    retried: {'true' if n['retried'] else 'false'}",
                f"    note: {q(n['note'])}",
                f"    takes: [{', '.join(q(t) for t in n['takes'])}]"]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("notes", type=Path, help="the operator's notes, e.g. notes/A_16000.txt")
    ap.add_argument("--model", required=True, help="the model's id in models.yaml, e.g. plain-bagel")
    ap.add_argument("--sessions", help="comma-separated session names, when the model ran in sessions these notes don't cover")
    ap.add_argument("--force", action="store_true", help="overwrite an existing yaml (hand fixes in it are lost)")
    a = ap.parse_args()
    path = a.notes.resolve()
    if SITE not in path.parents:
        sys.exit(f"{a.notes}: put the notes inside the site repo (e.g. notes/), so the yaml beside them is found by build_data.py")
    target = path.with_suffix(".yaml")
    if target.exists() and not a.force:
        sys.exit(f"{target.relative_to(SITE)} exists (it may hold hand fixes): pass --force to overwrite it")
    notes = parse(path)
    sessions, takes = takes_of(a.model, a.sessions.split(",") if a.sessions else None)
    align(notes, takes)
    for n in notes:
        extra = f"  {len(n['takes'])} takes" if len(n["takes"]) > 1 else ""
        print(f"  {n['n']:>4}  {n['move'].replace('->', ' -> '):<12} {n['outcome']:<13} {n['ended'] or '-':<6}"
              f"{' retried' if n['retried'] else '':<8}{extra:<9} {n['note']}")
    tally = Counter(n["outcome"] for n in notes)
    print(f"{len(notes)} moves, {len(takes)} takes in {', '.join(sessions)}: "
          + ", ".join(f"{tally[k]} {k}" for k in OUTCOMES if tally[k]))
    target.write_text(dump(path, a.model, sessions, notes))
    print(f"wrote {target.relative_to(SITE)}")


if __name__ == "__main__":
    main()
