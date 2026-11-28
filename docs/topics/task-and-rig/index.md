+++
title = "The task and the rig"
brand_sub = "the task · the arm · racks and slots · cameras · commands · earlier rigs"
description = "What the robot is asked to do and the hardware it does it with: the arm pair, the racks and their slots, the vials, the five cameras and the earlier rigs."
components = ["toc", "nav", "filelinks", "lightbox", "panel-switcher"]
page_css = ["build-sheet.css", "../site/assets/figure-columns.css"]
toc = [["The task", "#the-task"], ["The arm", "#the-arm"], ["Five cameras", "#the-five-cameras"], ["Who sees what", "#which-models-see-which-cameras"], ["Commands", "#what-a-command-looks-like"], ["Earlier rigs", "#earlier-rigs"], ["Not verified", "#not-verified"]]
+++

# The task and the rig

<section class="card" id="the-task">
<span id="scope"></span>

## One typed command moves one vial between named places, and nobody steers the arm

<p class="bs-lead">A person types one command, and the follower arm takes the vial from the named slot and puts it in the named slot of either rack or in the bin.</p>

<span id="racks-slots-and-the-bin"></span>
<style>
/* Local to this page: a figure with a second, narrower drawing shows it when the figure is too narrow
   for the wide drawing's labels to stay at 11 px or more. */
.fig-switch {container-type:inline-size;container-name:figswitch;}
.fig-switch > svg.fig-narrow {display:none;}
@container figswitch (max-width: 359.98px) {
  .fig-switch > svg.fig-wide {display:none;}
  .fig-switch > svg.fig-narrow {display:block;}
}
</style>
<figure id="fig-racks" class="fig-switch">
<svg class="inline-fig fig-wide" viewBox="0 0 1000 310" role="img" aria-label="The website's drawing of the table: the left rack with slots L1 to L6, the bin, and the right rack with slots R1 to R6, slots numbered 1 to 6 from left to right in each rack. An arrow shows the recorded move R3 to L6. Slots 1, 3 and 6 have solid rings, slot 4 a half-dashed ring and slots 2 and 5 dashed rings.">
<defs><marker id="fig-racks-head" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#39d2c0"/></marker></defs>
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<rect x="26" y="160" width="416" height="80" rx="40" fill="#1b2430" stroke="#2f3b4a" stroke-width="2"/>
<rect x="558" y="160" width="416" height="80" rx="40" fill="#1b2430" stroke="#2f3b4a" stroke-width="2"/>
<rect x="460" y="164" width="80" height="72" rx="10" fill="none" stroke="#a9b4c2" stroke-width="3"/>
<g font-family="'IBM Plex Mono',ui-monospace,monospace" font-size="34" font-weight="600" text-anchor="middle">
<circle cx="64" cy="200" r="30" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="64" y="212" fill="#e6edf3">L1</text>
<circle cx="132" cy="200" r="30" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="132" y="212" fill="#7d8896">L2</text>
<circle cx="200" cy="200" r="30" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="200" y="212" fill="#e6edf3">L3</text>
<circle cx="268" cy="200" r="30" fill="#121a24"/><path d="M238 200A30 30 0 0 1 298 200" fill="none" stroke="#e6edf3" stroke-width="3"/><path d="M298 200A30 30 0 0 1 238 200" fill="none" stroke="#e6edf3" stroke-width="3" stroke-dasharray="7 6"/><text x="268" y="212" fill="#e6edf3">L4</text>
<circle cx="336" cy="200" r="30" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="336" y="212" fill="#7d8896">L5</text>
<circle cx="404" cy="200" r="30" fill="#0f1d22" stroke="#39d2c0" stroke-width="4"/><text x="404" y="212" fill="#39d2c0">L6</text>
<circle cx="596" cy="200" r="30" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="596" y="212" fill="#e6edf3">R1</text>
<circle cx="664" cy="200" r="30" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="664" y="212" fill="#7d8896">R2</text>
<circle cx="732" cy="200" r="30" fill="#0f1d22" stroke="#39d2c0" stroke-width="4"/><text x="732" y="212" fill="#39d2c0">R3</text>
<circle cx="800" cy="200" r="30" fill="#121a24"/><path d="M770 200A30 30 0 0 1 830 200" fill="none" stroke="#e6edf3" stroke-width="3"/><path d="M830 200A30 30 0 0 1 770 200" fill="none" stroke="#e6edf3" stroke-width="3" stroke-dasharray="7 6"/><text x="800" y="212" fill="#e6edf3">R4</text>
<circle cx="868" cy="200" r="30" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="868" y="212" fill="#7d8896">R5</text>
<circle cx="936" cy="200" r="30" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="936" y="212" fill="#e6edf3">R6</text>
</g>
<path d="M716 160Q570 34 420 160" fill="none" stroke="#39d2c0" stroke-width="4" marker-end="url(#fig-racks-head)"/>
<text x="568" y="62" font-size="36" font-weight="600" fill="#39d2c0" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,monospace">R3 → L6</text>
<text x="234" y="292" font-size="34" fill="#a9b4c2" text-anchor="middle">left rack</text>
<text x="500" y="292" font-size="34" fill="#a9b4c2" text-anchor="middle">bin</text>
<text x="766" y="292" font-size="34" fill="#a9b4c2" text-anchor="middle">right rack</text>
</g>
</svg>
<svg class="inline-fig fig-narrow" viewBox="0 0 420 360" role="img" aria-label="The website's drawing of the table, stacked for a narrow screen: the left rack with slots L1 to L6, the bin, and the right rack with slots R1 to R6, slots numbered 1 to 6 from left to right in each rack. An arrow shows the recorded move R3 to L6. Slots 1, 3 and 6 have solid rings, slot 4 a half-dashed ring and slots 2 and 5 dashed rings.">
<defs><marker id="fig-racks-head-narrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#39d2c0"/></marker></defs>
<g font-family="'IBM Plex Sans',system-ui,sans-serif">
<text x="18" y="44" font-size="24" fill="#a9b4c2">left rack</text>
<rect x="18" y="66" width="388" height="60" rx="30" fill="#1b2430" stroke="#2f3b4a" stroke-width="2"/>
<rect x="175" y="160" width="70" height="56" rx="10" fill="none" stroke="#a9b4c2" stroke-width="3"/>
<text x="163" y="196" font-size="24" fill="#a9b4c2" text-anchor="end">bin</text>
<text x="18" y="258" font-size="24" fill="#a9b4c2">right rack</text>
<rect x="18" y="280" width="388" height="60" rx="30" fill="#1b2430" stroke="#2f3b4a" stroke-width="2"/>
<g font-family="'IBM Plex Mono',ui-monospace,monospace" font-size="23" font-weight="600" text-anchor="middle">
<circle cx="52" cy="96" r="27" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="52" y="104" fill="#e6edf3">L1</text><circle cx="116" cy="96" r="27" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="116" y="104" fill="#7d8896">L2</text><circle cx="180" cy="96" r="27" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="180" y="104" fill="#e6edf3">L3</text><circle cx="244" cy="96" r="27" fill="#121a24"/><path d="M217 96A27 27 0 0 1 271 96" fill="none" stroke="#e6edf3" stroke-width="3"/><path d="M271 96A27 27 0 0 1 217 96" fill="none" stroke="#e6edf3" stroke-width="3" stroke-dasharray="7 6"/><text x="244" y="104" fill="#e6edf3">L4</text><circle cx="308" cy="96" r="27" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="308" y="104" fill="#7d8896">L5</text><circle cx="372" cy="96" r="27" fill="#0f1d22" stroke="#39d2c0" stroke-width="4"/><text x="372" y="104" fill="#39d2c0">L6</text>
<circle cx="52" cy="310" r="27" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="52" y="318" fill="#e6edf3">R1</text><circle cx="116" cy="310" r="27" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="116" y="318" fill="#7d8896">R2</text><circle cx="180" cy="310" r="27" fill="#0f1d22" stroke="#39d2c0" stroke-width="4"/><text x="180" y="318" fill="#39d2c0">R3</text><circle cx="244" cy="310" r="27" fill="#121a24"/><path d="M217 310A27 27 0 0 1 271 310" fill="none" stroke="#e6edf3" stroke-width="3"/><path d="M271 310A27 27 0 0 1 217 310" fill="none" stroke="#e6edf3" stroke-width="3" stroke-dasharray="7 6"/><text x="244" y="318" fill="#e6edf3">R4</text><circle cx="308" cy="310" r="27" fill="#121a24" stroke="#7d8896" stroke-width="3" stroke-dasharray="7 6"/><text x="308" y="318" fill="#7d8896">R5</text><circle cx="372" cy="310" r="27" fill="#121a24" stroke="#e6edf3" stroke-width="3"/><text x="372" y="318" fill="#e6edf3">R6</text>
</g>
<path d="M184 282Q300 200 364 130" fill="none" stroke="#39d2c0" stroke-width="4" marker-end="url(#fig-racks-head-narrow)"/>
<text x="404" y="244" font-size="24" font-weight="600" fill="#39d2c0" text-anchor="end" font-family="'IBM Plex Mono',ui-monospace,monospace">R3 → L6</text>
</g>
</svg>
<figcaption><b>Figure 1.</b> The table as every page of the website draws it, with the recorded move <code>R3 → L6</code>. In the 100- and 220-demonstration sets, slots 1, 3 and 6 (solid rings) are sources and destinations, slot 4 (half dashed) is only a source, and slots 2 and 5 (dashed) are neither: they are held out. The bin is only ever a destination. A schematic drawn in the page source from the record, not a plan of the table.</figcaption>
</figure>

<div class="bs-grid g2">
<div class="bs-part bs-teal"><span class="bs-label">Read the figure</span><h3>Twelve slots and a bin, named by position</h3><ul>
<li><b>Left rack</b> <code>L1</code>…<code>L6</code>: the rack to the left of the follower arm, seen from the arm. It is the top rack in the overhead camera.</li>
<li><b>Right rack</b> <code>R1</code>…<code>R6</code>: the other one, the bottom rack in the overhead camera.</li>
<li><b>Slot 1</b> is the hole nearest the follower arm.</li>
<li><b>The bin</b> sits between the racks and is never a source.</li>
</ul></div>
<div class="bs-part bs-violet"><span class="bs-label">Words used on these pages</span><h3>A move, a command, a rollout</h3><ul>
<li><b>Move</b>: one source slot and one destination, written <code>R3 → L6</code>.</li>
<li><b>Command</b>: the sentence typed to the robot. It names positions, never colours.</li>
<li><b>Rollout</b>: one attempt by the robot alone at one command; a <b>session</b> holds several.</li>
<li><b>Held out</b>: never recorded on purpose, to test whether a model reaches slots no demonstration used.</li>
</ul></div>
</div>

[Figure 1](#fig-racks) is the drawing the website uses for every move. A move is the whole task: one vial, from one named slot to one named place, and nobody steers the arm while it runs. The held-out slots test whether a model can reach slots no demonstration used ([the task](task-and-rig-record.html#the-task), [racks, slots and the bin](task-and-rig-record.html#racks-slots-and-the-bin)). Everything on this page is read from the website's files and the Lab notes; none of it was checked on the rig or reviewed by a person yet ([not verified](#not-verified)).

</section>

<section class="card" id="the-arm">
<span id="demonstrate-train-run"></span>

## A person drives the leader arm to teach; the follower arm then works alone

<p class="bs-lead">Every model on the website came out of the same three steps: a person demonstrates with the SO-101 arm pair, a model learns from the recordings, and the model then drives the follower arm by itself.</p>

<figure id="fig-loop">
<div class="bs-flow" role="img" aria-label="Step 1, demonstrate: a person moves the leader arm, the follower arm copies it, and all cameras and joint positions are logged. Step 2, train: three kinds of model learn from the demonstrations, pi 0.5, FLUX 3 Action and Isaac 0.5. Step 3, run: the model reads the command, the camera images and the joint angles and drives the six joints of the follower arm; nobody steers it.">
<div class="bs-node bs-teal"><span class="bs-label">Step 1</span><b>Demonstrate</b><ul><li>a person moves the leader arm and the follower copies it</li><li>all cameras and the joint positions are logged</li></ul></div>
<div class="bs-arrow"><span>recordings</span></div>
<div class="bs-node bs-violet"><span class="bs-label">Step 2</span><b>Train</b><ul><li>three kinds of model learn from the demonstrations</li><li>π0.5, FLUX 3 Action and Isaac 0.5</li></ul></div>
<div class="bs-arrow"><span>a model</span></div>
<div class="bs-node bs-orange"><span class="bs-label">Step 3</span><b>Run</b><ul><li>the model reads the command, the camera images and the joint angles</li><li>it drives the follower's six joints; nobody steers it</li></ul></div>
</div>
<figcaption><b>Figure 2.</b> Demonstrate, train, run: the loop behind every model on the website. A diagram drawn in the page source from the record; it shows no measured results.</figcaption>
</figure>

<div class="bs-grid g2">
<div class="bs-part bs-teal"><span class="bs-label">The arm</span><h3>A 3D-printed SO-101 with six joints</h3><ul>
<li>The pair is a leader and a follower. The follower does the work in a rollout; in the photograph of the current rig it is on the left, with the leader in the foreground.</li>
<li>A vial between the gripper's jaws stops them at about 8° (5.8–10.2°); empty jaws close to 0.4–4.5°.</li>
<li>The sources name the gripper and the wrist pitch (<code>wrist_flex</code>), and pan, lift and elbow. The name of the sixth joint is not stated.</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">The computer</span><h3>The workstation, hardware not stated</h3><ul>
<li>The current rig runs on a computer the sources call "the workstation"; its hardware is not stated in this repository.</li>
<li>The August work ran on a Jetson Thor rig instead (<a href="#earlier-rigs">earlier rigs</a>).</li>
</ul></div>
</div>

[Figure 2](#fig-loop) is the whole method in three steps. The same follower arm both copies the person during a demonstration and acts alone in a rollout, so what a model learns is how this arm moved while a person drove it ([demonstrate, train, run](task-and-rig-record.html#demonstrate-train-run), [the arm](task-and-rig-record.html#the-arm)). Which moves were demonstrated is in [Demonstrations](demonstrations.html); how rollouts are run and scored is in [Evaluation](evaluation.html).

<!-- fold: detail Two wiring incidents in the Lab notes -->
<span id="wiring-incidents-recorded-in-the-lab-notes"></span>

- **4 November 2026.** The USB hub `9-2` carries the wrist camera, the right camera and both arms. Its devices re-enumerated about 66 times that day, and rollouts 8 and 9 of that session are not valid data because of it. The note's fix was to move both arm cables to motherboard ports or use a powered hub; whether this was done is not stated ([Arm test, 4 Nov](b4000-arm-test-4nov.html)).
- **9 November 2026, 00:05:28.** The follower stopped answering once (`Failed to sync read 'Present_Position'`): the motor bus dropped out ([Arm test, 8–9 Nov](b16000-arm-test-8nov.html)).

<!-- /fold -->

</section>

<section class="card" id="the-five-cameras">

## Five colour cameras watch the table from five places, all at 30 frames a second

<p class="bs-lead">One camera looks down on the whole table, three look across it from different heights and sides, and one rides on the gripper.</p>

<div class="bs-grid g2">
<figure id="fig-rig-photo">
<img src="../../public/img/setup_current.webp" width="1362" height="1599" loading="lazy" alt="The current rig, labelled: the right, top-down, left-top and left-bottom cameras on stands and an arm above the table, the wrist camera on the follower arm, two racks with coloured vials, the bin, the follower arm on the left and the leader arm in the foreground.">
<figcaption><b>Figure 3.</b> The current rig, with the labels of the website's photograph (<code>public/img/setup_current.webp</code>).</figcaption>
</figure>
<figure id="fig-camera-stills">
<div class="panel-switcher" data-panel-switcher data-panel-default="top_down">
<div class="panel-switcher-controls" role="group" aria-label="Camera shown">
<button type="button" data-panel-choice="top_down" aria-pressed="false" aria-controls="cam-top-down">Overhead</button>
<button type="button" data-panel-choice="left_top" aria-pressed="false" aria-controls="cam-left-top">Across the table</button>
<button type="button" data-panel-choice="left_bottom" aria-pressed="false" aria-controls="cam-left-bottom">Near eye level</button>
<button type="button" data-panel-choice="right" aria-pressed="false" aria-controls="cam-right">From the side</button>
<button type="button" data-panel-choice="wrist" aria-pressed="false" aria-controls="cam-wrist">On the gripper</button>
</div>
<div id="cam-top-down" data-panel="top_down"><img src="../../public/img/cams/top_down.webp" width="640" height="480" loading="lazy" alt="The overhead camera's view of the table."><p><code>top_down</code> <b>Overhead</b>: the only high-angle view; it sees both racks, the bin and the arm at once, with no people in it.</p></div>
<div id="cam-left-top" data-panel="left_top"><img src="../../public/img/cams/left_top.webp" width="640" height="480" loading="lazy" alt="The across-the-table camera's view, with the operator in the frame."><p><code>left_top</code> <b>Across the table</b>: high, across the table. The operator is in view in every frame, on purpose: someone usually stands there during a rollout too.</p></div>
<div id="cam-left-bottom" data-panel="left_bottom"><img src="../../public/img/cams/left_bottom.webp" width="640" height="480" loading="lazy" alt="The near-eye-level camera's view of the racks."><p><code>left_bottom</code> <b>Near eye level</b>: the colour stream of a RealSense camera. The vials look largest here, and which holes hold a vial can be read.</p></div>
<div id="cam-right" data-panel="right"><img src="../../public/img/cams/right.webp" width="640" height="480" loading="lazy" alt="The side camera's wide view of the workspace."><p><code>right</code> <b>From the side</b>: a wide view of the workspace from the other side. The operator sits in the right 16% of this camera in every frame.</p></div>
<div id="cam-wrist" data-panel="wrist"><img src="../../public/img/cams/wrist.webp" width="640" height="480" loading="lazy" alt="The wrist camera's close view from the gripper."><p><code>wrist</code> <b>On the gripper</b>: close up, mounted on the gripper; the vial fills the frame during a grasp.</p></div>
</div>
<figcaption><b>Figure 4.</b> What each camera sees: one demonstration frame per camera, as the website shows it (640 × 480 stills in <code>public/img/cams/</code>, made by <code>scripts/make_cams.py</code>). Each names the key in the recordings and the name the pages use.</figcaption>
</figure>
</div>

[Figure 3](#fig-rig-photo) shows where the cameras stand around the table, and [Figure 4](#fig-camera-stills) what each of them sees; choose a camera above the still. A sixth stream, `rs_depth`, is the RealSense depth stream: it was recorded only in the second sitting of 3 November, loses the translucent vials, and no model is trained on it ([the five cameras](task-and-rig-record.html#the-five-cameras)). The pages call `left_bottom` "near eye level" in one place and describe it as near table level in another; which is its true height was not checked.

</section>

<section class="card" id="which-models-see-which-cameras">

## Most models see all five colour cameras; two see only the overhead and wrist views

<p class="bs-lead">The π0.5 models take all five colour cameras, Isaac 0.5 Expert and Crispy Falafel take two, and no model is trained on depth.</p>

<div class="fig-cols">
<figure id="fig-camera-matrix" class="fig-switch">
<svg class="inline-fig fig-wide" viewBox="0 0 600 400" role="img" aria-label="A matrix of cameras against models. The pi 0.5 models see top_down, left_top, left_bottom, right and wrist. Isaac 0.5 Expert and Crispy Falafel see top_down and wrist. Sweet Corn sees left, from the earlier camera layout, and wrist. No model sees rs_depth.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif" font-size="22" font-weight="600" fill="#e6edf3" text-anchor="middle">
<text x="262" y="34">π0.5</text><text x="262" y="62">models</text>
<text x="348" y="34">Isaac 0.5</text><text x="348" y="62">Expert</text>
<text x="434" y="34">Crispy</text><text x="434" y="62">Falafel</text>
<text x="520" y="34">Sweet</text><text x="520" y="62">Corn</text>
</g>
<g stroke="#2f3b4a" stroke-width="2">
<path d="M16 80H584M16 125H584M16 170H584M16 215H584M16 260H584"/>
<path d="M16 305H584" stroke="#7d8896" stroke-width="3"/>
<path d="M16 350H584M16 395H584"/>
</g>
<g font-family="'IBM Plex Mono',ui-monospace,monospace" font-size="22" fill="#e6edf3">
<text x="20" y="110">top_down</text><text x="20" y="155">left_top</text><text x="20" y="200">left_bottom</text><text x="20" y="245">right</text><text x="20" y="290">wrist</text>
<text x="20" y="335" fill="#a9b4c2">rs_depth</text><text x="20" y="380" fill="#a9b4c2">left (earlier)</text>
</g>
<g fill="#39d2c0">
<circle cx="262" cy="102" r="11"/><circle cx="262" cy="147" r="11"/><circle cx="262" cy="192" r="11"/><circle cx="262" cy="237" r="11"/><circle cx="262" cy="282" r="11"/>
<circle cx="348" cy="102" r="11"/><circle cx="348" cy="282" r="11"/>
<circle cx="434" cy="102" r="11"/><circle cx="434" cy="282" r="11"/>
<circle cx="520" cy="282" r="11"/><circle cx="520" cy="372" r="11"/>
</g>
<text x="391" y="335" font-size="22" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Sans',system-ui,sans-serif">no model</text>
</svg>
<svg class="inline-fig fig-narrow" viewBox="0 0 450 392" role="img" aria-label="A matrix of cameras against models, drawn for a narrow screen. The pi 0.5 models see top_down, left_top, left_bottom, right and wrist. Isaac 0.5 Expert and Crispy Falafel see top_down and wrist. Sweet Corn sees left, from the earlier camera layout, and wrist. No model sees rs_depth.">
<g font-family="'IBM Plex Sans',system-ui,sans-serif" font-size="20" font-weight="600" fill="#e6edf3" text-anchor="middle">
<text x="186" y="52">π0.5</text><text x="186" y="76">models</text><text x="260" y="28">Isaac</text><text x="260" y="52">0.5</text><text x="260" y="76">Expert</text><text x="334" y="52">Crispy</text><text x="334" y="76">Falafel</text><text x="408" y="52">Sweet</text><text x="408" y="76">Corn</text>
</g>
<g stroke="#2f3b4a" stroke-width="2">
<path d="M8 90H444M8 132H444M8 172H444M8 212H444M8 252H444"/>
<path d="M8 292H444" stroke="#7d8896" stroke-width="3"/>
<path d="M8 332H444M8 388H444"/>
</g>
<g font-family="'IBM Plex Mono',ui-monospace,monospace" font-size="20" fill="#e6edf3">
<text x="10" y="119">top_down</text><text x="10" y="159">left_top</text><text x="10" y="199">left_bottom</text><text x="10" y="239">right</text><text x="10" y="279">wrist</text>
<text x="10" y="319" fill="#a9b4c2">rs_depth</text><text x="10" y="356" fill="#a9b4c2">left</text><text x="10" y="380" fill="#a9b4c2">(earlier)</text>
</g>
<g fill="#39d2c0">
<circle cx="186" cy="112" r="10"/><circle cx="260" cy="112" r="10"/><circle cx="334" cy="112" r="10"/><circle cx="186" cy="152" r="10"/><circle cx="186" cy="192" r="10"/><circle cx="186" cy="232" r="10"/><circle cx="186" cy="272" r="10"/><circle cx="260" cy="272" r="10"/><circle cx="334" cy="272" r="10"/><circle cx="408" cy="272" r="10"/><circle cx="408" cy="360" r="10"/>
</g>
<text x="297" y="319" font-size="20" fill="#a9b4c2" text-anchor="middle" font-family="'IBM Plex Sans',system-ui,sans-serif">no model</text>
</svg>
<figcaption><b>Figure 5.</b> Which model sees which camera, from <code>cams</code> in <code>src/data/registry.json</code>. The five colour cameras are above the thick line. Drawn in the page source from the record.</figcaption>
</figure>
<div class="bs-part bs-teal"><span class="bs-label">Read the figure</span><h3>Three groups of models</h3><ul>
<li><b>π0.5, all five colour cameras</b>: Plain Bagel, Mango Pudding, Mango Lassi, Mango Sorbet, Mango Chutney, Spicy Chicken, Mango Rice, Pretzel One and Pretzel Two.</li>
<li><b>Overhead and wrist only</b>: Isaac 0.5 Expert (Isaac 0.5) and Crispy Falafel (FLUX 3 Action).</li>
<li><b>An earlier layout</b>: Sweet Corn (FLUX 3 Action) saw <code>left</code>, re-aimed high, and <code>wrist</code>.</li>
<li>Rollout recordings store the same cameras the model saw.</li>
</ul></div>
</div>

<div class="bs-part bs-orange" id="camera-position-changes"><span class="bs-label">Camera position changes</span><h3>Since 4 November the across-the-table camera has been off the place where most training demonstrations were recorded</h3><ul>
<li><b>Between the 14 and the 28 October recordings.</b> <code>left_top</code> sits slightly differently in the first 70 of the 220 demonstrations than in the later 150; the operator said it "moved before the 2nd batch".</li>
<li><b>4 November, 18:31–18:33.</b> It was bumped about 12 px down and 6 px left at 640×480, about 6 px at the model's 224×224 input. Every arm test since ran with it away from where 150 of the 220 training demonstrations were recorded. The other three scene cameras stayed within 1 px.</li>
<li>Whether it was put back after 9 November is not stated.</li>
</ul></div>

[Figure 5](#fig-camera-matrix) shows which models a camera change can reach: `left_top` feeds every π0.5 model and none of the models that see only the overhead and wrist views ([which models see which cameras](task-and-rig-record.html#which-models-see-which-cameras), [camera position changes](task-and-rig-record.html#camera-position-changes)). What the change means for the recorded data is in [Demonstrations](demonstrations.html#camera-differences-between-batches); the bump itself is in the [Arm test, 9 Nov](a16000-arm-test-9nov.html).

</section>

<section class="card" id="what-a-command-looks-like">

## A command names the source and the destination by position, never by colour

<p class="bs-lead">So that a command stays unambiguous when two vials share a colour, it names slot and rack; which vial to move is left to the person typing.</p>

<figure id="fig-command">
<div class="bs-flow" role="img" aria-label="The typed sentence: move the vial from position 3 of the right rack to slot 6 of the left rack. It names the source, slot 3 of the right rack, and the destination, slot 6 of the left rack. The data writes the move as R3->L6, the pages as R3 → L6.">
<div class="bs-node bs-teal"><span class="bs-label">Typed by a person</span><b>The command</b><ul><li>"Move the vial from <em>position 3 of the right rack</em> to <em>slot 6 of the left rack</em>."</li><li>one recorded wording of this move</li></ul></div>
<div class="bs-arrow"><span>names</span></div>
<div class="bs-node bs-violet"><span class="bs-label">Source and destination</span><b>The move</b><ul><li>source: slot 3 of the right rack</li><li>destination: slot 6 of the left rack</li><li>a destination can also be the bin</li></ul></div>
<div class="bs-arrow"><span>written</span></div>
<div class="bs-node bs-orange"><span class="bs-label">In the data and on pages</span><b><code>R3->L6</code> · <code>R3 → L6</code></b><ul><li>the data writes <code>&lt;source&gt;-&gt;&lt;destination&gt;</code>, such as <code>L3->bin</code></li><li>the pages draw an arrow</li></ul></div>
</div>
<figcaption><b>Figure 6.</b> One recorded command for the move <code>R3 → L6</code> (<code>wordings.example</code> in <code>src/data/october.json</code>) and the two ways the move is written. A diagram drawn in the page source from the record.</figcaption>
</figure>

<div class="bs-grid g2">
<div class="bs-part bs-violet"><span class="bs-label">At the robot</span><h3>The operator starts a rollout with <code>/t</code></h3><ul>
<li>The Lab notes write a rollout as <code>/t &lt;source&gt; &lt;destination&gt;</code>, for example <code>/t R3 L1</code> or <code>/t L3 bin</code>.</li>
<li>The operator's observation is <code>/note &lt;what happened&gt;</code>, which <code>tools/assess_rollouts.py</code> reads back.</li>
<li>The rollout program itself is not in this repository.</li>
</ul></div>
<div class="bs-part bs-muted" id="the-vials"><span class="bs-label">The vials</span><h3>Translucent plastic, three colours</h3><ul>
<li>The vials are translucent plastic; the RealSense depth stream loses them.</li>
<li>The October recording used red, cyan and dark green vials.</li>
<li>The pages also say "lime" and "green" for the third colour; whether these are the same vials is not stated.</li>
</ul></div>
</div>

[Figure 6](#fig-command) follows one command from the sentence to the move. The demonstrations use many wordings of each move; the pools they were drawn from are in [Demonstrations](demonstrations.html#how-the-commands-are-worded). The record has the exact forms ([what a command looks like](task-and-rig-record.html#what-a-command-looks-like), [the vials](task-and-rig-record.html#the-vials)).

</section>

<section class="card" id="earlier-rigs">

## The rig changed twice, and in August the racks were named from a different viewpoint

<p class="bs-lead">The August work ran on a Jetson Thor rig with three cameras, an early-October layout used two, and the current rig has used five since mid-October.</p>

<div class="scroll" role="region" aria-label="The three rigs compared" tabindex="0" data-reader-horizontal>
<table>
<thead><tr><th></th><th>August 2026</th><th>Early October 2026</th><th>From mid-October 2026</th></tr></thead>
<tbody>
<tr><th>Computer</th><td>Jetson Thor rig</td><td>not stated</td><td>the workstation</td></tr>
<tr><th>Cameras</th><td>side, top and wrist, plus a depth stream the policy did not use</td><td><code>left</code>, re-aimed high, and <code>wrist</code></td><td>five colour cameras, plus <code>rs_depth</code> in one recording</td></tr>
<tr><th>Racks and bin</th><td>two six-slot racks at a diagonal to the arm, the bin on the left</td><td>not stated</td><td>two six-slot racks, the bin between them</td></tr>
<tr><th>Naming</th><td>from the side camera: the left rack is the one by the bin; slots 1 to 6 from left to right</td><td>not stated</td><td>from the follower arm: the left rack is to its left; slot 1 nearest the arm</td></tr>
<tr><th>Vials</th><td>red, cyan and green, three of each</td><td>not stated</td><td>red, cyan and dark green</td></tr>
</tbody>
</table>
</div>

<div class="bs-grid g2">
<div class="bs-part bs-orange"><span class="bs-label">Reading August results</span><h3>The same slot name can mean a different hole</h3><ul>
<li>In August "left rack" meant the rack by the bin, named from the side camera; now it means the rack to the left of the follower arm.</li>
<li>The August evaluation recordings ran at about 3.5 frames a second; 79 human-scored rollouts over 15 commands, 22–24 August 2026.</li>
</ul></div>
<div class="bs-part bs-muted"><span class="bs-label">Not stated</span><h3>What carried over is unknown</h3><ul>
<li>Whether the August rig used the same physical arm, racks or vials as the current one.</li>
<li>Where the early-October cameras stood: that layout is known only from three rollout recordings of 7 October and from Sweet Corn's entry.</li>
</ul></div>
</div>

The table puts the three rigs in order, oldest first. The change that matters most for reading old results is the naming: a slot code from August and the same code today need not name the same hole ([earlier rigs](task-and-rig-record.html#earlier-rigs)).

</section>

<section class="card" id="not-verified">
<span id="where-these-facts-come-from"></span>

## None of this was checked on the rig, and no person has reviewed it yet

<p class="bs-lead">The facts here come from the website's pages, its generated data and the Lab notes; the robot, the recordings and the rollout program are not in this repository.</p>

<div class="bs-board">
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>Review by a person</b><span>The record was written by AI agents from the repository's files and checked only by the documentation build and lint. It waits for a <a href="docs.open.human-review.md.html">review by someone who knows the rig</a>.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>Generated numbers</b><span>Numbers from <code>src/data/</code> are as recorded at commit <code>8065309</code> (2026-11-28) and were not re-derived: the scripts need the <code>~/lerobot</code> checkout.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>The arm</b><span>The name of the sixth joint is not stated.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>The cameras</b><span>The recording resolution of each camera is not stated; 640 × 480 is the size of the website's stills. Whether <code>left_bottom</code> sits near eye level or near table level was not checked.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>After 4 November</b><span>Whether <code>left_top</code> was put back and whether the USB hub was rewired are not stated.</span></div>
<div class="bs-row"><span class="bs-state bs-wait">Open</span><b>The vials</b><span>Whether "dark green", "lime" and the August "green" are the same vials is not stated.</span></div>
</div>

Every point above is listed with its sources in the record's [not verified](task-and-rig-record.html#not-verified) section, and [where these facts come from](task-and-rig-record.html#where-these-facts-come-from) names the files they were read from. Until the review, read this page as a careful summary of the repository's files, not as confirmed knowledge of the rig. The [whole record](task-and-rig-record.html) is the authoritative text.

</section>
