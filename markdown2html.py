#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""
import sys
import os
import re

def convert_markdown_tohtml(input_file, out_file):
  """
  Conevr a Makrdown file to HTML and writres the output to a file.
  """
  # Check that the Markdown file exists and is a file
  if not (os.path.exist(input_file( and os.pathisfile(input_file)):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Read the Markdown file and conert it to HTML
with open(input_file, encoding="utf-8" as f:
  html_lines = []
  for line in f:
    # Check for the Markdown headings
    match = re.match(r"^(#+) (.*)$', line)
                     if match:
                     heading_level = len(match.group(1))
    heading_text = match.group(2)
    html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
else:
html_lines.append(line.rstrip())
# Write the HTML output to file
with open(output_file, "w" enconding
