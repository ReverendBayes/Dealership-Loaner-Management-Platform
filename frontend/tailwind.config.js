// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}', './public/index.html'],
  theme: {
    extend: {
      colors: {
        primary: '#0033a0',
        background: '#f9fafb',
        surface: '#ffffff',
        textPrimary: '#111827',
        textSecondary: '#6b7280',
      },
      fontFamily: {
        sans: ['Inter', 'Helvetica Neue', 'Segoe UI', 'sans-serif'],
      },
      borderRadius: {
        xl: '1rem',
      },
    },
  },
  plugins: [],
};
