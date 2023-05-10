import markdown
import os
import sys
import re

def convert_file(input_path):
    if os.path.isdir(input_path):
        # If the input is a directory, convert all Markdown files within it
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    convert_single_file(file_path, root)  # Pass the root directory path as an argument
    else:
        # If the input is a single file, convert it
        convert_single_file(input_path, os.path.dirname(input_path))  # Pass the parent directory path

def convert_single_file(input_path, root_path):
    # Generate the output file path by replacing the ".md" extension with ".html"
    output_path = input_path.replace(".md", ".html")

    with open(input_path, "r") as f:
        text = f.read()

    # Create a Markdown instance with the 'tables' extension
    md = markdown.Markdown(extensions=['tables'])

    # Convert Markdown to HTML
    html = md.convert(text)

    # Convert HTML comments to HTML tags
    html = re.sub(r'<!--(.*?)-->', r'<\1>', html)

    # Find the relative path from the input file to the root directory
    relative_path = os.path.relpath(root_path, os.path.dirname(input_path))

    # Construct the paths to the HEAD.html and TAIL.html files relative to the input file
    head_path = os.path.join(relative_path, "HEAD.html")
    tail_path = os.path.join(relative_path, "TAIL.html")

    # Read the contents of HEAD.html
    if os.path.isfile(head_path):
        with open(head_path, "r") as head_file:
            head_contents = head_file.read()

        # Modify the stylesheet link based on the relative path
        stylesheet_link = f'<link rel="stylesheet" href="{os.path.join("..", relative_path, "style.css")}">'
        head_contents = head_contents.replace("</head>", f"{stylesheet_link}\n</head>")

        # Append HEAD.html contents to the HTML
        html = head_contents + html

    # Read the contents of TAIL.html
    if os.path.isfile(tail_path):
        with open(tail_path, "r") as tail_file:
            tail_contents = tail_file.read()

        # Append TAIL.html contents to the HTML
        html += tail_contents

    # Modify links to local .md files to point to .html files
    html = re.sub(r'<a href="(.*?)\.md">', r'<a href="\1.html">', html)

    with open(output_path, "w") as f:
        f.write(html)

    print(f"Conversion successful. HTML saved to {output_path}")

if __name__ == "__main__":
    # Check if an input file or directory path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide the input Markdown file or directory path.")
        sys.exit(1)

    input_path = sys.argv[1]

    # Check if the input path exists
    if not os.path.exists(input_path):
        print("Input path does not exist.")
        sys.exit(1)

    convert_file(input_path)
