from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
com=['line','scale','move','rotate','save']
com_2=['ident','apply','display','quit']
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,"r")
    lines = f.read().split('\n')
    i=0
    while(i<len(lines)-1):
        print(i)
        print(points)
        if lines[i] in com:
            command="make_"+lines[i]
            temp=i+1
            temp=lines[temp]
            if lines[i] == "rotate":
                command=command[:-3]
                temp=temp.split()
                command=command+temp[0].upper()
                mat=eval(command)(eval(temp[1]))
                matrix_mult(mat,transform)
            elif lines[i] == "line":
                temp= [int(j) for j in temp.split()]
                add_edge(points,*temp)
            elif lines[i] == "save":
                clear_screen(screen)
                draw_lines(points,screen,color)
                save_extension(screen,temp)
            else:
                temp= [int(j) for j in temp.split()]
                mat=eval(command)(*temp)
                matrix_mult(mat,transform)
            i+=2
        elif lines[i] in com_2:
            if lines[i] =="ident":
                transform=new_matrix()
                ident(transform)
            elif lines[i] == "apply":
                matrix_mult(transform,points)
            elif lines[i] == "display":
                clear_screen(screen)
                draw_lines(points,screen,color)
                display(screen)
            elif lines[i] == "quit":
                return
            i+=1
            
