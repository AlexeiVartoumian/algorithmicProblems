import re
import os
import sys

def process_markdown_content(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    blocks = re.split(r'(<\/?\w+[^>]*>)', content)
    
    processed_content = ""
    first = True
    for block in blocks:
        if re.match(r'(<\/?\w+[^>]*>)', block):
            processed_content += block
            first = True
            continue
        
        if first:
            block = re.sub(r'(\n\s*)?(!\[Equation]\(svg_equations/equation_\d+\.svg\))', r'\1\n\n\2', block, count=1)
            first = False
        else:
            block = re.sub(r'\n\s*(!\[Equation\]\(svg_equations/equation_\d+\.svg\))', r' \1', block)
        
        processed_content += block
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python postprocess.py <folder name>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    input_file = os.path.join(folder_path, "output.md")
    output_file = os.path.join(folder_path, "output.md")
    
    process_markdown_content(input_file, output_file)
    print(f"Postprocessing completed. Check {output_file} for the result.")

if __name__ == "__main__":
    main()