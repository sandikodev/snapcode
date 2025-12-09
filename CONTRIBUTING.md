# Contributing to SnapCode

Thank you for your interest in contributing! 🎉

## Ways to Contribute

### 🎨 Features
- New OS window themes
- New color themes
- Export formats (PDF, SVG)
- UI/UX improvements

### 🐛 Bug Fixes
- Browser compatibility issues
- Rendering bugs
- Performance improvements

### 📝 Documentation
- Fix typos or improve clarity
- Add examples
- Translate to other languages

### 💡 Ideas
- Suggest new features
- Share use cases
- Provide feedback

## Getting Started

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/snapcode.git
cd snapcode
```

### 2. Make Changes
- Edit `index.html` (single file app!)
- Test in browser: `open index.html`
- No build step needed!

### 3. Test
- Test in multiple browsers (Chrome, Firefox, Safari)
- Test all OS themes
- Test all export features
- Check responsive design

### 4. Commit
```bash
git add .
git commit -m "feat: add your feature description"
```

Use conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - UI/styling
- `refactor:` - Code refactoring
- `perf:` - Performance improvement

### 5. Push & PR
```bash
git push origin your-branch-name
```

Then open a Pull Request on GitHub.

## Code Guidelines

### HTML/CSS/JS
- Keep everything in `index.html` (buildless philosophy)
- Use CDN for dependencies
- Maintain Alpine.js reactive patterns
- Follow existing code style
- Add comments for complex logic

### Testing Checklist
- [ ] Works in Chrome
- [ ] Works in Firefox
- [ ] Works in Safari
- [ ] Mobile responsive
- [ ] All themes work
- [ ] Export functions work
- [ ] No console errors

## Adding New Features

### New OS Theme
1. Add theme to `osThemes` object
2. Add CSS classes for window chrome
3. Test with all color themes
4. Update README

### New Color Theme
1. Add theme to Prism.js themes
2. Test syntax highlighting
3. Ensure good contrast
4. Update README

### New Export Format
1. Add export function
2. Test with various content types
3. Handle edge cases
4. Update UI

## Need Help?

- 💬 [Open a Discussion](https://github.com/sandikodev/snapcode/discussions)
- 🐛 [Report a Bug](https://github.com/sandikodev/snapcode/issues)
- 📧 Contact: [@sandikodev](https://github.com/sandikodev)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn
- Focus on the code, not the person

---

**Thank you for contributing!** 🚀

*ngode-ngide kode ngadi-ngadi*
