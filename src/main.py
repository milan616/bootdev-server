from genpub import gen_public
from genpage import generate_page, generate_pages_recursive
from textnode import TextNode, TextType
import os, shutil
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    shutil.rmtree("./docs", ignore_errors=True)
    gen_public("./static", "./docs")
    generate_pages_recursive(basepath, "./content", "./template.html", "./docs")

main()
