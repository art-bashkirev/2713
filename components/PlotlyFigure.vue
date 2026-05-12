<!-- PlotlyFigure.vue -->
<template>
  <div>
    <div ref="plotlyContainer" class="plotly-figure"></div>
  </div>
</template>
  
<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import Papa from 'papaparse';

let plotlyModulePromise: Promise<typeof import('plotly.js-basic-dist-min')> | null = null;

const loadPlotly = async () => {
  plotlyModulePromise ??= import('plotly.js-basic-dist-min');
  return plotlyModulePromise;
};

const resolveCsvUrl = (csvUrl: string) => {
  if (/^https?:\/\//i.test(csvUrl) || csvUrl.startsWith('data:') || csvUrl.startsWith('/')) {
    return csvUrl;
  }

  if (csvUrl.startsWith('public/')) {
    return `/${csvUrl.slice('public/'.length)}`;
  }

  return `/${csvUrl}`;
};

const props = defineProps({
  csvUrl: {
    type: String,
    required: false,
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
const localCsvText = ref<string | null>(null);

const fetchData = async () => {
  if (localCsvText.value) {
    return localCsvText.value;
  }
  if (props.csvUrl) {
    const response = await fetch(resolveCsvUrl(props.csvUrl));
    const text = await response.text();
    return text;
  }
  throw new Error('No CSV source provided');
};

const parseCSV = (csvText: string) => {
  return new Promise<any[]>((resolve, reject) => {
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

const createPlot = (data: any[]) => {
  if (!plotlyContainer.value) {
    return;
  }

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
    xaxis: { title: "x"},
    yaxis: { title: "y"},
    margin: {t: 20, b: 20, r: 20, l: 20},
  };

  void loadPlotly().then(({ default: Plotly }) => {
    Plotly.newPlot(plotlyContainer.value, plotData, layout, {displaylogo: false, staticPlot: true});
  });
};

const loadAndPlot = async () => {
  try {
    const csvText = await fetchData();
    const data = await parseCSV(csvText);
    createPlot(data);
  } catch (error) {
    console.error('Error fetching or parsing CSV:', error);
  }
};

const onFileChange = (e: Event) => {
  const files = (e.target as HTMLInputElement).files;
  if (files && files.length > 0) {
    const reader = new FileReader();
    reader.onload = (event) => {
      localCsvText.value = event.target?.result as string;
      loadAndPlot();
    };
    reader.readAsText(files[0]);
  }
};

onMounted(loadAndPlot);

// Re-plot if csvUrl changes and no local file is loaded
watch(() => props.csvUrl, () => {
  if (!localCsvText.value) loadAndPlot();
});
</script>
  
<style scoped>
.plotly-figure {
  width: 350px;
  height: 300px;
}
</style>