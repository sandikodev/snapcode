# SnapCode - Linting & Validation Setup

## 🛠️ Tools Installed

### HTML Validation
- **HTMLHint** - Fast HTML linter
- **html-validate** - Comprehensive HTML validator

### JavaScript Linting
- **ESLint** - JavaScript/HTML linting with Alpine.js support

### Code Formatting
- **Prettier** - Code formatter

### Custom Validation
- **validate.js** - Custom SnapCode-specific checks

## 📋 Available Commands

### Quick Check (Recommended)
```bash
pnpm run check:main
```
Runs custom validation + HTML linting + main JS linting

### Individual Tools
```bash
# Custom validation (SnapCode-specific checks)
pnpm run validate:custom

# HTML validation
pnpm run lint:html          # HTMLHint (fast)
pnpm run validate           # html-validate (comprehensive)

# JavaScript linting
pnpm run lint:js:main       # Main files only
pnpm run lint:js            # All files (includes celebration/)

# Code formatting
pnpm run format:main        # Format main files
pnpm run format             # Format all files
```

## ✅ Current Status

### Custom Validation Results
```
🔍 SnapCode Validation Report

✅ DOCTYPE declaration
✅ HTML lang attribute  
✅ Meta charset
✅ Meta viewport
✅ Title tag
✅ Alpine.js x-data
✅ No x-if templates (should use x-show)
✅ Service Worker registration

📊 File size: 80KB
✅ File size is optimal

📋 Summary: 8 passed, 0 failed
🎉 All checks passed!
```

### HTMLHint Results
```
✅ No HTML structure errors found
✅ Tailwind CSS classes allowed (id-class-value: false)
```

### ESLint Issues Found
**Main Issues to Fix:**
- Missing browser globals (btoa, atob, location, alert, etc.)
- Unused variables and empty catch blocks
- Missing function definitions (loadKatex)

## 🔧 Configuration Files

### `.htmlhintrc`
- Tailwind CSS friendly (allows utility classes)
- Standard HTML validation rules

### `eslint.config.js`
- ES modules support
- Alpine.js globals defined
- Browser environment configured
- External library globals (marked, DOMPurify, etc.)

### `.prettierrc`
- 2-space indentation
- Single quotes
- 100 character line width

### `validate.js`
- Custom SnapCode-specific checks
- File size monitoring
- Alpine.js template validation

## 🎯 Next Steps

1. **Fix ESLint Issues** - Add missing browser globals
2. **Setup Pre-commit Hooks** - Auto-run linting before commits
3. **CI/CD Integration** - Add linting to GitHub Actions
4. **Code Coverage** - Add testing and coverage reports

## 📊 File Analysis

- **Main file**: `index.html` (80KB) ✅ Optimal size
- **Architecture**: Single-file buildless app
- **Dependencies**: All from CDN (no node_modules)
- **Framework**: Alpine.js + Tailwind CSS

## 🚀 Benefits

1. **Code Quality** - Consistent formatting and error detection
2. **Bug Prevention** - Catch issues before deployment  
3. **Maintainability** - Easier to read and modify code
4. **Team Collaboration** - Consistent code style
5. **Performance** - Detect potential performance issues
