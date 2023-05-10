import markdown
import os
import sys

def convert_file(input_path):
    # Generate the output file path by replacing the ".md" extension with ".html"
    output_path = input_path.replace(".md", ".html")

    with open(input_path, "r") as f:
        text = f.read()

    # Convert Markdown to HTML
    html = markdown.markdown(text)

    with open(output_path, "w") as f:
        f.write(html)

    print(f"Conversion successful. HTML saved to {output_path}")

def convert_directory(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            # If the path is a directory, recursively convert files in the directory
            convert_directory(path)
        elif filename.endswith(".md"):
            # If the file has a ".md" extension, convert it to HTML
            convert_file(path)

# Check if the input path is provided
if len(sys.argv) < 2:
    print("Usage: python markdown_to_html.py <input_path>")
    sys.exit(1)

# Get the input path from the command line argument
input_path = sys.argv[1]

if os.path.isdir(input_path):
    # If the input path is a directory, convert all Markdown files in the directory
    convert_directory(input_path)
else:
    # If the input path is a file, convert the file to HTML
    convert_file(input_path)
