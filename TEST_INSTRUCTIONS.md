# 🧪 Test Instructions

## Quick Test

### Option 1: Direct Open (Simple)
```bash
# Just open in browser
open index.html
# or
firefox index.html
# or
google-chrome index.html
```

### Option 2: Web Server (Recommended)
```bash
# Start web server
cd /home/dev/web/instances/clients/services/mantra.studio/snapcode.me
python3 -m http.server 8000

# Open browser
# Navigate to: http://localhost:8000
```

---

## Test Checklist

### ✅ Test 1: Tab Switching
- [ ] Open index.html
- [ ] See "Markdown" and "File Explorer" tabs
- [ ] Click "File Explorer" tab
- [ ] Tab switches successfully

### ✅ Test 2: Load Docs Folder
- [ ] Click "Docs" button (purple)
- [ ] Wait 1-2 seconds
- [ ] See 8 files in list:
  - INDEX.md
  - FOLDER_LOADING.md
  - FILE_EXPLORER_FEATURE.md
  - STRUCTURE.md
  - QUICKSTART.md
  - CHANGES_SUMMARY.txt
  - apply_patch.py
  - file-explorer-patch.html

### ✅ Test 3: Load Content Folder
- [ ] Click "Content" button (green)
- [ ] See 3 files added:
  - default.md
  - sample.md
  - token cost.md

### ✅ Test 4: Select File
- [ ] Click any file in list
- [ ] File gets purple highlight
- [ ] Auto-switch to "Markdown" tab
- [ ] Content appears in editor
- [ ] Filename updates in preview window

### ✅ Test 5: Delete File
- [ ] Hover over a file
- [ ] Red [X] button appears
- [ ] Click [X]
- [ ] File removed from list

### ✅ Test 6: Manual Upload
- [ ] Click "+ Add File" button
- [ ] Select a .md or .txt file
- [ ] File added to list
- [ ] Auto-selected and loaded

### ✅ Test 7: No Duplicates
- [ ] Click "Docs" button
- [ ] Click "Docs" button again
- [ ] Verify no duplicate files

### ✅ Test 8: Preview & Export
- [ ] Select a file
- [ ] See preview in right panel
- [ ] Adjust settings (theme, font, etc)
- [ ] Click "Export PNG"
- [ ] Image downloads successfully

---

## Expected Results

### File Explorer UI
```
┌─────────────────────────────────────────────────────┐
│ File Explorer                                       │
│                                                     │
│  [Content]  [Docs]  [+ Add File]                   │
│     🟢        🟣         🔵                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  📄 INDEX.md                              [X]       │
│     1.1 KB                                          │
│  ─────────────────────────────────────────────────  │
│  📄 FOLDER_LOADING.md                     [X]       │
│     2.7 KB                                          │
│  ─────────────────────────────────────────────────  │
│  📄 FILE_EXPLORER_FEATURE.md              [X]       │
│     3.8 KB                                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Troubleshooting

### Files not loading?
```bash
# Make sure you're using web server
python3 -m http.server 8000

# Check browser console for errors
# Press F12 → Console tab
```

### CORS errors?
```
Solution: Use web server (python3 -m http.server)
Don't open file:// directly for folder loading
```

### Buttons not working?
```
1. Check browser console (F12)
2. Refresh page (Ctrl+R / Cmd+R)
3. Clear cache (Ctrl+Shift+R / Cmd+Shift+R)
```

---

## Success Criteria

✅ All 8 tests pass  
✅ No console errors  
✅ Files load correctly  
✅ Preview works  
✅ Export works  

---

## Performance Check

- [ ] Folder loads in < 2 seconds
- [ ] File selection is instant
- [ ] No UI lag
- [ ] Smooth tab switching

---

**Ready to test!** 🚀
