from manim import *

Title.set_default(tex_template=TexTemplate(
    tex_compiler = "xelatex", 
    # tex_compiler = "luatex" でも可
    output_format = ".xdv", 
    preamble = r"""
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{zxjatype}
        \setCJKmainfont{IPAPMincho}
        \setCJKsansfont{IPAPGothic}
        \setCJKmonofont{IPAGothic}
    """
))

Text.set_default(font='IPAGothic')
