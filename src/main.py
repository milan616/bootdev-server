from genpub import gen_public
from genpage import generate_page, generate_pages_recursive
from textnode import TextNode, TextType
import os, shutil

def main():
    shutil.rmtree("./public", ignore_errors=True)
    gen_public("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

main()
