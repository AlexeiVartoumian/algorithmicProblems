import re
from bs4 import BeautifulSoup

def extract_svg(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    svg_spans = soup.find_all('span', class_='MathJax_SVG')
    
    for span in svg_spans:
        svg = span.find('svg')
        if svg:
            # Extract the SVG content
            svg_content = str(svg)
            # Replace the span with the SVG content
            span.replace_with(BeautifulSoup(svg_content, 'html.parser'))
    
    return str(soup)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Process the content
    processed_content = extract_svg(content)
    
    # Remove the style tag for MathJax
    processed_content = re.sub(r'<style id="MathJax_SVG_styles">.*?</style>', '', processed_content, flags=re.DOTALL)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_content)

# Usage
input_file = 'input.html'
output_file = 'output.md'
process_file(input_file, output_file)