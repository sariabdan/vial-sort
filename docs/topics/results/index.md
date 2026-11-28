+++
title = "Results"
brand_sub = "no run passed · 100 against 220 · far slots · open problems · disagreements · where the numbers live"
description = "What came out of the arm tests: no run has passed the gate yet, the newer demonstrations made the destination follow the command, and where the per-run numbers live."
components = ["toc", "nav", "filelinks"]
page_css = ["build-sheet.css"]
toc = [["No run passed", "#readings-at-commit-8065309"], ["100 against 220", "#the-100-against-the-220"], ["On the robot", "#what-each-model-did-on-the-robot-as-written"], ["Not solved", "#what-is-not-solved"], ["Disagreements", "#where-sources-disagree"], ["Where the numbers live", "#where-the-results-live"]]
+++

# Results

<section class="card" id="readings-at-commit-8065309">
<span id="scope"></span>

## No run has passed yet: every run has fewer than 10 rollouts at every rack slot

<p class="bs-lead">At commit <code>8065309</code> the data held 22 runs and 287 scored rollouts, and every run was disqualified because no run had 10 rollouts at any of the 12 rack slots.</p>

<div class="bs-grid g2">
<figure id="fig-no-pass">
<svg class="inline-fig" viewBox="0 0 520 330" role="img" aria-label="Top: the most rollouts any run had at one rack slot was 9, short of the 10 the pass mark needs at every slot. Bottom: of the 335 takes in the data, 287 were scored, 44 were left out and 4 belong to no run.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif" font-size="24">
<text x="20" y="28" fill="#a9b4c2">most rollouts at one slot, any run</text>
<rect x="20" y="46" width="324" height="40" rx="4" fill="#39d2c0"/>
<text x="332" y="74" fill="#0d1117" font-weight="600" text-anchor="end">9</text>
<path d="M380 40V96" stroke="#ffa657" stroke-width="3" stroke-dasharray="6 5"/>
<text x="390" y="74" fill="#ffa657" font-weight="600">10 needed</text>
<path d="M20 104H500" stroke="#2f3b4a" stroke-width="2"/>
<text x="20" y="130" fill="#7d8896" text-anchor="middle">0</text><text x="200" y="130" fill="#7d8896" text-anchor="middle">5</text><text x="380" y="130" fill="#7d8896" text-anchor="middle">10</text>
<text x="20" y="186" fill="#a9b4c2">the 335 takes in the data</text>
<rect x="20" y="202" width="411" height="40" fill="#39d2c0"/>
<rect x="431" y="202" width="63" height="40" fill="#ffa657"/>
<rect x="494" y="202" width="6" height="40" fill="#7d8896"/>
<text x="20" y="274" fill="#39d2c0" font-weight="600">287 scored</text>
<text x="490" y="274" fill="#ffa657" font-weight="600" text-anchor="end">44 left out</text>
<path d="M497 244V296" stroke="#7d8896" stroke-width="2"/>
<text x="490" y="314" fill="#a9b4c2" text-anchor="end">4 in no run</text>
</g>
</svg>
<figcaption><b>Figure 1.</b> Why every verdict is "Disqualified": the most rollouts any run had at one slot, against the 10 needed at each slot (top), and what happened to the takes in the data (bottom). Readings at commit <code>8065309</code>, drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">Read the figure</span><h3>Short of the gate at all 12 slots</h3><ul>
<li>Every verdict was "Disqualified: under 10 rollouts at 12 of 12 slots". The Results page still shows each run's numbers over the slots it was tried at.</li>
<li>Only five runs had a rollout asked for a held-out destination. The bin is never part of a score.</li>
<li>The 44 left out are restarts of noted moves, rollouts that ended within 3 s, commands the scorer cannot read and the earlier table layout of 7 Oct. The 4 takes of Isaac's first session, 25 Nov, came before the noted sheet.</li>
</ul></div>
</div>

[Figure 1](#fig-no-pass) shows the reason no run passed. It is not a low score: it is too few rollouts per slot to score at all. These are readings of the data at one commit; the live numbers of every run are on the website's [Results page](https://cognitive-software-labs.github.io/vial-sort/results/), and a rebuild of the data can change them ([readings at commit 8065309](results-record.html#readings-at-commit-8065309)). The score, the pass mark and the 12-move gate are defined in [Evaluation](evaluation.html).

</section>

<section class="card" id="the-100-against-the-220">
<span id="what-the-home-page-compares-π05-on-the-100-demonstrations-versus-the-220"></span>

## On the newer 220 demonstrations the destination follows the command

<p class="bs-lead">On the same 31 moves, Plain Bagel, trained from the base model on the 220 demonstrations, put 21 vials in the asked slot; Mango Pudding, continued from the 100-demonstration model, put 11.</p>

<div class="bs-grid g2">
<figure id="fig-three-runs">
<svg class="inline-fig" viewBox="0 0 540 330" role="img" aria-label="The three pi 0.5 runs the home page compares. Mango Rice, 12k, sync, was trained on the 100 demonstrations. Mango Pudding, 16k, sync, continued from Mango Rice on the 220. Plain Bagel, 16k, sync, was trained from the base model on the 220.">
<defs><marker id="fig-three-runs-head" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#a9b4c2"/></marker></defs>
<g font-family="'IBM Plex Sans',system-ui,sans-serif" font-size="24">
<rect x="10" y="20" width="180" height="70" rx="10" fill="#121a24" stroke="#7d8896" stroke-width="2"/>
<text x="100" y="50" fill="#e6edf3" font-weight="600" text-anchor="middle">100</text><text x="100" y="76" fill="#a9b4c2" text-anchor="middle">demonstrations</text>
<rect x="10" y="190" width="180" height="70" rx="10" fill="#121a24" stroke="#7d8896" stroke-width="2"/>
<text x="100" y="220" fill="#e6edf3" font-weight="600" text-anchor="middle">220</text><text x="100" y="246" fill="#a9b4c2" text-anchor="middle">demonstrations</text>
<rect x="240" y="20" width="292" height="70" rx="10" fill="#121a24" stroke="#ffa657" stroke-width="2.5"/>
<text x="256" y="50" fill="#ffa657" font-weight="600">Mango Rice</text><text x="256" y="76" fill="#a9b4c2">12k · sync</text>
<rect x="240" y="130" width="292" height="70" rx="10" fill="#121a24" stroke="#bc8cff" stroke-width="2.5"/>
<text x="256" y="160" fill="#bc8cff" font-weight="600">Mango Pudding</text><text x="256" y="186" fill="#a9b4c2">16k · sync</text>
<rect x="240" y="240" width="292" height="70" rx="10" fill="#121a24" stroke="#39d2c0" stroke-width="2.5"/>
<text x="256" y="270" fill="#39d2c0" font-weight="600">Plain Bagel</text><text x="256" y="296" fill="#a9b4c2">16k · sync, from base</text>
<path d="M190 55H232" stroke="#a9b4c2" stroke-width="2.5" marker-end="url(#fig-three-runs-head)"/>
<path d="M386 90V122" stroke="#a9b4c2" stroke-width="2.5" marker-end="url(#fig-three-runs-head)"/>
<text x="396" y="114" fill="#a9b4c2">continued</text>
<path d="M190 215L232 175" stroke="#a9b4c2" stroke-width="2.5" marker-end="url(#fig-three-runs-head)"/>
<path d="M190 235L232 268" stroke="#a9b4c2" stroke-width="2.5" marker-end="url(#fig-three-runs-head)"/>
</g>
</svg>
<figcaption><b>Figure 2.</b> The three π0.5 runs the home page compares, each the row with the most rollouts of its model, and the demonstrations each learned from. Drawn in the page source from the record.</figcaption>
</figure>
<figure id="fig-paired">
<svg class="inline-fig" viewBox="0 0 520 440" role="img" aria-label="Plain Bagel and Mango Pudding on the same 31 moves, 8 to 9 November. In the asked slot: Plain Bagel 21, Mango Pudding 11. Grasp failures: Plain Bagel 1, Mango Pudding 7. Move by move, the Lab note ranks Plain Bagel better on 16 moves, the same on 10 and Mango Pudding better on 5.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif" font-size="24">
<text x="10" y="26" fill="#a9b4c2">in the asked slot, of 31 moves</text>
<text x="10" y="64" fill="#39d2c0" font-weight="600">Plain Bagel</text><rect x="200" y="44" width="203" height="30" rx="3" fill="#39d2c0"/><text x="411" y="66" fill="#e6edf3" font-weight="600">21</text>
<text x="10" y="104" fill="#bc8cff" font-weight="600">Mango Pudding</text><rect x="200" y="84" width="106" height="30" rx="3" fill="#bc8cff"/><text x="314" y="106" fill="#e6edf3" font-weight="600">11</text>
<text x="10" y="158" fill="#a9b4c2">grasp failures, of 31 moves</text>
<text x="10" y="196" fill="#39d2c0" font-weight="600">Plain Bagel</text><rect x="200" y="176" width="10" height="30" rx="3" fill="#39d2c0"/><text x="218" y="198" fill="#e6edf3" font-weight="600">1</text>
<text x="10" y="236" fill="#bc8cff" font-weight="600">Mango Pudding</text><rect x="200" y="216" width="68" height="30" rx="3" fill="#bc8cff"/><text x="276" y="238" fill="#e6edf3" font-weight="600">7</text>
<text x="10" y="290" fill="#a9b4c2">which did better, move by move</text>
<rect x="10" y="304" width="258" height="34" fill="#39d2c0"/><rect x="268" y="304" width="161" height="34" fill="#7d8896"/><rect x="429" y="304" width="81" height="34" fill="#bc8cff"/>
<text x="139" y="329" fill="#0d1117" font-weight="600" text-anchor="middle">16</text><text x="348" y="329" fill="#0d1117" font-weight="600" text-anchor="middle">10</text><text x="469" y="329" fill="#0d1117" font-weight="600" text-anchor="middle">5</text>
<rect x="10" y="356" width="16" height="16" fill="#39d2c0"/><text x="34" y="371" fill="#e6edf3">Plain Bagel better</text>
<rect x="10" y="386" width="16" height="16" fill="#7d8896"/><text x="34" y="401" fill="#e6edf3">the same</text>
<rect x="10" y="416" width="16" height="16" fill="#bc8cff"/><text x="34" y="431" fill="#e6edf3">Mango Pudding better</text>
</g>
</svg>
<figcaption><b>Figure 3.</b> Plain Bagel against Mango Pudding on the same 31 moves, 8–9 Nov, as the Lab notes record them. Bars share one scale. Drawn in the page source from the record.</figcaption>
</figure>
</div>

[Figure 2](#fig-three-runs) shows what the home page compares: one run of the model trained on the first 100 demonstrations and two of the models trained on the 220. The first 100 were recorded one destination per sitting, so the first model took the destination from the camera images; in the newer demonstrations one layout is recorded three times, to three destinations, so only the command can tell them apart ([Demonstrations](demonstrations.html)). The numbers of these three runs are on the website's [Results page](https://cognitive-software-labs.github.io/vial-sort/results/), under the preset "π0.5: 100 → 220 demonstrations".

[Figure 3](#fig-paired) is the cleanest comparison in the repository, because both models ran the same moves ([Arm test, 9 Nov](a16000-arm-test-9nov.html)). Whether either passed the 12-move gate is in [Evaluation](evaluation.html). The home page's "In short" band describes the run with the latest test day; at commit `8065309` that was Isaac 0.5 Expert · 21k · sync ([what the home page compares](results-record.html#what-the-home-page-compares-π05-on-the-100-demonstrations-versus-the-220)).

</section>

<section class="card" id="what-each-model-did-on-the-robot-as-written">

## Asked for a far or held-out slot, the vial often lands nearer the middle of the rack

<p class="bs-lead">Isaac 0.5 Expert put 15 of the 20 vials asked for slot 4 or 5 at slot 3, and Plain Bagel's held-out right-rack slots pull toward the middle.</p>

<div class="bs-grid g2">
<figure id="fig-pulls">
<svg class="inline-fig" viewBox="0 0 500 372" role="img" aria-label="Two rows of six slots. Isaac 0.5 Expert: of 20 rollouts asked for slot 4 or 5, 15 ended at slot 3 and none at slot 5. Plain Bagel, right rack: asked R2 it went to R1 three times; asked R4, to R3 four times of five.">
<defs><marker id="fig-pulls-head" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#ffa657"/></marker></defs>
<g font-family="'IBM Plex Sans',system-ui,sans-serif" font-size="24">
<text x="10" y="28" fill="#e6edf3" font-weight="600">Isaac 0.5 Expert</text>
<g font-family="'IBM Plex Mono',ui-monospace,monospace" font-weight="600" text-anchor="middle">
<circle cx="50" cy="130" r="26" fill="#121a24" stroke="#7d8896" stroke-width="2.5"/><text x="50" y="138" fill="#a9b4c2">1</text>
<circle cx="130" cy="130" r="26" fill="#121a24" stroke="#7d8896" stroke-width="2.5"/><text x="130" y="138" fill="#a9b4c2">2</text>
<circle cx="210" cy="130" r="26" fill="#2a1d10" stroke="#ffa657" stroke-width="3"/><text x="210" y="138" fill="#ffa657">3</text>
<circle cx="290" cy="130" r="26" fill="#121a24" stroke="#e6edf3" stroke-width="2.5" stroke-dasharray="6 5"/><text x="290" y="138" fill="#e6edf3">4</text>
<circle cx="370" cy="130" r="26" fill="#121a24" stroke="#e6edf3" stroke-width="2.5" stroke-dasharray="6 5"/><text x="370" y="138" fill="#e6edf3">5</text>
<circle cx="450" cy="130" r="26" fill="#121a24" stroke="#7d8896" stroke-width="2.5"/><text x="450" y="138" fill="#a9b4c2">6</text>
</g>
<path d="M330 98Q300 60 228 100" fill="none" stroke="#ffa657" stroke-width="3" marker-end="url(#fig-pulls-head)"/>
<text x="330" y="72" fill="#ffa657" font-weight="600">15 of 20 at 3</text>
<text x="370" y="186" fill="#a9b4c2" text-anchor="middle">0 at 5</text>
<text x="330" y="214" fill="#a9b4c2" text-anchor="middle">asked: slot 4 or 5</text>
<text x="10" y="258" fill="#e6edf3" font-weight="600">Plain Bagel, right rack</text>
<g font-family="'IBM Plex Mono',ui-monospace,monospace" font-size="22" font-weight="600" text-anchor="middle">
<circle cx="50" cy="342" r="24" fill="#2a1d10" stroke="#ffa657" stroke-width="3"/><text x="50" y="349" fill="#ffa657">R1</text>
<circle cx="130" cy="342" r="24" fill="#121a24" stroke="#e6edf3" stroke-width="2.5" stroke-dasharray="6 5"/><text x="130" y="349" fill="#e6edf3">R2</text>
<circle cx="210" cy="342" r="24" fill="#2a1d10" stroke="#ffa657" stroke-width="3"/><text x="210" y="349" fill="#ffa657">R3</text>
<circle cx="290" cy="342" r="24" fill="#121a24" stroke="#e6edf3" stroke-width="2.5" stroke-dasharray="6 5"/><text x="290" y="349" fill="#e6edf3">R4</text>
<circle cx="370" cy="342" r="24" fill="#121a24" stroke="#7d8896" stroke-width="2.5"/><text x="370" y="349" fill="#a9b4c2">R5</text>
<circle cx="450" cy="342" r="24" fill="#121a24" stroke="#7d8896" stroke-width="2.5"/><text x="450" y="349" fill="#a9b4c2">R6</text>
</g>
<path d="M124 316Q96 294 64 316" fill="none" stroke="#ffa657" stroke-width="3" marker-end="url(#fig-pulls-head)"/>
<path d="M284 316Q256 294 224 316" fill="none" stroke="#ffa657" stroke-width="3" marker-end="url(#fig-pulls-head)"/>
<text x="90" y="298" fill="#ffa657" font-weight="600" text-anchor="middle">3×</text>
<text x="250" y="298" fill="#ffa657" font-weight="600" text-anchor="middle">4 of 5</text>
</g>
</svg>
<figcaption><b>Figure 4.</b> Where the vial ended when the arm was asked for a far or held-out slot. Dashed white rings: the slots asked for, all held out as destinations; orange: where the vial ended. From <code>confusion</code> in <code>src/data/results.json</code>, readings at commit <code>8065309</code>; drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-violet"><span class="bs-label">The Lab notes, as written</span><h3>Three arm tests, three findings</h3><ul>
<li><b>4 Nov</b>, Mango Lassi, Mango Sorbet, Mango Chutney: the grasp failures came from a normalisation mismatch, the gripper's range widened from 37.4° to 50.8° when the datasets merged. Pinning the quantiles fixed it; then the arm went to the middle of the rack whatever the digit (<a href="b4000-arm-test-4nov.html">Arm test, 4 Nov</a>).</li>
<li><b>8 Nov</b>, Mango Pudding: the destination followed the command, but the far slots were squeezed toward the middle (<a href="b16000-arm-test-8nov.html">Arm test, 8–9 Nov</a>).</li>
<li><b>9 Nov</b>, Plain Bagel: slot 6 in 9 of 9, and slots 4 and 5 once each; what was left was mostly the drop (<a href="a16000-arm-test-9nov.html">Arm test, 9 Nov</a>).</li>
</ul></div>
</div>

[Figure 4](#fig-pulls) draws two readings of the data: the vial lands short of the far and held-out slots, toward the middle of the rack. The Lab notes describe the same pattern in the operator's words, and show it shrinking from Mango Pudding to Plain Bagel. Each model's written account of its tests is on the website's Results page, in the "What happened" tab ([what each model did on the robot](results-record.html#what-each-model-did-on-the-robot-as-written)).

</section>

<section class="card" id="what-is-not-solved">

## Unseen destinations, the pass mark and small numbers are still open

<p class="bs-lead">The home page names four things that are not solved, and the last arm test of Plain Bagel adds the drop and a bumped camera.</p>

<div class="bs-board">
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>Unseen destinations</b><span>The models do much worse on the slots no demonstration used as a destination than on the others.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>The pass mark</b><span>No run has reached 70% with at least 10 rollouts at every slot.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>Small numbers</b><span>Many runs have a handful of rollouts, so one rollout moves a run a long way.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>Not a planned evaluation</b><span>These are test runs made during development; how they are run and scored is in <a href="evaluation.html">Evaluation</a>.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>The drop</b><span>On 9 Nov, Plain Bagel missed 6 drops at the right slot, the gripper opening within 3–5° per joint of the successful releases.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>The bumped camera</b><span>The across-the-table camera (<code>left_top</code>) was bumped on 4 Nov; its effect is not proven (<a href="task-and-rig.html#camera-position-changes">Task and rig</a>).</span></div>
</div>

The first four points are the home page's own list, with its numbers filled from the data at build time; the last two are from the [Arm test, 9 Nov](a16000-arm-test-9nov.html) ([what is not solved](results-record.html#what-is-not-solved)).

</section>

<section class="card" id="where-sources-disagree">

## The written accounts and the scored data disagree in six places

<p class="bs-lead">Where a model's written account or a Lab note gives other counts than the scored data, the difference is listed, not resolved: which side is right needs the logs and recordings on the workstation.</p>

<div class="scroll" role="region" aria-label="Where the written accounts and the data disagree" tabindex="0" data-reader-horizontal>
<table>
<thead><tr><th>Where</th><th>The written source says</th><th>The data says</th></tr></thead>
<tbody>
<tr><th>Rollouts of 4 Nov</th><td>The Lab note: 35 rollouts for B at 4000 (6 full successes, 14 failed at the grasp), 10 for <code>004000_q37</code> (9 picked up, 1 placed), 4 for <code>004000_q37g</code> (0 grasped).</td><td>Mango Lassi 37 rollouts (21 picked up, 6 in the asked slot), Mango Sorbet 11 (9, 1), Mango Chutney 7 (1, 1).</td></tr>
<tr><th>Mango Rice, sync</th><td>Two of six in the asked slot, both slot 3; the right vial every time the command was worded as in training.</td><td>Two sync runs: 12k with 1 of 6 (at L3), 10k with 1 of 2 (at R3). Right vial in 4 of 6 and 2 of 2; the wording is not recorded.</td></tr>
<tr><th>Crispy Falafel, 30k</th><td>Grasped the asked vial in 4 of 4 grasps.</td><td>2 of 4 rollouts picked up the right vial.</td></tr>
<tr><th>Isaac, slot 4</th><td>The vial went to slot 4 five times.</td><td>Slot 4 three times, plus one dropped behind R4 and one wrong vial put in R4, counted as never picked up.</td></tr>
<tr><th>Reaching the slot</th><td>The Lab notes' 12-move gate counts a missed drop at the right slot as the right slot.</td><td>A missed drop is not in the asked slot.</td></tr>
<tr><th>Pretzel Two</th><td>Its account describes a table-top test.</td><td>That test is separate from the scored rollouts and has no counts.</td></tr>
</tbody>
</table>
</div>

The table lists the disagreements in the record's words ([where sources disagree](results-record.html#where-sources-disagree)). None of them was traced: a Lab note scores from the operator's words, the data from the scorer. Until they are, quote the data's counts as the scored ones and the accounts as what was written.

</section>

<section class="card" id="where-the-results-live">
<span id="not-verified"></span>

## Every count comes from the operator's notes and the rollout reports; every score is computed when the website is built

<p class="bs-lead">The counts sit in <code>src/data/results.json</code>; the score, the shares and the verdict are not stored anywhere, but computed from those counts each time the website is built.</p>

<figure id="fig-pipeline">
<div class="bs-flow" role="img" aria-label="Measured at the arm: the operator's notes in notes/ and the rollout reports and recordings in the ~/lerobot checkout. Scripts build_data.py and notes_to_yaml.py write the counts into src/data/results.json and every session into src/data/rollouts.json. At build time scoreRun in src/lib/score.ts computes the score, the shares and the verdict, and the Results page shows them.">
<div class="bs-node bs-teal"><span class="bs-label">Measured at the arm</span><b>Notes and reports</b><ul><li>the operator's notes in <code>notes/</code></li><li>rollout reports and recordings in <code>~/lerobot</code>, not in this repository</li></ul></div>
<div class="bs-arrow"><span>scripts</span></div>
<div class="bs-node bs-violet"><span class="bs-label">Generated data</span><b>Counts per run</b><ul><li><code>src/data/results.json</code>: one row per run, the three stages, per slot</li><li><code>src/data/rollouts.json</code>: every session and take</li></ul></div>
<div class="bs-arrow"><span>build</span></div>
<div class="bs-node bs-orange"><span class="bs-label">Computed, not stored</span><b>Score and verdict</b><ul><li><code>scoreRun</code> in <code>src/lib/score.ts</code></li><li>shown on the website's Results page</li></ul></div>
</div>
<figcaption><b>Figure 5.</b> From the arm to the Results page. A diagram drawn in the page source from the record; it shows no measured results.</figcaption>
</figure>

<div class="bs-grid g2">
<div class="bs-part bs-teal"><span class="bs-label">To read the numbers</span><ul>
<li>The live <a href="https://cognitive-software-labs.github.io/vial-sort/results/">Results page</a> renders every run.</li>
<li>No script in this repository prints the scores outside the website's build; <code>npm run build</code>, then the Results page in <code>dist/</code>, is the reproduction.</li>
<li>The record maps each number to its file and key (<a href="results-record.html#where-the-results-live">where the results live</a>).</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Not verified</span><ul>
<li>No count was checked against the recordings or the rollout reports; they are not in this repository.</li>
<li>The readings at commit <code>8065309</code> were counted by hand and by a one-off script outside the repository, not by building the website.</li>
<li>The record was written by AI agents and waits for a <a href="docs.open.human-review.md.html">review by a person</a>.</li>
</ul></div>
</div>

[Figure 5](#fig-pipeline) is why this page shows readings at one commit and links the website for the rest: a copy of the run table would go stale with every rebuild of the data ([not verified](results-record.html#not-verified)).

</section>
