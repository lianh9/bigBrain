from markdown import markdown
import pdfkit

'''
setting input to markdown file and output to pdf
'''
input_filename = 'README.md'
output_filename = 'README.pdf'

'''
open the input file change the text to html4 and then use pdfkit to convert to pdf
'''
with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)
