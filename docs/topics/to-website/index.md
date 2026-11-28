+++
title = "Back to the website"
slug = "to-website"
description = "Leaves the documentation for the project's public website."
reader = false
raw = true
page_only = "a menu entry that leads to the public website; the documentation menu takes only its own pages"
components = ["nav"]
page_css = ["build-sheet.css", "home.css"]
toc = []
+++

<div class="home">
<header class="home-hero">
<div>
<h1>The vial-sort website</h1>
<p>The public website shows the data, the models, the training and the results. This documentation is published beside it.</p>
<div class="home-cta">
<a id="to-website" href="https://cognitive-software-labs.github.io/vial-sort/">Go to the website</a>
<a class="alt" href="index.html">Stay in the documentation</a>
</div>
</div>
</header>
</div>
<script>location.replace(document.getElementById('to-website').href);</script>
