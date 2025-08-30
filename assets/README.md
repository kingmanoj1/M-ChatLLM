# 📸 Assets Folder

This folder contains images, screenshots, and other media files for the README.

## 🖼️ Required Screenshots

To make your README complete, add these screenshots:

### **1. light-theme.png**
- Take a screenshot of your web interface in light mode
- Show a conversation with the AI
- Recommended size: 1200x800 pixels
- Format: PNG for crisp text

### **2. dark-theme.png**  
- Screenshot of the same interface in dark mode
- Toggle the theme using the 🌙 button
- Same size and format as light theme

### **3. demo.gif**
- Record a screen recording showing:
  - Typing a message
  - Real-time streaming response
  - Using the stop button
- Convert to GIF using tools like:
  - **LICEcap** (Windows/Mac)
  - **peek** (Linux)
  - **ffmpeg** command line
- Keep under 5MB for GitHub

## 📝 How to Add Screenshots

### **Method 1: Direct Upload**
1. Take screenshots of your running application
2. Save them in this `assets/` folder with the exact names above
3. Commit and push to GitHub

### **Method 2: GitHub Issues Method**
1. Go to your GitHub repo
2. Create a new issue
3. Drag & drop your image into the issue description
4. GitHub generates a URL like: `https://github.com/user/repo/assets/123456/uuid.png`
5. Copy this URL and replace the `./assets/filename.png` paths in README.md
6. Close the issue

### **Method 3: External Hosting**
- Upload to Imgur, Cloudinary, or other image hosts
- Replace the local paths with external URLs

## 🎥 Recording Demo GIF

### Using ffmpeg (Linux/Mac/Windows):
```bash
# Record screen area
ffmpeg -f x11grab -s 1200x800 -i :0.0+100,100 -t 30 -r 15 demo.mp4

# Convert to optimized GIF
ffmpeg -i demo.mp4 -vf "fps=10,scale=800:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i demo.mp4 -i palette.png -filter_complex "fps=10,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" demo.gif
```

### Using peek (Linux):
```bash
sudo apt install peek  # Ubuntu/Debian
# Run peek, select area, record, save as GIF
```

## 📐 Image Specifications

| Image | Dimensions | Format | Max Size | Purpose |
|-------|------------|--------|----------|---------|
| light-theme.png | 1200x800 | PNG | 2MB | Light mode UI |
| dark-theme.png | 1200x800 | PNG | 2MB | Dark mode UI |
| demo.gif | 800x600 | GIF | 5MB | Live demonstration |

## ✅ Checklist

- [ ] `light-theme.png` - Light mode screenshot
- [ ] `dark-theme.png` - Dark mode screenshot  
- [ ] `demo.gif` - Streaming demo recording
- [ ] Images are properly sized and optimized
- [ ] All images display correctly in README
- [ ] File sizes are reasonable for GitHub

Once you add these files, your README will have professional-looking screenshots that showcase your project's features! 
