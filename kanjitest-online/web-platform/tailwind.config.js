/** @type {import('tailwindcss').Config} */
module.exports = {
  // 1. CONTENT: Tells Tailwind exactly which files to scan for classes.
  // Without these paths, your site will remain "blank" and unstyled.
  content: [
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  
  theme: {
    extend: {
      // 2. TYPOGRAPHY: Adding support for professional Japanese font rendering.
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        japanese: [
          "Hiragino Sans", 
          "Hiragino Kaku Gothic ProN", 
          "Meiryo", 
          "sans-serif"
        ],
      },
      // 3. ANIMATIONS: Adding micro-interactions for a premium UI/UX feel.
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
      // 4. DEPTH: Custom shadows to give the "Bento Box" its modern look.
      boxShadow: {
        'bento': '0 20px 40px -15px rgba(0, 0, 0, 0.05)',
        'premium': '0 10px 30px -10px rgba(37, 99, 235, 0.15)',
      }
    },
  },
  plugins: [],
}
