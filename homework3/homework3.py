'''
PDF homework assignment for week 3
generated using pylatex
https://jeltef.github.io/PyLaTeX/
'''

from pylatex import Document, Section, Subsection, Itemize, Enumerate, Description, \
    Subsection, Command, NoEscape, Math, Alignat, Figure
from pylatex.utils import italic, NoEscape
import os


def fill_document(doc):
    with doc.create(Section('Chapter 9', numbering=True)):
        with doc.create(Subsection('True/False', numbering=True)):
            with doc.create(Enumerate()) as enum:
                #1
                enum.add_item(NoEscape('True. $u\cdot v$ results in a scalar so the order of multiplication does not matter.'))
                #2
                enum.add_item(NoEscape('False. $<1,2,3>\\times <4,5,6> = <-3,6,-3>$ However, $<4,5,6> \\times <1,2,3> = <3,-6,3>$ \
                    Thus $u \\times v = -v \\times u$'))
                #3
                enum.add_item('True. Though the signs are opposite for $u \\times v$ and $v \\times u$, once the components are \
                    squared they will be the same so the magnitudes are equal.')
                #4
                enum.add_item(NoEscape('True.  $u \\cdot v$ will be a scalar so it does not matter what order $k$ and u and v are multipled.'))
                #5
                enum.add_item(NoEscape('True.  It does not matter what order the scalar is multiplied with the vector.'))
                #6
                enum.add_item(NoEscape('True. $|u \\times w|$ is the area of a parallelogram with sides u and w.  \
                    If you connect this to the parallelogram with sides v and w by the shared side w, you will get a total area \
                    of u+v by w, which is the same as $(u+v) \\times w$'))
                #7
                enum.add_item(NoEscape('True.  The final result is a scalar, so it does not matter what order the components are multipled by the cross and dot product.'))
                #8
                enum.add_item(NoEscape('False. The cross product of two vectors is another vector so order of operations matters.  \
                    $u \\times (v \\times w) = v(u \\times w) - w(u \\times v)$'))
                #9
                enum.add_item(NoEscape('True.  Because this can be rewritten as $v \\cdot (u \\times u)$ and $u \\times u = 0$ this is true.'))
                #10
                enum.add_item(NoEscape('True.  $(u+v)\\times v = u \\times v + v \\times v$ and $v\\times v = 0$ so this is true.'))
                #11
                enum.add_item(NoEscape('True. The cross product of two unit vectors will have a magnitude of one, so it will also be a unit vector.'))
                #12
                enum.add_item(NoEscape('False.  It represents a line only if one and only one coefficient is 0.'))
                #13
                enum.add_item(NoEscape('True.  Because $z^2=0$ the set of all points described is a circle in the xy-plane'))
                #14
                enum.add_item(NoEscape('False.  $u \\cdot v = u_1 v_1 + u_2 v_2$, which is a scalar, not a vector.'))
                #15
                enum.add_item(NoEscape('False.  $<1,1,0> \\cdot <-1,1,0> = 0$'))
                #16
                enum.add_item(NoEscape('False.  If u and v are non-zero, parallel vectors then $u \\times v = 0$  Example, $<1,1,0> \\times <2,2,0> = <0,0,0>$'))
                #17
                enum.add_item(NoEscape('True.  If $u \\cdot v = 0$ that means either u or v is zero.'))
                #18
                enum.add_item(NoEscape('True. $|u \\cdot v| = \\sqrt{u_1 v_1^2 + u_2 v_2^2 + u_3 v_3^2}$ \
                    and $||u|| ||v|| = \\sqrt{u_1^2+u_2^2+u_3^2}\\sqrt{v_1^2+v_2^2+v_3^2}$.  If you square \
                    both sides and multiply out the right, you see that the highest multiple of the left is 2 while the right is 4'))


if __name__ == '__main__':
    # Basic document
    doc = Document()

    doc.preamble.append(Command('title', 'Homework 3'))
    doc.preamble.append(Command('author', 'Ann Kidder'))
    doc.preamble.append(Command('date', 'September 22, 2017'))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('KidderAnnHW3', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax