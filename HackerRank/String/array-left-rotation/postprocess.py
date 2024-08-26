import re
import os

def process_markdown_content(content, outputfile):

    with open(input_file, 'r' , encoding ='utf-8') as file :
        content = file.read()
    
    blocks = re.split(r'(<\/?\w+[^>]*>)',content)
    

    processed_content = ""

    first = True
    for block in blocks:

        if re.match(r'(<\/?\w+[^>]*>)',block):
            #nested html add to processed
            processed_content+= block
            first = True
            continue
        
        if first:
            block = re.sub(r'(\n\s*)?(!\[Equation]\(svg_equations/equation_\d+\.svg\))',r'\1\n\n\2', block, count= 1)
            first = False
        else:
            block = re.sub(r'\n\s*(!\[Equation\]\(svg_equations/equation_\d+\.svg\))', r' \1', block)
        


        processed_content+=block
    
    #processed_content = ''.join(processed_content)

    print(processed_content)
    with open(outputfile , 'w' ,encoding='utf-8') as file:
        file.write(processed_content)
     


input_file = 'output.md'
outputfile = 'output2.md'

process_markdown_content(input_file, outputfile)




