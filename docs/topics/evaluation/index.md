+++
title = "Evaluation"
brand_sub = "the score · why · stages · notes or arm · left out · the rollout · the 12-move gate · caveats"
description = "How a model is tested on the arm and scored: the score of a run, the three outcome stages, scoring from the operator's notes or from the arm, the 12-move gate and what the numbers cannot say."
components = ["toc", "nav", "filelinks", "code"]
page_css = ["build-sheet.css"]
toc = [["The score", "#the-score-of-a-run"], ["Why this score", "#why-it-is-built-this-way"], ["Three stages", "#the-three-outcome-stages"], ["Notes or arm", "#how-a-rollout-is-scored"], ["Left out", "#what-is-scored-and-what-is-left-out"], ["A rollout", "#how-a-rollout-is-run"], ["12-move gate", "#the-12-move-gate"], ["Cannot say", "#what-the-numbers-cannot-say"], ["Disagreements", "#where-sources-disagree"]]
+++

# Evaluation

<section class="card" id="the-score-of-a-run">
<span id="scope"></span><span id="definition"></span><span id="worked-out-on-one-run"></span>

## A run's score is the mean of its 12 rack-slot shares; it passes only at 70% with 10 rollouts at every slot

<p class="bs-lead">For each rack slot, the score takes the share of rollouts asked to end there that ended in the asked slot, and averages those shares; the bin is left out.</p>

<div class="bs-grid g2">
<figure id="fig-score">
<svg class="inline-fig" viewBox="0 0 520 520" role="img" aria-label="The share of rollouts in the asked slot at each of the 12 rack slots, for Isaac 0.5 Expert at 21k in sync mode. Left rack: L1 2 of 2, L2 5 of 5, L3 2 of 2, L4 0 of 5, L5 0 of 5, L6 2 of 2. Right rack: R1 2 of 2, R2 4 of 5, R3 1 of 2, R4 0 of 5, R5 0 of 5, R6 2 of 2. A dashed line marks the 70% pass mark.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="24" font-size="24" fill="#a9b4c2">left rack</text>
<path d="M46 91L512 91" stroke="#ffa657" stroke-width="2" stroke-dasharray="6 5"/>
<text x="8" y="85" font-size="22" fill="#ffa657" font-weight="600">70%</text>
<path d="M46 196L512 196" stroke="#2f3b4a" stroke-width="2"/>
<rect x="58" y="46" width="44" height="150" rx="3" fill="#39d2c0"/>
<text x="80" y="224" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L1</text>
<text x="80" y="252" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">2/2</text>
<rect x="138" y="46" width="44" height="150" rx="3" fill="#bc8cff"/>
<text x="160" y="224" font-size="22" fill="#bc8cff" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L2</text>
<text x="160" y="252" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">5/5</text>
<rect x="218" y="46" width="44" height="150" rx="3" fill="#39d2c0"/>
<text x="240" y="224" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L3</text>
<text x="240" y="252" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">2/2</text>
<rect x="298" y="192" width="44" height="4" rx="1" fill="#bc8cff"/>
<text x="320" y="224" font-size="22" fill="#bc8cff" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L4</text>
<text x="320" y="252" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">0/5</text>
<rect x="378" y="192" width="44" height="4" rx="1" fill="#bc8cff"/>
<text x="400" y="224" font-size="22" fill="#bc8cff" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L5</text>
<text x="400" y="252" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">0/5</text>
<rect x="458" y="46" width="44" height="150" rx="3" fill="#39d2c0"/>
<text x="480" y="224" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">L6</text>
<text x="480" y="252" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">2/2</text>
<text x="10" y="286" font-size="24" fill="#a9b4c2">right rack</text>
<path d="M46 353L512 353" stroke="#ffa657" stroke-width="2" stroke-dasharray="6 5"/>
<text x="8" y="347" font-size="22" fill="#ffa657" font-weight="600">70%</text>
<path d="M46 458L512 458" stroke="#2f3b4a" stroke-width="2"/>
<rect x="58" y="308" width="44" height="150" rx="3" fill="#39d2c0"/>
<text x="80" y="486" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R1</text>
<text x="80" y="514" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">2/2</text>
<rect x="138" y="338" width="44" height="120" rx="3" fill="#bc8cff"/>
<text x="160" y="486" font-size="22" fill="#bc8cff" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R2</text>
<text x="160" y="514" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">4/5</text>
<rect x="218" y="383" width="44" height="75" rx="3" fill="#39d2c0"/>
<text x="240" y="486" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R3</text>
<text x="240" y="514" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">1/2</text>
<rect x="298" y="454" width="44" height="4" rx="1" fill="#bc8cff"/>
<text x="320" y="486" font-size="22" fill="#bc8cff" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R4</text>
<text x="320" y="514" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">0/5</text>
<rect x="378" y="454" width="44" height="4" rx="1" fill="#bc8cff"/>
<text x="400" y="486" font-size="22" fill="#bc8cff" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R5</text>
<text x="400" y="514" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">0/5</text>
<rect x="458" y="308" width="44" height="150" rx="3" fill="#39d2c0"/>
<text x="480" y="486" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">R6</text>
<text x="480" y="514" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">2/2</text>
</g>
</svg>
<figcaption><b>Figure 1.</b> The score worked out on one run, Isaac 0.5 Expert · 21k · sync: the share in the asked slot at each rack slot, with the rollouts behind it. Teal: slots 1, 3 and 6, the destinations the demonstrations used; violet: slots 2, 4 and 5, held out. From <code>by_destination</code> in <code>src/data/results.json</code> at commit <code>8065309</code>; drawn in the page source from the record.</figcaption>
</figure>
<div>
<div class="bs-specs"><div><span class="bs-label">Trained slots</span><b>91.7%</b></div><div><span class="bs-label">Held-out slots</span><b>30%</b></div><div><span class="bs-label">Score</span><b>60.8% ≈ 61%</b></div></div>
<div class="bs-part bs-teal"><span class="bs-label">The definition</span><ul>
<li><b>Share of a slot</b>: rollouts that ended in the asked slot, over the rollouts asked to end there.</li>
<li><b>Score</b>: the plain mean of the shares of the rack slots that had at least one rollout. The trained-slot and held-out shares are the same mean over slots 1, 3, 6 and over 2, 4, 5 of both racks.</li>
<li><b>Pass</b>: at least 10 rollouts at every one of the 12 rack slots, and a score of at least 70%. Otherwise "Below 70%", or "Disqualified: under 10 rollouts at k of 12 slots".</li>
<li><b>Weak slot</b>: a slot at 50% or less.</li>
</ul></div>
</div>
</div>

[Figure 1](#fig-score) shows the score on the newest run scored from the operator's notes. Its six trained slots average 91.7% and its six held-out slots 30%, so the score is 60.8%; with 2 to 5 rollouts per slot it is still disqualified. Pooled over every rollout it would be 20 of 42, 48%, and the median of its shares is 90%: four slots at 0% pull the mean down where a median would hide them. The score is defined once, in `src/lib/score.ts`, "as agreed with the supervisor on 24 Nov 2026" ([the score of a run](evaluation-record.html#the-score-of-a-run)). What the runs scored is in [Results](results.html).

</section>

<section class="card" id="why-it-is-built-this-way">
<span id="the-fixed-slot-split-and-the-training-sets"></span>

## Every slot counts the same, and the 70% bar is on the mean, not on each slot

<p class="bs-lead">A per-slot mean stops the slots tried most from deciding the score, and a bar on the mean keeps luck at ten rollouts from failing a good model.</p>

<div class="bs-grid g2">
<figure id="fig-why-mean">
<svg class="inline-fig" viewBox="0 0 520 418" role="img" aria-label="Top: twelve slot shares, seven at 80% and five at 0%. Their median is 80%, their mean 47%. Bottom: for a model that really works 80% of the time at every slot, the chance that one slot scores 6 of 10 or less is 0.121, and the chance that at least one of 12 slots scores below 7 of 10 is 0.79.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="24" fill="#a9b4c2">seven slots at 80%, five at 0%</text>
<path d="M20 150L500 150" stroke="#2f3b4a" stroke-width="2"/>
<path d="M20 146L20 156" stroke="#7d8896" stroke-width="2"/>
<text x="20" y="182" font-size="22" fill="#7d8896">0%</text>
<path d="M260 146L260 156" stroke="#7d8896" stroke-width="2"/>
<text x="260" y="182" font-size="22" fill="#7d8896" text-anchor="middle">50%</text>
<path d="M500 146L500 156" stroke="#7d8896" stroke-width="2"/>
<text x="500" y="182" font-size="22" fill="#7d8896" text-anchor="end">100%</text>
<circle cx="20" cy="134" r="8" fill="#ff7b72"/>
<circle cx="20" cy="114" r="8" fill="#ff7b72"/>
<circle cx="20" cy="94" r="8" fill="#ff7b72"/>
<circle cx="20" cy="74" r="8" fill="#ff7b72"/>
<circle cx="20" cy="54" r="8" fill="#ff7b72"/>
<circle cx="404.0" cy="134" r="7" fill="#39d2c0"/>
<circle cx="404.0" cy="120" r="7" fill="#39d2c0"/>
<circle cx="404.0" cy="106" r="7" fill="#39d2c0"/>
<circle cx="404.0" cy="92" r="7" fill="#39d2c0"/>
<circle cx="404.0" cy="78" r="7" fill="#39d2c0"/>
<circle cx="404.0" cy="64" r="7" fill="#39d2c0"/>
<circle cx="404.0" cy="50" r="7" fill="#39d2c0"/>
<path d="M245.6 40L245.6 150" stroke="#ffa657" stroke-width="3"/>
<text x="253.6" y="62" font-size="24" fill="#ffa657" font-weight="600">mean 47%</text>
<text x="420" y="74" font-size="24" fill="#e6edf3" font-weight="600">median</text>
<text x="420" y="100" font-size="24" fill="#e6edf3" font-weight="600">80%</text>
<text x="10" y="226" font-size="22" fill="#a9b4c2">a model really 80% good at every slot,</text>
<text x="10" y="252" font-size="22" fill="#a9b4c2">with 10 rollouts at each:</text>
<text x="10" y="292" font-size="22" fill="#e6edf3">one slot at 6 of 10 or less</text>
<rect x="10" y="302" width="58.08" height="30" rx="3" fill="#bc8cff"/>
<text x="76.08" y="325" font-size="22" fill="#bc8cff" font-weight="600">0.121</text>
<text x="10" y="366" font-size="22" fill="#e6edf3">at least one of 12 slots below 7 of 10</text>
<rect x="10" y="376" width="379.2" height="30" rx="3" fill="#bc8cff"/>
<text x="397.2" y="399" font-size="22" fill="#bc8cff" font-weight="600">0.79</text>
</g>
</svg>
<figcaption><b>Figure 2.</b> Two reasons the Testing page gives. Top: twelve slot shares where a median hides five failing slots and the mean does not. Bottom: how often a model that is really 80% good would show a weak slot by luck, as binomial arithmetic checked for the record. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-violet"><span class="bs-label">The reasons, as the Testing page gives them</span><ul>
<li><b>Every place counts the same</b>, however many rollouts went there. In machine-learning words each share is that slot's recall and the score is the balanced accuracy.</li>
<li><b>The bin is left out</b>: it is an easy target and would lift the score.</li>
<li><b>No true negatives</b>: every rollout asks for some slot, so a miss is a vial that ended anywhere else.</li>
<li><b>Not plain accuracy</b>: pooling would let the slots tried most decide.</li>
<li><b>The mean, not the median</b>: the median hides slots that fail.</li>
<li><b>The bar on the mean</b>: ten rollouts leave room for luck; the mean of 120 evens it out.</li>
</ul></div>
</div>

[Figure 2](#fig-why-mean) draws the two numerical arguments. Seven slots at 80% and five at 0% have a median of 80% but a mean of 47%. A slot that really works 80% of the time scores 6 of 10 or less about one time in eight, so a model that good everywhere would show at least one slot below 7 of 10 about four times in five. The split into trained and held-out slots is fixed for every run, and it matches all three training sets as recorded ([why it is built this way](evaluation-record.html#why-it-is-built-this-way)).

</section>

<section class="card" id="the-three-outcome-stages">
<span id="the-outcome-kinds-and-how-they-map-to-the-stages"></span><span id="where-every-vial-ended-the-confusion-matrix"></span><span id="terms"></span>

## Every rollout ends in one of three stages: never picked it up, picked up but not in the asked slot, or in the asked slot

<p class="bs-lead">A rollout counts at the furthest stage it reached, and a vial dropped beside the asked slot is a failure like one put in another slot.</p>

<div class="bs-grid g2">
<figure id="fig-stages">
<svg class="inline-fig" viewBox="0 0 520 330" role="img" aria-label="The six outcomes a note can be read as, and the stage each counts as. placed is In the asked slot. drop_missed, off_slot and never_let_go are Picked up, not in the asked slot. no_grasp and wrong_vial are Never picked it up.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<rect x="262" y="15" width="250" height="50" rx="10" fill="#121a24" stroke="#39d2c0" stroke-width="2.5"/>
<text x="278" y="48" font-size="22" fill="#39d2c0" font-weight="600">In the asked slot</text>
<rect x="262" y="115" width="250" height="72" rx="10" fill="#121a24" stroke="#ffa657" stroke-width="2.5"/>
<text x="278" y="145" font-size="22" fill="#ffa657" font-weight="600">Picked up, not</text>
<text x="278" y="173" font-size="22" fill="#ffa657" font-weight="600">in the asked slot</text>
<rect x="262" y="245" width="250" height="72" rx="10" fill="#121a24" stroke="#ff7b72" stroke-width="2.5"/>
<text x="278" y="275" font-size="22" fill="#ff7b72" font-weight="600">Never picked</text>
<text x="278" y="303" font-size="22" fill="#ff7b72" font-weight="600">it up</text>
<text x="10" y="48" font-size="22" fill="#e6edf3" font-family="'IBM Plex Mono',ui-monospace,monospace">placed</text>
<path d="M186 40L256 40" stroke="#39d2c0" stroke-width="2.5"/>
<text x="10" y="124" font-size="22" fill="#e6edf3" font-family="'IBM Plex Mono',ui-monospace,monospace">drop_missed</text>
<path d="M186 116L256 151" stroke="#ffa657" stroke-width="2.5"/>
<text x="10" y="159" font-size="22" fill="#e6edf3" font-family="'IBM Plex Mono',ui-monospace,monospace">off_slot</text>
<path d="M186 151L256 151" stroke="#ffa657" stroke-width="2.5"/>
<text x="10" y="194" font-size="22" fill="#e6edf3" font-family="'IBM Plex Mono',ui-monospace,monospace">never_let_go</text>
<path d="M186 186L256 151" stroke="#ffa657" stroke-width="2.5"/>
<text x="10" y="271" font-size="22" fill="#e6edf3" font-family="'IBM Plex Mono',ui-monospace,monospace">no_grasp</text>
<path d="M186 263L256 281" stroke="#ff7b72" stroke-width="2.5"/>
<text x="10" y="306" font-size="22" fill="#e6edf3" font-family="'IBM Plex Mono',ui-monospace,monospace">wrong_vial</text>
<path d="M186 298L256 281" stroke="#ff7b72" stroke-width="2.5"/>
</g>
</svg>
<figcaption><b>Figure 3.</b> The six outcomes an operator's note is read as, and the stage each one counts as (<code>NOTE_STAGE</code> in <code>scripts/build_data.py</code>). Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">The stages, worst to best</span><ul>
<li><b>Never picked it up</b>: the gripper closed on another vial, on an empty hole or not at all, or closed on the right vial and never lifted it.</li>
<li><b>Picked up, not in the asked slot</b>: the right vial was picked up but let go at another slot, dropped in front of or behind the asked slot, or never let go.</li>
<li><b>In the asked slot</b>: the vial ended there. From notes, that is what the operator saw; from the arm, the arm let go at the asked slot within half a slot, unless a person saw otherwise.</li>
</ul></div>
</div>

[Figure 3](#fig-stages) shows how a note becomes a stage. A missed drop beside the asked slot counts as a failure, "the operator's rule, 24 Nov"; a wrong vial counts as never picked up even when it was then put in the asked slot. A run's funnel is rollouts, then "Picked up the right vial", then "In the asked slot". For runs scored from notes, a table of where every vial ended gives each slot's share as its diagonal ([the three outcome stages](evaluation-record.html#the-three-outcome-stages), [the confusion matrix](evaluation-record.html#where-every-vial-ended-the-confusion-matrix)). The page's terms follow the project's [list of terms](docs.development.conventions.md.html#terms).

</section>

<section class="card" id="how-a-rollout-is-scored">
<span id="from-the-arm-the-scorer"></span><span id="eye-checks"></span><span id="from-the-operators-notes"></span><span id="the-notes-format"></span><span id="from-a-note-to-an-outcome-scriptsnotes_to_yamlpy"></span>

## Three runs are scored from the operator's notes; the other 19 from the arm, which cannot see the vial

<p class="bs-lead">A run is scored one way only: from what the operator saw and wrote at the robot, or from the arm's joint angles by a scorer that a person's eye check sometimes overrules.</p>

<div class="bs-grid g2">
<div class="bs-part bs-teal"><span class="bs-label">From the operator's notes</span><h3>Isaac 0.5 Expert, Plain Bagel, Mango Pudding</h3><ul>
<li>The operator types one line per move, <code>&lt;n&gt;: &lt;source&gt; &lt;destination&gt;: &lt;what happened&gt;</code>.</li>
<li><code>scripts/notes_to_yaml.py</code> reads only the part after the last "then" and applies fixed rules in order; a note no rule reads stops the script, "so nothing is guessed".</li>
<li>The note is the score: these rollouts are not counted as eye checks.</li>
</ul></div>
<div>
<div class="bs-part bs-orange"><span class="bs-label">From the arm</span><h3>The scorer, all other runs</h3><ul>
<li>It reads the joint angles, finds each grasp and release, and matches the arm's pose to the same moment of the demonstrations to find the slot.</li>
<li>It is accurate to about half a slot and cannot see the vial.</li>
<li>A rollout it scores as in the asked slot that a person saw outside it becomes "Picked up, not in the asked slot".</li>
</ul></div>
<figure id="fig-eye-checks">
<svg class="inline-fig" viewBox="0 0 520 166" role="img" aria-label="Of 53 rollouts scored from the arm that a person watched, the vial was in the slot in 11, not in it in 39, and could not be told in 3.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">53 rollouts that a person watched</text>
<rect x="10" y="42" width="103.774" height="40" rx="0" fill="#39d2c0"/>
<rect x="113.774" y="42" width="367.925" height="40" rx="0" fill="#ff7b72"/>
<rect x="481.698" y="42" width="28.3019" height="40" rx="0" fill="#7d8896"/>
<text x="10" y="116" font-size="22" fill="#39d2c0" font-weight="600">11 in the slot</text>
<text x="297.736" y="116" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">39 not in it</text>
<path d="M495.849 84L495.849 132" stroke="#7d8896" stroke-width="2"/>
<text x="510" y="154" font-size="22" fill="#a9b4c2" text-anchor="end">3 could not be told</text>
</g>
</svg>
<figcaption><b>Figure 4.</b> The eye checks of rollouts scored from the arm (<code>eye</code> in <code>src/data/results.json</code>, at commit <code>8065309</code>). Drawn in the page source from the record.</figcaption>
</figure>
</div>
</div>

[Figure 4](#fig-eye-checks) is why a score from the arm is weaker evidence than one from notes: of the 53 rollouts a person watched, the vial was outside the slot in 39. The scorer and the rollout program are in the `~/lerobot` checkout, so what is known of them comes from the website's pages and the comments in `scripts/build_data.py` ([how a rollout is scored](evaluation-record.html#how-a-rollout-is-scored)).

<!-- fold: code How the operator writes a note -->

The writing guide printed in each notes file, a few of its lines:

```text
1: L1 R2: success
3: L1 R4: put in R3
13: L3 R4: missed drop in front of R3
8: R1 L3: didn't grasp
5: L1 R2: didn't grasp, then success
6: R1 L2: success (restart: vial knocked over)
```

A slot is a side and a number: L or R, 1–6 with 1 nearest the arm, or `bin`. The full guide, the eight reading rules and the three notes files are in the record ([the notes format](evaluation-record.html#the-notes-format), [from a note to an outcome](evaluation-record.html#from-a-note-to-an-outcome-scriptsnotes_to_yamlpy)).

<!-- /fold -->

</section>

<section class="card" id="what-is-scored-and-what-is-left-out">
<span id="resets-restarts-and-retries"></span>

## 287 rollouts in 22 runs were scored; restarts are most of what was left out

<p class="bs-lead">Every rollout over 3 s with a readable command is scored, moves no demonstration contains included; a noted move counts once, so its earlier takes are restarts.</p>

<div class="bs-grid g2">
<figure id="fig-left-out">
<svg class="inline-fig" viewBox="0 0 520 386" role="img" aria-label="Rollouts left out of the counts: 20 restarts of a move noted once, 11 that ended within 3 seconds, 11 from the earlier table layout of 7 October and 2 whose command the scorer cannot read. Isaac's first session, 4 takes, is not counted at all.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="32" font-size="22" fill="#a9b4c2">restarts of a move noted once</text>
<rect x="10" y="42" width="400" height="30" rx="3" fill="#ffa657"/>
<text x="418" y="65" font-size="22" fill="#ffa657" font-weight="600">20</text>
<text x="10" y="106" font-size="22" fill="#a9b4c2">ended within 3 seconds</text>
<rect x="10" y="116" width="220" height="30" rx="3" fill="#ffa657"/>
<text x="238" y="139" font-size="22" fill="#ffa657" font-weight="600">11</text>
<text x="10" y="180" font-size="22" fill="#a9b4c2">earlier table layout, 7 Oct</text>
<rect x="10" y="190" width="220" height="30" rx="3" fill="#ffa657"/>
<text x="238" y="213" font-size="22" fill="#ffa657" font-weight="600">11</text>
<text x="10" y="254" font-size="22" fill="#a9b4c2">command the scorer cannot read</text>
<rect x="10" y="264" width="40" height="30" rx="3" fill="#ffa657"/>
<text x="58" y="287" font-size="22" fill="#ffa657" font-weight="600">2</text>
<text x="10" y="328" font-size="22" fill="#a9b4c2">Isaac's first session, not counted</text>
<rect x="10" y="338" width="80" height="30" rx="3" fill="#7d8896"/>
<text x="98" y="361" font-size="22" fill="#7d8896" font-weight="600">4</text>
</g>
</svg>
<figcaption><b>Figure 5.</b> What is left out of the counts, at commit <code>8065309</code> (<code>left_out</code> in <code>src/data/results.json</code>, <code>SESSION_RUN</code> in <code>scripts/build_data.py</code>). Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-orange"><span class="bs-label">Restarts and retries</span><ul>
<li>A <b>restart</b> is a new take of the same move. The noted result goes on the move's last take; the takes before it are left out and counted as restarts. A restart that was not the model's fault is written <code>&lt;result&gt; (restart: &lt;why&gt;)</code>.</li>
<li>A <b>retry</b> the note mentions, <code>&lt;first try&gt;, then &lt;final result&gt;</code>, counts as its final result.</li>
<li>Of the 287 scored rollouts, 92 were on moves no demonstration contains, held-out slots included.</li>
<li>Isaac's first session, 25 Nov, came before the noted sheet; it gets a run of its own that no model claims.</li>
</ul></div>
</div>

[Figure 5](#fig-left-out) shows that restarts are the largest share of what is left out. Restarts in the data: 3 for Isaac 0.5 Expert, 11 for Plain Bagel, 6 for Mango Pudding ([what is scored and what is left out](evaluation-record.html#what-is-scored-and-what-is-left-out), [resets, restarts and retries](evaluation-record.html#resets-restarts-and-retries)).

</section>

<section class="card" id="how-a-rollout-is-run">
<span id="execution-modes-and-replanning"></span><span id="session-settings-recorded-in-the-lab-notes"></span>

## A rollout starts from the home pose and runs until a person stops it; in sync mode no model reached the 30 actions a second it aims for

<p class="bs-lead">The follower arm starts every rollout from the pose every demonstration started from, the model drives it from the cameras and joint angles, and each session is stored as a LeRobot dataset.</p>

<div class="bs-grid g2">
<figure id="fig-rates">
<svg class="inline-fig" viewBox="0 0 520 356" role="img" aria-label="Actions a second on the arm against the target of 30: pi 0.5 in sync mode about 24 to 26, Isaac 0.5 in sync mode about 21, Crispy Falafel on FLUX 15.5 in the one session whose rate was logged, and Sweet Corn on FLUX 15.3 on 7 October.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<path d="M460 20L460 330" stroke="#ffa657" stroke-width="2.5" stroke-dasharray="6 5"/>
<text x="454" y="344" font-size="22" fill="#ffa657" text-anchor="end" font-weight="600">target 30</text>
<text x="10" y="32" font-size="22" fill="#e6edf3">π0.5, sync</text>
<rect x="10" y="42" width="360" height="30" rx="3" fill="#39d2c0"/>
<rect x="370" y="42" width="30" height="30" rx="0" fill="#39d2c0"/>
<rect x="370" y="42" width="30" height="30" fill="#0d1117" fill-opacity=".45"/>
<text x="362" y="65" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">about 24 to 26</text>
<text x="10" y="108" font-size="22" fill="#e6edf3">Isaac 0.5, sync</text>
<rect x="10" y="118" width="315" height="30" rx="3" fill="#79c0ff"/>
<text x="333" y="141" font-size="22" fill="#79c0ff" font-weight="600">about 21</text>
<text x="10" y="184" font-size="22" fill="#e6edf3">Crispy Falafel, FLUX</text>
<rect x="10" y="194" width="232.5" height="30" rx="3" fill="#bc8cff"/>
<text x="250.5" y="217" font-size="22" fill="#bc8cff" font-weight="600">15.5</text>
<text x="10" y="260" font-size="22" fill="#e6edf3">Sweet Corn, FLUX, 7 Oct</text>
<rect x="10" y="270" width="229.5" height="30" rx="3" fill="#7d8896"/>
<text x="247.5" y="293" font-size="22" fill="#7d8896" font-weight="600">15.3</text>
</g>
</svg>
<figcaption><b>Figure 6.</b> Actions a second on the arm, as the Testing page and the models' "On the robot" notes give them. The π0.5 bar shows its stated range, 24 to 26. Sweet Corn was not scored. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">One rollout</span><ol>
<li><b>Home pose</b>: so a crash in the last session cannot shift "home".</li>
<li><b>The command</b>: from 21 October a short code ("R3 L1") expands to the exact training wording; before that it was typed by hand.</li>
<li><b>The run</b>: a person starts it; it ends when a person stops it or a camera drops off the bus.</li>
<li><b>Replanning</b>: every few dozen actions. In sync mode the arm waits for each replan; with RTC it does not.</li>
<li><b>Stored</b>: one LeRobot dataset per session, uploaded to Hugging Face.</li>
</ol></div>
</div>

[Figure 6](#fig-rates) shows why sync mode is slow: the arm waits at each replan. π0.5 replans every 15 actions in the sessions of 8–9 Nov, FLUX 3 Action every 32 with a freeze of about 1.3 s, and Isaac 0.5 plans 60 actions in about half a second and runs 30. Of the 22 runs, 16 are sync and 6 are RTC. From 4 Nov 18:33 every arm test ran with the across-the-table camera shifted ([Task and rig](task-and-rig.html#camera-position-changes); [how a rollout is run](evaluation-record.html#how-a-rollout-is-run)).

</section>

<section class="card" id="the-12-move-gate">
<span id="the-offline-gate"></span>

## Plain Bagel met the 12-move gate with no margin; Mango Pudding did not

<p class="bs-lead">The 12-move gate keeps the vial layout fixed and changes only the destination in the command, so a model that reads the destination off the cameras cannot pass.</p>

<div class="bs-grid g2">
<figure id="fig-gate">
<svg class="inline-fig" viewBox="0 0 520 480" role="img" aria-label="The 12-move gate in the Lab notes. Mango Pudding: placed right 5 of 12, right slot counting missed drops 7 of 12 against a pass of 9, right vial picked up 10 of 12 against a pass of 11. Plain Bagel: 7, 9 and 11 of 12.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="30" font-size="22" fill="#a9b4c2">placed right</text>
<rect x="200" y="42" width="125" height="34" rx="3" fill="#bc8cff"/>
<text x="10" y="67" font-size="22" fill="#bc8cff" font-weight="600">Mango Pudding</text>
<text x="317" y="67" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">5</text>
<rect x="200" y="86" width="175" height="34" rx="3" fill="#39d2c0"/>
<text x="10" y="111" font-size="22" fill="#39d2c0" font-weight="600">Plain Bagel</text>
<text x="367" y="111" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">7</text>
<text x="10" y="170" font-size="22" fill="#a9b4c2">right slot, counting missed drops</text>
<rect x="200" y="182" width="175" height="34" rx="3" fill="#bc8cff"/>
<text x="10" y="207" font-size="22" fill="#bc8cff" font-weight="600">Mango Pudding</text>
<text x="367" y="207" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">7</text>
<rect x="200" y="226" width="225" height="34" rx="3" fill="#39d2c0"/>
<text x="10" y="251" font-size="22" fill="#39d2c0" font-weight="600">Plain Bagel</text>
<text x="417" y="251" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">9</text>
<path d="M425 178L425 266" stroke="#ffa657" stroke-width="3" stroke-dasharray="6 5"/>
<text x="419" y="284" font-size="22" fill="#ffa657" text-anchor="end" font-weight="600">pass ≥ 9</text>
<text x="10" y="310" font-size="22" fill="#a9b4c2">right vial picked up</text>
<rect x="200" y="322" width="250" height="34" rx="3" fill="#bc8cff"/>
<text x="10" y="347" font-size="22" fill="#bc8cff" font-weight="600">Mango Pudding</text>
<text x="442" y="347" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">10</text>
<rect x="200" y="366" width="275" height="34" rx="3" fill="#39d2c0"/>
<text x="10" y="391" font-size="22" fill="#39d2c0" font-weight="600">Plain Bagel</text>
<text x="467" y="391" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">11</text>
<path d="M475 318L475 406" stroke="#ffa657" stroke-width="3" stroke-dasharray="6 5"/>
<text x="469" y="424" font-size="22" fill="#ffa657" text-anchor="end" font-weight="600">pass ≥ 11</text>
<text x="500" y="470" font-size="22" fill="#7d8896" text-anchor="end">of 12</text>
<path d="M200 440L500 440" stroke="#2f3b4a" stroke-width="2"/>
</g>
</svg>
<figcaption><b>Figure 7.</b> The 12-move gate as the Lab notes applied it: Mango Pudding on 8–9 Nov, Plain Bagel on 9 Nov. "Right slot" counts a missed drop at the right slot as reaching it, which the score does not. Drawn in the page source from the record.</figcaption>
</figure>
<div>
<div class="scroll" role="region" aria-label="The three blocks of the 12-move gate" tabindex="0" data-reader-horizontal>
<table>
<thead><tr><th>Block</th><th>Layout</th><th>Commands</th></tr></thead>
<tbody>
<tr><th>A</th><td>vial at R3</td><td><code>/t R3 L1</code>, <code>/t R3 L3</code>, <code>/t R3 L6</code>, <code>/t R3 bin</code></td></tr>
<tr><th>B</th><td>vial at L3</td><td><code>/t L3 R1</code>, <code>/t L3 R3</code>, <code>/t L3 R6</code>, <code>/t L3 bin</code></td></tr>
<tr><th>C</th><td>as needed</td><td><code>/t R6 R1</code>, <code>/t R1 R6</code>, <code>/t L1 L6</code>, <code>/t L6 L1</code></td></tr>
</tbody>
</table>
</div>
<div class="bs-part bs-muted"><span class="bs-label">Not part of the score</span><ul>
<li>The gate is a protocol of the November sessions, written in the Lab note of 4 Nov. The website does not show it.</li>
<li>On strict first tries Plain Bagel is 8 of 12 right slot, one short. L1 → L6 is in none of the 220 demonstrations; without it Mango Pudding still fails.</li>
<li>The offline gate, a checkpoint shown recorded frames without the robot, is a different test; <a href="training.html">Training</a> owns it.</li>
</ul></div>
</div>
</div>

[Figure 7](#fig-gate) shows both sessions against the two pass marks, at least 9 of 12 right slot and at least 11 of 12 right vial. Mango Lassi on 4 Nov was "not met", over all 35 rollouts. Isaac's notes carry a stopping rule of the same kind; 6 of its 16 held-out moves in blocks 1–4 ended in the asked slot, and the test went on ([the 12-move gate](evaluation-record.html#the-12-move-gate)).

</section>

<section class="card" id="what-the-numbers-cannot-say">

## The numbers are small, uncontrolled and partly from a scorer that cannot see the vial

<p class="bs-lead">These are test runs made during development, not a planned evaluation; read each run's numbers with its rollout count and how it was scored.</p>

<div class="bs-board">
<div class="bs-row"><span class="bs-state bs-wait">Limit</span><b>Small</b><span>The biggest run has 82 rollouts and many have one to five. No run has 10 rollouts at any rack slot, so every run is disqualified.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Limit</span><b>Not controlled</b><span>The runs differ in training data, length and mode.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Limit</span><b>Not planned</b><span>49 sessions, uneven in the moves tried, with no fixed number of rollouts per move.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Limit</span><b>Not comparable with August</b><span>The August pages show a person-scored evaluation of a different, earlier system, 79 rollouts.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Limit</span><b>The scorer cannot see the vial</b><span>For the 19 runs scored from the arm, of the 53 rollouts a person watched, 39 had the vial outside the slot.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Limit</span><b>One person's reading</b><span>The notes are the operator's reading at the robot, turned into outcomes by fixed rules; a misreading is fixed by hand in the yaml.</span></div>
</div>

The list is the Testing page's "What the numbers cannot say" and the home page's "What is not solved" ([what the numbers cannot say](evaluation-record.html#what-the-numbers-cannot-say)).

</section>

<section class="card" id="where-sources-disagree">
<span id="not-verified"></span><span id="where-these-facts-come-from"></span>

## Three disagreements stay open, and the scorer's own code was not read

<p class="bs-lead">The scorer and the rollout program are not in this repository, so this page describes them as the website and the code comments do, and lists where sources disagree.</p>

<div class="bs-grid g2">
<div class="bs-part bs-orange"><span class="bs-label">Where sources disagree</span><ul>
<li><b>Reaching the slot</b>: the 12-move gate counts a missed drop at the right slot as the right slot; the score, since "the operator's rule, 24 Nov", does not.</li>
<li><b>Rollout counts of 4 Nov</b>: the Lab note counts 35 rollouts for B at 4000, 10 for <code>004000_q37</code> and 4 for <code>004000_q37g</code>; the data has 37 for Mango Lassi, 11 for Mango Sorbet and 7 for Mango Chutney. Not traced.</li>
<li><b>Sweet Corn's rate</b>: the Testing page gives FLUX 15.5 a second in the one session whose rate was logged; the data also gives Sweet Corn 15.3 Hz on 7 October.</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Not verified</span><ul>
<li>The scorer, the rollout program and the eye checks were not read; the first two are in the <code>~/lerobot</code> checkout.</li>
<li><code>scripts/notes_to_yaml.py</code> and <code>scripts/build_data.py</code> were read, not run; whether the yaml files carry hand fixes is not known.</li>
<li>π0.5's rate in RTC mode, the October replan interval and whether the 60 s limit applied beyond 8–9 Nov are not stated.</li>
<li>The record was written by AI agents and waits for a <a href="docs.open.human-review.md.html">review by a person</a>.</li>
</ul></div>
</div>

The full lists, with their sources, are in the record ([where sources disagree](evaluation-record.html#where-sources-disagree), [not verified](evaluation-record.html#not-verified)).

</section>
