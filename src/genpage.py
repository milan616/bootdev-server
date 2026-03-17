from htmlnode import HTMLNode, markdown_to_html_node
import os, shutil

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[0:2] == "# ":
            return line[2:]

    raise Exception("header not found")

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    os.makedirs(dest_dir_path, exist_ok=True)

    contents = os.listdir(dir_path_content)

    for content in contents:
        from_path = os.path.join(dir_path_content, content)
        if os.path.isfile(from_path):
            dest_path = os.path.join(dest_dir_path, content.replace("md", "html"))
            generate_page(basepath, from_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, content)
            generate_pages_recursive(basepath, from_path, template_path, dest_path)

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""

    try:
        with open(from_path, 'r') as f:
            markdown = f.read()
        with open(template_path, 'r') as f:
            template = f.read()
    except Exception as e:
        raise e

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    try:
        path = dest_path[0:dest_path.rfind("/")]
        os.makedirs(path, exist_ok=True)
        with open(dest_path, 'w') as f:
            f.write(template)
    except Exception as e:
        raise e
