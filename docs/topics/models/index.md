+++
title = "Models"
brand_sub = "the family tree · the shared recipe · October · November · Isaac · FLUX · earlier and planned · disagreements"
description = "Every model of the project: what it started from, what it was trained on, what it saw, its settings and what it showed on the arm."
components = ["toc", "nav", "filelinks"]
page_css = ["build-sheet.css"]
toc = [["The family tree", "#all-models"], ["Shared recipe", "#the-shared-pi05-recipe"], ["October", "#spicy-chicken"], ["November", "#mango-lassi"], ["Isaac", "#isaac-05-expert"], ["FLUX", "#crispy-falafel"], ["Earlier and planned", "#the-august-policies"], ["Disagreements", "#where-sources-disagree"]]
+++

# Models

<section class="card" id="all-models">
<span id="scope"></span><span id="where-the-facts-come-from"></span><span id="per-model-facts-at-a-glance"></span><span id="readings-at-commit-8065309"></span>

## Every model descends from one of three starting checkpoints, and most π0.5 models are fine-tunes of one another

<p class="bs-lead">The π0.5, Isaac 0.5 and FLUX 3 Action models were all fine-tuned on the project's demonstrations; Plain Bagel, with 82, has the most scored rollouts.</p>

<div class="bs-grid g2">
<figure id="fig-family">
<svg class="inline-fig" viewBox="0 0 520 884" role="img" aria-label="The family tree of the twelve trained models, with the scored rollouts of each. From the pi 0.5 base weights: Spicy Chicken, on the 100 demonstrations as recorded, 12k steps, 27 rollouts; its probes Pretzel One, 361 steps, 3 rollouts, and Pretzel Two, 500 steps, 17 rollouts; Mango Rice, on a cleaned copy of the 100, 12k steps, 10 rollouts; from Mango Rice, Mango Lassi on the 220, 4k steps, 37 rollouts, with Mango Sorbet, ranges set back, 11, and Mango Chutney, gripper set back, 7; and Mango Pudding on the 220, 16k steps, 31 rollouts; Plain Bagel from the base on the 220, 16k steps, 82 rollouts. From Isaac 0.5 for SO-100 and SO-101: Isaac 0.5 Expert on the 220 minus 8, 21k steps, 42 rollouts. From FLUX 3 Action for SO-101: Crispy Falafel on the 100 with two cameras, 30k steps, 20 rollouts, and Sweet Corn on one task, 10k steps, none scored.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="510" y="26" font-size="22" fill="#a9b4c2" text-anchor="end">rollouts</text>
<text x="10" y="78" font-size="22" fill="#a9b4c2" font-weight="600">π0.5 base weights</text>
<text x="36" y="112" font-size="22" fill="#39d2c0" font-weight="600">Spicy Chicken</text>
<text x="36" y="138" font-size="22" fill="#7d8896">100, as recorded · 12k</text>
<rect x="395" y="96" width="37.8" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="114" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">27</text>
<path d="M18 88V105H32" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="62" y="170" font-size="22" fill="#39d2c0" font-weight="600">Pretzel One</text>
<text x="62" y="196" font-size="22" fill="#7d8896">probe · 361 steps</text>
<rect x="395" y="154" width="4.2" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="172" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">3</text>
<path d="M44 146V163H58" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="62" y="228" font-size="22" fill="#39d2c0" font-weight="600">Pretzel Two</text>
<text x="62" y="254" font-size="22" fill="#7d8896">probe · 500 steps</text>
<rect x="395" y="212" width="23.8" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="230" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">17</text>
<path d="M44 146V221H58" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="36" y="286" font-size="22" fill="#39d2c0" font-weight="600">Mango Rice</text>
<text x="36" y="312" font-size="22" fill="#7d8896">100, cleaned copy · 12k</text>
<rect x="395" y="270" width="14" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="288" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">10</text>
<path d="M18 88V279H32" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="62" y="344" font-size="22" fill="#39d2c0" font-weight="600">Mango Lassi</text>
<text x="62" y="370" font-size="22" fill="#7d8896">220 · 4k</text>
<rect x="395" y="328" width="51.8" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="346" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">37</text>
<path d="M44 320V337H58" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="88" y="402" font-size="22" fill="#39d2c0" font-weight="600">Mango Sorbet</text>
<text x="88" y="428" font-size="22" fill="#7d8896">ranges set back</text>
<rect x="395" y="386" width="15.4" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="404" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">11</text>
<path d="M70 378V395H84" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="88" y="460" font-size="22" fill="#39d2c0" font-weight="600">Mango Chutney</text>
<text x="88" y="486" font-size="22" fill="#7d8896">gripper set back</text>
<rect x="395" y="444" width="9.8" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="462" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">7</text>
<path d="M70 378V453H84" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="62" y="518" font-size="22" fill="#39d2c0" font-weight="600">Mango Pudding</text>
<text x="62" y="544" font-size="22" fill="#7d8896">220 · 16k</text>
<rect x="395" y="502" width="43.4" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="520" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">31</text>
<path d="M44 320V511H58" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="36" y="576" font-size="22" fill="#39d2c0" font-weight="600">Plain Bagel</text>
<text x="36" y="602" font-size="22" fill="#7d8896">220 · 16k</text>
<rect x="395" y="560" width="114.8" height="22" rx="2" fill="#39d2c0"/>
<text x="388" y="578" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">82</text>
<path d="M18 88V569H32" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="10" y="646" font-size="22" fill="#a9b4c2" font-weight="600">Isaac 0.5 SO-100/101</text>
<text x="36" y="680" font-size="22" fill="#79c0ff" font-weight="600">Isaac 0.5 Expert</text>
<text x="36" y="706" font-size="22" fill="#7d8896">220 minus 8 · 21k</text>
<rect x="395" y="664" width="58.8" height="22" rx="2" fill="#79c0ff"/>
<text x="388" y="682" font-size="22" fill="#79c0ff" text-anchor="end" font-weight="600">42</text>
<path d="M18 656V673H32" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="10" y="750" font-size="22" fill="#a9b4c2" font-weight="600">FLUX 3 Action SO-101</text>
<text x="36" y="784" font-size="22" fill="#bc8cff" font-weight="600">Crispy Falafel</text>
<text x="36" y="810" font-size="22" fill="#7d8896">100, two cameras · 30k</text>
<rect x="395" y="768" width="28" height="22" rx="2" fill="#bc8cff"/>
<text x="388" y="786" font-size="22" fill="#bc8cff" text-anchor="end" font-weight="600">20</text>
<path d="M18 760V777H32" fill="none" stroke="#2f3b4a" stroke-width="2"/>
<text x="36" y="842" font-size="22" fill="#bc8cff" font-weight="600">Sweet Corn</text>
<text x="36" y="868" font-size="22" fill="#7d8896">one task · 10k</text>
<text x="388" y="844" font-size="22" fill="#7d8896" text-anchor="end" font-weight="600">0</text>
<path d="M18 760V835H32" fill="none" stroke="#2f3b4a" stroke-width="2"/>
</g>
</svg>
<figcaption><b>Figure 1.</b> What each model started from, what it was trained on and for how many steps, and its scored rollouts (<code>rollouts</code> in <code>src/data/registry.json</code>, readings at commit <code>8065309</code>). "100" and "220" are the demonstration sets. Sweet Corn's rollouts are on the earlier table layout and are not scored. Drawn in the page source from the record.</figcaption>
</figure>
<div>
<div class="bs-part bs-teal"><span class="bs-label">Read the figure</span><ul>
<li><b>π0.5</b> (teal): two runs from the base on the 100 demonstrations, Spicy Chicken and Mango Rice, and their fine-tunes; Plain Bagel from the base on the 220.</li>
<li><b>Isaac 0.5</b> (blue), by Perceptron: only its action expert trained, from a checkpoint already fine-tuned on SO-100 and SO-101 arms.</li>
<li><b>FLUX 3 Action</b> (violet), by Black Forest Labs: LoRA fine-tunes that see two cameras.</li>
<li>The Lab notes call Plain Bagel "A" and Mango Pudding "B"; that their "base12k" is Mango Rice is inferred.</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Where a model is named</span><ul>
<li><code>models.yaml</code> is the only place a model gets a name. <code>scripts/build_data.py</code> joins it to its sessions, training log and saved config.</li>
<li>The website's <a href="https://cognitive-software-labs.github.io/vial-sort/models/">Models page</a> shows every model's settings, notes and checkpoints.</li>
</ul></div>
</div>
</div>

[Figure 1](#fig-family) shows why the models must be read as a family: Mango Lassi, Mango Pudding, Mango Sorbet and Mango Chutney all carry Mango Rice's weights, and Pretzel One and Pretzel Two carry Spicy Chicken's. The rollout counts are readings of the data at one commit; a rebuild can change them ([all models](models-record.html#all-models), [readings at commit 8065309](models-record.html#readings-at-commit-8065309)). Their scores are in [Results](results.html).

</section>

<section class="card" id="the-shared-pi05-recipe">
<span id="settings-shared-by-the-π05-runs"></span>

## The π0.5 runs share one recipe and differ only in starting weights, learning rate and length

<p class="bs-lead">The seven π0.5 models with a saved training config differ only in starting weights, learning rate, warm-up, decay, steps and passes; everything else, from the batch of 16 to the seed, is the same.</p>

<div class="scroll" role="region" aria-label="The settings in which the pi 0.5 runs differ" tabindex="0" data-reader-horizontal>
<table>
<thead><tr><th>Model</th><th>Started from</th><th>Peak learning rate</th><th>Warm-up, decay</th><th>Steps</th><th>Passes</th></tr></thead>
<tbody>
<tr><th>Spicy Chicken</th><td>π0.5 base</td><td>2.5e-05</td><td>400, 12,000</td><td>12,000</td><td>3.27</td></tr>
<tr><th>Mango Rice</th><td>π0.5 base</td><td>2.5e-05</td><td>400, 12,000</td><td>12,000</td><td>4.14</td></tr>
<tr><th>Mango Lassi</th><td>Mango Rice at 12,000</td><td>1e-05</td><td>133, 4,000</td><td>4,000</td><td>0.57</td></tr>
<tr><th>Mango Pudding</th><td>Mango Rice at 12,000</td><td>1e-05</td><td>533, 16,000</td><td>16,000</td><td>2.27</td></tr>
<tr><th>Plain Bagel</th><td>π0.5 base</td><td>2.5e-05</td><td>533, 16,000</td><td>16,000</td><td>2.27</td></tr>
</tbody>
</table>
</div>

<div class="bs-grid g2">
<div class="bs-part bs-teal"><span class="bs-label">The same in all seven</span><ul>
<li>A full fine-tune, batch size 16, no validation split, the five cameras, final learning rate 2.5e-06, seed 1,000.</li>
<li>The config's warm-up of 1,000 steps and decay of 30,000 are scaled to fit each run.</li>
<li>Mango Sorbet and Mango Chutney are Mango Lassi's weights with no further training.</li>
</ul></div>
<div class="bs-part bs-violet"><span class="bs-label">What the model takes and gives</span><ul>
<li>In: five 640×480 colour cameras, the 6 joint positions and the command.</li>
<li>Out: 6 joint targets in chunks of 50, run with <code>n_action_steps=15</code>.</li>
<li>From the Hugging Face cards written by <code>scripts/upload_hf.py</code>.</li>
</ul></div>
</div>

The table gives the settings in which the runs differ, as each model's section of the record states them; Mango Sorbet and Mango Chutney share Mango Lassi's row. Every other setting is on the website's Models page under each model ([settings shared by the π0.5 runs](models-record.html#settings-shared-by-the-π05-runs)). How the runs were trained is in [Training](training.html).

</section>

<section class="card" id="spicy-chicken">
<span id="pretzel-one"></span><span id="pretzel-two"></span><span id="mango-rice"></span>

## In October each π0.5 run fixed the last one's failure, until Mango Rice left home at every checkpoint and its reach followed the source slot

<p class="bs-lead">Spicy Chicken froze at home, two short probes found why, and Mango Rice, trained from the base on a cleaned copy of the 100 demonstrations, moved but read the destination off the picture.</p>

<div class="bs-grid g2">
<figure id="fig-october">
<svg class="inline-fig" viewBox="0 0 520 582" role="img" aria-label="The October pi 0.5 runs in order. Spicy Chicken, 15 to 16 October, froze at home because it had learned the operator leaning in as its cue to move. With the start frames swapped, Pretzel One, 19 October, left home but let go too early, because the trim cut at the first loosening of the gripper. Trimmed at the real let-go, Pretzel Two, 19 October, left home, and its destinations landed at slot 3 whatever the digit. A new run from the base, Mango Rice, 21 October, leaves home at every checkpoint, and its reach follows the source slot, never the destination.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<rect x="10" y="8" width="500" height="104" rx="10" fill="#121a24" stroke="#ffa657" stroke-width="2.5"/>
<text x="26" y="40" font-size="22" fill="#ffa657" font-weight="600">Spicy Chicken · 15–16 Oct</text>
<text x="26" y="70" font-size="22" fill="#e6edf3">froze at home: it had learned the</text>
<text x="26" y="98" font-size="22" fill="#e6edf3">operator leaning in as its cue to move</text>
<path d="M60 116V152" stroke="#a9b4c2" stroke-width="2.5"/><path d="M52 146L60 158L68 146Z" fill="#a9b4c2"/>
<text x="80" y="144" font-size="22" fill="#a9b4c2">start frames swapped</text>
<rect x="10" y="162" width="500" height="104" rx="10" fill="#121a24" stroke="#ffa657" stroke-width="2.5"/>
<text x="26" y="194" font-size="22" fill="#ffa657" font-weight="600">Pretzel One · 19 Oct</text>
<text x="26" y="224" font-size="22" fill="#e6edf3">left home, but let go too early: the trim</text>
<text x="26" y="252" font-size="22" fill="#e6edf3">cut at the first loosening of the gripper</text>
<path d="M60 270V306" stroke="#a9b4c2" stroke-width="2.5"/><path d="M52 300L60 312L68 300Z" fill="#a9b4c2"/>
<text x="80" y="298" font-size="22" fill="#a9b4c2">trim at the real let-go</text>
<rect x="10" y="316" width="500" height="104" rx="10" fill="#121a24" stroke="#ffa657" stroke-width="2.5"/>
<text x="26" y="348" font-size="22" fill="#ffa657" font-weight="600">Pretzel Two · 19 Oct</text>
<text x="26" y="378" font-size="22" fill="#e6edf3">left home; destinations landed at</text>
<text x="26" y="406" font-size="22" fill="#e6edf3">slot 3 whatever the digit</text>
<path d="M60 424V460" stroke="#a9b4c2" stroke-width="2.5"/><path d="M52 454L60 466L68 454Z" fill="#a9b4c2"/>
<text x="80" y="452" font-size="22" fill="#a9b4c2">new run from the base</text>
<rect x="10" y="470" width="500" height="104" rx="10" fill="#121a24" stroke="#39d2c0" stroke-width="2.5"/>
<text x="26" y="502" font-size="22" fill="#39d2c0" font-weight="600">Mango Rice · 21 Oct</text>
<text x="26" y="532" font-size="22" fill="#e6edf3">leaves home at every checkpoint; reach</text>
<text x="26" y="560" font-size="22" fill="#e6edf3">follows the source, never the destination</text>
</g>
</svg>
<figcaption><b>Figure 2.</b> The October π0.5 runs in order: what each one showed and what the next one changed. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-orange"><span class="bs-label">What the cleaned copy changed</span><ul>
<li>The idle start and end of each demonstration are cut: 58,650 frames became 46,361.</li>
<li>About 8% of the samples at the home pose have the images that showed the operator swapped for views of the arm with nobody near it.</li>
<li>The 100 wordings are replaced by 32 canonical sentences, one per move.</li>
<li>Why the destination still fails: the 100 demonstrations were recorded one destination per sitting, so the destination is read off the picture.</li>
</ul></div>
</div>

[Figure 2](#fig-october) is the October story. Spicy Chicken's freeze was found on 19 October with offline tests: half of all frames at the home pose are the idle start of a demonstration and half the idle end, from the same pose, so the policy told them apart by the operator leaning over the robot. In sync mode on 21 October, Mango Rice took the right vial every time the command was worded exactly as in training ([Spicy Chicken](models-record.html#spicy-chicken), [Mango Rice](models-record.html#mango-rice)). The demonstrations that fixed the destination are in [Demonstrations](demonstrations.html).

</section>

<section class="card" id="mango-lassi">
<span id="mango-sorbet"></span><span id="mango-chutney"></span><span id="mango-pudding"></span><span id="plain-bagel"></span>

## In November the retrains on the 220 first lost the grasp to a scaling mismatch, then followed the command

<p class="bs-lead">Merging the datasets widened the gripper's scaling range, so Mango Lassi's closing commands came out too open; with the ranges pinned, Mango Pudding and Plain Bagel took the destination from the command.</p>

<div class="bs-grid g2">
<figure id="fig-ranges">
<svg class="inline-fig" viewBox="0 0 520 400" role="img" aria-label="The top of the range used to scale each joint. Gripper: 37.4 degrees before the datasets merged, the value pinned, against 50.8 degrees after the datasets merged, in Mango Lassi. Wrist flex: 31.5 degrees in Mango Lassi, set back to 43.2 degrees.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">top of the range used for scaling (q99)</text>
<text x="10" y="66" font-size="22" fill="#e6edf3" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">gripper</text>
<rect x="10" y="76" width="261.8" height="30" rx="3" fill="#39d2c0"/>
<text x="279.8" y="99" font-size="22" fill="#39d2c0" font-weight="600">37.4°</text>
<text x="10" y="132" font-size="22" fill="#a9b4c2">before merging, pinned</text>
<rect x="10" y="146" width="355.6" height="30" rx="3" fill="#ff7b72"/>
<text x="373.6" y="169" font-size="22" fill="#ff7b72" font-weight="600">50.8°</text>
<text x="10" y="202" font-size="22" fill="#a9b4c2">merged, Mango Lassi</text>
<text x="10" y="244" font-size="22" fill="#e6edf3" font-weight="600" font-family="'IBM Plex Mono',ui-monospace,monospace">wrist_flex</text>
<rect x="10" y="254" width="220.5" height="30" rx="3" fill="#ff7b72"/>
<text x="238.5" y="277" font-size="22" fill="#ff7b72" font-weight="600">31.5°</text>
<text x="10" y="310" font-size="22" fill="#a9b4c2">Mango Lassi</text>
<rect x="10" y="324" width="302.4" height="30" rx="3" fill="#39d2c0"/>
<text x="320.4" y="347" font-size="22" fill="#39d2c0" font-weight="600">43.2°</text>
<text x="10" y="380" font-size="22" fill="#a9b4c2">set back</text>
</g>
</svg>
<figcaption><b>Figure 3.</b> The top of the range used to scale each joint (q99), before and after the datasets merged and after the patch, as the 4 Nov Lab note gives them. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">Five models, in order</span><ul>
<li><b>Mango Lassi</b>, 4 Nov: failed at the grasp in 14 of 35 rollouts; every closing command came out about a third too open.</li>
<li><b>Mango Sorbet</b>, both ranges set back with no training: failed at the grasp once in 10, but put the vial in the asked slot once; it went to the middle of the rack.</li>
<li><b>Mango Chutney</b>, the gripper alone set back: failed at the grasp in all four moves. Both joints must be set back; all six are pinned before retraining.</li>
<li><b>Mango Pudding</b>, from Mango Rice, 16,000 steps: 11 of 31 in the asked slot; the far slots pulled toward the middle.</li>
<li><b>Plain Bagel</b>, from the base, 16,000 steps: 51 of 82 in the asked slot, 21 of the 31 moves Mango Pudding also ran.</li>
</ul></div>
</div>

[Figure 3](#fig-ranges) is the mechanism of the 4 Nov failures: a model trained on from Mango Rice keeps Mango Rice's scale, so the wider merged range turns every inherited gripper command too open. Plain Bagel, trained from the base, learns the gripper range of this data from scratch, so the mismatch cannot happen ([Mango Lassi](models-record.html#mango-lassi), [Plain Bagel](models-record.html#plain-bagel)). The Lab notes have the sessions: [Arm test, 4 Nov](b4000-arm-test-4nov.html), [Arm test, 8–9 Nov](b16000-arm-test-8nov.html), [Arm test, 9 Nov](a16000-arm-test-9nov.html).

</section>

<section class="card" id="isaac-05-expert">

## Isaac 0.5 Expert put the vial in the asked slot almost every time at slots 1, 2, 3 and 6, and never at slots 4 and 5

<p class="bs-lead">Of 42 moves scored from the operator's notes it put 20 in the asked slot: almost every one to slots 1, 2, 3 and 6, and none of the 20 to slots 4 and 5.</p>

<div class="bs-grid g2">
<figure id="fig-isaac">
<svg class="inline-fig" viewBox="0 0 520 438" role="img" aria-label="Isaac 0.5 Expert. On the robot, 25 to 27 November, in the asked slot: slots 1, 3 and 6, 11 of 12; slot 2, 9 of 10; slots 4 and 5, 0 of 20. Offline, on the 8 held-out demonstrations, its predicted next second is 2.8 degrees off per joint, against 5.2 for holding still and 8.4 for the checkpoint before this training.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">in the asked slot, 25–27 Nov</text>
<text x="10" y="68" font-size="22" fill="#e6edf3">slots 1, 3, 6</text>
<rect x="170" y="44" width="300" height="32" rx="3" fill="#121a24" stroke="#2f3b4a" stroke-width="2"/>
<rect x="170" y="44" width="275" height="32" rx="3" fill="#79c0ff"/>
<text x="437" y="68" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">11/12</text>
<text x="10" y="114" font-size="22" fill="#e6edf3">slot 2</text>
<rect x="170" y="90" width="300" height="32" rx="3" fill="#121a24" stroke="#2f3b4a" stroke-width="2"/>
<rect x="170" y="90" width="270" height="32" rx="3" fill="#79c0ff"/>
<text x="432" y="114" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">9/10</text>
<text x="10" y="160" font-size="22" fill="#e6edf3">slots 4 and 5</text>
<rect x="170" y="136" width="300" height="32" rx="3" fill="#121a24" stroke="#2f3b4a" stroke-width="2"/>
<text x="178" y="160" font-size="22" fill="#ff7b72" font-weight="600">0/20</text>
<text x="10" y="214" font-size="22" fill="#a9b4c2">offline: next second, error per joint</text>
<text x="10" y="246" font-size="22" fill="#e6edf3">Isaac 0.5 Expert</text>
<rect x="10" y="254" width="134.4" height="30" rx="3" fill="#79c0ff"/>
<text x="152.4" y="277" font-size="22" fill="#79c0ff" font-weight="600">2.8°</text>
<text x="10" y="316" font-size="22" fill="#e6edf3">holding still</text>
<rect x="10" y="324" width="249.6" height="30" rx="3" fill="#7d8896"/>
<text x="267.6" y="347" font-size="22" fill="#7d8896" font-weight="600">5.2°</text>
<text x="10" y="386" font-size="22" fill="#e6edf3">before this training</text>
<rect x="10" y="394" width="403.2" height="30" rx="3" fill="#7d8896"/>
<text x="421.2" y="417" font-size="22" fill="#7d8896" font-weight="600">8.4°</text>
</g>
</svg>
<figcaption><b>Figure 4.</b> Isaac 0.5 Expert on the robot, by destination, and offline on the 8 held-out demonstrations. Asked for slot 4 or 5, the vial went to slot 3 fifteen times and slot 4 five times. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">The model</span><ul>
<li>Started from Perceptron's Isaac 0.5, already fine-tuned on SO-100 and SO-101 arms. Only the action expert trains: all 36 billion parameters need far more memory than the project's GPUs have.</li>
<li>Trained on the 220 demonstrations minus 8 held out, 24–25 Nov, in 13 hours on the workstation's RTX PRO 6000 (96 GB).</li>
<li>It sees two cameras, overhead and wrist: the checkpoint has exactly two camera slots.</li>
<li>It plans 60 actions in about half a second and runs 30, about 21 actions a second on the arm. The right vial was picked up in 41 of 42.</li>
</ul></div>
</div>

[Figure 4](#fig-isaac) shows the gap between the slots the demonstrations used and slots 4 and 5: slot 2 is also held out as a destination and still worked 9 times in 10. The bin and source slots 2 and 5 were not tried ([Isaac 0.5 Expert](models-record.html#isaac-05-expert)).

</section>

<section class="card" id="crispy-falafel">
<span id="which-camera-flux-looked-through"></span><span id="sweet-corn"></span>

## FLUX 3 Action read the source slot but not the destination, at about half the target rate

<p class="bs-lead">Crispy Falafel, a LoRA fine-tune that sees the overhead and wrist cameras, put the vial in the asked slot in 1 of 4 rollouts at 30,000 steps, and ran at 15.5 actions a second against 30.</p>

<div class="bs-grid g2">
<figure id="fig-flux">
<svg class="inline-fig" viewBox="0 0 520 478" role="img" aria-label="Top: the picture FLUX sees is divided into 8 by 8 cells, and one rack of six slots covers about two of them. Bottom: Crispy Falafel ran at 15.5 actions a second on the arm, against a target of 30.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<path d="M10 10L10 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 10L330 10" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M50 10L50 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 50L330 50" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M90 10L90 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 90L330 90" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M130 10L130 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 130L330 130" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M170 10L170 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 170L330 170" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M210 10L210 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 210L330 210" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M250 10L250 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 250L330 250" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M290 10L290 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 290L330 290" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M330 10L330 330" stroke="#2f3b4a" stroke-width="1.5"/>
<path d="M10 330L330 330" stroke="#2f3b4a" stroke-width="1.5"/>
<rect x="130" y="170" width="80" height="40" rx="0" fill="#bc8cff33" stroke="#bc8cff" stroke-width="2.5"/>
<circle cx="138.0" cy="190" r="4.5" fill="#e6edf3"/>
<circle cx="150.8" cy="190" r="4.5" fill="#e6edf3"/>
<circle cx="163.6" cy="190" r="4.5" fill="#e6edf3"/>
<circle cx="176.4" cy="190" r="4.5" fill="#e6edf3"/>
<circle cx="189.2" cy="190" r="4.5" fill="#e6edf3"/>
<circle cx="202.0" cy="190" r="4.5" fill="#e6edf3"/>
<text x="350" y="40" font-size="22" fill="#a9b4c2">the picture,</text>
<text x="350" y="66" font-size="22" fill="#a9b4c2">8 × 8 cells</text>
<text x="350" y="190" font-size="22" fill="#bc8cff" font-weight="600">one rack of</text>
<text x="350" y="216" font-size="22" fill="#bc8cff" font-weight="600">six slots:</text>
<text x="350" y="242" font-size="22" fill="#bc8cff" font-weight="600">about 2 cells</text>
<path d="M214 190L344 212" stroke="#bc8cff" stroke-width="2"/>
<text x="10" y="384" font-size="22" fill="#a9b4c2">on the arm, actions a second</text>
<rect x="10" y="400" width="232.5" height="32" rx="3" fill="#bc8cff"/>
<text x="250.5" y="424" font-size="22" fill="#bc8cff" font-weight="600">15.5</text>
<path d="M460 392L460 440" stroke="#ffa657" stroke-width="2.5" stroke-dasharray="6 5"/>
<text x="454" y="466" font-size="22" fill="#ffa657" text-anchor="end" font-weight="600">target 30</text>
</g>
</svg>
<figcaption><b>Figure 5.</b> Why the destination fails, as <code>models.yaml</code> gives it: a rack of six slots covers about two of the 8 by 8 cells FLUX divides its picture into. A schematic drawn in the page source from the record, not a capture of the picture.</figcaption>
</figure>
<div class="bs-part bs-violet"><span class="bs-label">Three FLUX runs, three scene cameras</span><ul>
<li><b>Flux five</b>: 5 demonstrations, a low side camera; deleted on 22 October.</li>
<li><b>Sweet Corn</b>: one task, the first 25 demonstrations, <code>left</code> re-aimed high; 15.3 a second on 7 October, on the earlier table layout, so none of its rollouts is scored.</li>
<li><b>Crispy Falafel</b>: the 100 demonstrations, the overhead camera, chosen because it is the only high-angle view, has no people in it and stays readable in the dark runs.</li>
<li>The runs also differ in data, length and normalisation: a sequence, not a controlled comparison.</li>
</ul></div>
</div>

[Figure 5](#fig-flux) draws the record's explanation. FLUX has no real-time chunking, so it always runs in sync mode and freezes for about 1.3 s every 32 actions ([Crispy Falafel](models-record.html#crispy-falafel), [which camera FLUX looked through](models-record.html#which-camera-flux-looked-through)).

</section>

<section class="card" id="the-august-policies">
<span id="planned-and-considered"></span>

## Before October, four policies ran on the August rig; two more models were planned or considered and never trained

<p class="bs-lead">Only π0.5 was deployed and evaluated in August; MolmoAct2 is planned and LingBot-VA was considered and set aside.</p>

<div class="bs-grid g2">
<div class="bs-part bs-muted"><span class="bs-label">August 2026, Jetson Thor rig, three cameras</span><ul>
<li><b>π0.5 with a frozen backbone</b>: <code>vial-sort-v5</code>, 150 demonstrations, 30k steps, 12k deployed.</li>
<li><b>π0</b>: <code>vial-sort-v1</code>, 100 demonstrations, 30k steps.</li>
<li><b>GR00T N1.5</b>: <code>vial-sort-v4</code>, 20k steps.</li>
<li><b>ACT</b>: set up and not carried through.</li>
<li>These rest on the August report and project notes, which are not in this repository.</li>
</ul></div>
<div class="bs-part bs-violet"><span class="bs-label">Planned and considered</span><ul>
<li><b>MolmoAct2</b>, by the Allen Institute for AI: planned on the 100 demonstrations; not trained.</li>
<li><b>LingBot-VA</b>, a world-action model: its published time per inference is far too slow for closed-loop control.</li>
<li>The website's Models page lists both under "Planned and considered".</li>
</ul></div>
</div>

The August policies are written into the data from the report and the project notes, since no log on the workstation measures them ([the August policies](models-record.html#the-august-policies), [planned and considered](models-record.html#planned-and-considered)). The August rig is described in [Task and rig](task-and-rig.html#earlier-rigs).

</section>

<section class="card" id="where-sources-disagree">
<span id="not-verified"></span>

## Several facts are stated differently in two sources, and no number was checked against the training logs

<p class="bs-lead">The training logs, configs and session logs are on the workstation, so where <code>models.yaml</code>, the Lab notes and the generated data disagree, the record lists both sides.</p>

<div class="bs-grid g2">
<div class="bs-part bs-orange"><span class="bs-label">Where sources disagree, for example</span><ul>
<li><b>Mango Rice in sync mode</b>: two of six in the asked slot in <code>models.yaml</code>; 1 of 6 at 12,000 and 1 of 2 at 10,000 in the data.</li>
<li><b>Spicy Chicken at 7,000 steps</b>: both valid rollouts right in <code>models.yaml</code>; 9 rollouts, 2 in the asked slot, in the data.</li>
<li><b>Crispy Falafel's right vial</b>: 4 of 4 grasps in <code>models.yaml</code>; right vial gripped in 2 of 4 rollouts in the data.</li>
<li><b>Mango Rice's reach</b>: follows the source "from 2,000 steps on" in <code>models.yaml</code>; from 5k on the Training page and its card.</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Not verified</span><ul>
<li>Whether the published checkpoints are the same files as those on the workstation or cluster.</li>
<li>Any number in <code>models.yaml</code>, the Lab notes or <code>src/data/</code>, against the training logs.</li>
<li>Whether every Hugging Face repository listed in <code>scripts/upload_hf.py</code> exists.</li>
<li>The record was written by AI agents and waits for a <a href="docs.open.human-review.md.html">review by a person</a>.</li>
</ul></div>
</div>

Every disagreement is in the record with both sources ([where sources disagree](models-record.html#where-sources-disagree), [not verified](models-record.html#not-verified)).

</section>
