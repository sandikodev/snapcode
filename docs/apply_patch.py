#!/usr/bin/env python3
with open('index.html', 'r') as f:
    lines = f.readlines()

# Find insertion point (after line with "bg-gray-800 rounded-lg shadow-2xl p-6")
insert_idx = None
for i, line in enumerate(lines):
    if 'bg-gray-800 rounded-lg shadow-2xl p-6' in line and '<!-- Editor -->' in lines[i-1]:
        insert_idx = i + 1
        break

if not insert_idx:
    print("Could not find insertion point")
    exit(1)

# Tab switcher HTML
tab_html = '''            <!-- Tab Switcher -->
            <div class="flex items-center gap-2 mb-4 border-b border-gray-700 pb-2">
              <button
                @click="editorMode = 'markdown'"
                :class="editorMode === 'markdown' ? 'bg-gray-700 text-white' : 'text-gray-400 hover:text-white'"
                class="px-4 py-2 rounded-t-lg transition text-sm font-medium"
              >
                Markdown
              </button>
              <button
                @click="editorMode = 'explorer'"
                :class="editorMode === 'explorer' ? 'bg-gray-700 text-white' : 'text-gray-400 hover:text-white'"
                class="px-4 py-2 rounded-t-lg transition text-sm font-medium"
              >
                File Explorer
              </button>
            </div>

            <!-- Markdown Editor -->
            <div x-show="editorMode === 'markdown'">
'''

# Insert tab switcher
lines.insert(insert_idx, tab_html)

# Find where to close markdown editor div (before settings section)
close_idx = None
for i in range(insert_idx, len(lines)):
    if '<div class="mt-4 space-y-4">' in lines[i]:
        close_idx = i
        break

if close_idx:
    lines.insert(close_idx, '            </div>\n\n')
    
    # Add file explorer
    explorer_html = '''            <!-- File Explorer -->
            <div x-show="editorMode === 'explorer'">
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-xl font-semibold text-white">File Explorer</h2>
                <button
                  @click="$refs.fileInput.click()"
                  class="px-3 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition flex items-center gap-2 text-sm"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M12 4v16m8-8H4"></path>
                  </svg>
                  Add File
                </button>
                <input type="file" x-ref="fileInput" @change="addFile" class="hidden" accept=".md,.txt,.js,.html,.css,.json">
              </div>
              
              <div class="bg-gray-900 rounded-lg h-96 overflow-y-auto">
                <template x-if="files.length === 0">
                  <div class="flex flex-col items-center justify-center h-full text-gray-500">
                    <svg class="w-16 h-16 mb-4" fill="none" stroke="currentColor" stroke-width="1" viewBox="0 0 24 24">
                      <path d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path>
                    </svg>
                    <p>No files yet</p>
                    <p class="text-sm mt-2">Click "Add File" to start</p>
                  </div>
                </template>
                
                <template x-if="files.length > 0">
                  <div class="divide-y divide-gray-800">
                    <template x-for="(file, index) in files" :key="index">
                      <div 
                        @click="selectFile(index)"
                        :class="selectedFileIndex === index ? 'bg-purple-600/20 border-l-4 border-purple-500' : 'hover:bg-gray-800'"
                        class="p-3 cursor-pointer transition flex items-center justify-between group"
                      >
                        <div class="flex items-center gap-3 flex-1 min-w-0">
                          <svg class="w-5 h-5 text-blue-400 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                            <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                          </svg>
                          <div class="flex-1 min-w-0">
                            <p class="text-white text-sm font-medium truncate" x-text="file.name"></p>
                            <p class="text-gray-500 text-xs" x-text="formatFileSize(file.size)"></p>
                          </div>
                        </div>
                        <button
                          @click.stop="removeFile(index)"
                          class="opacity-0 group-hover:opacity-100 p-1 hover:bg-red-600/20 rounded transition"
                        >
                          <svg class="w-4 h-4 text-red-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                            <path d="M6 18L18 6M6 6l12 12"></path>
                          </svg>
                        </button>
                      </div>
                    </template>
                  </div>
                </template>
              </div>
            </div>

'''
    lines.insert(close_idx + 1, explorer_html)

# Write back
with open('index.html', 'w') as f:
    f.writelines(lines)

print("✅ Patch applied successfully!")
print("File Explorer feature has been added with tab switcher.")
