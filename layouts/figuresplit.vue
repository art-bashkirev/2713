<!--
  Usage:
```md
---
layout: two-cols-header
---
This spans both
::left::
# Left
This shows on the left
::right::
# Right
This shows on the right
::bottom::
This shows at the bottom, aligned to the end (bottom) of the grid
```
-->

<script setup lang="ts">
import PlotlyFigure from '../components/PlotlyFigure.vue'; // Import the Plotly component

const props = defineProps({
  class: {
    type: String,
  },
  layoutClass: {
    type: String,
  },
});

// Example data and layout for the Plotly figure
const plotData = [
  {
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    mode: 'markers',
    type: 'scatter',
  },
];

const plotLayout = {
  title: 'Figure',
};
</script>

<template>
    <div class="slidev-layout two-cols-header w-full h-full" :class="layoutClass">
      <div class="col-header">
        <slot />
      </div>
      <div class="col-left" :class="props.class">
        <slot name="left" />
      </div>
      <div class="col-right" :class="props.class">
        <PlotlyFigure 
          csvUrl="https://raw.githubusercontent.com/art-bashkirev/2713-pub/main/data-csv/7581-A.csv" 
          xColumn="ColumnX" 
          yColumn="ColumnY" 
        />
      </div>
      <div class="col-bottom" :class="props.class">
        <slot name="bottom" />
      </div>
    </div>
  </template>

<style scoped>
.two-cols-header {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Left column fixed width, right column takes remaining space */
  grid-template-rows: auto 1fr auto; /* Adjust rows to fit content */
}

.col-header {
  grid-area: 1 / 1 / 2 / 3; /* Header spans both columns */
}

.col-left {
  grid-area: 2 / 1 / 3 / 2; /* Left column */
}

.col-right {
  grid-area: 2 / 2 / 3 / 3; /* Right column */
}

.col-bottom {
  grid-area: 3 / 1 / 4 / 3; /* Bottom spans both columns */
}
</style>