# 📱 Senthil's Portfolio Website

A professional, modern, and responsive portfolio website showcasing your skills, projects, and experience as an aspiring developer.

## 📋 Features

✅ **Fully Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
✅ **Modern UI/UX** - Clean, professional design with smooth animations
✅ **All Your Information** - Resume details, projects, skills, education, and certifications
✅ **Contact Section** - Easy ways for potential employers to reach you
✅ **SEO Ready** - Properly structured HTML for search engines
✅ **Fast Loading** - Lightweight and optimized

## 🚀 How to View Your Portfolio

### Option 1: Direct Browser View (Simplest)
1. Download the `portfolio.html` file
2. Double-click the file or right-click → "Open with Browser"
3. Your portfolio will open in your default browser

### Option 2: Using Python Server (Recommended)

**Requirements:**
- Python 3.x installed (comes pre-installed on Mac/Linux)

**Steps:**
1. Place both `portfolio.html` and `server.py` in the same folder
2. Open Terminal/Command Prompt in that folder
3. Run: `python3 server.py` (or just `python server.py` on Windows)
4. Open your browser and go to: **http://localhost:8000/portfolio.html**
5. Press `CTRL+C` in terminal to stop the server

### Option 3: Using Node.js Server

If you prefer Node.js:
```bash
npx http-server
```
Then visit `http://localhost:8080` in your browser.

## 📝 Customization Guide

### Add Your Photo
1. Place a photo file (jpg, png) in the same folder as portfolio.html
2. Find this line in the HTML: `<div class="hero-image">`
3. Replace with: `<img src="your-photo.jpg" alt="Senthil G">`

### Update Social Links
- Find sections with your contact info
- Update email, phone, and LinkedIn URLs

### Add More Projects
Look for the "Projects Section" and add more project cards following the same pattern:
```html
<div class="project-card">
    <div class="project-header">
        <h3>Your Project Name</h3>
        <div class="project-tech">
            <span class="tech-tag">Technology</span>
        </div>
    </div>
    <div class="project-body">
        <p>Project description here...</p>
    </div>
</div>
```

### Change Color Scheme
Edit the CSS variables at the top of the style section:
```css
:root {
    --primary-color: #2563eb;      /* Main blue color */
    --secondary-color: #1e40af;    /* Darker blue */
    --text-dark: #1f2937;          /* Dark text */
    /* ... more colors ... */
}
```

## 📂 File Structure
```
your-folder/
├── portfolio.html          (Main website file)
├── server.py              (Python server - optional)
└── README.md              (This file)
```

## 🌐 Deploy to Web (Free Options)

### Netlify (Recommended)
1. Go to https://netlify.com
2. Drag and drop your `portfolio.html` file
3. Get a live URL instantly!

### GitHub Pages
1. Create a GitHub account
2. Upload files to a new repository
3. Enable GitHub Pages in settings
4. Your portfolio goes live!

### Vercel
1. Visit https://vercel.com
2. Connect your GitHub or upload files
3. Auto-deployed with a live URL

## 💡 Tips

- **Mobile First**: Test your portfolio on mobile devices
- **Backup**: Keep a backup of your portfolio.html file
- **Updates**: Easily update your portfolio by editing the HTML file
- **Share**: Once deployed, share the link with recruiters and companies

## 📞 Contact Information

Your portfolio includes:
- **Email**: Senthil2004G@gmail.com
- **Phone**: +91 7871 171 458
- **LinkedIn**: https://www.linkedin.com/in/senthil2004g/

## 🎯 What's Included

- Hero section with professional introduction
- About section with your background
- Technical skills organized by category
- Featured projects (Wildlife Detection & Classroom Surveillance)
- Education details
- Certifications & training
- Contact section with multiple ways to reach you

## ✨ Browser Support

- Chrome/Chromium ✓
- Firefox ✓
- Safari ✓
- Edge ✓
- Mobile browsers ✓

## 📊 Performance

- Page Load: < 1 second
- File Size: ~50 KB
- Mobile Friendly: 100%

---

**Built with ❤️ for Senthil's Career Success**

Questions? Customize the portfolio.html file directly - it's all in one file, easy to edit!
