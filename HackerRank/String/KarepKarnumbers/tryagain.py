import re
import os
from bs4 import BeautifulSoup

# def extract_and_save_svg(html_content, output_dir):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     svg_spans = soup.find_all('span', class_='MathJax_SVG')
    
#     for i, span in enumerate(svg_spans, 1):
#         svg = span.find('svg')
#         if svg:
#             # Extract the SVG content
#             svg_content = str(svg)
            
#             # Save SVG to a file
#             svg_filename = f'equation_{i}.svg'
#             with open(os.path.join(output_dir, svg_filename), 'w', encoding='utf-8') as svg_file:
#                 svg_file.write(svg_content)
            
#             # Replace the span with a Markdown image reference
#             span.replace_with(BeautifulSoup(f'![Equation](equation_{i}.svg)', 'html.parser'))
    
#     return str(soup)
def extract_and_save_svg(html_content, output_dir):
    soup = BeautifulSoup(html_content, 'html.parser')
    svg_spans = soup.find_all('span', class_='MathJax_SVG')
    
    for i, span in enumerate(svg_spans, 1):
        svg = span.find('svg')
        if svg:
            # Format the SVG content
            svg['xmlns'] = "http://www.w3.org/2000/svg"
            svg['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
            
            # Remove unnecessary attributes
            for attr in ['role', 'focusable', 'style']:
                if attr in svg.attrs:
                    del svg[attr]
            
            # Ensure correct ordering of width, height, and viewBox attributes
            width = svg.get('width')
            height = svg.get('height')
            viewBox = svg.get('viewBox')
            del svg['width']
            del svg['height']
            del svg['viewBox']
            svg['width'] = width
            svg['height'] = height
            svg['viewBox'] = viewBox
            
            svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
{svg.prettify()}"""
            
            # Save SVG to a file
            svg_filename = f'equation_{i}.svg'
            with open(os.path.join(output_dir, svg_filename), 'w', encoding='utf-8') as svg_file:
                svg_file.write(svg_content)
            
            # Replace the span with a Markdown image reference
            span.replace_with(BeautifulSoup(f'![Equation]({svg_filename})', 'html.parser'))
    
    return str(soup)

def html_to_markdown(element):
    if element.name == 'p':
        return element.get_text() + '\n\n'
    elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        return '#' * int(element.name[1]) + ' ' + element.get_text() + '\n\n'
    elif element.name == 'ul':
        return ''.join('- ' + li.get_text() + '\n' for li in element.find_all('li')) + '\n'
    elif element.name == 'ol':
        return ''.join(f'{i}. ' + li.get_text() + '\n' for i, li in enumerate(element.find_all('li'), 1)) + '\n'
    elif element.name == 'blockquote':
        return ''.join('> ' + p.get_text() + '\n' for p in element.find_all('p')) + '\n'
    elif element.name == 'pre':
        return '```\n' + element.get_text() + '\n```\n\n'
    else:
        return str(element) + '\n\n'

def process_file(input_file, output_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process the content
    processed_content = extract_and_save_svg(content, output_dir)
    
    # Remove the style tag for MathJax
    processed_content = re.sub(r'<style id="MathJax_SVG_styles">.*?</style>', '', processed_content, flags=re.DOTALL)
    
    # Convert remaining HTML to Markdown-like format
    soup = BeautifulSoup(processed_content, 'html.parser')
    markdown_content = ''
    
    # If there's a body, use its children, otherwise use the top-level elements
    elements = soup.body.children if soup.body else soup.children
    
    for element in elements:
        if element.name:  # Skip NavigableString objects
            markdown_content += html_to_markdown(element)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

# Usage
input_file = 'input.html'
output_file = 'output3.md'
output_dir = 'svg_equations'
process_file(input_file, output_file, output_dir)

print(f"Conversion completed. Check {output_file} for the result and {output_dir} for the SVG files.")