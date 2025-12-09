# 📁 Folder Loading Feature

## ✅ New Feature Added

File Explorer sekarang bisa load files dari folder `content/` dan `docs/` dengan satu klik!

---

## 🎯 How to Use

### 1. Load Content Folder
```
1. Klik tab "File Explorer"
2. Klik tombol "Content" (hijau)
3. Files dari folder content/ akan ter-load
```

### 2. Load Docs Folder
```
1. Klik tab "File Explorer"
2. Klik tombol "Docs" (purple)
3. Files dari folder docs/ akan ter-load
```

### 3. Manual Upload
```
1. Klik tombol "+ Add File" (biru)
2. Pilih file dari komputer
3. File akan ditambahkan ke list
```

---

## 📂 Folder Structure

```
snapcode.me/
├── content/               # Sample content
│   ├── default.md
│   └── sample.md
│
├── docs/                  # Documentation
│   ├── INDEX.md
│   ├── FILE_EXPLORER_FEATURE.md
│   ├── STRUCTURE.md
│   ├── QUICKSTART.md
│   └── CHANGES_SUMMARY.txt
│
└── index.html            # Main app
```

---

## 🎨 UI Buttons

| Button | Color | Function |
|--------|-------|----------|
| **Content** | 🟢 Green | Load content folder |
| **Docs** | 🟣 Purple | Load docs folder |
| **+ Add File** | 🔵 Blue | Upload manual file |

---

## 🔧 Technical Details

### loadFolder Method
```javascript
async loadFolder(folder) {
  const folderFiles = {
    'content': ['default.md', 'sample.md'],
    'docs': ['INDEX.md', 'FILE_EXPLORER_FEATURE.md', ...]
  };
  
  // Fetch each file
  for (const filename of fileList) {
    const response = await fetch(`${folder}/${filename}`);
    if (response.ok) {
      const content = await response.text();
      this.files.push({
        name: filename,
        content: content,
        size: content.length
      });
    }
  }
}
```

---

## ✨ Features

- ✅ Load multiple files dengan satu klik
- ✅ Duplicate detection (tidak load file yang sama 2x)
- ✅ Error handling (skip file yang tidak ada)
- ✅ Visual feedback dengan warna button berbeda
- ✅ Async loading (tidak block UI)

---

## 📝 Example Workflow

```
Step 1: Open File Explorer
├── Klik tab "File Explorer"

Step 2: Load Docs
├── Klik button "Docs"
├── Wait for loading
└── 5 files ter-load

Step 3: Browse Files
├── Klik INDEX.md
├── Read documentation
├── Klik QUICKSTART.md
└── Learn how to use

Step 4: Export
├── Adjust settings
├── Click "Export PNG"
└── Download beautiful image
```

---

## 🚀 Benefits

1. **Quick Access**: Load semua docs dengan 1 klik
2. **No Manual Upload**: Tidak perlu upload satu-satu
3. **Organized**: Files terorganisir dalam folder
4. **Fast**: Async loading, tidak block UI
5. **Smart**: Skip duplicate files

---

**Status**: ✅ Ready to use!
