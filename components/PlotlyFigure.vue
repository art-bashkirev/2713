<!-- PlotlyFigure.vue -->
<template>
    <div ref="plotlyContainer" class="plotly-figure"></div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import Plotly from 'plotly.js-dist-min';
  import Papa from 'papaparse';
  
  const props = defineProps({
    csvUrl: {
      type: String,
      required: true,
    },
    xColumn: {
      type: String,
      required: true,
    },
    yColumn: {
      type: String,
      required: true,
    },
  });
  
  const plotlyContainer = ref(null);
  
  const fetchData = async () => {
    const response = await fetch(props.csvUrl);
    const text = await response.text();
    return text;
  };
  
  const parseCSV = (csvText) => {
    return new Promise((resolve, reject) => {
      Papa.parse(csvText, {
        header: true,
        complete: (results) => {
          resolve(results.data);
        },
        error: (error) => {
          reject(error);
        },
      });
    });
  };
  
  const createPlot = (data) => {
    const xData = data.map(row => parseFloat(row[props.xColumn]));
    const yData = data.map(row => parseFloat(row[props.yColumn]));
  
    const plotData = [
      {
        x: xData,
        y: yData,
        mode: 'markers',
        type: 'scatter',
      },
    ];
  
    const layout = {
      title: 'CSV Data Plot',
      xaxis: { title: props.xColumn },
      yaxis: { title: props.yColumn },
    };
  
    Plotly.newPlot(plotlyContainer.value, plotData, layout, {displaylogo: false, staticPlot: true});
  };
  
  onMounted(async () => {
    try {
      const csvText = await fetchData();
      const data = await parseCSV(csvText);
      createPlot(data);
    } catch (error) {
      console.error('Error fetching or parsing CSV:', error);
    }
  });
  </script>
  
  <style scoped>
  .plotly-figure {
    width: 450px;
    height: 500px;
  }
  </style>