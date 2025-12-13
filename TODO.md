# SnapCode - TODO List

> **Iterasi konsisten untuk penyempurnaan SnapCode**

Last Updated: 2025-12-13

---

## ✅ Completed

### UI/UX Improvements
- [x] Keyboard shortcuts (Ctrl+E export, Ctrl+Z undo, Ctrl+Y redo, F11 fullscreen)
- [x] Improved drag & drop (visual feedback - purple ring)
- [x] Loading states untuk export (spinner overlay)
- [x] Toast notifications untuk actions
- [x] Fullscreen mode (F11 / Ctrl+Shift+F)
- [x] Print view (print-friendly CSS)
- [x] Auto-save to localStorage
- [x] Undo/Redo (50-step history)
- [x] Settings persistence (theme, font, etc)

### Features - Export
- [x] SVG export (vector format)
- [x] Copy as HTML
- [x] Share via URL (encode markdown in URL)

### Performance
- [x] Lazy load Mermaid.js (only when needed)
- [x] Lazy load KaTeX (only when needed)
- [x] Service Worker (offline support)
- [x] FOUC prevention

### Accessibility
- [x] ARIA labels
- [x] Skip to content link
- [x] Focus indicators
- [x] Semantic HTML

### Bug Fixes
- [x] Bullet points & numbered lists styling
- [x] Mermaid not defined error (lazy load fix)
- [x] SVG path error (copy icon)
- [x] Service Worker CORS error

---

## 🎯 Priority: High

### Features - Export
- [ ] PDF export (print-ready)

### Mobile
- [x] Better mobile responsive (toolbar buttons)
- [ ] Touch gestures support
- [ ] Mobile-optimized controls

---

## 🎯 Priority: Medium

### Features - OS Themes
- [ ] Ubuntu theme (orange accent)
- [ ] Fedora theme (blue accent)
- [ ] Linux Mint theme
- [ ] Elementary OS theme
- [ ] Pop!_OS theme

### Features - Color Themes
- [ ] Solarized Light
- [ ] Solarized Dark
- [ ] One Dark
- [ ] Gruvbox
- [ ] Tokyo Night
- [ ] Catppuccin

### Code Quality
- [ ] Refactor large functions (split into smaller)
- [ ] Add JSDoc comments
- [ ] Better error handling (try-catch)
- [ ] Input validation

### Documentation
- [ ] Add screenshots to README
- [ ] Create video tutorial
- [ ] More usage examples
- [ ] FAQ section

---

## 🎯 Priority: Low

### Features - Advanced
- [ ] Custom fonts support
- [ ] Custom window chrome colors
- [ ] Animation support (GIF export)
- [ ] Multiple pages/slides
- [ ] Templates library
- [ ] Preset configurations

### Testing
- [ ] Browser compatibility tests
- [ ] Performance benchmarks
- [ ] Automated testing (Playwright/Cypress)
- [ ] Visual regression testing

### Infrastructure
- [ ] CI/CD pipeline improvements
- [ ] Version tagging
- [ ] Changelog automation

---

## 🐛 Known Issues

### Bugs to Fix
- [ ] Copy to clipboard tidak work di Firefox (fallback needed)
- [ ] Export PNG quality di Safari
- [ ] Mobile scrolling issue

### Browser Compatibility
- [ ] Test di Safari 14+
- [ ] Test di Firefox 88+
- [ ] Test di Edge 90+
- [ ] Test di Chrome Android
- [ ] Test di Safari iOS

---

## 💡 Ideas / Future Considerations

### Long-term Vision
- [ ] Desktop app (Electron/Tauri)
- [ ] Browser extension
- [ ] VS Code extension
- [ ] CLI tool
- [ ] API service

### Integrations
- [ ] GitHub integration (save to gist)
- [ ] Notion integration
- [ ] Obsidian plugin

---

## 📊 Feature Summary

| Category | Done | Total | Progress |
|----------|------|-------|----------|
| UI/UX | 9 | 9 | ✅ 100% |
| Export | 3 | 4 | 🟡 75% |
| Performance | 4 | 4 | ✅ 100% |
| Accessibility | 4 | 4 | ✅ 100% |
| Mobile | 1 | 3 | 🟡 33% |
| Themes | 0 | 11 | ⬜ 0% |

---

*Last updated: December 13, 2025*
