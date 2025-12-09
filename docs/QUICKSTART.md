# 🚀 Quick Start - File Explorer Feature

## ✅ Apa yang Sudah Ditambahkan?

Fitur **File Explorer** yang memungkinkan Anda mengelola multiple files dan switch antara Markdown Editor dan File Explorer.

---

## 📖 Cara Menggunakan

### 1. Buka File
```bash
# Buka di browser
open index.html

# Atau jika ada web server
python3 -m http.server 8000
# Lalu buka http://localhost:8000
```

### 2. Gunakan File Explorer

#### Upload File
1. Klik tab **"File Explorer"**
2. Klik tombol **"+ Add File"**
3. Pilih file (.md, .txt, .js, .html, .css, .json)
4. File akan muncul di list

#### Select File
1. Klik file di list
2. Otomatis switch ke tab **"Markdown"**
3. Content file ter-load di editor
4. Filename ter-update di window title

#### Delete File
1. Hover mouse ke file di list
2. Tombol **[X]** akan muncul
3. Klik **[X]** untuk delete

---

## 🎨 Features

### Tab Switcher
- **Markdown**: Editor markdown (existing)
- **File Explorer**: File manager (new)

### File Explorer
- ✅ Upload multiple files
- ✅ File list dengan nama & ukuran
- ✅ Visual feedback (purple highlight untuk selected file)
- ✅ Delete file dengan hover effect
- ✅ Empty state yang informatif

### Markdown Editor
- ✅ Semua fitur existing tetap ada
- ✅ Load content dari file explorer
- ✅ Filename auto-update

---

## 🔧 Technical Details

### State Management (Alpine.js)
```javascript
editorMode: 'markdown'      // Current active tab
files: []                   // Array of uploaded files
selectedFileIndex: null     // Currently selected file
```

### Methods
```javascript
addFile(event)              // Handle file upload
selectFile(index)           // Load file to editor
removeFile(index)           // Delete file from list
formatFileSize(bytes)       // Format file size display
```

---

## 🎯 Use Cases

### 1. Multiple Markdown Files
```
1. Upload README.md
2. Upload CHANGELOG.md
3. Upload CONTRIBUTING.md
4. Switch between files dengan klik
5. Export each as PNG
```

### 2. Code Snippets
```
1. Upload example.js
2. Upload styles.css
3. Upload index.html
4. Preview dengan syntax highlighting
5. Export as beautiful images
```

### 3. Documentation
```
1. Upload multiple .md files
2. Edit dan preview
3. Export untuk presentation
4. Share as images
```

---

## 🐛 Troubleshooting

### File tidak ter-upload?
- Check file extension (.md, .txt, .js, .html, .css, .json)
- Check file size (browser limit ~50MB)
- Check console untuk error

### File tidak ter-load?
- Pastikan file adalah text file
- Binary files tidak supported
- Check encoding (UTF-8 recommended)

### Tab tidak switch?
- Check browser console
- Refresh page
- Clear browser cache

---

## 🚀 Next Steps

### Untuk Developer:
1. Test semua fitur
2. Customize styling jika perlu
3. Add more file types di accept attribute
4. Implement Code Editor tab (future)

### Untuk User:
1. Upload files
2. Create beautiful screenshots
3. Export as PNG
4. Share on social media

---

## 📝 Example Workflow

```
Step 1: Upload Files
├── Click "File Explorer" tab
├── Click "+ Add File"
└── Select multiple files

Step 2: Edit & Preview
├── Click file in list
├── Edit in Markdown tab
├── See preview in real-time
└── Adjust settings (theme, font, etc)

Step 3: Export
├── Click "Export PNG"
├── High-quality 2x resolution
└── Download image

Step 4: Manage Files
├── Upload more files
├── Delete unused files
└── Switch between files easily
```

---

## 💡 Tips

1. **Organize Files**: Upload related files together
2. **Use Descriptive Names**: Easier to find in list
3. **Delete Unused**: Keep list clean
4. **Test Different Themes**: Each file can have different theme
5. **Adjust Settings**: Font size, padding, watermark per file

---

## 🎓 Advanced Usage

### Batch Processing
```
1. Upload 10 markdown files
2. For each file:
   - Select file
   - Adjust theme
   - Export PNG
3. Result: 10 beautiful images
```

### Template System
```
1. Create template.md with common structure
2. Upload template
3. Duplicate content
4. Modify for each use case
5. Export variations
```

---

## 📞 Support

- **Bug Reports**: Check console, report issue
- **Feature Requests**: Document in GitHub issues
- **Questions**: Check README.md

---

## ✨ Summary

**Before**: Single markdown editor  
**After**: Multi-file manager dengan tab switcher  
**Future**: Code editor dengan syntax highlighting

**Status**: ✅ Ready to use!

---

**Happy Coding! 🚀**  
*ngode-ngide kode ngadi-ngadi*
