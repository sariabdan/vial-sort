+++
title = "Training"
brand_sub = "the destination shortcut · the offline gate · the scaling fix · the cluster · the probes · the runs · the data · disagreements"
description = "How the models were trained and tested without the robot: why the first models read the destination off the picture, the scaling mismatch and its fix, the cluster retrains, the offline probes and the loss curves."
components = ["toc", "nav", "filelinks"]
page_css = ["build-sheet.css"]
toc = [["The shortcut", "#why-the-first-models-read-the-destination-off-the-picture"], ["Offline gate", "#the-offline-gate-of-mango-rice"], ["The scaling fix", "#normalisation-and-the-quantile-pinning"], ["The cluster", "#the-retrains-on-the-university-cluster"], ["Cluster probes", "#the-probes-of-the-cluster-retrains"], ["The runs", "#the-runs"], ["The data", "#data-preparation-that-training-depends-on"], ["Disagreements", "#where-sources-disagree"]]
+++

# Training

<section class="card" id="why-the-first-models-read-the-destination-off-the-picture">
<span id="scope"></span><span id="where-the-numbers-come-from"></span><span id="the-destination-probe-of-21-october"></span><span id="the-offline-probes"></span>

## The first models read the destination off the camera picture, not the command; the fix was in the data

<p class="bs-lead">Asked for another destination, Mango Rice followed the words 19% of the time; shown another demonstration's camera images, it followed the cameras 81% of the time.</p>

<div class="bs-grid g2">
<figure id="fig-probe">
<svg class="inline-fig" viewBox="0 0 520 636" role="img" aria-label="The destination probe of 21 October, on Mango Rice at 12k and at 2k steps, on training frames. Replays its own demonstration's destination: 100% and 88%. Another source vial named: goes there 94% and 94%. Another destination named: follows it 19% and 31%. No command: follows the other destination 19% and 27%. All five camera images from the other demonstration: follows the cameras 81% and 75%. Joint positions from the other demonstration: 10% and 15%.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<rect x="10" y="8" width="18" height="18" rx="2" fill="#39d2c0"/>
<text x="36" y="25" font-size="22" fill="#e6edf3">at 12k</text>
<rect x="140" y="8" width="18" height="18" rx="2" fill="#bc8cff"/>
<text x="166" y="25" font-size="22" fill="#e6edf3">at 2k</text>
<text x="10" y="68" font-size="22" fill="#a9b4c2">replays its own demonstration</text>
<rect x="10" y="78" width="400" height="24" rx="2" fill="#39d2c0"/>
<text x="418" y="98" font-size="22" fill="#39d2c0" font-weight="600">100%</text>
<rect x="10" y="106" width="352" height="24" rx="2" fill="#bc8cff"/>
<text x="370" y="126" font-size="22" fill="#bc8cff" font-weight="600">88%</text>
<text x="10" y="166" font-size="22" fill="#a9b4c2">another source named: goes there</text>
<rect x="10" y="176" width="376" height="24" rx="2" fill="#39d2c0"/>
<text x="394" y="196" font-size="22" fill="#39d2c0" font-weight="600">94%</text>
<rect x="10" y="204" width="376" height="24" rx="2" fill="#bc8cff"/>
<text x="394" y="224" font-size="22" fill="#bc8cff" font-weight="600">94%</text>
<text x="10" y="264" font-size="22" fill="#e6edf3" font-weight="600">another destination named: follows it</text>
<rect x="10" y="274" width="76" height="24" rx="2" fill="#39d2c0"/>
<text x="94" y="294" font-size="22" fill="#39d2c0" font-weight="600">19%</text>
<rect x="10" y="302" width="124" height="24" rx="2" fill="#bc8cff"/>
<text x="142" y="322" font-size="22" fill="#bc8cff" font-weight="600">31%</text>
<text x="10" y="362" font-size="22" fill="#a9b4c2">no command: follows the other one</text>
<rect x="10" y="372" width="76" height="24" rx="2" fill="#39d2c0"/>
<text x="94" y="392" font-size="22" fill="#39d2c0" font-weight="600">19%</text>
<rect x="10" y="400" width="108" height="24" rx="2" fill="#bc8cff"/>
<text x="126" y="420" font-size="22" fill="#bc8cff" font-weight="600">27%</text>
<text x="10" y="460" font-size="22" fill="#e6edf3" font-weight="600">all cameras swapped: follows them</text>
<rect x="10" y="470" width="324" height="24" rx="2" fill="#39d2c0"/>
<text x="342" y="490" font-size="22" fill="#39d2c0" font-weight="600">81%</text>
<rect x="10" y="498" width="300" height="24" rx="2" fill="#bc8cff"/>
<text x="318" y="518" font-size="22" fill="#bc8cff" font-weight="600">75%</text>
<text x="10" y="558" font-size="22" fill="#a9b4c2">joint positions swapped: follows them</text>
<rect x="10" y="568" width="40" height="24" rx="2" fill="#39d2c0"/>
<text x="58" y="588" font-size="22" fill="#39d2c0" font-weight="600">10%</text>
<rect x="10" y="596" width="60" height="24" rx="2" fill="#bc8cff"/>
<text x="78" y="616" font-size="22" fill="#bc8cff" font-weight="600">15%</text>
</g>
</svg>
<figcaption><b>Figure 1.</b> The destination probe of 21 October: how often Mango Rice does what each row says, on training frames, at 12k and at 2k steps (<code>src/lib/probe.ts</code>). The two rows in bold are the finding. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-orange"><span class="bs-label">Why, in four steps</span><ol>
<li>The first 100 demonstrations were recorded one destination per sitting, with the bin and the light changing between sittings.</li>
<li>The camera picture says which sitting a frame is from.</li>
<li>The sitting says the destination, because each sitting had only one.</li>
<li>So the destination is read off the picture, and the words that name it are not needed.</li>
</ol><p>The source slot was learned, because it changed within a sitting.</p></div>
</div>

[Figure 1](#fig-probe) is the evidence: the model goes to another source when the command names it, but ignores a changed destination and follows swapped camera images instead, and the result is the same at 2k and 12k, so it is not overtraining. The fix was in the data: in the newer demonstrations one layout is recorded three times, to three destinations, so only the command can tell them apart ([Demonstrations](demonstrations.html)). Then Mango Pudding's destination followed the command on the arm ([why the first models read the destination off the picture](training-record.html#why-the-first-models-read-the-destination-off-the-picture), [the destination probe](training-record.html#the-destination-probe-of-21-october)).

</section>

<section class="card" id="the-offline-gate-of-mango-rice">

## Mango Rice's offline gate passed the source check from 5k on and never read the destination

<p class="bs-lead">Every 1,000 steps a checkpoint of Mango Rice was shown recorded frames without the robot; it left home every time, but read the destination on 0 of 7 frames at every checkpoint.</p>

<div class="bs-grid g2">
<figure id="fig-gate">
<svg class="inline-fig" viewBox="0 0 520 482" role="img" aria-label="The offline gate of Mango Rice at every checkpoint from 1k to 12k steps. Leaves home: 9 of 9 frames at every checkpoint. Reach follows the source: passes at 2k and from 5k on, fails at 1k, 3k and 4k. Binds the two numbers to their roles: fails at every checkpoint. Reads the destination: 0 of 7 frames at every checkpoint.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="150" y="28" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600">home</text>
<text x="250" y="28" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600">source</text>
<text x="350" y="28" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600">roles</text>
<text x="450" y="28" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600">destination</text>
<text x="60" y="69" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">1k</text>
<path d="M70 78L510 78" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="50" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="70" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="50" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="250" y="70" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="315" y="50" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="70" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="50" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="70" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="105" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">2k</text>
<path d="M70 114L510 114" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="86" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="106" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="86" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="106" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="86" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="106" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="86" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="106" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="141" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">3k</text>
<path d="M70 150L510 150" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="122" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="142" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="122" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="250" y="142" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="315" y="122" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="142" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="122" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="142" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="177" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">4k</text>
<path d="M70 186L510 186" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="158" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="178" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="158" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="250" y="178" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="315" y="158" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="178" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="158" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="178" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="213" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">5k</text>
<path d="M70 222L510 222" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="194" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="214" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="194" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="214" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="194" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="214" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="194" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="214" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="249" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">6k</text>
<path d="M70 258L510 258" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="230" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="250" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="230" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="250" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="230" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="250" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="230" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="250" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="285" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">7k</text>
<path d="M70 294L510 294" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="266" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="286" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="266" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="286" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="266" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="286" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="266" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="286" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="321" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">8k</text>
<path d="M70 330L510 330" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="302" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="322" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="302" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="322" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="302" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="322" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="302" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="322" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="357" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">9k</text>
<path d="M70 366L510 366" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="338" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="358" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="338" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="358" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="338" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="358" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="338" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="358" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="393" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">10k</text>
<path d="M70 402L510 402" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="374" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="394" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="374" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="394" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="374" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="394" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="374" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="394" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="429" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">11k</text>
<path d="M70 438L510 438" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="410" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="430" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="410" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="430" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="410" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="430" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="410" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="430" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
<text x="60" y="465" font-size="22" fill="#e6edf3" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">12k</text>
<path d="M70 474L510 474" stroke="#2f3b4a" stroke-width="1"/>
<rect x="115" y="446" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="150" y="466" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">9/9</text>
<rect x="215" y="446" width="70" height="26" rx="4" fill="#39d2c033" stroke="#39d2c0" stroke-width="2"/>
<text x="250" y="466" font-size="22" fill="#39d2c0" text-anchor="middle" font-weight="600">pass</text>
<rect x="315" y="446" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="350" y="466" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">fail</text>
<rect x="415" y="446" width="70" height="26" rx="4" fill="none" stroke="#ff7b72" stroke-width="2"/>
<text x="450" y="466" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">0/7</text>
</g>
</svg>
<figcaption><b>Figure 2.</b> The offline gate of Mango Rice, one row per checkpoint (<code>checkpoints</code> in <code>src/data/gate.json</code>, readings at commit <code>8065309</code>). Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">The four checks</span><ul>
<li><b>Home</b>: shown the first frame of nine real rollouts at home, does it predict a move away, on all three random seeds?</li>
<li><b>Source</b>: with vials in right-rack slots 1, 3 and 6, does the predicted shoulder angle order the slots as the demonstrations do, by at least 15°?</li>
<li><b>Roles</b>: does "from position 3 … to slot 1" reach differently from "from position 1 … to slot 3", by at least 8°?</li>
<li><b>Destination</b>: one second after a grasp, is the reach ordered by the asked destination, by at least 10°, on at least 4 of 7 frames?</li>
</ul></div>
</div>

[Figure 2](#fig-gate) shows checks that do not move with the error: the insertion error fell from 4.8° to 1.4° and the gripper error from 7.1° to 1.7° over the same checkpoints. "0/7" is a real count: no destination frame passed at any checkpoint. The record notes that <code>models.yaml</code> says the reach follows the source "from 2,000 steps on", while the gate fails at 3k and 4k ([the offline gate of Mango Rice](training-record.html#the-offline-gate-of-mango-rice)).

</section>

<section class="card" id="normalisation-and-the-quantile-pinning">
<span id="how-each-family-scales-its-data"></span><span id="the-mismatch-that-broke-mango-lassi"></span><span id="the-fix-and-the-test"></span>

## Merging the datasets widened the gripper's scale by 36%, and setting both grasp joints back fixed the grasp

<p class="bs-lead">A fine-tune keeps the scale of the model it starts from, so when the merged data stretched the gripper's range from 37.4° to 50.8°, every gripper command Mango Lassi inherited came out wider.</p>

<div class="bs-grid g2">
<figure id="fig-commands">
<svg class="inline-fig" viewBox="0 0 520 374" role="img" aria-label="Gripper commands Mango Rice meant, and what they became with the wider scale of the merged data: 5.0 degrees became 6.8, 8.0 became 10.9 and 12.0 became 16.3.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">a gripper command, in degrees</text>
<path d="M80 330L440 330" stroke="#2f3b4a" stroke-width="1"/>
<text x="70" y="338" font-size="22" fill="#7d8896" text-anchor="end">0</text>
<path d="M80 255L440 255" stroke="#2f3b4a" stroke-width="1"/>
<text x="70" y="263" font-size="22" fill="#7d8896" text-anchor="end">5</text>
<path d="M80 180L440 180" stroke="#2f3b4a" stroke-width="1"/>
<text x="70" y="188" font-size="22" fill="#7d8896" text-anchor="end">10</text>
<path d="M80 105L440 105" stroke="#2f3b4a" stroke-width="1"/>
<text x="70" y="113" font-size="22" fill="#7d8896" text-anchor="end">15</text>
<text x="130" y="362" font-size="22" fill="#a9b4c2" text-anchor="middle" font-weight="600">meant</text>
<text x="390" y="362" font-size="22" fill="#ff7b72" text-anchor="middle" font-weight="600">became</text>
<path d="M130 255L390 228" stroke="#ff7b72" stroke-width="2.5"/>
<circle cx="130" cy="255" r="6" fill="#39d2c0"/><circle cx="390" cy="228" r="6" fill="#ff7b72"/>
<text x="120" y="263" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">5.0</text>
<text x="400" y="236" font-size="22" fill="#ff7b72" font-weight="600">6.8</text>
<path d="M130 210L390 166.5" stroke="#ff7b72" stroke-width="2.5"/>
<circle cx="130" cy="210" r="6" fill="#39d2c0"/><circle cx="390" cy="166.5" r="6" fill="#ff7b72"/>
<text x="120" y="218" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">8.0</text>
<text x="400" y="174.5" font-size="22" fill="#ff7b72" font-weight="600">10.9</text>
<path d="M130 150L390 85.5" stroke="#ff7b72" stroke-width="2.5"/>
<circle cx="130" cy="150" r="6" fill="#39d2c0"/><circle cx="390" cy="85.5" r="6" fill="#ff7b72"/>
<text x="120" y="158" font-size="22" fill="#39d2c0" text-anchor="end" font-weight="600">12.0</text>
<text x="400" y="93.5" font-size="22" fill="#ff7b72" font-weight="600">16.3</text>
</g>
</svg>
<figcaption><b>Figure 3.</b> Gripper commands Mango Rice meant and what they became with the merged data's scale, as the 4 Nov Lab note gives them. On the arm: "failed pickup (but not missed)". Drawn in the page source from the record.</figcaption>
</figure>
<figure id="fig-grasp">
<svg class="inline-fig" viewBox="0 0 520 368" role="img" aria-label="Grasp on each version's own rollouts, 4 November. Mango Lassi, as trained, gripper q99 50.8 and wrist 31.5: 60%, 21 of 35. Mango Chutney, gripper set back to 37.4, wrist left at 31.5: 0%, 0 of 4. Mango Sorbet, gripper 37.4 and wrist 43.2: 90%, 9 of 10.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="26" font-size="22" fill="#a9b4c2">grasp, on its own rollouts</text>
<text x="10" y="64" font-size="22" fill="#e6edf3" font-weight="600">Mango Lassi</text>
<rect x="10" y="74" width="400" height="28" rx="3" fill="#121a24" stroke="#2f3b4a" stroke-width="1.5"/>
<rect x="10" y="74" width="240" height="28" rx="3" fill="#ff7b72"/>
<text x="258" y="96" font-size="22" fill="#ff7b72" font-weight="600">60%, 21 of 35</text>
<text x="10" y="132" font-size="22" fill="#7d8896">q99: gripper 50.8, wrist 31.5</text>
<text x="10" y="172" font-size="22" fill="#e6edf3" font-weight="600">Mango Chutney</text>
<rect x="10" y="182" width="400" height="28" rx="3" fill="#121a24" stroke="#2f3b4a" stroke-width="1.5"/>
<text x="18" y="204" font-size="22" fill="#ff7b72" font-weight="600">0%, 0 of 4</text>
<text x="10" y="240" font-size="22" fill="#7d8896">q99: gripper 37.4, wrist 31.5</text>
<text x="10" y="280" font-size="22" fill="#e6edf3" font-weight="600">Mango Sorbet</text>
<rect x="10" y="290" width="400" height="28" rx="3" fill="#121a24" stroke="#2f3b4a" stroke-width="1.5"/>
<rect x="10" y="290" width="360" height="28" rx="3" fill="#39d2c0"/>
<text x="362" y="312" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">90%, 9 of 10</text>
<text x="10" y="348" font-size="22" fill="#7d8896">q99: gripper 37.4, wrist 43.2</text>
</g>
</svg>
<figcaption><b>Figure 4.</b> Grasp on each version's own rollouts, 4 Nov: as trained, with only the gripper set back, and with both grasp joints set back. Mango Chutney ran Mango Sorbet's hard cases. Drawn in the page source from the record.</figcaption>
</figure>
</div>

[Figure 3](#fig-commands) shows the mechanism: "a grip becomes a loose hold". LeRobot's merge does not recompute percentiles; 15 of the 220 episodes open the gripper past 37.4° and set the scale for all of them. The wrist range moved too, tilting the gripper about 4.3° down at a typical grasp, and in the unpatched checkpoint the two errors partly cancelled, which is why [Figure 4](#fig-grasp) shows setting back the gripper alone as the worst of the three. Both cluster retrains then pinned all six joints in the dataset before training, and on 8 Nov every grasp of Mango Pudding that picked the vial up was commanded shut: "the 4 Nov scale problem is gone" ([the mismatch](training-record.html#the-mismatch-that-broke-mango-lassi), [the fix and the test](training-record.html#the-fix-and-the-test)).

</section>

<section class="card" id="the-retrains-on-the-university-cluster">

## Plain Bagel and Mango Pudding trained side by side on the university cluster, each in two chained 12-hour jobs

<p class="bs-lead">Both runs trained every weight of π0.5 on the 220 demonstrations, 16,000 steps at batch 16, one per A100 80 GB card, at 4.8 s a step.</p>

<div class="bs-grid g2">
<figure id="fig-cluster">
<svg class="inline-fig" viewBox="0 0 520 256" role="img" aria-label="The two retrains on the university cluster. Mango Pudding ran from Friday 6 November 13:41 to Saturday 7 November 11:18; Plain Bagel from Saturday 01:34 to Saturday 23:10, each on its own A100.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<path d="M10 30L10 214" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="10" y="244" font-size="22" fill="#7d8896">Fri 12:00</text>
<path d="M170 30L170 214" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="170" y="244" font-size="22" fill="#7d8896" text-anchor="middle">Sat 00:00</text>
<path d="M330 30L330 214" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="330" y="244" font-size="22" fill="#7d8896" text-anchor="middle">Sat 12:00</text>
<path d="M490 30L490 214" stroke="#2f3b4a" stroke-width="1.5" stroke-dasharray="4 6"/>
<text x="490" y="244" font-size="22" fill="#7d8896" text-anchor="end">Sun 00:00</text>
<text x="32.4444" y="48" font-size="22" fill="#bc8cff" font-weight="600">Mango Pudding</text>
<rect x="32.4444" y="60" width="288.222" height="30" rx="4" fill="#bc8cff"/>
<text x="40.4444" y="82" font-size="22" fill="#0d1117" font-weight="600">Fri 13:41</text>
<text x="312.667" y="82" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">Sat 11:18</text>
<text x="190.889" y="148" font-size="22" fill="#39d2c0" font-weight="600">Plain Bagel</text>
<rect x="190.889" y="160" width="288" height="30" rx="4" fill="#39d2c0"/>
<text x="198.889" y="182" font-size="22" fill="#0d1117" font-weight="600">Sat 01:34</text>
<text x="470.889" y="182" font-size="22" fill="#0d1117" text-anchor="end" font-weight="600">Sat 23:10</text>
</g>
</svg>
<figcaption><b>Figure 5.</b> When the two retrains ran, 6–7 Nov, as the 7 Nov Lab note gives the start and finish. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">How it ran</span><ul>
<li><b>Chained jobs</b>: each job saves a checkpoint, works out whether the next one fits in its time limit, and if not hands over to a job it queued beforehand.</li>
<li><b>Memory</b>: a full fine-tune peaks at about 38 GiB at batch 16; the fused AdamW avoids an extra copy of the weights.</li>
<li><b>Video</b>: decoded with PyAV, since the cluster has no FFmpeg libraries for torchcodec; "the frames are the same".</li>
<li><b>Same recipe</b>: operator-free starts, a checkpoint every 1,000 steps, quantiles pinned for all six joints; learning rate 1e-5 for Mango Pudding, 2.5e-5 for Plain Bagel.</li>
</ul></div>
</div>

[Figure 5](#fig-cluster) shows the two runs overlapping on the cluster's two A100 cards; the speed was limited by the GPU, not by data loading, so they did not slow each other down. Both losses fell to about 0.009 ([the retrains on the university cluster](training-record.html#the-retrains-on-the-university-cluster), [Retrains on the cluster, 7 Nov](retrains-on-the-cluster-7nov.html)).

</section>

<section class="card" id="the-probes-of-the-cluster-retrains">
<span id="the-short-fine-tunes-and-patched-checkpoints"></span>

## Offline, both retrains left home and read the source; neither passed the destination probe, yet Plain Bagel followed the digit on the arm

<p class="bs-lead">Three probes ran on checkpoints 8,000 and 10,000 to 16,000 of both runs; they were flat across checkpoints, so the last one was kept.</p>

<div class="bs-grid g2">
<figure id="fig-shortcut">
<svg class="inline-fig" viewBox="0 0 520 528" role="img" aria-label="probe_shortcut on the two cluster retrains: the share of frames, 1 second after the grasp, where the model follows the swapped episode, as a range over checkpoints 8,000 and 10,000 to 16,000. Prompt names another destination: Mango Pudding 12 to 21%, Plain Bagel 12 to 21%. No prompt: 31 to 33% and 21 to 42%. Four scene cameras swapped: 62 to 65% and 46 to 58%. All five cameras swapped: 75 to 83% and 71 to 79%. Source, another vial named, at the start frame: 81 to 94% and 88 to 94%.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<rect x="10" y="8" width="18" height="18" rx="2" fill="#bc8cff"/>
<text x="36" y="25" font-size="22" fill="#e6edf3">Mango Pudding</text>
<rect x="220" y="8" width="18" height="18" rx="2" fill="#39d2c0"/>
<text x="246" y="25" font-size="22" fill="#e6edf3">Plain Bagel</text>
<text x="10" y="68" font-size="22" fill="#a9b4c2">prompt names another destination</text>
<path d="M10 89L410 89" stroke="#2f3b4a" stroke-width="1"/>
<rect x="58" y="78" width="36" height="22" rx="3" fill="#bc8cff"/>
<text x="104" y="97" font-size="22" fill="#bc8cff" font-weight="600">12–21%</text>
<path d="M10 115L410 115" stroke="#2f3b4a" stroke-width="1"/>
<rect x="58" y="104" width="36" height="22" rx="3" fill="#39d2c0"/>
<text x="104" y="123" font-size="22" fill="#39d2c0" font-weight="600">12–21%</text>
<text x="10" y="164" font-size="22" fill="#a9b4c2">no prompt</text>
<path d="M10 185L410 185" stroke="#2f3b4a" stroke-width="1"/>
<rect x="134" y="174" width="8" height="22" rx="3" fill="#bc8cff"/>
<text x="152" y="193" font-size="22" fill="#bc8cff" font-weight="600">31–33%</text>
<path d="M10 211L410 211" stroke="#2f3b4a" stroke-width="1"/>
<rect x="94" y="200" width="84" height="22" rx="3" fill="#39d2c0"/>
<text x="188" y="219" font-size="22" fill="#39d2c0" font-weight="600">21–42%</text>
<text x="10" y="260" font-size="22" fill="#a9b4c2">4 scene cameras swapped</text>
<path d="M10 281L410 281" stroke="#2f3b4a" stroke-width="1"/>
<rect x="258" y="270" width="12" height="22" rx="3" fill="#bc8cff"/>
<text x="280" y="289" font-size="22" fill="#bc8cff" font-weight="600">62–65%</text>
<path d="M10 307L410 307" stroke="#2f3b4a" stroke-width="1"/>
<rect x="194" y="296" width="48" height="22" rx="3" fill="#39d2c0"/>
<text x="252" y="315" font-size="22" fill="#39d2c0" font-weight="600">46–58%</text>
<text x="10" y="356" font-size="22" fill="#a9b4c2">all 5 cameras swapped</text>
<path d="M10 377L410 377" stroke="#2f3b4a" stroke-width="1"/>
<rect x="310" y="366" width="32" height="22" rx="3" fill="#bc8cff"/>
<text x="352" y="385" font-size="22" fill="#bc8cff" font-weight="600">75–83%</text>
<path d="M10 403L410 403" stroke="#2f3b4a" stroke-width="1"/>
<rect x="294" y="392" width="32" height="22" rx="3" fill="#39d2c0"/>
<text x="336" y="411" font-size="22" fill="#39d2c0" font-weight="600">71–79%</text>
<text x="10" y="452" font-size="22" fill="#a9b4c2">source: other vial named</text>
<path d="M10 473L410 473" stroke="#2f3b4a" stroke-width="1"/>
<rect x="334" y="462" width="52" height="22" rx="3" fill="#bc8cff"/>
<text x="396" y="481" font-size="22" fill="#bc8cff" font-weight="600">81–94%</text>
<path d="M10 499L410 499" stroke="#2f3b4a" stroke-width="1"/>
<rect x="362" y="488" width="24" height="22" rx="3" fill="#39d2c0"/>
<text x="396" y="507" font-size="22" fill="#39d2c0" font-weight="600">88–94%</text>
</g>
</svg>
<figcaption><b>Figure 6.</b> <code>probe_shortcut</code> on the two retrains: the share of frames, 1 s after the grasp, where the model follows the swapped episode, as a range over the checkpoints, from the 9 Nov Lab note. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-violet"><span class="bs-label">The three probes, as the 9 Nov Lab note reads them</span><ul>
<li><code>probe_go</code>: both leave home at every checkpoint; all 9 real start frames move 72 to 88°.</li>
<li><code>probe_digits</code>: both pass the source and roles checks; the destination check fails, 0 of 7 frames for Mango Pudding and 1 to 2 of 7 for Plain Bagel, whose spread is larger on the same frames.</li>
<li><code>probe_shortcut</code> asks for a change of destination mid-carry, when the arm already moves to the recorded one, so on the newer data it does not separate the two models.</li>
<li>On the arm, with the command there from the start, Plain Bagel went where the digit said within one unchanged scene.</li>
</ul></div>
</div>

[Figure 6](#fig-shortcut) shows Plain Bagel leaning less on the scene cameras than Mango Pudding, while neither follows a changed destination prompt mid-carry. The note's judgement is that the probe was built for the failure of the 100-demonstration models and needs a cleaner version for the newer data ([the probes of the cluster retrains](training-record.html#the-probes-of-the-cluster-retrains)). The short fine-tunes and patched checkpoints are explained on [Models](models.html#spicy-chicken).

</section>

<section class="card" id="the-runs">
<span id="training-logs-per-run"></span><span id="interruptions-and-resumes"></span><span id="loss-curves"></span><span id="learning-rate-schedules-and-lengths"></span><span id="readings-at-commit-8065309"></span>

## Eight runs have a loss curve, and a low loss does not say how the arm behaves

<p class="bs-lead">Plain Bagel and Mango Pudding both end at a loss of 0.009 from different starting weights, and their results on the arm differ widely.</p>

<div class="bs-grid g2">
<figure id="fig-loss">
<svg class="inline-fig" viewBox="0 0 520 620" role="img" aria-label="Start loss at step 100, hollow, and end loss, filled, of the eight runs with a loss curve, on a log scale. pi 0.5: Spicy Chicken 0.125 to 0.009, Mango Rice 0.105 to 0.007, Mango Lassi 0.069 to 0.014, Mango Pudding 0.085 to 0.009, Plain Bagel 0.099 to 0.009. Isaac 0.5 Expert 0.041 to 0.003. FLUX 3 Action: Crispy Falafel 0.2342 to 0.088, Sweet Corn 0.2668 to 0.085.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="10" y="30" font-size="22" fill="#a9b4c2" font-weight="600">π0.5</text>
<text x="10" y="62" font-size="22" fill="#e6edf3">Spicy Chicken  0.125 → 0.009</text>
<path d="M149.1 78L392.429 78" stroke="#39d2c0" stroke-width="3"/>
<circle cx="392.4" cy="78" r="7" fill="#0d1117" stroke="#39d2c0" stroke-width="3"/><circle cx="149.1" cy="78" r="7" fill="#39d2c0"/>
<text x="10" y="118" font-size="22" fill="#e6edf3">Mango Rice  0.105 → 0.007</text>
<path d="M125.858 134L376.305 134" stroke="#39d2c0" stroke-width="3"/>
<circle cx="376.3" cy="134" r="7" fill="#0d1117" stroke="#39d2c0" stroke-width="3"/><circle cx="125.9" cy="134" r="7" fill="#39d2c0"/>
<text x="10" y="174" font-size="22" fill="#e6edf3">Mango Lassi  0.069 → 0.014</text>
<path d="M189.962 190L337.476 190" stroke="#39d2c0" stroke-width="3"/>
<circle cx="337.5" cy="190" r="7" fill="#0d1117" stroke="#39d2c0" stroke-width="3"/><circle cx="190.0" cy="190" r="7" fill="#39d2c0"/>
<text x="10" y="230" font-size="22" fill="#e6edf3">Mango Pudding  0.085 → 0.009</text>
<path d="M149.1 246L356.762 246" stroke="#39d2c0" stroke-width="3"/>
<circle cx="356.8" cy="246" r="7" fill="#0d1117" stroke="#39d2c0" stroke-width="3"/><circle cx="149.1" cy="246" r="7" fill="#39d2c0"/>
<text x="10" y="286" font-size="22" fill="#e6edf3">Plain Bagel  0.099 → 0.009</text>
<path d="M149.1 302L370.863 302" stroke="#39d2c0" stroke-width="3"/>
<circle cx="370.9" cy="302" r="7" fill="#0d1117" stroke="#39d2c0" stroke-width="3"/><circle cx="149.1" cy="302" r="7" fill="#39d2c0"/>
<text x="10" y="350" font-size="22" fill="#a9b4c2" font-weight="600">Isaac 0.5</text>
<text x="10" y="382" font-size="22" fill="#e6edf3">Isaac 0.5 Expert  0.041 → 0.003</text>
<path d="M47.4983 398L289.336 398" stroke="#79c0ff" stroke-width="3"/>
<circle cx="289.3" cy="398" r="7" fill="#0d1117" stroke="#79c0ff" stroke-width="3"/><circle cx="47.5" cy="398" r="7" fill="#79c0ff"/>
<text x="10" y="446" font-size="22" fill="#a9b4c2" font-weight="600">FLUX 3 Action</text>
<text x="10" y="478" font-size="22" fill="#e6edf3">Crispy Falafel  0.2342 → 0.088</text>
<path d="M359.97 494L450.495 494" stroke="#bc8cff" stroke-width="3"/>
<circle cx="450.5" cy="494" r="7" fill="#0d1117" stroke="#bc8cff" stroke-width="3"/><circle cx="360.0" cy="494" r="7" fill="#bc8cff"/>
<text x="10" y="534" font-size="22" fill="#e6edf3">Sweet Corn  0.2668 → 0.085</text>
<path d="M356.762 550L462.548 550" stroke="#bc8cff" stroke-width="3"/>
<circle cx="462.5" cy="550" r="7" fill="#0d1117" stroke="#bc8cff" stroke-width="3"/><circle cx="356.8" cy="550" r="7" fill="#bc8cff"/>
<path d="M47.4983 576L47.4983 584" stroke="#7d8896" stroke-width="2"/>
<text x="47.4983" y="610" font-size="22" fill="#7d8896">0.003</text>
<path d="M158.844 576L158.844 584" stroke="#7d8896" stroke-width="2"/>
<text x="158.844" y="610" font-size="22" fill="#7d8896" text-anchor="middle">0.01</text>
<path d="M260.446 576L260.446 584" stroke="#7d8896" stroke-width="2"/>
<text x="260.446" y="610" font-size="22" fill="#7d8896" text-anchor="middle">0.03</text>
<path d="M371.792 576L371.792 584" stroke="#7d8896" stroke-width="2"/>
<text x="371.792" y="610" font-size="22" fill="#7d8896" text-anchor="middle">0.1</text>
<path d="M473.395 576L473.395 584" stroke="#7d8896" stroke-width="2"/>
<text x="473.395" y="610" font-size="22" fill="#7d8896" text-anchor="end">0.3</text>
<path d="M10 576L500 576" stroke="#2f3b4a" stroke-width="2"/>
</g>
</svg>
<figcaption><b>Figure 7.</b> Start loss at step 100 (hollow) and end loss (filled) of each run with a curve, readings at commit <code>8065309</code> (<code>points</code> in <code>src/data/training.json</code>). Each kind measures its loss its own way, so compare runs only within a kind. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-muted"><span class="bs-label">What a curve cannot say</span><ul>
<li>There is no validation loss for the π0.5 and FLUX runs: every demonstration is used for training, so a curve cannot show when a model starts to memorise. The robot is the only test.</li>
<li>Isaac 0.5 Expert is the exception: 8 demonstrations were held out and scored offline.</li>
<li>Crispy Falafel's loss was flat from about 8,000 steps.</li>
<li>Runs with more than one log were stopped and resumed from a saved checkpoint: Plain Bagel and Mango Pudding from 8,000, Spicy Chicken from 7,000 and again from 8,000, Crispy Falafel from 10,000.</li>
</ul></div>
</div>

[Figure 7](#fig-loss) puts the eight curves' ends side by side. The 4 Nov Lab note records an overfit ceiling for π0.5 near 3 passes, about 21,000 steps on the 220 demonstrations; the retrains were set to 16,000 steps, 2.3 passes. The full curves are on the website's [Training page](https://cognitive-software-labs.github.io/vial-sort/training/) ([the runs](training-record.html#the-runs), [loss curves](training-record.html#loss-curves)).

</section>

<section class="card" id="data-preparation-that-training-depends-on">
<span id="image-augmentation"></span>

## Three changes to the data, and the same image augmentations, sit under every later run

<p class="bs-lead">Cutting the idle start and end, removing the operator from the start frames and one sentence per move came from what the October models showed.</p>

<div class="scroll" role="region" aria-label="Data changes that training depends on" tabindex="0" data-reader-horizontal>
<table>
<thead><tr><th>Change</th><th>First used in</th><th>What it is</th><th>Why</th></tr></thead>
<tbody>
<tr><th>Idle start and end cut</th><td>Pretzel One; corrected for Pretzel Two and Mango Rice</td><td>The corrected trim cuts at the widest opening after the grasp, the real let-go, not at the first loosening</td><td>The idle home pose was both the cue to go and the cue to stay</td></tr>
<tr><th>Operator-free start</th><td>Pretzel One and every later π0.5 run; Isaac on the wrist camera only</td><td>The first frames, where the operator leaned over the robot, replaced by views of the arm at home with nobody near it</td><td>Spicy Chicken had learned the operator leaning in as its cue to move</td></tr>
<tr><th>One sentence per move</th><td>Mango Rice and later</td><td>The 100 wordings replaced by 32 canonical sentences</td><td>Not stated beyond the change itself</td></tr>
<tr><th>Two cameras only</th><td>Crispy Falafel, Sweet Corn</td><td>One scene view and the wrist view</td><td>The FLUX input</td></tr>
</tbody>
</table>
</div>

<div class="bs-grid g2">
<div class="bs-part bs-teal"><span class="bs-label">Image augmentation</span><ul>
<li>π0.5 runs with a config and Isaac 0.5 Expert: colour jitter (brightness ±20%, contrast ±20%, saturation ±50%, hue ±0.05), sharpness, and a small shift and rotation (≤5% and ±5°), up to 3 per image.</li>
<li>FLUX: no augmentation recorded; prompt dropout 0.1 instead.</li>
</ul></div>
<div class="bs-part bs-violet"><span class="bs-label">How each family scales its data</span><ul>
<li><b>π0.5</b>: the 1st and 99th percentile of the training set.</li>
<li><b>Isaac 0.5</b>: the checkpoint's own percentiles, widened only where this data reaches further.</li>
<li><b>FLUX 3 Action</b>: the base's files rewritten with this data's percentiles.</li>
</ul></div>
</div>

The table lists what training used; the trims and wordings as data belong to [Demonstrations](demonstrations.html) ([data preparation](training-record.html#data-preparation-that-training-depends-on), [image augmentation](training-record.html#image-augmentation)).

</section>

<section class="card" id="where-sources-disagree">
<span id="not-verified"></span>

## Some losses, dates and checks are stated differently in two sources, and no number was checked against the logs

<p class="bs-lead">The training logs, probe outputs and configs are on the workstation, so where the sources disagree the record lists both sides.</p>

<div class="bs-grid g2">
<div class="bs-part bs-orange"><span class="bs-label">Where sources disagree, for example</span><ul>
<li><b>Crispy Falafel's loss</b>: 0.249 to 0.087 in <code>models.yaml</code>; 0.2342 to 0.088 in the data.</li>
<li><b>Sweet Corn's loss</b>: 0.345 to 0.089 in <code>models.yaml</code>; 0.2668 to 0.085 in the data.</li>
<li><b>Seeds of the leaves-home check</b>: all three random seeds for Mango Rice's gate; 4 of 4 seeds for the cluster probe. They may be two versions of the check.</li>
<li><b>The two retrains' run facts</b>: exactly 21.5 h each in the data; about 21.6 h each from the Lab note's timestamps.</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Not verified</span><ul>
<li>No loss, duration, memory figure or probe result was checked against the logs or probe outputs.</li>
<li>The training dates of Mango Rice, Mango Lassi and Sweet Corn, and the hardware of Mango Lassi and the two probes, are not stated.</li>
<li>The probe scripts, <code>tools/pin_quantiles.py</code> and <code>train.sh</code> are cited but not in this repository.</li>
<li>The record was written by AI agents and waits for a <a href="docs.open.human-review.md.html">review by a person</a>.</li>
</ul></div>
</div>

Every disagreement is in the record with both sources ([where sources disagree](training-record.html#where-sources-disagree), [not verified](training-record.html#not-verified)).

</section>
