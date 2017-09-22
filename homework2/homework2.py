'''
PDF homework assignment for week 2 
generated using pylatex
https://jeltef.github.io/PyLaTeX/
'''

from pylatex import Document, Section, Subsection, Itemize, Enumerate, Description, \
    Subsection, Command, NoEscape, Math, Alignat, Figure
from pylatex.utils import italic, NoEscape
import os


def fill_document(doc):
    with doc.create(Section('Basic Concept Problems', numbering=True)):
        # Question 1: prove the pythagorean theorem
        with doc.create(Figure(position='h!')) as pythagorean_pic:
            image_filename = os.path.join(os.path.dirname(__file__), 'pythagorean.jpg')
            pythagorean_pic.add_image(image_filename, width='350px')
        
        # Question 2: prove the law of cosines
        with doc.create(Figure(position='h!')) as tri_pic:
            image_filename = os.path.join(os.path.dirname(__file__), 'triangle.jpg')
            tri_pic.add_image(image_filename, width='100px')
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'&\textnormal{Given a triangle with sides A, B, and C }')
                agn.append(r'\textnormal{with height h and an angle } \theta\\')
                agn.append(r'& \textnormal{we know that the left triangle will}')
                agn.append(r'\textnormal{ have the property } m^2+h^2=B^2\\')
                agn.append(r'&\textnormal{and the right triangle will have the property }')
                agn.append(r' h^2 + n^2 = C^2\\ &\textnormal{by the pythagorean theorem.}')
                agn.append(r'\textnormal{ Therefore:}\\')
                agn.append(r'&n = A - m\\')
                agn.append(r'&\textnormal{and } h^2 + (A-m)^2 = C^2\\')
                agn.append(r'&B^2-m^2+A^2-2Am+m^2 = C^2\\')
                agn.append(r'&\textnormal{Furthermore, we know } cos\theta = \frac{m}{B}\\')
                agn.append(r'&\textnormal{Therefore:}\\')
                agn.append(r'&B^2+A^2 -2ABcos\theta = C^2')
    
    with doc.create(Section('9.3', numbering=False)):
        with doc.create(Subsection('20', numbering=False)):
            with doc.create(Figure(position='h!')) as tri2_pic:
                image_filename = os.path.join(os.path.dirname(__file__), 'tri2.jpg')
                tri2_pic.add_image(image_filename, width='150px')
                with doc.create(Alignat(numbering=False, escape=False)) as agn:
                    agn.append(r'\vec{u} &= <-2,3,2>\\')
                    agn.append(r'\vec{v} &= <3,-2,-4>\\')
                    agn.append(r'\vec{w} &= <1,1,-2>\\')
                    agn.append(r'\textnormal{The angle at D:} \\')
                    agn.append(r'<-2,3,2>\cdot<1,1,-2> &=\|<-2,3,2>\| \|<1,1,-2>\|cosd\\')
                    agn.append(r'-3 &= \sqrt{17}\sqrt{6}cosd\\')
                    agn.append(r'cos^-1(\frac{-3}{\sqrt{102}}) &= d\\')
                    agn.append(r'd & \approx{107.28}^\circ\\')

                    agn.append(r'\textnormal{The angle at E:} \\')
                    agn.append(r'-(<-2,3,2>)\cdot<3,-2,-4> &=\|<-2,3,2>\| \|<3,-2,-4>\|cose\\')
                    agn.append(r'20 &= \sqrt{17}\sqrt{29}cose\\')
                    agn.append(r'cos^-1(\frac{20}{\sqrt{493}}) &= e\\')
                    agn.append(r'e & \approx{25.74}^\circ\\')

                    agn.append(r'\textnormal{The angle at F:} \\')
                    agn.append(r'-(<1,1,-2>)\cdot-(<3,-2,-4>) &=\|<1,1,-2>\| \|<3,-2,-4>\|cosf\\')
                    agn.append(r'9 &= \sqrt{6}\sqrt{29}cosf\\')
                    agn.append(r'cos^-1(\frac{9}{\sqrt{174}}) &= f\\')
                    agn.append(r'f & \approx{46.98}^\circ\\')
        
        # projections
        with doc.create(Subsection('30', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\|a\| &= \sqrt{5}\\')
                agn.append(r'comp_a b &= \frac{a \cdot b}{\|a\|} = \frac{-4+2}{\sqrt{5}} = \frac{-2}{\sqrt{5}}\\')
                agn.append(r'\textnormal{The vector projection is:}\\')
                agn.append(r'proj_a b &= \frac{-2}{\sqrt{5}}\frac{<1,2>}{\sqrt{5}} = \frac{-2}{5} <1,2>\\')
                agn.append(r'proj_a b &= <\frac{-2}{5}, \frac{-4}{5}>')
        with doc.create(Subsection('31', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'a = <2,-1,4> & \textnormal{ and } b = <0,1,\frac{1}{2}>\\')
                agn.append(r'\| a \| &= \sqrt{4+1+16} = \sqrt{21}\\')
                agn.append(r'comp_a b &= \frac{a \cdot b}{\sqrt{21}} = \frac{1}{\sqrt{21}}\\')
                agn.append(r'\textnormal{The vector projection is:}\\')
                agn.append(r'proj_a b &= \frac{1}{\sqrt{21}}\frac{<2,-1,4>}{\sqrt{21}} = \frac{1}{21}<2,-1,4>\\')
                agn.append(r'proj_a b &= <\frac{2}{21},\frac{-1}{21},\frac{4}{21}>\\')
        with doc.create(Subsection('43', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\intertext{Let all sides of the cube be length = 1, and let the edges lie along the x, y, z axis}\\')
                agn.append(r'\text{The diagonal vector, }\vec{d}\text{ from (0,0,0) to (1,1,1) = <1,1,1>}\\')
                agn.append(r'\text{Let the unit vector } \vec{k} = <0,0,1> \text{be a side.}\\')
                agn.append(r'\text{The angle between } \vec{d} \text{ and } \vec{k} \text{ is:}\\')
                agn.append(r'cos\theta &= \frac{<0,0,1> \cdot <1,1,1>}{\|u\|\|v\|}\\')
                agn.append(r'&= \frac{0+0+1}{\sqrt{1}\sqrt{3}}\\')
                agn.append(r'&= \frac{1}{\sqrt{3}} \\')
                agn.append(r'\theta &= cos^-1 \frac{1}{\sqrt{3}}\\')
                agn.append(r'&= 54.74^\circ')
        with doc.create(Subsection('46', numbering=False)):
            with doc.create(Figure(position='h!')) as ang_pic:
                image_filename = os.path.join(os.path.dirname(__file__), 'ang1.jpg')
                ang_pic.add_image(image_filename, width='150px')
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'cos\alpha &= \frac{a \cdot c}{\|a\| \|c\|}\\')
                agn.append(r'&= \frac{a \cdot (\|a\|b+\|b\|a))}{\|a\| \|c\|}\\')
                agn.append(r'&= \frac{a \cdot \|a\|a \cdot b + \|b\|a \cdot a}{\|a\| \|c\|}\\')
                agn.append(r'&= \frac{\|a\|a \cdot b + \|b\| \|a\|^2}{\|a\| \|c\|}\\')
                agn.append(r'&= \frac{a \cdot b + \|b\| \|a\|}{\|c\|}\\')
                agn.append(r'cos\beta &= \frac{b \cdot c}{\|b\| \|c\|}\\')
                agn.append(r'&= \frac{b \cdot (\|a\|b+\|b\|a))}{\|b\| \|c\|}\\')
                agn.append(r'&= \frac{\|a\| b \cdot b + \|b\|a \cdot b}{\|b\| \|c\|}\\')
                agn.append(r'&= \frac{\|a\| \|b\|^2 + \|b\| a \cdot b}{\|b\| \|c\|}\\')
                agn.append(r'&= \frac{\|a\| \|b\| + a \cdot b}{\|c\|}\\')
                agn.append(r'\textnormal{Now we can see that } cos \alpha = cos \beta\\')
                agn.append(r' \frac{a \cdot b + \|b\| \|a\|}{\|c\|} &= \frac{\|a\| \|b\| + a \cdot b}{\|c\|}\\')

    with doc.create(Section('9.4', numbering=False)):
        with doc.create(Subsection('20', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\intertext{The cross product is orthogonol to both i+j+k and 2i+k:}\\')
                agn.append(r'i+j+k = <1,1,1> & \textnormal{ and } 2i+k = <2,0,1>\\')
                agn.append(r'<1,1,1>\times <2,0,1> &= (1-0) \vec{i}+(2-1) \vec{j}+(0-2) \vec{k}\\')
                agn.append(r'<1,1,1>\times <2,0,1> &= <1,1,-2>\\')
                agn.append(r'\intertext{Divide by the magnitude to find the unit vector:}\\')
                agn.append(r'\textnormal{unit vector } &= \frac{<1,1,-2>}{\sqrt{1+1+4}}\\')
                agn.append(r'&= <\frac{1}{\sqrt{6}},\frac{1}{\sqrt{6}},\frac{-2}{\sqrt{6}}>\\')
                agn.append(r'\intertext{The second unit vector would be the negative of the first:}\\')
                agn.append(r'&= <\frac{-1}{\sqrt{6}},\frac{-1}{\sqrt{6}},\frac{2}{\sqrt{6}}>\\')

        with doc.create(Subsection('22', numbering=False)):
            with doc.create(Figure(position='h!')) as para_pic:
                image_filename = os.path.join(os.path.dirname(__file__), 'para1.jpg')
                para_pic.add_image(image_filename, width='150px')
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\vec{u} = <2,5,0> \textnormal{ and } \vec{v} = <0,1,3>\\')
                agn.append(r'A &= \|<2,5,0> \times <0,1,3>\| \\')
                agn.append(r'A &= \|<-15,6,-2>\| \\')
                agn.append(r'A &= \sqrt{265}')

        with doc.create(Subsection('24', numbering=False)):
            with doc.create(Subsection('a)', numbering=False)):
                with doc.create(Alignat(numbering=False, escape=False)) as agn:
                    agn.append(r'\vec{PQ} = <1,2,1> \textnormal{ and } \vec{PR} = <5,0,-2>\\')
                    agn.append(r'\textnormal{The vector orthogonol to the plane = } \vec{PQ} \times \vec{PR}\\')
                    agn.append(r'\vec{PQ} \times \vec{PR} = <-5,7,-10>\\')
            with doc.create(Subsection('b)', numbering=False)):
                with doc.create(Alignat(numbering=False, escape=False)) as agn:
                    agn.append(r'A &= \frac{\|<-5,7,-10>\|}{2}\\')
                    agn.append(r'A &= \frac{\sqrt{174}}{2} \approx 6.6')

        with doc.create(Subsection('33', numbering=False)):
            with doc.create(Subsection('a)', numbering=False)):
                with doc.create(Alignat(numbering=False, escape=False)) as agn:
                    agn.append(r'd &= \|b\|sin\theta\\')
                    agn.append(r'&=\frac{\|a\|}{\|a\|}\|b\|sin\theta\\')
                    agn.append(r'&= \frac{\|a\|\|b\|sin\theta}{\|a\|}\\')
                    agn.append(r'&= \frac{\|a \times b\|}{\|a\|}\\')
            with doc.create(Subsection('b)', numbering=False)):
                with doc.create(Alignat(numbering=False, escape=False)) as agn:
                    agn.append(r'\vec{a} = <-1,-2,-1> \textnormal{ and } \vec{b} = <1, -5, -7>\\')
                    agn.append(r'd &= \frac{\|<-1,-2,-1> \times <1, -5, -7>\|}{\sqrt{1+4+1}}\\')
                    agn.append(r'&= \frac{\|<9,-15,7>\|}{\sqrt{6}}\\')
                    agn.append(r'&= \frac{\sqrt{355}}{\sqrt{6}}\\')
                    agn.append(r'd & \approx 7.69\\')

    with doc.create(Section('9.5', numbering=False)):
        with doc.create(Subsection('2', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\textnormal{vector equation } &= <6,-5,2> + t<1,3,\frac{-2}{3}>\\')
                agn.append(r'&= <6+t, -5+3t, 2+\frac{-2}{3}t>\\')
                agn.append(r'\textnormal{The parametric equations are:}\\')
                agn.append(r'x(t) &= 6+t\\')
                agn.append(r'y(t) &= -5+3t\\')
                agn.append(r'z(t) &= 2+\frac{-2}{3}t\\')
        with doc.create(Subsection('5', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'x(t) &= 1+t\\')
                agn.append(r'y(t) &= 3t\\')
                agn.append(r'z(t) &= 6+t\\')
        with doc.create(Subsection('10', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\vec{n_1} = <1,2,3> \textnormal{ and } \vec{n_2} = <1,-1,1>\\')
                agn.append(r'<1,2,3> \times <1,-1,1> \textnormal{is a line parallel to the line of intersection.}\\')
                agn.append(r'<1,2,3> \times <1,-1,1> = <5,2,-3>\\')
                agn.append(r'\textnormal{Plug in z=0 to solve x, y and find a point on the line of intersection}\\')
                agn.append(r'x+2y=1 \textnormal{ and } x-y &=1\\')
                agn.append(r'\textnormal{This gives us } 3y &= 0 \\')
                agn.append(r'\textnormal{Therefore (1,0,0) lies on the line of intersection and the symmetric equations are:}\\')
                agn.append(r'\frac{x-1}{5} &= \frac{y}{2} = \frac{-z}{3}\\')
                agn.append(r'\textnormal{And the parametric equations are:}\\')
                agn.append(r'x(t) &= 1+5t\\')
                agn.append(r'y(t) &= 2t\\')
                agn.append(r'z(t) &= -3t\\')
        with doc.create(Subsection('18', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\textnormal{Check ratio of coefficients to test if parallel:}\\')
                agn.append(r'\frac{1}{-1} = \frac{3}{1} = \frac{-1}{3}\\')
                agn.append(r'-1 \neq 3 \neq -3 \textnormal{therefore the lines are NOT parallel}\\')
                agn.append(r'\textnormal{Solve system of equations to test if intersecting:}\\')
                agn.append(r'1 +2t &= -1+s\\')
                agn.append(r'3t &= 4+s\\')
                agn.append(r'2-t &= 1+3s\\')
                agn.append(r'\textnormal{Solve the first equation for t:}\\')
                agn.append(r'2t &=-2+s\\')
                agn.append(r't &= -1 + \frac{s}{2}\\')
                agn.append(r'\textnormal{Plug into the second equation:}\\')
                agn.append(r'3(-1+\frac{s}{2}) = 4+s\\')
                agn.append(r'-3+\frac{3s}{2} = 4+s\\')
                agn.append(r'\frac{s}{2} = 7\\')
                agn.append(r's = 14\\')
                agn.append(r'\textnormal{Plug s=14 this into the equation for t:}\\')
                agn.append(r't=-1+\frac{14}{2} = -6\\')
                agn.append(r'\textnormal{Plug s=14 and t=-6 into the third equation:}\\')
                agn.append(r'2+-6 = 1+3(14)\\')
                agn.append(r'-4 \neq 43 \textnormal{therefore the lines do not intersect.}\\')
                agn.append(r'\textnormal{Since the lines are not parallel and do not intersect, they must be skew.}\\')
        with doc.create(Subsection('25', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'P(0,1,1) \textnormal{ and }Q(1,0,1) \textnormal{ and }R(1,1,0)\\')
                agn.append(r'\vec{PQ} = <1-0,0-1,1-1> &= <1,-1,0>\\')
                agn.append(r'\vec{PR} = <1-0,1-1,0-1> &= <1,0,-1>\\')
                agn.append(r'\textnormal{Take the cross product to get the coefficients of the plane equation:}\\')
                agn.append(r'<1,-1,0> \times <1,0,-1> = <1,1,1> \\')
                agn.append(r'\textnormal{Use P as the point for the equation of the plane:}\\')
                agn.append(r'1(x-0)+1(y-1)+1(z-1) &= 0\\')
                agn.append(r'x+y+z &=2\\')
        with doc.create(Subsection('27', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\textnormal{The points P(6,0,-2) and Q(4,3,7) are on the plane.}\\')
                agn.append(r'\textnormal{Set t=1 to get a third point on the plane, R(2,8,11)}\\')
                agn.append(r'\vec{PQ} = <4-6,3-0,7-(-2)> = <-2,3,9>\\')
                agn.append(r'\vec{PR} = <2-6,8-0,11-(-2)> = <-4,8,13>\\')
                agn.append(r'\textnormal{Take the cross product to get the coefficients of the plane equation:}\\')
                agn.append(r'<-2,3,9> \times <-4,8,13> = <-33,-10,-4>\\')
                agn.append(r'\textnormal{Use P as the point for the equation of the plane:}\\')
                agn.append(r'-33(x-6)+-10(y-0)+-4(z+2) &= 0\\')
                agn.append(r'-33x+198-10y-4z-8 &= 0\\')
                agn.append(r'-33x-10y-4z &= -190')
        with doc.create(Subsection('32', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\textnormal{Let Q be the plane that we are looking for.}\\')
                agn.append(r'\textnormal{Set z=0 to get a point on the line of intersection:}\\')
                agn.append(r'(1,3,0)\\')
                agn.append(r'\textnormal{To get a normal vector for Q, take the cross product of two vectors parallel to Q.}\\')
                agn.append(r'\textnormal{The normal vector of the plane perpendicular to Q is parallel to Q:}\\')
                agn.append(r'<1,1,-2>\\')
                agn.append(r'\textnormal{Get a second vector parallel to Q by taking the cross product of the normal vectors }\\')
                agn.append(r'\textnormal{of the two planes that form the line of intersection that Q passes through.}\\')
                agn.append(r'<1,0,-1> \times <0,1,2> &= <1,-2,1>\\')
                agn.append(r'\textnormal{Now take the cross product of these two vectors:}\\')
                agn.append(r'<1,1,-2> \times <1,-2,1> &= <-3,-3,-3>\\')
                agn.append(r'\textnormal{Plug these into the plane equation:}\\')
                agn.append(r'-3(x-1)-3(y-3)-3(z-0) &= 0\\')
                agn.append(r'-3x+3-3y+9-3z &= 0\\')
                agn.append(r'-3x-3y-3z &= -12\\')
                agn.append(r'-3(x+y+z) &= -12\\')
                agn.append(r'x+y+z &= 4\\')
        with doc.create(Subsection('56', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'd &= \frac{|1(6)+(-2)(0)+(-4)(-2) + (-8)|}{\sqrt{1^2+(-2)^2+(-4)^2}}\\')
                agn.append(r'&= \frac{|6+8-8|}{\sqrt{21}}\\')
                agn.append(r'&= \frac{6}{\sqrt{21}}\\ ')
                agn.append(r'd &\approx 1.31\\')
        with doc.create(Subsection('58', numbering=False)):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\textnormal{To find the distance we need a point on one plane.}\\')
                agn.append(r'\textnormal{Plug in z=0 to the first equation.}\\')
                agn.append(r'0 &= 4y - 2x\\')
                agn.append(r'y &= \frac{1}{2}x\\')
                agn.append(r'\textnormal{Therefore the point (2,1,0) is on the first plane.}\\')
                agn.append(r'\textnormal{Now we can use the distance formula.}\\')
                agn.append(r'd &= \frac{|3(2) + -6(1) + 9(0) + -1|}{\sqrt{3^2+(-6)^2+9^2}}\\')
                agn.append(r'&= \frac{|6-6-1|}{\sqrt{126}}\\')
                agn.append(r'&= \frac{1}{\sqrt{126}}\\')
                agn.append(r'd & \approx .09\\')



if __name__ == '__main__':
    # Basic document
    doc = Document()

    doc.preamble.append(Command('title', 'Homework 2'))
    doc.preamble.append(Command('author', 'Ann Kidder'))
    doc.preamble.append(Command('date', 'September 16, 2017'))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('KidderAnnHW2', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax