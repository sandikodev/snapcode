# SnapCode - TODO List

> **Iterasi konsisten untuk penyempurnaan SnapCode**

Last Updated: 2025-12-10

---

## 🎯 Priority: High

### UI/UX Improvements
- [ ] Dark mode untuk editor UI (bukan hanya preview)
- [ ] Keyboard shortcuts (Ctrl+S save, Ctrl+E export, dll)
- [ ] Better mobile experience (responsive controls)
- [ ] Improved drag & drop (visual feedback)
- [ ] Loading states untuk export
- [ ] Toast notifications untuk actions

### Features - Export
- [ ] SVG export (vector format)
- [ ] PDF export (print-ready)
- [ ] Copy as HTML
- [ ] Share via URL (encode markdown in URL)

### Performance
- [ ] Lazy load Mermaid.js (only when needed)
- [ ] Lazy load KaTeX (only when needed)
- [ ] Optimize html2canvas rendering
- [ ] Better caching strategy
- [ ] Reduce initial load time

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
- [ ] Accessibility improvements (ARIA labels)
- [ ] Input validation
- [ ] Sanitize user input

### Documentation
- [ ] Add screenshots to README
- [ ] Create video tutorial
- [ ] API documentation (if needed)
- [ ] More usage examples
- [ ] FAQ section
- [ ] Troubleshooting guide

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
- [ ] Accessibility testing (axe-core)

### Infrastructure
- [ ] CI/CD pipeline
- [ ] Automated deployment
- [ ] Version tagging
- [ ] Changelog automation
- [ ] Release notes

### Community
- [ ] Contributor guide improvements
- [ ] Issue templates refinement
- [ ] Discussion categories
- [ ] Community showcase
- [ ] Plugin system (future)

---

## 🐛 Known Issues

### Bugs to Fix
- [ ] Copy to clipboard tidak work di Firefox
- [ ] Mermaid diagram kadang tidak render
- [ ] Export PNG quality di Safari
- [ ] Mobile scrolling issue
- [ ] Font loading race condition

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
- [ ] Collaboration features (real-time)

### Integrations
- [ ] GitHub integration (save to gist)
- [ ] Notion integration
- [ ] Obsidian plugin
- [ ] Discord bot
- [ ] Slack app

### Monetization (Optional)
- [ ] Premium themes
- [ ] Cloud storage
- [ ] Team features
- [ ] API access
- [ ] Priority support

---

## 📊 Metrics to Track

### Performance
- [ ] Initial load time < 1s
- [ ] Export time < 2s
- [ ] Memory usage < 100MB
- [ ] Bundle size < 60KB

### Quality
- [ ] Lighthouse score > 90
- [ ] Accessibility score > 95
- [ ] SEO score > 90
- [ ] Best practices > 90

### Community
- [ ] GitHub stars
- [ ] Contributors count
- [ ] Issues resolved
- [ ] PR merged

---

## 🎯 Current Sprint (Week 1)

### Focus: Core Improvements
- [ ] Dark mode UI
- [ ] Keyboard shortcuts
- [ ] SVG export
- [ ] Better mobile UX

### Goals
- Improve user experience
- Add most requested features
- Fix critical bugs
- Update documentation

---

## 📝 Notes

### Development Principles
- Keep it buildless (no npm build)
- Single HTML file philosophy
- Progressive enhancement
- Accessibility first
- Performance matters

### Contribution Guidelines
- One feature per PR
- Test in multiple browsers
- Update README if needed
- Follow code style
- Add comments for complex logic

---

## 🚀 Completed

### v1.0.0 (2025-12-10)
- ✅ Initial release
- ✅ 5 OS themes (macOS, Windows, Chrome OS)
- ✅ 4 color themes (Dracula, Monokai, GitHub, Nord)
- ✅ Fira Code ligatures
- ✅ Mermaid diagrams
- ✅ KaTeX math
- ✅ PNG export
- ✅ Copy to clipboard
- ✅ Drag & drop
- ✅ Open source (MIT)
- ✅ Documentation
- ✅ Contributing guidelines

---

**Last Review:** 2025-12-10  
**Next Review:** Weekly (every Monday)

*ngode-ngide kode ngadi-ngadi* 🚀
