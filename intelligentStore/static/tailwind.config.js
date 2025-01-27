const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  darkMode: 'Media', // Enable class-based dark mode
  content: [
    './src/**/*.{html,js}',
    './node_modules/flowbite/**/*.js', // Include Flowbite
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['InterVariable', ...defaultTheme.fontFamily.sans], // Corrected font family
      },
    },
  },
  plugins: [
    require('flowbite/plugin'), // Enable Flowbite plugin
  ],
};