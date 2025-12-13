#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.log('🔍 SnapCode Validation Report\n');

// Check if index.html exists
const indexPath = path.join(__dirname, 'index.html');
if (!fs.existsSync(indexPath)) {
  console.error('❌ index.html not found');
  process.exit(1);
}

// Read and analyze HTML file
const html = fs.readFileSync(indexPath, 'utf8');

// Basic HTML structure checks
const checks = [
  {
    name: 'DOCTYPE declaration',
    test: () => html.includes('<!DOCTYPE html>'),
    fix: 'Add <!DOCTYPE html> at the beginning'
  },
  {
    name: 'HTML lang attribute',
    test: () => html.includes('<html lang='),
    fix: 'Add lang attribute to <html> tag'
  },
  {
    name: 'Meta charset',
    test: () => html.includes('<meta charset='),
    fix: 'Add <meta charset="UTF-8"> in <head>'
  },
  {
    name: 'Meta viewport',
    test: () => html.includes('name="viewport"'),
    fix: 'Add viewport meta tag for responsive design'
  },
  {
    name: 'Title tag',
    test: () => html.includes('<title>') && html.includes('</title>'),
    fix: 'Add <title> tag in <head>'
  },
  {
    name: 'Alpine.js x-data',
    test: () => html.includes('x-data='),
    fix: 'Ensure Alpine.js is properly initialized'
  },
  {
    name: 'No x-if templates (should use x-show)',
    test: () => !html.includes('x-if='),
    fix: 'Replace x-if with x-show to avoid cloneNode errors'
  },
  {
    name: 'Service Worker registration',
    test: () => html.includes('serviceWorker.register'),
    fix: 'Add service worker registration for PWA'
  }
];

let passed = 0;
let failed = 0;

checks.forEach(check => {
  if (check.test()) {
    console.log(`✅ ${check.name}`);
    passed++;
  } else {
    console.log(`❌ ${check.name}`);
    console.log(`   💡 ${check.fix}\n`);
    failed++;
  }
});

// File size check
const stats = fs.statSync(indexPath);
const fileSizeKB = Math.round(stats.size / 1024);
console.log(`\n📊 File size: ${fileSizeKB}KB`);

if (fileSizeKB > 100) {
  console.log('⚠️  File is getting large, consider optimization');
} else {
  console.log('✅ File size is optimal');
}

// Summary
console.log(`\n📋 Summary: ${passed} passed, ${failed} failed`);

if (failed === 0) {
  console.log('🎉 All checks passed!');
  process.exit(0);
} else {
  console.log('🔧 Please fix the issues above');
  process.exit(1);
}
