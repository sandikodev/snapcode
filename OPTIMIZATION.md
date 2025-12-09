# SnapCode - Performance Optimization

> **Buildless optimization strategies untuk Lighthouse score 90+**

## 🎯 Target Metrics

- **Performance:** 90+ (currently: ~40)
- **Accessibility:** 95+ (currently: ~85)
- **Best Practices:** 90+ (currently: ~75)
- **SEO:** 95+ (currently: ~90)

---

## 🚀 Quick Wins (No Build Required)

### 1. Lazy Load Dependencies ✅ Priority: HIGH

**Problem:** All CDN scripts load immediately (blocking)

**Solution:**
```javascript
// Load only when needed
function loadKaTeX() {
  if (window.katex) return Promise.resolve();
  return Promise.all([
    loadCSS('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css'),
    loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js')
  ]);
}

function loadMermaid() {
  if (window.mermaid) return Promise.resolve();
  return loadScript('https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js');
}

// Trigger on checkbox enable
```

**Impact:** -500KB initial load, +2s faster FCP

### 2. Defer Non-Critical CSS ✅ Priority: HIGH

**Problem:** KaTeX CSS blocks render

**Solution:**
```html
<!-- Preload then apply -->
<link rel="preload" href="katex.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="katex.css"></noscript>
```

**Impact:** +1s faster FCP

### 3. Optimize Font Loading ✅ Priority: HIGH

**Problem:** Fira Code blocks render

**Solution:**
```css
@font-face {
  font-family: 'Fira Code';
  src: url('...') format('woff2');
  font-display: swap; /* Show fallback immediately */
}
```

**Impact:** +0.5s faster FCP

### 4. Add Resource Hints ✅ Priority: MEDIUM

```html
<!-- DNS prefetch for CDN -->
<link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>

<!-- Preload critical resources -->
<link rel="preload" href="alpine.js" as="script">
<link rel="preload" href="marked.js" as="script">
```

**Impact:** +0.3s faster connection

### 5. Inline Critical CSS ✅ Priority: HIGH

**Problem:** Tailwind CDN blocks render

**Solution:**
```html
<style>
  /* Inline only critical above-the-fold CSS */
  .container { max-width: 1200px; margin: 0 auto; }
  /* ... */
</style>
<!-- Load full Tailwind after -->
<link rel="stylesheet" href="tailwind-cdn" media="print" onload="this.media='all'">
```

**Impact:** +1.5s faster FCP

---

## 🔧 Medium Effort Optimizations

### 6. Service Worker for Caching ✅ Priority: MEDIUM

```javascript
// sw.js - Cache CDN resources
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('snapcode-v1').then((cache) => {
      return cache.addAll([
        '/index.html',
        'https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js',
        // ... other CDN resources
      ]);
    })
  );
});
```

**Impact:** Instant repeat visits

### 7. Image Optimization ✅ Priority: LOW

**Problem:** No images currently, but for future

**Solution:**
- Use WebP with fallback
- Lazy load images
- Add width/height attributes

### 8. Reduce JavaScript Execution ✅ Priority: MEDIUM

**Problem:** Large Alpine.js component

**Solution:**
- Split into smaller components
- Use `x-init` for deferred initialization
- Debounce expensive operations

```javascript
// Debounce markdown parsing
Alpine.effect(() => {
  clearTimeout(this.parseTimeout);
  this.parseTimeout = setTimeout(() => {
    this.parsedMarkdown = this.parseMarkdown();
  }, 300);
});
```

**Impact:** -200ms TTI

---

## 🎨 Accessibility Improvements

### 9. ARIA Labels ✅ Priority: HIGH

```html
<button aria-label="Export as PNG">Export</button>
<input aria-label="Markdown content" />
<select aria-label="Choose OS theme">...</select>
```

### 10. Keyboard Navigation ✅ Priority: HIGH

```javascript
// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.key === 's') {
    e.preventDefault();
    exportImage();
  }
});
```

### 11. Focus Indicators ✅ Priority: MEDIUM

```css
button:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}
```

---

## 📊 Best Practices

### 12. Add Meta Tags ✅ Priority: HIGH

```html
<meta name="description" content="Create beautiful markdown images">
<meta name="theme-color" content="#7c3aed">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### 13. HTTPS Only ✅ Priority: HIGH

Already done via GitHub Pages

### 14. No Console Errors ✅ Priority: HIGH

```javascript
// Add error handling
try {
  // risky operation
} catch (e) {
  console.error('Error:', e);
  // Show user-friendly message
}
```

---

## 🔍 SEO Improvements

### 15. Structured Data ✅ Priority: MEDIUM

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "SnapCode",
  "description": "Create beautiful markdown images",
  "url": "https://sandikodev.github.io/snapcode"
}
</script>
```

### 16. Open Graph Tags ✅ Priority: MEDIUM

```html
<meta property="og:title" content="SnapCode">
<meta property="og:description" content="...">
<meta property="og:image" content="og-image.png">
```

---

## 📈 Measurement Strategy

### Before Optimization
```
Performance: ~40
Accessibility: ~85
Best Practices: ~75
SEO: ~90
```

### After Quick Wins (Target)
```
Performance: 70+
Accessibility: 95+
Best Practices: 90+
SEO: 95+
```

### After All Optimizations (Target)
```
Performance: 90+
Accessibility: 98+
Best Practices: 95+
SEO: 98+
```

---

## 🛠️ Implementation Plan

### Phase 1: Quick Wins (1-2 hours)
- [ ] Lazy load KaTeX
- [ ] Lazy load Mermaid
- [ ] Defer non-critical CSS
- [ ] Add resource hints
- [ ] Optimize font loading

### Phase 2: Medium Effort (2-4 hours)
- [ ] Service Worker
- [ ] Reduce JS execution
- [ ] ARIA labels
- [ ] Keyboard navigation

### Phase 3: Polish (1-2 hours)
- [ ] Structured data
- [ ] Open Graph tags
- [ ] Error handling
- [ ] Focus indicators

---

## 🎯 Trade-offs

### Buildless Philosophy
✅ **Pros:**
- No build step
- Easy to contribute
- Single file simplicity
- No node_modules

❌ **Cons:**
- Larger initial bundle
- No tree-shaking
- No code splitting
- Manual optimization

### Our Approach
**Keep buildless, but optimize smartly:**
- Lazy load heavy dependencies
- Use modern browser APIs
- Leverage CDN caching
- Progressive enhancement

---

## 📝 Notes

### Why Not Use Build Tools?

1. **Educational Value** - Show that optimization possible without tools
2. **Simplicity** - Anyone can edit single HTML file
3. **Philosophy** - Prove buildless can be performant
4. **Accessibility** - Lower barrier to contribution

### When to Consider Build Tools?

- If bundle > 200KB
- If need code splitting
- If need tree-shaking
- If team prefers it

**For now: Stay buildless, optimize manually** 🚀

---

**Last Updated:** 2025-12-10  
**Next Review:** After Phase 1 implementation

*ngode-ngide kode ngadi-ngadi*
