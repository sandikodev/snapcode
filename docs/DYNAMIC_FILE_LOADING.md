# 🔄 Dynamic File Loading

## ❓ Pertanyaan: Apakah Harus Hardcoded?

**Jawaban:** Tidak! Sekarang sudah support **dynamic loading** dengan fallback ke hardcoded.

---

## 🎯 Dua Mode

### Mode 1: Dynamic (dengan server.py) ⭐ Recommended
```bash
# Start server dengan API
python3 server.py

# API endpoints:
# http://localhost:8000/api/files/content
# http://localhost:8000/api/files/docs
```

**Pros:**
- ✅ Auto-detect semua files di folder
- ✅ Tidak perlu update code saat tambah file
- ✅ Real-time file list

**Cons:**
- ⚠️ Perlu Python server running

### Mode 2: Static (tanpa server) 
```bash
# Buka langsung
open index.html
```

**Pros:**
- ✅ No server needed
- ✅ Works offline

**Cons:**
- ⚠️ File list hardcoded
- ⚠️ Manual update saat ada file baru

---

## 🔧 How It Works

### Smart Fallback System
```javascript
async loadFolder(folder) {
  try {
    // 1. Try dynamic API first
    const api = await fetch(`/api/files/${folder}`);
    if (api.ok) {
      // Load files dynamically ✅
    } else {
      // 2. Fallback to hardcoded list
      const hardcoded = { ... };
    }
  } catch {
    // Use hardcoded
  }
}
```

### API Response Format
```json
[
  {
    "name": "INDEX.md",
    "size": 1234
  },
  {
    "name": "QUICKSTART.md",
    "size": 5678
  }
]
```

---

## 🚀 Usage

### Option A: With Dynamic Loading
```bash
# Start server
python3 server.py

# Open browser
http://localhost:8000

# Click "Docs" → Auto-loads ALL files in docs/
# Add new file to docs/ → Automatically detected!
```

### Option B: Static Mode
```bash
# Just open
open index.html

# Click "Docs" → Loads hardcoded list
# Add new file → Need to update code
```

---

## 📝 Server API

### Endpoint: `/api/files/{folder}`

**Request:**
```
GET /api/files/docs
```

**Response:**
```json
[
  {"name": "INDEX.md", "size": 1100},
  {"name": "QUICKSTART.md", "size": 4500},
  {"name": "STRUCTURE.md", "size": 11000}
]
```

**Features:**
- ✅ CORS enabled
- ✅ Auto-sorted by name
- ✅ Real-time directory scan
- ✅ Error handling

---

## 🎨 Benefits

### Dynamic Mode:
1. **Auto-Discovery**: Detects new files automatically
2. **No Maintenance**: No code updates needed
3. **Scalable**: Works with any number of files
4. **Real-time**: Always up-to-date

### Static Mode:
1. **Simple**: No server setup
2. **Portable**: Single HTML file
3. **Offline**: Works without network
4. **Fast**: No API calls

---

## 🔒 Security

### Browser Limitations:
- ❌ Cannot read filesystem directly
- ❌ Cannot list directory without server
- ✅ Can only read files user selects
- ✅ Can fetch files via HTTP

### Server Security:
- ✅ Only serves files in project directory
- ✅ CORS enabled for localhost
- ✅ No write operations
- ✅ Path validation

---

## 📊 Comparison

| Feature | Dynamic | Static |
|---------|---------|--------|
| Auto-detect files | ✅ | ❌ |
| No server needed | ❌ | ✅ |
| Real-time updates | ✅ | ❌ |
| Offline support | ❌ | ✅ |
| Maintenance | Low | High |
| Setup complexity | Medium | Low |

---

## 🧪 Testing

### Test Dynamic Mode:
```bash
# 1. Start server
python3 server.py

# 2. Add new file
echo "# Test" > docs/TEST.md

# 3. Click "Docs" button
# → TEST.md automatically appears!
```

### Test Static Mode:
```bash
# 1. Open directly
open index.html

# 2. Click "Docs" button
# → Only hardcoded files appear
```

---

## 💡 Recommendation

**For Development:** Use `python3 server.py` (dynamic)  
**For Production:** Deploy with proper web server  
**For Demo:** Use static mode (no setup)

---

## 🎯 Summary

**Q:** Apakah harus hardcoded?  
**A:** Tidak! Sekarang support dynamic dengan smart fallback.

**Q:** Bagaimana cara dynamic?  
**A:** Gunakan `python3 server.py`

**Q:** Apakah bisa tanpa server?  
**A:** Ya, fallback ke hardcoded list.

---

**Status:** ✅ Both modes supported!  
**Recommended:** Use server.py for best experience 🚀
