/* ./setup/shiki.ts */
import { defineShikiSetup } from '@slidev/types'
// import customLanguage from './customLanguage.tmLanguage.json'
// import customTheme from './customTheme.tmTheme.json'

export default defineShikiSetup(() => {
  return {
    themes: {
      dark: 'plastic',
      light: 'catppuccin-latte',
    },
    langs: [
      'python',
      'markdown',
      'javascript',
      'typescript',
      'cpp'
      // ...
    ],
    transformers: [
      // ...
    ],
  }
})