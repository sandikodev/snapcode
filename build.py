#!/usr/bin/env python3
"""
Build script for GitHub Pages deployment
Generates file list JSON for each folder
"""
import os
import json

def generate_file_list(folder):
    """Generate list of files in folder"""
    files = []
    folder_path = os.path.join(os.getcwd(), folder)
    
    if not os.path.exists(folder_path):
        return files
    
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            files.append({
                'name': filename,
                'size': os.path.getsize(filepath)
            })
    
    # Sort by name
    files.sort(key=lambda x: x['name'])
    return files

def main():
    # Generate file lists
    folders = ['content', 'docs']
    
    for folder in folders:
        files = generate_file_list(folder)
        
        # Save to JSON
        output_file = f'{folder}/files.json'
        with open(output_file, 'w') as f:
            json.dump(files, f, indent=2)
        
        print(f'✅ Generated {output_file} ({len(files)} files)')
    
    print('\n🚀 Build complete! Ready for GitHub Pages.')

if __name__ == '__main__':
    main()
