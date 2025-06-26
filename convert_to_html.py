import sys
import os
import markdown


def convert_to_html(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html = markdown.markdown(md_text, extensions=[
            'extra',        # tables, fenced code blocks, etc.
            'codehilite',   # syntax highlight for code blocks
            'toc',          # table of contents
        ]
    )

    # Wrap in a minimal HTML document
    full_html = f"""<!DOCTYPE html>
                    <html lang="en">
                    <head>
                      <meta charset="UTF-8">
                      <title>{os.path.basename(input_path)}</title>
                      <style>
                        /* Basic styling */
                        body {{ font-family: sans-serif; max-width: 800px; margin: 2rem auto; line-height: 1.6; padding: 0 1rem; }}
                        pre code {{ background: #f4f4f4; padding: 0.5rem; display: block; overflow-x: auto; }}
                        code {{ background: #f4f4f4; padding: 0.2rem 0.4rem; }}
                        blockquote {{ border-left: 4px solid #ccc; padding-left: 1rem; color: #666; }}
                      </style>
                    </head>
                    <body>
                    {html}
                    </body>
                    </html>
                    """

    # Write HTML out
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"Converted `{input_path}` → `{output_path}`")

def main():
    input_md = sys.argv[1]
    output_html = sys.argv[2]

    if not os.path.isfile(input_md):
        print(f"Error: `{input_md}` does not exist or is not a file.")
        sys.exit(1)

    convert_to_html(input_md, output_html)

if __name__ == "__main__":
    main()
