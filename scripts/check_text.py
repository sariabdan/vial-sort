#!/usr/bin/env python3
"""Catch words glued together in the built pages, and anything private that leaked into them.

    python3 scripts/check_text.py dist

Astro drops a line break that sits next to a {value}, so "over\\n{n} rollouts" builds as
"over79 rollouts". This reads the visible text of every page and flags those joins, then greps
every built file for LAN addresses, home paths and tokens. Exits 1 on any finding.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        self.skip += tag in ("script", "style", "pre", "code")

    def handle_endtag(self, tag):
        self.skip -= tag in ("script", "style", "pre", "code")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


# words that legitimately mix letters and digits; identifiers (pi05_base, vial-flux25) are skipped whole
OK = re.compile(r"^(?:bfloat16|MolmoAct2|v\d+|π0(?:\.5)?|[LR][1-6]|\d+k|\d+(?:st|nd|rd|th)|D435i|N1\.5|3D|av1|h264|\d+(?:px|fps|h))$", re.I)
GLUE = [re.compile(p) for p in (r"[a-z]{2,}\d", r"\d[a-z]{3,}", r"[a-z0-9][.;:,][A-Z]", r"\)[a-z]", r"[a-z]\(")]
PRIVATE = re.compile(r"192\.168\.|/home/|hf_[A-Za-z0-9]{10,}|gho_[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{10,}")


def glued(token):
    word = token.strip("“”\"'.,;:!?()[]")
    if not word or OK.match(word) or re.search(r"[_/=]|-.*\d|\d.*-", word):
        return False
    return any(g.search(token) for g in GLUE)


# Words the October pages must not use (they are defined terms: a "take" is a rollout, "gripped" was ambiguous).
# The August pages under previous/ keep their own vocabulary.
BANNED = re.compile(r"\b(?:gripped|gripping|(?:\d+|of|per|all|each|every|these|those|many|few|scored|short|more) takes?|(?:a|one|each|every) take)\b", re.I)


def lint_sources():
    """A line that ends in a word and the next starts an inline element can lose the space between them
    when Astro renders the page ("The\\n<a>results</a>" becomes "Theresults")."""
    bad = 0
    src = Path(__file__).resolve().parents[1] / "src"
    for f in list(src.rglob("*.astro")):
        text = f.read_text()
        body = text.split("---", 2)[2] if text.startswith("---") else text
        body = re.sub(r"<style>.*?</style>|<script>.*?</script>", "", body, flags=re.S)
        for m in re.finditer(r"[A-Za-z,.;:)]\n[ \t]*<(?:a|strong|code|em|span)\b", body):
            print(f"{f.relative_to(src.parent)}: line break before an inline element: ...{body[max(0, m.start() - 24): m.end()]!r}")
            bad += 1
    return bad


def main(root):
    bad = lint_sources()
    for page in sorted(Path(root).rglob("*.html")):
        p = Text()
        p.feed(page.read_text())
        if "previous" not in page.relative_to(root).parts:
            for m in BANNED.finditer(" ".join(p.parts)):
                print(f"{page.relative_to(root)}: banned word on an October page: {m.group(0)!r}")
                bad += 1
        for token in " ".join(p.parts).split():
            if glued(token):
                print(f"{page.relative_to(root)}: glued? {token}")
                bad += 1
    for f in Path(root).rglob("*"):
        if f.is_file() and f.suffix in (".html", ".js", ".json", ".css", ".txt", ".xml"):
            for m in PRIVATE.finditer(f.read_text(errors="ignore")):
                print(f"{f.relative_to(root)}: private? {m.group(0)}")
                bad += 1
    print("text check:", "clean" if not bad else f"{bad} finding(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "dist")
