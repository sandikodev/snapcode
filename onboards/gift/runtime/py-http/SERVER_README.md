# 🚀 Server with Dynamic File Loading

## ✅ Jawaban: TIDAK Harus Hardcoded!

Sekarang SnapCode support **dynamic file loading** dengan Python server.

---

## 🎯 Quick Start

### Start Server:
```bash
python3 server.py
```

### Open Browser:
```
http://localhost:8000
```

### Test API:
```bash
# List files in content/
curl http://localhost:8000/api/files/content

# List files in docs/
curl http://localhost:8000/api/files/docs
```

---

## 🔄 How It Works

### 1. Start Server
```bash
$ python3 server.py
🚀 Server running at http://localhost:8000
📁 API: http://localhost:8000/api/files/content
📁 API: http://localhost:8000/api/files/docs

Press Ctrl+C to stop
```

### 2. Click "Docs" Button
```
Browser → GET /api/files/docs
Server → Scan docs/ folder
Server → Return JSON list of files
Browser → Load each file automatically
```

### 3. Add New File
```bash
# Add new file
echo "# New Doc" > docs/NEW_FILE.md

# Click "Docs" button again
# → NEW_FILE.md automatically appears!
```

---

## 📁 API Endpoints

### GET /api/files/{folder}

**Example:**
```bash
curl http://localhost:8000/api/files/docs
```

**Response:**
```json
[
  {
    "name": "INDEX.md",
    "size": 1100
  },
  {
    "name": "QUICKSTART.md",
    "size": 4500
  }
]
```

---

## ✨ Benefits

### Dynamic Loading:
- ✅ **Auto-detect** new files
- ✅ **No code updates** needed
- ✅ **Real-time** file list
- ✅ **Scalable** to any number of files

### Smart Fallback:
- ✅ Works **with** server (dynamic)
- ✅ Works **without** server (hardcoded)
- ✅ Automatic detection
- ✅ No configuration needed

---

## 🎨 Usage Examples

### Example 1: Add Documentation
```bash
# 1. Create new doc
echo "# API Guide" > docs/API_GUIDE.md

# 2. Refresh browser
# 3. Click "Docs" button
# → API_GUIDE.md appears automatically!
```

### Example 2: Add Content
```bash
# 1. Add sample
echo "# Example" > content/example.md

# 2. Click "Content" button
# → example.md loaded!
```

### Example 3: Organize Files
```bash
# Move files around
mv docs/old.md docs/archive/

# Click "Docs" button
# → Only current files shown
```

---

## 🔧 Technical Details

### Server Features:
- **CORS enabled** for localhost
- **JSON API** for file listing
- **Static file serving** for HTML/CSS/JS
- **Error handling** for missing folders
- **Sorted output** by filename

### Code Structure:
```python
class DirectoryListingHandler:
    def do_GET(self):
        if path.startswith('/api/files/'):
            # Return JSON file list
        else:
            # Serve static files
```

---

## 🚫 Limitations

### Browser Security:
- Cannot read filesystem directly
- Cannot list directories without server
- This is by design (security)

### Solution:
- Use Python server for dynamic loading
- Fallback to hardcoded for static mode

---

## 📊 Comparison

| Mode | Setup | Auto-detect | Offline |
|------|-------|-------------|---------|
| **Dynamic** | `python3 server.py` | ✅ Yes | ❌ No |
| **Static** | `open index.html` | ❌ No | ✅ Yes |

---

## 💡 Recommendations

**Development:** Use server.py (dynamic)  
**Production:** Deploy with web server  
**Demo/Offline:** Use static mode

---

## 🧪 Testing

### Test 1: Dynamic Loading
```bash
# Start server
python3 server.py

# Add file
echo "# Test" > docs/TEST.md

# Reload browser → Click "Docs"
# ✅ TEST.md appears!
```

### Test 2: Fallback
```bash
# Open without server
open index.html

# Click "Docs"
# ✅ Hardcoded files appear
```

---

## 🎯 Summary

**Q:** Harus hardcoded?  
**A:** ❌ TIDAK! Sekarang support dynamic.

**Q:** Bagaimana cara dynamic?  
**A:** ✅ `python3 server.py`

**Q:** Bisa tanpa server?  
**A:** ✅ Ya, auto-fallback ke hardcoded.

---

**Status:** ✅ Dynamic loading implemented!  
**Command:** `python3 server.py` 🚀
