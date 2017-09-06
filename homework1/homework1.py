'''
PDF homework assignment generated using pylatex
https://jeltef.github.io/PyLaTeX/
'''


from pylatex import Document, Section, Subsection, Itemize, Enumerate, Description, \
    Subsection, Command, NoEscape, Math, Alignat, Figure
from pylatex.utils import italic, NoEscape
import os


def fill_document(doc):
    with doc.create(Section('Section 9.1', numbering=False)):
        with doc.create(Subsection('8', numbering=False)):
            with doc.create(Enumerate(enumeration_symbol=r"\alph*)",
                                  options={'start': 1})) as enum:
                enum.add_item('5')
                enum.add_item('3')
                enum.add_item('7')
                enum.add_item(NoEscape('$\sqrt{49+25}\\approx 8.6$'))
                enum.add_item(NoEscape('$\sqrt{9+25}\\approx 5.8$'))
                enum.add_item(NoEscape('$\sqrt{49+9}\\approx 7.6$'))
        with doc.create(Subsection('12', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'radius = \sqrt{(\sqrt{1^2+2^2})^2+3^2} &= \sqrt{14} \\')
                agn.append(r'(x-1)^2+(y-2)^2+(z-3)^2 &= (\sqrt{14})^2\\')
                agn.append(r'(x-1)^2+(y-2)^2+(z-3)^2 &= 14')
        with doc.create(Subsection('14', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'x^2+8x+y^2-6y+z^2+2z &= -17\\')
                agn.append(r'(x+4)^2-16+(y-3)^2-9+(z+1)^2-1 &= -17\\')
                agn.append(r'(x+4)^2+(y-3)^2+(z+1)^2 &= -17 +16+9+1\\')
                agn.append(r'(x+4)^2+(y-3)^2+(z+1)^2 &= 9\\')
            doc.append('The equation represents a sphere with center (-4,3,-1) and radius = 3')
        with doc.create(Subsection('16', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'3(x^2+y^2+z^2) &=10+6y+12z\\')
                agn.append(r'x^2+y^2+z^2 &=\frac{10}{3}+2y+4z\\')
                agn.append(r'x^2+y^2-2y+z^2-4z &=\frac{10}{3}\\')
                agn.append(r'x^2+(y-1)^2-2+(z-2)^2-4 &=\frac{10}{3}\\')
                agn.append(r'x^2+(y-1)^2+(z-2)^2 &=\frac{10}{3}+2+4\\')
                agn.append(r'x^2+(y-1)^2+(z-2)^2 &=\frac{28}{3}\\')
            doc.append('The equation represents a sphere with center (0,1,2) and radius =')
            doc.append(NoEscape('$2\sqrt{\\frac{7}{3}}$'))
        with doc.create(Subsection('21-32', numbering=False)):
            with doc.create(Enumerate(enumeration_symbol=r"\arabic*)",
                                      options={'start': 21})) as enum:
                enum.add_item('The vertical plane that lies over the line given by x=5 in the xy-plane')
                enum.add_item('The vertical plane that lies over the line given by y=-2 in the xy-plane')
                enum.add_item('The subspace containing all numbers smaller than the plane that goes through y=8')
                enum.add_item('The subspace containing all numbes larger than the vertical plane that lies over the line given by x=-3 in the xy-plane')
                enum.add_item('The subspace contained between (and including) the xy-planes that pass through z=0 and z=6')
                enum.add_item('The cup-shaped shell defined by spinning the parabola given by ')
                doc.append(NoEscape('$z^2=1$'))
                doc.append(' spun around the z-axis')
                enum.add_item('The circle that lies in the xy-plane and is centered at (0,0,-1) and has a radius = 2')
                enum.add_item('The cylindrical shell of radius = 4 that is centered around the x-axis')
                enum.add_item('The subspace contained within the sphere centered at (0,0,0) with radius ')
                doc.append(NoEscape('$\leq\sqrt{3}$'))
                enum.add_item('The plane that extends out from the line given by x=z')
                enum.add_item('The subspace that is outside the sphere centered at (0,0,1) with a radius of 1')
        with doc.create(Subsection('38', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\sqrt{(x+1)^2+(y-5)^2+(z-3)^2} &= 2\sqrt{(x-6)^2+(y-2)^2+(z+2)^2}\\')
                agn.append(r'x^2+2x+1+y^2-10y+25+z^2-6z+9 &= 4(x^2-12x+36+y^2-4y\\ \
                    &\textnormal{   }+4+z^2+4z+4)\\')
                agn.append(r'4x^2-x^2-48x-2x+4y^2-y^2-16y+10y+4z^2-z^2+16z+6z &= -141\\')
                agn.append(r'3x^2-50x+3y^2-6y+3z^2+22z &=-141\\')
                agn.append(r'x^2-\frac{50}{3}x+y^2-2y+z^2+\frac{22}{3}z &=-47\\')
                agn.append(r'(x-\frac{25}{3})^2+(y-1)^2+(z-\frac{11}{3})^2 &=-47+\frac{625}{9}+\frac{121}{9}\\')
                agn.append(r'(x-\frac{25}{3})^2+(y-1)^2+(z-\frac{11}{3})^2 &=\frac{323}{9}\\')
        doc.append('The center is (25/3, 1, 11/3) and the radius is ')
        doc.append(NoEscape('$\\frac{\\sqrt{323}}{3}$'))

    with doc.create(Section('Section 9.2', numbering=False)):
        with doc.create(Subsection('22', numbering=False)):
            doc.append(NoEscape('$\\langle \\frac{-6}{\\sqrt{6}}, \\frac{12}{\\sqrt{6}}, \\frac{6}{\\sqrt{6}}\\rangle$'))
        with doc.create(Subsection('28', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'wind = &\langle 50cos(\frac{7\pi}{4}), 50sin(\frac{7\pi}{4}) \rangle \
                    \\plane = &\langle 250cos(\frac{\pi}{6}), 250sin(\frac{\pi}{6}) \rangle\\')
                agn.append(r'true course = \langle 251.86, 89.64\rangle \textnormal{ and  } & \
                    ground speed = \sqrt{251.86^2 + 89.64^2} = 267.34\\')
        with doc.create(Subsection('38', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\vec{i} = & \langle 1,0,0 \rangle\\')
                agn.append(r'\vec{j} = & \langle 0,1,0 \rangle\\')
                agn.append(r'\vec{k} = & \langle 0,0,1 \rangle\\')
                agn.append(r'\vec{v} = &  \langle a\vec{i},b\vec{j},c\vec{k} \rangle\\')
                agn.append(r'hypotenuse = \rvert\rvert v\rvert\rvert = & \sqrt{a^2+b^2+c^2}\\')
                agn.append(r'cos\alpha = & \frac{a}{\sqrt{a^2+b^2+c^2}}\\')
                agn.append(r'cos\beta = & \frac{b}{\sqrt{a^2+b^2+c^2}}\\')
                agn.append(r'cos\gamma = & \frac{c}{\sqrt{a^2+b^2+c^2}}\\')
                agn.append(r'cos^2\alpha + cos^2\beta + cos^2\gamma = & \frac{a^2}{a^2+b^2+c^2} + \
                           \frac{b^2}{a^2+b^2+c^2} + \frac{c^2}{a^2+b^2+c^2}\\')
                agn.append(r'cos^2\alpha + cos^2\beta + cos^2\gamma = & 1\\')
        with doc.create(Subsection('43', numbering=False)):
            with doc.create(Figure(position='h!')) as triangle_pic:
                image_filename = os.path.join(os.path.dirname(__file__), 'tri1.jpg')
                triangle_pic.add_image(image_filename, width='255px')

if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    fill_document(doc)

    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Homework 1'))
    doc.preamble.append(Command('author', 'Ann Kidder'))
    doc.preamble.append(Command('date', 'September 4, 2017'))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('basic_maketitle', clean_tex=False)



    doc.generate_pdf('basic_maketitle2', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax