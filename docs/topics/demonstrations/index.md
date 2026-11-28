+++
title = "Demonstrations"
brand_sub = "the two sets · why the 220 · which moves · the wording · the batches · training copies · published · disagreements"
description = "The demonstrations the models learned from: the 100 and the 220, why the 220 were recorded the way they were, which moves they cover, how the commands are worded and the copies the models trained on."
components = ["toc", "nav", "filelinks", "panel-switcher"]
page_css = ["build-sheet.css"]
toc = [["The two sets", "#the-two-training-sets"], ["Why the 220", "#why-the-220-were-recorded-the-way-they-were"], ["Which moves", "#coverage-move-by-move"], ["Wording", "#how-the-commands-are-worded"], ["The batches", "#camera-differences-between-batches"], ["Training copies", "#training-copies-of-the-sets"], ["Published", "#where-the-data-is-published"], ["Disagreements", "#where-the-sources-disagree"]]
+++

# Demonstrations

<section class="card" id="the-two-training-sets">
<span id="scope"></span><span id="where-these-facts-come-from"></span><span id="what-a-demonstration-is"></span><span id="readings-at-commit-8065309"></span>

## The models learned from two sets: the 100, recorded in one afternoon, and the 220, which add 150 demonstrations

<p class="bs-lead">A demonstration is one move recorded while a person drives the leader arm; the 220 keep 70 of the 100 and add 51 recorded on 28 October and 99 on 3 November.</p>

<div class="bs-grid g2">
<figure id="fig-sets">
<svg class="inline-fig" viewBox="0 0 520 300" role="img" aria-label="What the two training sets are made of. The 100, recorded on 14 October: 70 kept in the 220 and 30, too dark, left out. The 220: those 70 from the 100, 51 recorded on 28 October and 99 on 3 November with the depth stream; the 150 new ones were recorded with three destinations per layout.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">the 100, recorded 14 Oct</text>
<rect x="10" y="40" width="159.091" height="40" rx="0" fill="#7d8896"/>
<rect x="169.091" y="40" width="68.1818" height="40" rx="0" fill="#121a24" stroke="#7d8896" stroke-width="2" stroke-dasharray="6 5"/>
<text x="89.5455" y="68" font-size="22" fill="#0d1117" text-anchor="middle" font-weight="600">70</text>
<text x="203.182" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600">30</text>
<text x="247.273" y="68" font-size="22" fill="#a9b4c2">too dark: not in the 220</text>
<text x="10" y="136" font-size="22" fill="#a9b4c2">the 220</text>
<rect x="10" y="150" width="159.091" height="40" rx="0" fill="#7d8896"/>
<rect x="169.091" y="150" width="115.909" height="40" rx="0" fill="#39d2c0"/>
<rect x="285" y="150" width="225" height="40" rx="0" fill="#bc8cff"/>
<text x="89.5455" y="178" font-size="22" fill="#0d1117" text-anchor="middle" font-weight="600">70</text>
<text x="227.045" y="178" font-size="22" fill="#0d1117" text-anchor="middle" font-weight="600">51</text>
<text x="397.5" y="178" font-size="22" fill="#0d1117" text-anchor="middle" font-weight="600">99</text>
<text x="10" y="222" font-size="22" fill="#7d8896">from the 100, 14 Oct</text>
<text x="169.091" y="252" font-size="22" fill="#39d2c0" font-weight="600">28 Oct</text>
<text x="510" y="222" font-size="22" fill="#bc8cff" text-anchor="end" font-weight="600">3 Nov, with depth</text>
<text x="169.091" y="282" font-size="22" fill="#e6edf3">three destinations per layout</text>
</g>
</svg>
<figcaption><b>Figure 1.</b> What the two sets are made of (<code>batches</code> in <code>src/data/ws220.json</code>, readings at commit <code>8065309</code>). Runs 15 to 20 of the 100 were dropped from the 220 as too dark. Drawn in the page source from the record.</figcaption>
</figure>
<div>
<div class="bs-specs"><div><span class="bs-label">The 100</span><b>58,650 frames</b></div><div><span class="bs-label">Length</span><b>33 min</b></div><div><span class="bs-label">Moves</span><b>32</b></div></div>
<div class="bs-specs"><div><span class="bs-label">The 220</span><b>141,735 frames</b></div><div><span class="bs-label">Length</span><b>79 min</b></div><div><span class="bs-label">Moves</span><b>48</b></div></div>
<div class="bs-part bs-teal"><span class="bs-label">The sets</span><ul>
<li>Both record the five colour cameras at 30 frames a second, as LeRobot datasets.</li>
<li>The 100 are published as <code>vial-sort-slots-100</code>, the 220 as <code>vial-sort-slots-220</code>.</li>
<li>On the 100: Spicy Chicken, Mango Rice, Pretzel One, Pretzel Two, Crispy Falafel. On the 220: Plain Bagel, Mango Pudding, Mango Lassi and its patched copies, and Isaac 0.5 Expert on 212 of them.</li>
</ul></div>
</div>
</div>

[Figure 1](#fig-sets) shows that the 220 are not all of one kind: 70 of them come from the 100 and were recorded one destination per run. The sizes are readings of the data at one commit ([the two training sets](demonstrations-record.html#the-two-training-sets), [readings at commit 8065309](demonstrations-record.html#readings-at-commit-8065309)). The website's [Data page](https://cognitive-software-labs.github.io/vial-sort/datasets/) shows both sets in full.

</section>

<section class="card" id="why-the-220-were-recorded-the-way-they-were">
<span id="the-100-demonstrations"></span>

## In the 100 each sitting had one destination, so the new 150 record one layout three times, to three destinations

<p class="bs-lead">When every scene of a sitting goes to the same place, the picture names the destination and a model need not read the command; three commands on one layout leave it nothing else.</p>

<div class="bs-grid g2">
<figure id="fig-contrast">
<svg class="inline-fig" viewBox="0 0 520 504" role="img" aria-label="Top: in the 100, every scene of one sitting goes to the same destination, so the picture gives the destination away. Bottom: in the 150 new demonstrations, one layout is recorded three times with three commands and three destinations, so only the command can tell them apart.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2" font-weight="600">the 100: one sitting, one destination</text>
<rect x="10" y="44" width="150" height="22" rx="4" fill="#121a24" stroke="#7d8896" stroke-width="1.5"/>
<text x="20" y="62" font-size="22" fill="#a9b4c2">scene 1</text>
<path d="M164 55L300 120" stroke="#7d8896" stroke-width="2"/>
<rect x="10" y="74" width="150" height="22" rx="4" fill="#121a24" stroke="#7d8896" stroke-width="1.5"/>
<text x="20" y="92" font-size="22" fill="#a9b4c2">scene 2</text>
<path d="M164 85L300 120" stroke="#7d8896" stroke-width="2"/>
<rect x="10" y="104" width="150" height="22" rx="4" fill="#121a24" stroke="#7d8896" stroke-width="1.5"/>
<text x="20" y="122" font-size="22" fill="#a9b4c2">scene 3</text>
<path d="M164 115L300 120" stroke="#7d8896" stroke-width="2"/>
<rect x="10" y="134" width="150" height="22" rx="4" fill="#121a24" stroke="#7d8896" stroke-width="1.5"/>
<text x="20" y="152" font-size="22" fill="#a9b4c2">scene 4</text>
<path d="M164 145L300 120" stroke="#7d8896" stroke-width="2"/>
<rect x="10" y="164" width="150" height="22" rx="4" fill="#121a24" stroke="#7d8896" stroke-width="1.5"/>
<text x="20" y="182" font-size="22" fill="#a9b4c2">scene 5</text>
<path d="M164 175L300 120" stroke="#7d8896" stroke-width="2"/>
<rect x="304" y="96" width="206" height="48" rx="8" fill="#121a24" stroke="#ff7b72" stroke-width="2.5"/>
<text x="407" y="128" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">one destination</text>
<text x="10" y="236" font-size="22" fill="#ff7b72">so the picture gives the destination away</text>
<text x="10" y="290" font-size="22" fill="#a9b4c2" font-weight="600">the new 150: one layout, three commands</text>
<rect x="10" y="340" width="150" height="60" rx="6" fill="#121a24" stroke="#39d2c0" stroke-width="2.5"/>
<text x="85" y="377" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">one layout</text>
<path d="M164 370L300 328" stroke="#39d2c0" stroke-width="2"/>
<rect x="304" y="310" width="206" height="40" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="407" y="337" font-size="22" fill="#e6edf3" text-anchor="middle">destination 1</text>
<path d="M164 370L300 380" stroke="#39d2c0" stroke-width="2"/>
<rect x="304" y="362" width="206" height="40" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="407" y="389" font-size="22" fill="#e6edf3" text-anchor="middle">destination 2</text>
<path d="M164 370L300 432" stroke="#39d2c0" stroke-width="2"/>
<rect x="304" y="414" width="206" height="40" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="407" y="441" font-size="22" fill="#e6edf3" text-anchor="middle">destination 3</text>
<text x="10" y="492" font-size="22" fill="#39d2c0">so only the command can tell them apart</text>
</g>
</svg>
<figcaption><b>Figure 2.</b> Why the 220 were recorded the way they were, as the Data page and the home page explain it. A schematic drawn in the page source from the record; it shows no recorded scene.</figcaption>
</figure>
<div class="bs-part bs-orange"><span class="bs-label">How the 100 were recorded, 14 October</span><ul>
<li><b>Twenty runs of five</b>, each in one sitting, one destination per run.</li>
<li><b>Always from the other rack</b>: 75 from one rack to the other, 25 to the bin, none inside a rack.</li>
<li><b>Colour never identifies the vial</b>: in 95 of the 100 scenes a second vial of the target's colour stands on the source rack.</li>
<li><b>The bin moves</b> every ten demonstrations; <b>the light fades</b> through the afternoon.</li>
<li><b>The operator is in view</b> at the start, leaning over the robot.</li>
<li>The wrist camera dropped off the bus three times; those three were recorded again.</li>
</ul></div>
</div>

[Figure 2](#fig-contrast) is the reason for the second set. The Lab notes call the new demonstrations "contrastive", and the 12-move gate tests a model the same way, a fixed layout with only the destination changed ([why the 220 were recorded the way they were](demonstrations-record.html#why-the-220-were-recorded-the-way-they-were), [Evaluation](evaluation.html#the-12-move-gate)). What the first models learned from the 100 is in [Training](training.html).

</section>

<section class="card" id="coverage-move-by-move">
<span id="held-out"></span>

## Both sets leave out the same slots on purpose; the 220 add moves inside one rack, with two gaps

<p class="bs-lead">Slots 2 and 5 are never a source and slots 2, 4 and 5 never a destination in either set; the 220 cover every other move between trained slots except L1 → L6 and L4 → L3.</p>

<div class="bs-grid g2">
<figure id="fig-coverage">
<div class="panel-switcher" data-panel-switcher data-panel-default="ws220">
<div class="panel-switcher-controls" role="group" aria-label="Demonstration set shown">
<button type="button" data-panel-choice="ws100" aria-pressed="false" aria-controls="coverage-100">The 100</button>
<button type="button" data-panel-choice="ws220" aria-pressed="false" aria-controls="coverage-220">The 220</button>
</div>
<div id="coverage-100" data-panel="ws100">
<svg class="inline-fig" viewBox="0 0 420 436" role="img" aria-label="Which moves the 100 cover: from each trained source slot, L1, L3, L4, L6, R1, R3, R4 and R6, to the three trained slots of the other rack and to the bin. No move stays inside a rack. 32 moves.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="237.5" y="22" font-size="22" fill="#a9b4c2" text-anchor="middle">destination</text>
<text x="90.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L1</text>
<text x="139.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L3</text>
<text x="188.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L6</text>
<text x="237.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R1</text>
<text x="286.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R3</text>
<text x="335.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R6</text>
<text x="384.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">bin</text>
<text x="56" y="107" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L1</text>
<text x="90.5" y="107" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="218" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="151" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L3</text>
<text x="139.5" y="151" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="218" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="195" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L4</text>
<rect x="218" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="239" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L6</text>
<text x="188.5" y="239" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="218" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="283" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R1</text>
<rect x="71" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="237.5" y="283" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="365" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="327" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R3</text>
<rect x="71" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="286.5" y="327" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="365" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="371" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R4</text>
<rect x="71" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="415" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R6</text>
<rect x="71" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="335.5" y="415" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="365" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
</g>
</svg>
</div>
<div id="coverage-220" data-panel="ws220">
<svg class="inline-fig" viewBox="0 0 420 436" role="img" aria-label="Which moves the 220 cover: every move from a trained source slot to a trained destination slot or the bin, moves inside one rack included, except L1 to L6 and L4 to L3. 48 moves.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="237.5" y="22" font-size="22" fill="#a9b4c2" text-anchor="middle">destination</text>
<text x="90.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L1</text>
<text x="139.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L3</text>
<text x="188.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L6</text>
<text x="237.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R1</text>
<text x="286.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R3</text>
<text x="335.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R6</text>
<text x="384.5" y="68" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">bin</text>
<text x="56" y="107" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L1</text>
<text x="90.5" y="107" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="120" y="84" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="169" y="84" width="39" height="32" rx="4" fill="none" stroke="#ff7b72" stroke-width="2.5"/>
<text x="188.5" y="108" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">×</text>
<rect x="218" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="84" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="151" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L3</text>
<rect x="71" y="128" width="39" height="32" rx="4" fill="#bc8cff"/>
<text x="139.5" y="151" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="169" y="128" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="218" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="128" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="195" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L4</text>
<rect x="71" y="172" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="120" y="172" width="39" height="32" rx="4" fill="none" stroke="#ff7b72" stroke-width="2.5"/>
<text x="139.5" y="196" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">×</text>
<rect x="169" y="172" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="218" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="172" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="239" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L6</text>
<rect x="71" y="216" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="120" y="216" width="39" height="32" rx="4" fill="#bc8cff"/>
<text x="188.5" y="239" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="218" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="267" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="316" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="365" y="216" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="283" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R1</text>
<rect x="71" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="237.5" y="283" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="267" y="260" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="316" y="260" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="365" y="260" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="327" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R3</text>
<rect x="71" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="218" y="304" width="39" height="32" rx="4" fill="#bc8cff"/>
<text x="286.5" y="327" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="316" y="304" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="365" y="304" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="371" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R4</text>
<rect x="71" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="218" y="348" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="267" y="348" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="316" y="348" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="365" y="348" width="39" height="32" rx="4" fill="#39d2c0"/>
<text x="56" y="415" font-size="22" fill="#a9b4c2" text-anchor="end" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R6</text>
<rect x="71" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="120" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="169" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
<rect x="218" y="392" width="39" height="32" rx="4" fill="#bc8cff"/>
<rect x="267" y="392" width="39" height="32" rx="4" fill="#bc8cff"/>
<text x="335.5" y="415" font-size="22" fill="#7d8896" text-anchor="middle">–</text>
<rect x="365" y="392" width="39" height="32" rx="4" fill="#39d2c0"/>
</g>
</svg>
</div>
</div>
<figcaption><b>Figure 3.</b> Which moves each set has at least one demonstration of, source by destination, for the trained slots. Teal: between the racks or to the bin; violet: inside one rack; red ×: no demonstration. Drawn in the page source from the record's rules and counts (32 moves in the 100, 48 in the 220), not from the per-move counts in the data.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">Read the figure</span><ul>
<li><b>Held out</b>: slots 2 and 5 never a source, slots 2, 4 and 5 never a destination, so slot 4 is only ever a source. They test whether a model can reach slots no demonstration used.</li>
<li><b>The 100</b>: 32 moves, none inside a rack; each source slot has 11 to 13 demonstrations.</li>
<li><b>The 220</b>: 48 moves, 51 demonstrations inside one rack and 41 to the bin.</li>
<li><b>Two gaps</b>: the Data page names L1 → L6; the data also has no L4 → L3. The 12-move gate used L1 → L6 anyway.</li>
</ul></div>
</div>

[Figure 3](#fig-coverage) shows the two sets side by side; choose a set above the matrix. The same-rack moves come only from the 150 new demonstrations. How many demonstrations each move has is in the data and on the Data page ([coverage move by move](demonstrations-record.html#coverage-move-by-move), [held out](demonstrations-record.html#held-out)).

</section>

<section class="card" id="how-the-commands-are-worded">

## Each part of a command comes from its own pool, so one rack-to-rack move has 38,400 possible wordings; the training copies keep one

<p class="bs-lead">A command names the source by slot and rack and the destination by slot and rack or the bin, never by colour, and the k-th demonstration of a move gets the k-th combination, so repeats are phrased differently.</p>

<div class="bs-grid g2">
<figure id="fig-wordings">
<svg class="inline-fig" viewBox="0 0 520 432" role="img" aria-label="The wording pools of the 100: 6 verbs, times 4 objects, times 5 slot forms by 4 rack forms for the source and again for the destination, times 4 sentence forms, gives 38,400 wordings of one rack-to-rack move; with 5 bin names in place of the destination, 9,600 for a move to the bin. The 100 recorded 100 wordings, one per demonstration, at most 4 for one move.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<rect x="10" y="12" width="152" height="80" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="86" y="50" font-size="28" fill="#39d2c0" text-anchor="middle" font-weight="600">6</text>
<text x="86" y="80" font-size="22" fill="#a9b4c2" text-anchor="middle">verbs</text>
<text x="172" y="60" font-size="26" fill="#a9b4c2" text-anchor="middle">×</text>
<rect x="182" y="12" width="152" height="80" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="258" y="50" font-size="28" fill="#39d2c0" text-anchor="middle" font-weight="600">4</text>
<text x="258" y="80" font-size="22" fill="#a9b4c2" text-anchor="middle">objects</text>
<text x="344" y="60" font-size="26" fill="#a9b4c2" text-anchor="middle">×</text>
<rect x="354" y="12" width="152" height="80" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="430" y="50" font-size="28" fill="#39d2c0" text-anchor="middle" font-weight="600">5 × 4</text>
<text x="430" y="80" font-size="22" fill="#a9b4c2" text-anchor="middle">source</text>
<text x="10" y="136" font-size="26" fill="#a9b4c2">×</text>
<rect x="44" y="104" width="170" height="80" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="129" y="142" font-size="28" fill="#39d2c0" text-anchor="middle" font-weight="600">5 × 4</text>
<text x="129" y="172" font-size="22" fill="#a9b4c2" text-anchor="middle">destination</text>
<text x="229" y="152" font-size="26" fill="#a9b4c2" text-anchor="middle">×</text>
<rect x="244" y="104" width="170" height="80" rx="8" fill="#121a24" stroke="#39d2c0" stroke-width="2"/>
<text x="329" y="142" font-size="28" fill="#39d2c0" text-anchor="middle" font-weight="600">4</text>
<text x="329" y="172" font-size="22" fill="#a9b4c2" text-anchor="middle">sentences</text>
<text x="10" y="232" font-size="24" fill="#e6edf3" font-weight="600">= 38,400 wordings of one</text>
<text x="10" y="262" font-size="24" fill="#e6edf3" font-weight="600">rack-to-rack move</text>
<text x="10" y="300" font-size="22" fill="#a9b4c2">to the bin, 5 bin names in place of</text>
<text x="10" y="328" font-size="22" fill="#a9b4c2">the destination: 9,600</text>
<path d="M10 352L510 352" stroke="#2f3b4a" stroke-width="2"/>
<text x="10" y="386" font-size="24" fill="#bc8cff" font-weight="600">recorded in the 100: 100 wordings,</text>
<text x="10" y="416" font-size="22" fill="#bc8cff">one per demonstration, at most 4 a move</text>
</g>
</svg>
<figcaption><b>Figure 4.</b> The wording pools of the 100 and the number of wordings they multiply to, as the Data page computes them (<code>coverage.pools</code> in <code>src/data/october.json</code>, readings at commit <code>8065309</code>). Design arithmetic, not a count of recorded wordings. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-violet"><span class="bs-label">How the wording was made</span><ul>
<li><b>Afterwards</b>: a run was recorded with its destination only; one script then read the recording sheet and rewrote every command. No video was touched.</li>
<li><b>Not at random</b>: the k-th demonstration of a move gets the k-th combination.</li>
<li>The example move <code>R3->L6</code> has three recorded wordings; slot 6 has "the last slot" in place of "spot 6".</li>
<li><b>The training copies</b> replace them with one sentence per move. How the published 220 word their commands is not stated.</li>
</ul></div>
</div>

[Figure 4](#fig-wordings) shows how far the recorded wordings are from the possible ones: 100 against tens of thousands per move. The models then trained on one sentence per move anyway ([how the commands are worded](demonstrations-record.html#how-the-commands-are-worded)). What a command looks like at the robot is in [Task and rig](task-and-rig.html#what-a-command-looks-like).

</section>

<section class="card" id="camera-differences-between-batches">
<span id="recording-batches-of-the-220"></span><span id="known-problems"></span>

## The three batches differ in light, in where one camera stood and in how the vial was released

<p class="bs-lead">The old 70 were recorded in fading light, with the across-the-table camera in another place and with a flatter wrist at release than the 150 new ones.</p>

<div class="bs-grid g2">
<figure id="fig-release">
<svg class="inline-fig" viewBox="0 0 520 238" role="img" aria-label="The wrist pitch at release: the old 70 released with a flatter wrist, wrist_flex minus 28 to minus 43 degrees, than the batches of 28 October and 3 November, minus 42 to minus 61.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">wrist_flex at release, degrees</text>
<path d="M80 44L80 196" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="80" y="226" font-size="22" fill="#7d8896" text-anchor="middle">-60</text>
<path d="M220 44L220 196" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="220" y="226" font-size="22" fill="#7d8896" text-anchor="middle">-40</text>
<path d="M360 44L360 196" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="360" y="226" font-size="22" fill="#7d8896" text-anchor="middle">-20</text>
<path d="M500 44L500 196" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="500" y="226" font-size="22" fill="#7d8896" text-anchor="end">0</text>
<text x="10" y="66" font-size="22" fill="#7d8896">the old 70, from the 100</text>
<rect x="199" y="76" width="105" height="30" rx="4" fill="#7d8896"/>
<text x="10" y="140" font-size="22" fill="#39d2c0">batches of 28 Oct and 3 Nov</text>
<rect x="73" y="150" width="133" height="30" rx="4" fill="#39d2c0"/>
</g>
</svg>
<figcaption><b>Figure 5.</b> The wrist pitch at release in the old 70 and in the two new batches, as the 9 Nov Lab note gives the ranges. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-orange"><span class="bs-label">What differs between batches</span><ul>
<li><b>Light</b>: the side cameras are almost black late in the 100; runs 15 to 20 were dropped from the 220.</li>
<li><b>The across-the-table camera</b> (<code>left_top</code>) sits slightly differently in the first 70 than in the later 150; 28 October is within a pixel of 3 November. It was bumped again on 4 Nov, after every recording.</li>
<li><b>Depth</b>: only the 3 November sitting has the RealSense depth stream; it is not in the 220 and no model trains on it.</li>
<li><b>Racks</b>: the pan per slot is the same in all three batches within 2–3°, so the racks have not moved sideways.</li>
</ul></div>
</div>

[Figure 5](#fig-release) shows the one difference in how the person demonstrated. The batches carry three sets of names: <code>ws100</code>, <code>contrast</code> and <code>contrast+depth</code> in the data; the first 70, first sitting and second sitting on the Data page; the old 70, batch 1 and batch 2 in the Lab notes ([camera differences between batches](demonstrations-record.html#camera-differences-between-batches), [known problems](demonstrations-record.html#known-problems)). The camera bump is drawn in [Task and rig](task-and-rig.html#camera-position-changes).

</section>

<section class="card" id="training-copies-of-the-sets">

## The models trained on cleaned copies with the idle start and end cut, not on the published sets

<p class="bs-lead">The cleaned copy of the 220 has 113,010 of its 141,735 frames: the idle start and end of each demonstration are cut, the operator is removed from the start frames and each move has one sentence.</p>

<div class="bs-grid g2">
<figure id="fig-copies">
<svg class="inline-fig" viewBox="0 0 520 596" role="img" aria-label="Frames of each copy the models trained on. The 100 as recorded, 58,650, for Spicy Chicken and Crispy Falafel. The first trim, 42,089, for Pretzel One. Trimmed at the let-go and cleaned, 46,361, for Pretzel Two and Mango Rice. The 220 as published, 141,735, not trained on as published. The 220 cleaned, 113,010, for Plain Bagel, Mango Pudding and Mango Lassi. The 220 minus 8, 108,253, for Isaac 0.5 Expert.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="28" font-size="22" fill="#e6edf3" font-weight="600">the 100, as recorded</text>
<rect x="10" y="38" width="194.486" height="26" rx="3" fill="#7d8896"/>
<text x="196.486" y="58" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">58,650</text>
<text x="10" y="90" font-size="22" fill="#7d8896">Spicy Chicken, Crispy Falafel</text>
<text x="10" y="126" font-size="22" fill="#e6edf3" font-weight="600">first trim</text>
<rect x="10" y="136" width="139.569" height="26" rx="3" fill="#39d2c0"/>
<text x="141.569" y="156" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">42,089</text>
<text x="10" y="188" font-size="22" fill="#7d8896">Pretzel One</text>
<text x="10" y="224" font-size="22" fill="#e6edf3" font-weight="600">trimmed at the let-go, cleaned</text>
<rect x="10" y="234" width="153.735" height="26" rx="3" fill="#39d2c0"/>
<text x="155.735" y="254" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">46,361</text>
<text x="10" y="286" font-size="22" fill="#7d8896">Pretzel Two, Mango Rice</text>
<text x="10" y="322" font-size="22" fill="#e6edf3" font-weight="600">the 220, published</text>
<rect x="10" y="332" width="470" height="26" rx="3" fill="#7d8896"/>
<text x="472" y="352" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">141,735</text>
<text x="10" y="384" font-size="22" fill="#7d8896">not trained on as published</text>
<text x="10" y="420" font-size="22" fill="#e6edf3" font-weight="600">the 220, cleaned</text>
<rect x="10" y="430" width="374.747" height="26" rx="3" fill="#bc8cff"/>
<text x="376.747" y="450" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">113,010</text>
<text x="10" y="482" font-size="22" fill="#7d8896">Plain Bagel, Mango Pudding, Mango Lassi</text>
<text x="10" y="518" font-size="22" fill="#e6edf3" font-weight="600">the 220 minus 8</text>
<rect x="10" y="528" width="358.972" height="26" rx="3" fill="#79c0ff"/>
<text x="360.972" y="548" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">108,253</text>
<text x="10" y="580" font-size="22" fill="#7d8896">Isaac 0.5 Expert</text>
</g>
</svg>
<figcaption><b>Figure 6.</b> Frames of each copy the models trained on, with the models that used it (<code>data</code> and <code>frames</code> in <code>src/data/registry.json</code>, <code>trim_frames</code> in <code>src/data/october.json</code>). Bars share one scale. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">What each copy changed</span><ul>
<li><b>First trim</b>: cut at the first loosening of the gripper; corrected to the real let-go for Pretzel Two and Mango Rice.</li>
<li><b>Operator-free start</b>: the start frames that showed the operator replaced by views of the arm with nobody near it; for Isaac 0.5 Expert on the wrist camera only.</li>
<li><b>One sentence per move</b>, in place of the varied wordings.</li>
<li>Which 8 demonstrations Isaac 0.5 Expert's copy leaves out, and why, is not stated.</li>
</ul></div>
</div>

[Figure 6](#fig-copies) shows how much each copy cut. The trimmed and canonical-wording copies are not among the published datasets ([training copies of the sets](demonstrations-record.html#training-copies-of-the-sets)). Why each change was made is in [Training](training.html#data-preparation-that-training-depends-on).

</section>

<section class="card" id="where-the-data-is-published">
<span id="earlier-demonstration-sets"></span>

## Four demonstration sets of the current rig are public on Hugging Face, beside the earlier sets of the August rig

<p class="bs-lead">The 100, the 220 and the two new batches alone are published in LeRobot format at 30 frames a second, and each episode can be watched in the LeRobot visualizer.</p>

<div class="scroll" role="region" aria-label="The published demonstration sets of the current rig" tabindex="0" data-reader-horizontal>
<table>
<thead><tr><th>Set</th><th>Episodes</th><th>Frames</th><th>Uploaded</th><th>Holds</th></tr></thead>
<tbody>
<tr><th><code>vial-sort-slots-100</code></th><td>100</td><td>58,650</td><td>2026-10-14</td><td>the 100</td></tr>
<tr><th><code>vial-sort-slots-220</code></th><td>220</td><td>141,735</td><td>2026-11-10</td><td>all three batches</td></tr>
<tr><th><code>vial-sort-contrast-51</code></th><td>51</td><td>36,420</td><td>2026-11-10</td><td>the batch of 28 Oct</td></tr>
<tr><th><code>vial-sort-contrast-99-depth</code></th><td>99</td><td>60,993</td><td>2026-11-10</td><td>the batch of 3 Nov, with <code>rs_depth</code></td></tr>
</tbody>
</table>
</div>

<div class="bs-grid g2">
<div class="bs-part bs-muted"><span class="bs-label">Earlier sets, August rig</span><ul>
<li>Six sets, <code>vial-sort-v1-static</code> to <code>vial-sort-v5</code>, uploaded 2026-06-07 to 2026-08-22, 40 to 150 episodes, with the cameras <code>cam_top</code>, <code>cam_wrist</code> and <code>cam_side</code>.</li>
<li>The August page calls them "versions 1 to 5"; no version 3 is listed.</li>
<li><code>vial-flux25</code>, 25 demonstrations of one task, is named only as Sweet Corn's training data.</li>
</ul></div>
<div class="bs-part bs-teal"><span class="bs-label">To find them</span><ul>
<li>The website's <a href="https://cognitive-software-labs.github.io/vial-sort/datasets/">Data page</a> lists every published set and the rollout recordings beside them.</li>
<li>The record maps each field to <code>datasets</code> in <code>src/data/datasets.json</code>.</li>
</ul></div>
</div>

The table gives the published sets as read at commit `8065309` ([where the data is published](demonstrations-record.html#where-the-data-is-published), [earlier demonstration sets](demonstrations-record.html#earlier-demonstration-sets)). The August rig is described in [Task and rig](task-and-rig.html#earlier-rigs).

</section>

<section class="card" id="where-the-sources-disagree">
<span id="not-verified"></span>

## The sources disagree on which runs were dark and on what "held out" means, and no number was checked against the recordings

<p class="bs-lead">The recordings and the recording sheets are on the workstation, so where the website's pages and the data disagree the record lists both sides.</p>

<div class="bs-grid g2">
<div class="bs-part bs-orange"><span class="bs-label">Where the sources disagree</span><ul>
<li><b>Which dark runs</b>: runs 15 to 20 dropped as too dark, 30 demonstrations; the side cameras almost black in demonstrations 75 to 99, 25 demonstrations.</li>
<li><b>"One layout recorded three times"</b> is said of the whole 220, while 70 of them come from the 100.</li>
<li><b>Gaps</b>: the Data page names one, L1 → L6; the data also has no L4 → L3.</li>
<li><b>"Held out"</b> means slots never recorded in the glossary, and 8 demonstrations removed from Isaac 0.5 Expert's copy in the data.</li>
<li><b>The third vial colour</b> is "dark green", "lime" or "green".</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Not verified</span><ul>
<li>No number was re-derived from the recordings, and no script of the repository was run.</li>
<li>How the published 220 word their commands is not stated.</li>
<li>Whether the 150 new demonstrations are exactly 17 and 33 layouts of three destinations each is not stated.</li>
<li>The record was written by AI agents and waits for a <a href="docs.open.human-review.md.html">review by a person</a>.</li>
</ul></div>
</div>

Every disagreement and open point is in the record with its sources ([where the sources disagree](demonstrations-record.html#where-the-sources-disagree), [not verified](demonstrations-record.html#not-verified)). The two meanings of "held out" are an open decision in the project's [list of terms](docs.development.conventions.md.html#terms).

</section>
