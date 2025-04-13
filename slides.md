---
author: Artem Bashkirev
keywords: 27, ЕГЭ Информатика
aspectRatio: 4/3
addons:
  - slidev-addon-python-runner
  - slidev-addon-sync
python:
  loadPackagesFromImports: true
fonts:
  sans: Ubuntu Sans Mono
  serif: Monaspace Xenon
  mono: Monaspace Krypton
drawings:
  syncAll: false

mdc: true
layout: full
---

<!-- THIS IS THE COVER -->

<style>
.huge-number {
  font: 40rem "Monaspace Neon", sans-serif;
  font-weight: 600;
  margin: 0;
  margin-top: 3rem;
  line-height: 1;
  background: linear-gradient(45deg, #ff0861, #ff2a63, #f43f47, #ff6a00, #ffd300);
  background-size: 300% 300%; /* Adjusted background size for better visibility */
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: gradient 15s ease infinite, pulse 5s ease infinite;
  position: relative; /* Changed to relative */
  text-shadow: 0 0 40px rgba(255, 8, 97, 0.7);
  filter: drop-shadow(0 0 20px rgba(255, 72, 0, 0.5));
  display: flex; /* Added for centering */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  height: 100%; /* Full height of the container */
  z-index: 1; /* Ensure number is above particles */
}

@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.void-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(ellipse at center, #000000 0%, #0a0a0a 100%);
  z-index: -1; /* Ensure background is behind other elements */
}

.glow-particles {
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0; /* Ensure particles are behind the number */
}

.glow-particles div {
  position: absolute;
  border-radius: 50%;
  mix-blend-mode: screen;
  animation: particle-anim 20s linear infinite;
}

@keyframes particle-anim {
  0% { transform: scale(0) translateY(0); opacity: 0; }
  50% { transform: scale(1.5) translateY(-100px); opacity: 0.5; }
  100% { transform: scale(0) translateY(-200px); opacity: 0; }
}
</style>

<div class="void-background">
  <div class="glow-particles">
  <!-- <div class="w-96 h-96 bg-gradient-to-r from-cyan-500/30 to-blue-600/30 top-1/4 left-1/4 blur-3xl"></div>
  <div class="w-64 h-64 bg-gradient-to-r from-red-500/40 to-purple-600/40 top-1/3 right-1/4 blur-2xl"></div> -->
  <div class="w-80 h-80 bg-gradient-to-r from-green-500/30 to-yellow-600/30 top-1/2 left-1/4 blur-2xl"></div>
  <div class="w-72 h-72 bg-gradient-to-r from-blue-500/40 to-pink-600/40 top-1/4 right-1/4 blur-3xl"></div>
  <div class="w-56 h-56 bg-gradient-to-r from-purple-500/30 to-orange-600/30 top-3/4 left-1/2 blur-2xl"></div>
  <div class="w-48 h-48 bg-gradient-to-r from-pink-500/40 to-cyan-600 /40 top-1/2 right-1/3 blur-3xl"></div>
  <div class="w-40 h-40 bg-gradient-to-r from-yellow-500/30 to-red-600/30 top-1/3 left-1/3 blur-2xl"></div>
  <div class="w-60 h-60 bg-gradient-to-r from-teal-500/40 to-indigo-600/40 top-1/4 left-3/4 blur-3xl"></div>
  <div class="w-72 h-72 bg-gradient-to-r from-orange-500/30 to-red-600/30 top-0 left-0 blur-3xl"></div>
</div>

  <h1 class="huge-number">27</h1>
</div>


<!--
THIS IS THE COVER
-->

