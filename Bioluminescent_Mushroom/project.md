---
layout: post
title: SprioScultpure
images:
  - image_path: 1-Concept.png
    title: Concept
    link: 1-Concept.png
  - image_path: 2-Design.png
    title: Design
    link: 2-Design.png
  - image_path: 3-Simulation.gif
    title: Simulation
    link: 3-Simulation.gif
  - image_path: 4-Result.png
    title: Result
    link: 4-Result.png
---

### Students:
Darius Dolha, Sangyoon Park   

### Images:

<link rel="stylesheet" href="/icd/Teaching-CDDF/gallery.css?v=1.0">

<div class="gallery">
  {% for image in page.images %}
    <img src="{{ image.image_path }}" class="gallery-img" width="360" alt="{{ image.title }}" onclick="openFullscreen(this)">
  {% endfor %}
</div>

<div class="fullscreen-overlay" onclick="closeFullscreen()">
  <img class="fullscreen-image">
</div>

<script src="/icd/Teaching-CDDF/gallery.js"></script>

### Abstract:

3D Spirograph.