
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
import random
import copy

# Code for the move in which middle part is stable and right side goes up and left side goes down.
    
def rightUp_leftDown(gearball):
    for k in range(1):
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        h=[]


        for i in range(26):
            a.append(gearball[i][10])        
            b.append(gearball[i][12])
            c.append(gearball[i][13])
            d.append(gearball[i][14])
            e.append(gearball[i][8])
            f.append(gearball[i][7])
            h.append(gearball[i][6])


        gearball[0][14]=d[6]
        gearball[3][14]=d[10]
        gearball[6][14]=d[14]
        gearball[10][14]=d[17]
        gearball[14][14]=d[20]
        gearball[17][14]=d[23]
        gearball[20][14]=d[0]
        gearball[23][14]=d[3]

        gearball[1][13]=c[7]
        gearball[2][13]=c[9]
        gearball[3][13]=c[10]
        gearball[4][13]=c[11]
        gearball[5][13]=c[13]

        gearball[7][13]=c[15]
        gearball[9][13]=c[16]
        gearball[10][13]=c[17]
        gearball[11][13]=c[18]
        gearball[13][13]=c[19]

        gearball[15][13]=c[21]
        gearball[16][13]=c[22]
        gearball[17][13]=c[23]
        gearball[18][13]=c[24]
        gearball[19][13]=c[25]

        gearball[21][13]=c[1]
        gearball[22][13]=c[2]
        gearball[23][13]=c[3]
        gearball[24][13]=c[4]
        gearball[25][13]=c[5]

        gearball[3][12]=b[10]
        gearball[10][12]=b[17]
        gearball[17][12]=b[23]
        gearball[23][12]=b[3]


        gearball[0][6]=h[20]
        gearball[3][6]=h[23]
        gearball[6][6]=h[0]
        gearball[10][6]=h[3]
        gearball[14][6]=h[6]
        gearball[17][6]=h[10]
        gearball[20][6]=h[14]
        gearball[23][6]=h[17]

        gearball[1][7]=f[21]
        gearball[2][7]=f[22]
        gearball[3][7]=f[23]
        gearball[4][7]=f[24]
        gearball[5][7]=f[25]

        gearball[7][7]=f[1]
        gearball[9][7]=f[2]
        gearball[10][7]=f[3]
        gearball[11][7]=f[4]
        gearball[13][7]=f[5]

        gearball[15][7]=f[7]
        gearball[16][7]=f[9]
        gearball[17][7]=f[10]
        gearball[18][7]=f[11]
        gearball[19][7]=f[13]

        gearball[21][7]=f[15]
        gearball[22][7]=f[16]
        gearball[23][7]=f[17]
        gearball[24][7]=f[18]
        gearball[25][7]=f[19]

        gearball[3][8]=e[23]
        gearball[10][8]=e[3]
        gearball[17][8]=e[10]
        gearball[23][8]=e[17]

        if gearball[0][10]=='=':
            gearball[0][10]="\\"
            gearball[6][10]="\\"
            gearball[14][10]="\\"
            gearball[20][10]="\\"

            gearball[5][11]=gearball[5][10]
            gearball[13][11]=gearball[13][10]
            gearball[19][11]=gearball[19][10]
            gearball[25][11]=gearball[25][10]

            gearball[1][9]=gearball[1][10]
            gearball[7][9]=gearball[7][10]
            gearball[15][9]=gearball[15][10]
            gearball[21][9]=gearball[21][10]

            gearball[5][10]=' '
            gearball[13][10]=' '
            gearball[19][10]=' '
            gearball[25][10]=' '

            gearball[1][10]=' '
            gearball[7][10]=' '
            gearball[15][10]=' '
            gearball[21][10]=' '

        elif gearball[0][10]=="\\":
            gearball[0][10]='/'
            gearball[6][10]='/'
            gearball[14][10]='/'
            gearball[20][10]='/'

            gearball[5][9]=gearball[7][9]
            gearball[13][9]=gearball[15][9]
            gearball[19][9]=gearball[21][9]
            gearball[25][9]=gearball[1][9]

            gearball[1][11]= gearball[25][11]
            gearball[7][11]=gearball[5][11]
            gearball[15][11]=gearball[13][11]
            gearball[21][11]=gearball[19][11]

            gearball[5][11]=' '
            gearball[13][11]=' '
            gearball[19][11]=' '
            gearball[25][11]=' '

            gearball[1][9]=' '
            gearball[7][9]=' '
            gearball[15][9]=' '
            gearball[21][9]=' '

        elif gearball[0][10]=='/':
            gearball[0][10]='='
            gearball[6][10]='='
            gearball[14][10]='='
            gearball[20][10]='='

            gearball[5][10]=gearball[5][9]
            gearball[13][10]=gearball[13][9]
            gearball[19][10]=gearball[19][9]
            gearball[25][10]=gearball[25][9]

            gearball[1][10]= gearball[1][11]
            gearball[7][10]=gearball[7][11]
            gearball[15][10]=gearball[15][11]
            gearball[21][10]=gearball[21][11]

            gearball[5][9]=' '
            gearball[13][9]=' '
            gearball[19][9]=' '
            gearball[25][9]=' '

            gearball[1][11]=' '
            gearball[7][11]=' '
            gearball[15][11]=' '
            gearball[21][11]=' '


    
        a=gearball[7][17]
        b=gearball[10][19]
        c=gearball[13][17]
        d=gearball[10][15]
        
        gearball[7][17]=d
        gearball[10][19]=a
        gearball[13][17]=b
        gearball[10][15]=c

        a=gearball[7][16]
        b=gearball[9][19]
        c=gearball[13][18]
        d=gearball[11][15]
        
        gearball[7][16]=d
        gearball[9][19]=a
        gearball[13][18]=b
        gearball[11][15]=c
        
        a=gearball[7][18]
        b=gearball[11][19]
        c=gearball[13][16]
        d=gearball[9][15]
        
        gearball[7][18]=d
        gearball[11][19]=a
        gearball[13][16]=b
        gearball[9][15]=c

#         a=gearball[6][17]
#         b=gearball[10][20]
#         c=gearball[14][17]
#         d=gearball[10][14]
        
#         gearball[6][17]=d
#         gearball[10][20]=a
#         gearball[14][17]=b
#         gearball[10][14]=c


        
        
        a=gearball[7][15]
        b=gearball[7][19]
        c=gearball[13][19]
        d=gearball[13][15]
        
        gearball[7][15]=d
        gearball[7][19]=a
        gearball[13][19]=b
        gearball[13][15]=c
        
        a=gearball[8][17]
        b=gearball[10][18]
        c=gearball[12][17]
        d=gearball[10][16]
        
        gearball[8][17]=d
        gearball[10][18]=a
        gearball[12][17]=b
        gearball[10][16]=c


        a=gearball[7][3]
        b=gearball[10][5]
        c=gearball[13][3]
        d=gearball[10][1]
        
        gearball[7][3]=d
        gearball[10][5]=a
        gearball[13][3]=b
        gearball[10][1]=c

        a=gearball[7][2]
        b=gearball[9][5]
        c=gearball[13][4]
        d=gearball[11][1]
        
        gearball[7][2]=d
        gearball[9][5]=a
        gearball[13][4]=b
        gearball[11][1]=c
        
        a=gearball[7][4]
        b=gearball[11][5]
        c=gearball[13][2]
        d=gearball[9][1]
        
        gearball[7][4]=d
        gearball[11][5]=a
        gearball[13][2]=b
        gearball[9][1]=c

#         a=gearball[6][3]
#         b=gearball[10][6]
#         c=gearball[14][3]
#         d=gearball[10][0]
        
#         gearball[6][3]=d
#         gearball[10][6]=a
#         gearball[14][3]=b
#         gearball[10][0]=c
        
        
    
        a=gearball[7][1]
        b=gearball[7][5]
        c=gearball[13][5]
        d=gearball[13][1]
        
        gearball[7][1]=d
        gearball[7][5]=a
        gearball[13][5]=b
        gearball[13][1]=c
        
        a=gearball[8][3]
        b=gearball[10][4]
        c=gearball[12][3]
        d=gearball[10][2]
        
        gearball[8][3]=d
        gearball[10][4]=a
        gearball[12][3]=b
        gearball[10][2]=c
        
        gearball[7][21]=gearball[25][13]
        gearball[7][22]=gearball[25][11]
        gearball[7][23]=gearball[25][10]
        gearball[7][24]=gearball[25][9]
        gearball[7][25]=gearball[25][7]
        gearball[9][21]=gearball[24][13]
        gearball[8][23]=gearball[24][10]
        gearball[9][25]=gearball[24][7]
        gearball[10][21]=gearball[23][13]
        gearball[10][22]=gearball[23][12]
        gearball[10][23]=gearball[23][10]
        gearball[10][24]=gearball[23][8]
        gearball[10][25]=gearball[23][7]
        gearball[11][21]=gearball[22][13]
        gearball[12][23]=gearball[22][10]
        gearball[11][25]=gearball[22][7]
        gearball[13][21]=gearball[21][13]
        gearball[13][21]=gearball[21][13]
        gearball[13][22]=gearball[21][11]
        gearball[13][23]=gearball[21][10]
        gearball[13][24]=gearball[21][9]
        gearball[13][25]=gearball[21][7]

        gearball[6][0]=gearball[0][6]
        gearball[14][0]=gearball[20][6]
        gearball[6][20]=gearball[0][14]
        gearball[14][20]=gearball[20][14]
        gearball[10][0]=gearball[23][6]
        gearball[10][20]=gearball[23][14]
        gearball[6][23]=gearball[0][10]
        gearball[14][23]=gearball[20][10]
        
        if gearball[3][6]=="\\":
            gearball[6][3]='/'
        elif gearball[3][6]=='/':
            gearball[6][3]="\\"
        else:
            gearball[6][3]=gearball[3][6]
            
        if gearball[17][6]=="\\":
            gearball[14][3]='/'
        elif gearball[17][6]=='/':
            gearball[14][3]="\\"
        else:
            gearball[14][3]=gearball[17][6]
                    
        if gearball[3][14]=="\\":
            gearball[6][17]='/'
        elif gearball[3][14]=='/':
            gearball[6][17]="\\"
        else:
            gearball[6][17]=gearball[3][14]

        if gearball[17][14]=="\\":
            gearball[14][17]='/'
        elif gearball[17][14]=='/':
            gearball[14][17]="\\"
        else:
            gearball[14][17]=gearball[17][14]

        
        return gearball

# Code for the move in which middle part is stable and right side goes down and left side goes up.
    
def rightDown_leftUp(gearball):
    for k in range(1):
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        h=[]


        for i in range(26):
            a.append(gearball[i][10])        
            b.append(gearball[i][12])
            c.append(gearball[i][13])
            d.append(gearball[i][14])
            e.append(gearball[i][8])
            f.append(gearball[i][7])
            h.append(gearball[i][6])


        gearball[0][14]=d[20]
        gearball[3][14]=d[23]
        gearball[6][14]=d[0]
        gearball[10][14]=d[3]
        gearball[14][14]=d[6]
        gearball[17][14]=d[10]
        gearball[20][14]=d[14]
        gearball[23][14]=d[17]

        gearball[1][13]=c[21]
        gearball[2][13]=c[22]
        gearball[3][13]=c[23]
        gearball[4][13]=c[24]
        gearball[5][13]=c[25]

        gearball[7][13]=c[1]
        gearball[9][13]=c[2]
        gearball[10][13]=c[3]
        gearball[11][13]=c[4]
        gearball[13][13]=c[5]

        gearball[15][13]=c[7]
        gearball[16][13]=c[9]
        gearball[17][13]=c[10]
        gearball[18][13]=c[11]
        gearball[19][13]=c[13]

        gearball[21][13]=c[15]
        gearball[22][13]=c[16]
        gearball[23][13]=c[17]
        gearball[24][13]=c[18]
        gearball[25][13]=c[19]

        gearball[3][12]=b[23]
        gearball[10][12]=b[3]
        gearball[17][12]=b[10]
        gearball[23][12]=b[17]


        gearball[0][6]=h[6]
        gearball[3][6]=h[10]
        gearball[6][6]=h[14]
        gearball[10][6]=h[17]
        gearball[14][6]=h[20]
        gearball[17][6]=h[23]
        gearball[20][6]=h[0]
        gearball[23][6]=h[3]

        gearball[1][7]=f[7]
        gearball[2][7]=f[9]
        gearball[3][7]=f[10]
        gearball[4][7]=f[11]
        gearball[5][7]=f[13]

        gearball[7][7]=f[15]
        gearball[9][7]=f[16]
        gearball[10][7]=f[17]
        gearball[11][7]=f[18]
        gearball[13][7]=f[19]

        gearball[15][7]=f[21]
        gearball[16][7]=f[22]
        gearball[17][7]=f[23]
        gearball[18][7]=f[24]
        gearball[19][7]=f[25]

        gearball[21][7]=f[1]
        gearball[22][7]=f[2]
        gearball[23][7]=f[3]
        gearball[24][7]=f[4]
        gearball[25][7]=f[5]

        gearball[3][8]=e[10]
        gearball[10][8]=e[17]
        gearball[17][8]=e[23]
        gearball[23][8]=e[3]

        if gearball[0][10]=='=':
            gearball[0][10]='/'
            gearball[6][10]='/'
            gearball[14][10]='/'
            gearball[20][10]='/'

            gearball[5][9]=gearball[5][10]
            gearball[13][9]=gearball[13][10]
            gearball[19][9]=gearball[19][10]
            gearball[25][9]=gearball[25][10]

            gearball[1][11]=gearball[1][10]
            gearball[7][11]=gearball[7][10]
            gearball[15][11]=gearball[15][10]
            gearball[21][11]=gearball[21][10]

            gearball[5][10]=' '
            gearball[13][10]=' '
            gearball[19][10]=' '
            gearball[25][10]=' '

            gearball[1][10]=' '
            gearball[7][10]=' '
            gearball[15][10]=' '
            gearball[21][10]=' '

        elif gearball[0][10]=='/':
            gearball[0][10]="\\"
            gearball[6][10]="\\"
            gearball[14][10]="\\"
            gearball[20][10]="\\"

            gearball[5][11]=gearball[7][11]
            gearball[13][11]=gearball[15][11]
            gearball[19][11]=gearball[21][11]
            gearball[25][11]=gearball[1][11]

            gearball[1][9]= gearball[25][9]
            gearball[7][9]=gearball[5][9]
            gearball[15][9]=gearball[13][9]
            gearball[21][9]=gearball[19][9]

            gearball[5][9]=' '
            gearball[13][9]=' '
            gearball[19][9]=' '
            gearball[25][9]=' '

            gearball[1][11]=' '
            gearball[7][11]=' '
            gearball[15][11]=' '
            gearball[21][11]=' '

        elif gearball[0][10]=="\\":
            gearball[0][10]='='
            gearball[6][10]='='
            gearball[14][10]='='
            gearball[20][10]='='

            gearball[5][10]=gearball[5][11]
            gearball[13][10]=gearball[13][11]
            gearball[19][10]=gearball[19][11]
            gearball[25][10]=gearball[25][11]

            gearball[1][10]= gearball[1][9]
            gearball[7][10]=gearball[7][9]
            gearball[15][10]=gearball[15][9]
            gearball[21][10]=gearball[21][9]

            gearball[5][11]=' '
            gearball[13][11]=' '
            gearball[19][11]=' '
            gearball[25][11]=' '

            gearball[1][9]=' '
            gearball[7][9]=' '
            gearball[15][9]=' '
            gearball[21][9]=' '



    
        a=gearball[7][17]
        b=gearball[10][19]
        c=gearball[13][17]
        d=gearball[10][15]
        
        gearball[7][17]=b
        gearball[10][19]=c
        gearball[13][17]=d
        gearball[10][15]=a

        a=gearball[7][16]
        b=gearball[9][19]
        c=gearball[13][18]
        d=gearball[11][15]
        
        gearball[7][16]=b
        gearball[9][19]=c
        gearball[13][18]=d
        gearball[11][15]=a
        
        a=gearball[7][18]
        b=gearball[11][19]
        c=gearball[13][16]
        d=gearball[9][15]
        
        gearball[7][18]=b
        gearball[11][19]=c
        gearball[13][16]=d
        gearball[9][15]=a

#         a=gearball[6][17]
#         b=gearball[10][20]
#         c=gearball[14][17]
#         d=gearball[10][14]
        
#         gearball[6][17]=b
#         gearball[10][20]=c
#         gearball[14][17]=d
#         gearball[10][14]=a
        

        
        a=gearball[7][15]
        b=gearball[7][19]
        c=gearball[13][19]
        d=gearball[13][15]
        
        gearball[7][15]=b
        gearball[7][19]=c
        gearball[13][19]=d
        gearball[13][15]=a
        
        a=gearball[8][17]
        b=gearball[10][18]
        c=gearball[12][17]
        d=gearball[10][16]
        
        gearball[8][17]=b
        gearball[10][18]=c
        gearball[12][17]=d
        gearball[10][16]=a



        a=gearball[7][3]
        b=gearball[10][5]
        c=gearball[13][3]
        d=gearball[10][1]
        
        gearball[7][3]=b
        gearball[10][5]=c
        gearball[13][3]=d
        gearball[10][1]=a

        a=gearball[7][2]
        b=gearball[9][5]
        c=gearball[13][4]
        d=gearball[11][1]
        
        gearball[7][2]=b
        gearball[9][5]=c
        gearball[13][4]=d
        gearball[11][1]=a
        
        a=gearball[7][4]
        b=gearball[11][5]
        c=gearball[13][2]
        d=gearball[9][1]
        
        gearball[7][4]=b
        gearball[11][5]=c
        gearball[13][2]=d
        gearball[9][1]=a

#         a=gearball[6][3]
#         b=gearball[10][6]
#         c=gearball[14][3]
#         d=gearball[10][0]
        
#         gearball[6][3]=b
#         gearball[10][6]=c
#         gearball[14][3]=d
#         gearball[10][0]=a
        
    
        a=gearball[7][1]
        b=gearball[7][5]
        c=gearball[13][5]
        d=gearball[13][1]
        
        gearball[7][1]=b
        gearball[7][5]=c
        gearball[13][5]=d
        gearball[13][1]=a
        
        a=gearball[8][3]
        b=gearball[10][4]
        c=gearball[12][3]
        d=gearball[10][2]
        
        gearball[8][3]=b
        gearball[10][4]=c
        gearball[12][3]=d
        gearball[10][2]=a
        
        gearball[7][21]=gearball[25][13]
        gearball[7][22]=gearball[25][11]
        gearball[7][23]=gearball[25][10]
        gearball[7][24]=gearball[25][9]
        gearball[7][25]=gearball[25][7]
        gearball[9][21]=gearball[24][13]
        gearball[8][23]=gearball[24][10]
        gearball[9][25]=gearball[24][7]
        gearball[10][21]=gearball[23][13]
        gearball[10][22]=gearball[23][12]
        gearball[10][23]=gearball[23][10]
        gearball[10][24]=gearball[23][8]
        gearball[10][25]=gearball[23][7]
        gearball[11][21]=gearball[22][13]
        gearball[12][23]=gearball[22][10]
        gearball[11][25]=gearball[22][7]
        gearball[13][21]=gearball[21][13]
        gearball[13][21]=gearball[21][13]
        gearball[13][22]=gearball[21][11]
        gearball[13][23]=gearball[21][10]
        gearball[13][24]=gearball[21][9]
        gearball[13][25]=gearball[21][7]

        gearball[6][0]=gearball[0][6]
        gearball[14][0]=gearball[20][6]
        gearball[6][20]=gearball[0][14]
        gearball[14][20]=gearball[20][14]
        gearball[10][0]=gearball[23][6]
        gearball[10][20]=gearball[23][14]
        gearball[6][23]=gearball[0][10]
        gearball[14][23]=gearball[20][10]
        
        if gearball[3][6]=="\\":
            gearball[6][3]='/'
        elif gearball[3][6]=='/':
            gearball[6][3]="\\"
        else:
            gearball[6][3]=gearball[3][6]
            
        if gearball[17][6]=="\\":
            gearball[14][3]='/'
        elif gearball[17][6]=='/':
            gearball[14][3]="\\"
        else:
            gearball[14][3]=gearball[17][6]
                    
        if gearball[3][14]=="\\":
            gearball[6][17]='/'
        elif gearball[3][14]=='/':
            gearball[6][17]="\\"
        else:
            gearball[6][17]=gearball[3][14]

        if gearball[17][14]=="\\":
            gearball[14][17]='/'
        elif gearball[17][14]=='/':
            gearball[14][17]="\\"
        else:
            gearball[14][17]=gearball[17][14]

        
        return gearball

# Code for the move in which middle part is stable and up side goes right and down side goes left.
    
    
def upRight_downLeft(gearball):
    for k in range(1):
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        h=[]


        for j in range(26):
            a.append(gearball[10][j])        
            b.append(gearball[12][j])
            c.append(gearball[13][j])
            d.append(gearball[14][j])
            e.append(gearball[8][j])
            f.append(gearball[7][j])
            h.append(gearball[6][j])


        gearball[14][0]=d[6]
        gearball[14][3]=d[10]
        gearball[14][6]=d[14]
        gearball[14][10]=d[17]
        gearball[14][14]=d[20]
        gearball[14][17]=d[23]
        gearball[14][20]=d[0]
        gearball[14][23]=d[3]

        gearball[13][1]=c[7]
        gearball[13][2]=c[9]
        gearball[13][3]=c[10]
        gearball[13][4]=c[11]
        gearball[13][5]=c[13]

        gearball[13][7]=c[15]
        gearball[13][9]=c[16]
        gearball[13][10]=c[17]
        gearball[13][11]=c[18]
        gearball[13][13]=c[19]

        gearball[13][15]=c[21]
        gearball[13][16]=c[22]
        gearball[13][17]=c[23]
        gearball[13][18]=c[24]
        gearball[13][19]=c[25]

        gearball[13][21]=c[1]
        gearball[13][22]=c[2]
        gearball[13][23]=c[3]
        gearball[13][24]=c[4]
        gearball[13][25]=c[5]

        gearball[12][3]=b[10]
        gearball[12][10]=b[17]
        gearball[12][17]=b[23]
        gearball[12][23]=b[3]


        gearball[6][0]=h[20]
        gearball[6][3]=h[23]
        gearball[6][6]=h[0]
        gearball[6][10]=h[3]
        gearball[6][14]=h[6]
        gearball[6][17]=h[10]
        gearball[6][20]=h[14]
        gearball[6][23]=h[17]

        gearball[7][1]=f[21]
        gearball[7][2]=f[22]
        gearball[7][3]=f[23]
        gearball[7][4]=f[24]
        gearball[7][5]=f[25]

        gearball[7][7]=f[1]
        gearball[7][9]=f[2]
        gearball[7][10]=f[3]
        gearball[7][11]=f[4]
        gearball[7][13]=f[5]

        gearball[7][15]=f[7]
        gearball[7][16]=f[9]
        gearball[7][17]=f[10]
        gearball[7][18]=f[11]
        gearball[7][19]=f[13]

        gearball[7][21]=f[15]
        gearball[7][22]=f[16]
        gearball[7][23]=f[17]
        gearball[7][24]=f[18]
        gearball[7][25]=f[19]

        gearball[8][3]=e[23]
        gearball[8][10]=e[3]
        gearball[8][17]=e[10]
        gearball[8][23]=e[17]

        if gearball[10][0]=='=':
            gearball[10][0]="\\"
            gearball[10][6]="\\"
            gearball[10][14]="\\"
            gearball[10][20]="\\"

            gearball[11][5]=gearball[10][5]
            gearball[11][13]=gearball[10][13]
            gearball[11][19]=gearball[10][19]
            gearball[11][25]=gearball[10][25]

            gearball[9][1]=gearball[10][1]
            gearball[9][7]=gearball[10][7]
            gearball[9][15]=gearball[10][15]
            gearball[9][21]=gearball[10][21]

            gearball[10][5]=' '
            gearball[10][13]=' '
            gearball[10][19]=' '
            gearball[10][25]=' '

            gearball[10][1]=' '
            gearball[10][7]=' '
            gearball[10][15]=' '
            gearball[10][21]=' '

        elif gearball[10][0]=="\\":
            gearball[10][0]='/'
            gearball[10][6]='/'
            gearball[10][14]='/'
            gearball[10][20]='/'

            gearball[9][5]=gearball[9][7]
            gearball[9][13]=gearball[9][15]
            gearball[9][19]=gearball[9][21]
            gearball[9][25]=gearball[9][1]

            gearball[11][1]= gearball[11][25]
            gearball[11][7]=gearball[11][5]
            gearball[11][15]=gearball[11][13]
            gearball[11][21]=gearball[11][19]

            gearball[11][5]=' '
            gearball[11][13]=' '
            gearball[11][19]=' '
            gearball[11][25]=' '

            gearball[9][1]=' '
            gearball[9][7]=' '
            gearball[9][15]=' '
            gearball[9][21]=' '

        elif gearball[10][0]=='/':
            gearball[10][0]='='
            gearball[10][6]='='
            gearball[10][14]='='
            gearball[10][20]='='

            gearball[10][5]=gearball[9][5]
            gearball[10][13]=gearball[9][13]
            gearball[10][19]=gearball[9][19]
            gearball[10][25]=gearball[9][25]

            gearball[10][1]= gearball[11][1]
            gearball[10][7]=gearball[11][7]
            gearball[10][15]=gearball[11][15]
            gearball[10][21]=gearball[11][21]

            gearball[9][5]=' '
            gearball[9][13]=' '
            gearball[9][19]=' '
            gearball[9][25]=' '

            gearball[11][1]=' '
            gearball[11][7]=' '
            gearball[11][15]=' '
            gearball[11][21]=' '




        a=gearball[1][10]
        b=gearball[3][13]
        c=gearball[5][10]
        d=gearball[3][7]
        
        gearball[1][10]=b
        gearball[3][13]=c
        gearball[5][10]=d
        gearball[3][7]=a

        a=gearball[1][9]
        b=gearball[2][13]
        c=gearball[5][11]
        d=gearball[4][7]
        
        gearball[1][9]=b
        gearball[2][13]=c
        gearball[5][11]=d
        gearball[4][7]=a

        a=gearball[1][11]
        b=gearball[4][13]
        c=gearball[5][9]
        d=gearball[2][7]
        
        gearball[1][11]=b
        gearball[4][13]=c
        gearball[5][9]=d
        gearball[2][7]=a

#         a=gearball[0][10]
#         b=gearball[3][14]
#         c=gearball[6][10]
#         d=gearball[3][6]
        
#         gearball[0][10]=b
#         gearball[3][14]=c
#         gearball[6][10]=d
#         gearball[3][6]=a
        
        
    
        a=gearball[1][7]
        b=gearball[1][13]
        c=gearball[5][13]
        d=gearball[5][7]
        
        gearball[1][7]=b
        gearball[1][13]=c
        gearball[5][13]=d
        gearball[5][7]=a
        
        a=gearball[2][10]
        b=gearball[3][12]
        c=gearball[4][10]
        d=gearball[3][8]
        
        gearball[2][10]=b
        gearball[3][12]=c
        gearball[4][10]=d
        gearball[3][8]=a



        a=gearball[15][10]
        b=gearball[17][13]
        c=gearball[19][10]
        d=gearball[17][7]
        
        gearball[15][10]=b
        gearball[17][13]=c
        gearball[19][10]=d
        gearball[17][7]=a
        
        a=gearball[15][9]
        b=gearball[16][13]
        c=gearball[19][11]
        d=gearball[18][7]
        
        gearball[15][9]=b
        gearball[16][13]=c
        gearball[19][11]=d
        gearball[18][7]=a

        a=gearball[15][11]
        b=gearball[18][13]
        c=gearball[19][9]
        d=gearball[16][7]
        
        gearball[15][11]=b
        gearball[18][13]=c
        gearball[19][9]=d
        gearball[16][7]=a

#         a=gearball[14][10]
#         b=gearball[17][14]
#         c=gearball[20][10]
#         d=gearball[17][6]
        
#         gearball[14][10]=b
#         gearball[17][14]=c
#         gearball[20][10]=d
#         gearball[17][6]=a
        
        
        
        a=gearball[15][7]
        b=gearball[15][13]
        c=gearball[19][13]
        d=gearball[19][7]
        
        gearball[15][7]=b
        gearball[15][13]=c
        gearball[19][13]=d
        gearball[19][7]=a
        
        a=gearball[16][10]
        b=gearball[17][12]
        c=gearball[18][10]
        d=gearball[17][8]
        
        gearball[16][10]=b
        gearball[17][12]=c
        gearball[18][10]=d
        gearball[17][8]=a
        
        gearball[25][13]=gearball[7][21]
        gearball[25][11]=gearball[7][22]
        gearball[25][10]=gearball[7][23]
        gearball[25][9]=gearball[7][24]
        gearball[25][7]=gearball[7][25]
        gearball[24][13]=gearball[9][21]
        gearball[24][10]=gearball[8][23]
        gearball[24][7]=gearball[9][25]
        gearball[23][13]=gearball[10][21]
        gearball[23][12]=gearball[10][22]
        gearball[23][10]=gearball[10][23]
        gearball[23][8]=gearball[10][24]
        gearball[23][7]=gearball[10][25]
        gearball[22][13]=gearball[11][21]
        gearball[22][10]=gearball[12][23]
        gearball[22][7]=gearball[11][25]
        gearball[21][13]=gearball[13][21]
        gearball[21][13]=gearball[13][21]
        gearball[21][11]=gearball[13][22]
        gearball[21][10]=gearball[13][23]
        gearball[21][9]=gearball[13][24]
        gearball[21][7]=gearball[13][25]

        gearball[0][6]=gearball[6][0]
        gearball[20][6]=gearball[14][0]
        gearball[0][14]=gearball[6][20]
        gearball[20][14]=gearball[14][20]
        gearball[23][6]=gearball[10][0]
        gearball[23][14]=gearball[10][20]
        gearball[0][10]=gearball[6][23]
        gearball[20][10]=gearball[14][23]
        
        if gearball[6][3]=="\\":
            gearball[3][6]='/'
        elif gearball[6][3]=='/':
            gearball[3][6]="\\"
        else:
            gearball[3][6]=gearball[6][3]
            
        if gearball[14][3]=="\\":
            gearball[17][6]='/'
        elif gearball[14][3]=='/':
            gearball[17][6]="\\"
        else:
            gearball[17][6]=gearball[14][3]
                    
        if gearball[6][17]=="\\":
            gearball[3][14]='/'
        elif gearball[6][17]=='/':
            gearball[3][14]="\\"
        else:
            gearball[3][14]=gearball[6][17]

        if gearball[14][17]=="\\":
            gearball[17][14]='/'
        elif gearball[14][17]=='/':
            gearball[17][14]="\\"
        else:
            gearball[17][14]=gearball[14][17]
        
        
        return gearball
    
# Code for the move in which middle part is stable and up side goes left and down side goes right.
    
def upLeft_downRight(gearball):
    for k in range(1):
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        h=[]


        for j in range(26):
            a.append(gearball[10][j])        
            b.append(gearball[12][j])
            c.append(gearball[13][j])
            d.append(gearball[14][j])
            e.append(gearball[8][j])
            f.append(gearball[7][j])
            h.append(gearball[6][j])


        gearball[14][0]=d[20]
        gearball[14][3]=d[23]
        gearball[14][6]=d[0]
        gearball[14][10]=d[3]
        gearball[14][14]=d[6]
        gearball[14][17]=d[10]
        gearball[14][20]=d[14]
        gearball[14][23]=d[17]

        gearball[13][1]=c[21]
        gearball[13][2]=c[22]
        gearball[13][3]=c[23]
        gearball[13][4]=c[24]
        gearball[13][5]=c[25]

        gearball[13][7]=c[1]
        gearball[13][9]=c[2]
        gearball[13][10]=c[3]
        gearball[13][11]=c[4]
        gearball[13][13]=c[5]

        gearball[13][15]=c[7]
        gearball[13][16]=c[9]
        gearball[13][17]=c[10]
        gearball[13][18]=c[11]
        gearball[13][19]=c[13]

        gearball[13][21]=c[15]
        gearball[13][22]=c[16]
        gearball[13][23]=c[17]
        gearball[13][24]=c[18]
        gearball[13][25]=c[19]

        gearball[12][3]=b[23]
        gearball[12][10]=b[3]
        gearball[12][17]=b[10]
        gearball[12][23]=b[17]


        gearball[6][0]=h[6]
        gearball[6][3]=h[10]
        gearball[6][6]=h[14]
        gearball[6][10]=h[17]
        gearball[6][14]=h[20]
        gearball[6][17]=h[23]
        gearball[6][20]=h[0]
        gearball[6][23]=h[3]

        gearball[7][1]=f[7]
        gearball[7][2]=f[9]
        gearball[7][3]=f[10]
        gearball[7][4]=f[11]
        gearball[7][5]=f[13]

        gearball[7][7]=f[15]
        gearball[7][9]=f[16]
        gearball[7][10]=f[17]
        gearball[7][11]=f[18]
        gearball[7][13]=f[19]

        gearball[7][15]=f[21]
        gearball[7][16]=f[22]
        gearball[7][17]=f[23]
        gearball[7][18]=f[24]
        gearball[7][19]=f[25]

        gearball[7][21]=f[1]
        gearball[7][22]=f[2]
        gearball[7][23]=f[3]
        gearball[7][24]=f[4]
        gearball[7][25]=f[5]

        gearball[8][3]=e[10]
        gearball[8][10]=e[17]
        gearball[8][17]=e[23]
        gearball[8][23]=e[3]

        if gearball[10][0]=='=':
            gearball[10][0]='/'
            gearball[10][6]='/'
            gearball[10][14]='/'
            gearball[10][20]='/'

            gearball[9][5]=gearball[10][5]
            gearball[9][13]=gearball[10][13]
            gearball[9][19]=gearball[10][19]
            gearball[9][25]=gearball[10][25]

            gearball[11][1]=gearball[10][1]
            gearball[11][7]=gearball[10][7]
            gearball[11][15]=gearball[10][15]
            gearball[11][21]=gearball[10][21]

            gearball[10][5]=' '
            gearball[10][13]=' '
            gearball[10][19]=' '
            gearball[10][25]=' '

            gearball[10][1]=' '
            gearball[10][7]=' '
            gearball[10][15]=' '
            gearball[10][21]=' '

        elif gearball[10][0]=='/':
            gearball[10][0]="\\"
            gearball[10][6]="\\"
            gearball[10][14]="\\"
            gearball[10][20]="\\"

            gearball[11][5]=gearball[11][7]
            gearball[11][13]=gearball[11][15]
            gearball[11][19]=gearball[11][21]
            gearball[11][25]=gearball[11][1]

            gearball[9][1]= gearball[9][25]
            gearball[9][7]=gearball[9][5]
            gearball[9][15]=gearball[9][13]
            gearball[9][21]=gearball[9][19]

            gearball[9][5]=' '
            gearball[9][13]=' '
            gearball[9][19]=' '
            gearball[9][25]=' '

            gearball[11][1]=' '
            gearball[11][7]=' '
            gearball[11][15]=' '
            gearball[11][21]=' '

        elif gearball[10][0]=="\\":
            gearball[10][0]='='
            gearball[10][6]='='
            gearball[10][14]='='
            gearball[10][20]='='

            gearball[10][5]=gearball[11][5]
            gearball[10][13]=gearball[11][13]
            gearball[10][19]=gearball[11][19]
            gearball[10][25]=gearball[11][25]

            gearball[10][1]= gearball[9][1]
            gearball[10][7]=gearball[9][7]
            gearball[10][15]=gearball[9][15]
            gearball[10][21]=gearball[9][21]

            gearball[11][5]=' '
            gearball[11][13]=' '
            gearball[11][19]=' '
            gearball[11][25]=' '

            gearball[9][1]=' '
            gearball[9][7]=' '
            gearball[9][15]=' '
            gearball[9][21]=' '



    
        a=gearball[1][10]
        b=gearball[3][13]
        c=gearball[5][10]
        d=gearball[3][7]
        
        gearball[1][10]=d
        gearball[3][13]=a
        gearball[5][10]=b
        gearball[3][7]=c
 
        a=gearball[1][9]
        b=gearball[2][13]
        c=gearball[5][11]
        d=gearball[4][7]
        
        gearball[1][9]=d
        gearball[2][13]=a
        gearball[5][11]=b
        gearball[4][7]=c

        a=gearball[1][11]
        b=gearball[4][13]
        c=gearball[5][9]
        d=gearball[2][7]
        
        gearball[1][11]=d
        gearball[4][13]=a
        gearball[5][9]=b
        gearball[2][7]=c

#         a=gearball[0][10]
#         b=gearball[3][14]
#         c=gearball[6][10]
#         d=gearball[3][6]
        
#         gearball[0][10]=d
#         gearball[3][14]=a
#         gearball[6][10]=b
#         gearball[3][6]=c
        


    
        a=gearball[1][7]
        b=gearball[1][13]
        c=gearball[5][13]
        d=gearball[5][7]
        
        gearball[1][7]=d
        gearball[1][13]=a
        gearball[5][13]=b
        gearball[5][7]=c
        
        a=gearball[2][10]
        b=gearball[3][12]
        c=gearball[4][10]
        d=gearball[3][8]
        
        gearball[2][10]=d
        gearball[3][12]=a
        gearball[4][10]=b
        gearball[3][8]=c




        a=gearball[15][10]
        b=gearball[17][13]
        c=gearball[19][10]
        d=gearball[17][7]
        
        gearball[15][10]=d
        gearball[17][13]=a
        gearball[19][10]=b
        gearball[17][7]=c
 
        a=gearball[15][9]
        b=gearball[16][13]
        c=gearball[19][11]
        d=gearball[18][7]
        
        gearball[15][9]=d
        gearball[16][13]=a
        gearball[19][11]=b
        gearball[18][7]=c

        a=gearball[15][11]
        b=gearball[18][13]
        c=gearball[19][9]
        d=gearball[16][7]
        
        gearball[15][11]=d
        gearball[18][13]=a
        gearball[19][9]=b
        gearball[16][7]=c

#         a=gearball[14][10]
#         b=gearball[17][14]
#         c=gearball[20][10]
#         d=gearball[17][6]
        
#         gearball[14][10]=d
#         gearball[17][14]=a
#         gearball[20][10]=b
#         gearball[17][6]=c
        
        a=gearball[15][7]
        b=gearball[15][13]
        c=gearball[19][13]
        d=gearball[19][7]
        
        gearball[15][7]=d
        gearball[15][13]=a
        gearball[19][13]=b
        gearball[19][7]=c
        
        a=gearball[16][10]
        b=gearball[17][12]
        c=gearball[18][10]
        d=gearball[17][8]
        
        gearball[16][10]=d
        gearball[17][12]=a
        gearball[18][10]=b
        gearball[17][8]=c
        
        gearball[25][13]=gearball[7][21]
        gearball[25][11]=gearball[7][22]
        gearball[25][10]=gearball[7][23]
        gearball[25][9]=gearball[7][24]
        gearball[25][7]=gearball[7][25]
        gearball[24][13]=gearball[9][21]
        gearball[24][10]=gearball[8][23]
        gearball[24][7]=gearball[9][25]
        gearball[23][13]=gearball[10][21]
        gearball[23][12]=gearball[10][22]
        gearball[23][10]=gearball[10][23]
        gearball[23][8]=gearball[10][24]
        gearball[23][7]=gearball[10][25]
        gearball[22][13]=gearball[11][21]
        gearball[22][10]=gearball[12][23]
        gearball[22][7]=gearball[11][25]
        gearball[21][13]=gearball[13][21]
        gearball[21][13]=gearball[13][21]
        gearball[21][11]=gearball[13][22]
        gearball[21][10]=gearball[13][23]
        gearball[21][9]=gearball[13][24]
        gearball[21][7]=gearball[13][25]

        gearball[0][6]=gearball[6][0]
        gearball[20][6]=gearball[14][0]
        gearball[0][14]=gearball[6][20]
        gearball[20][14]=gearball[14][20]
        gearball[23][6]=gearball[10][0]
        gearball[23][14]=gearball[10][20]
        gearball[0][10]=gearball[6][23]
        gearball[20][10]=gearball[14][23]
        
        if gearball[6][3]=="\\":
            gearball[3][6]='/'
        elif gearball[6][3]=='/':
            gearball[3][6]="\\"
        else:
            gearball[3][6]=gearball[6][3]
            
        if gearball[14][3]=="\\":
            gearball[17][6]='/'
        elif gearball[14][3]=='/':
            gearball[17][6]="\\"
        else:
            gearball[17][6]=gearball[14][3]
                    
        if gearball[6][17]=="\\":
            gearball[3][14]='/'
        elif gearball[6][17]=='/':
            gearball[3][14]="\\"
        else:
            gearball[3][14]=gearball[6][17]

        if gearball[14][17]=="\\":
            gearball[17][14]='/'
        elif gearball[14][17]=='/':
            gearball[17][14]="\\"
        else:
            gearball[17][14]=gearball[14][17]
        
        
        return gearball

# Code for the move in which middle part is stable and front face goes clockwise and back face goes anti-clockwise.
    
def FrontFaceClockwise_BackFaceAntiClockwise(gearball):
    for k in range(1):
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        h=[]


        for i in range(26):
            a.append(gearball[i][10])        
            b.append(gearball[i][12])
            c.append(gearball[i][13])
            d.append(gearball[i][14])
            e.append(gearball[i][8])
            f.append(gearball[i][7])
            h.append(gearball[i][6])


        gearball[0][14]=d[20]
        gearball[3][14]=d[23]
        gearball[6][14]=d[0]
        gearball[10][14]=d[3]
        gearball[14][14]=d[6]
        gearball[17][14]=d[10]
        gearball[20][14]=d[14]
        gearball[23][14]=d[17]

        gearball[1][13]=c[21]
        gearball[2][13]=c[22]
        gearball[3][13]=c[23]
        gearball[4][13]=c[24]
        gearball[5][13]=c[25]

        gearball[7][13]=c[1]
        gearball[9][13]=c[2]
        gearball[10][13]=c[3]
        gearball[11][13]=c[4]
        gearball[13][13]=c[5]

        gearball[15][13]=c[7]
        gearball[16][13]=c[9]
        gearball[17][13]=c[10]
        gearball[18][13]=c[11]
        gearball[19][13]=c[13]

        gearball[21][13]=c[15]
        gearball[22][13]=c[16]
        gearball[23][13]=c[17]
        gearball[24][13]=c[18]
        gearball[25][13]=c[19]

        gearball[3][12]=b[23]
        gearball[10][12]=b[3]
        gearball[17][12]=b[10]
        gearball[23][12]=b[17]


        gearball[0][6]=h[6]
        gearball[3][6]=h[10]
        gearball[6][6]=h[14]
        gearball[10][6]=h[17]
        gearball[14][6]=h[20]
        gearball[17][6]=h[23]
        gearball[20][6]=h[0]
        gearball[23][6]=h[3]

        gearball[1][7]=f[7]
        gearball[2][7]=f[9]
        gearball[3][7]=f[10]
        gearball[4][7]=f[11]
        gearball[5][7]=f[13]

        gearball[7][7]=f[15]
        gearball[9][7]=f[16]
        gearball[10][7]=f[17]
        gearball[11][7]=f[18]
        gearball[13][7]=f[19]

        gearball[15][7]=f[21]
        gearball[16][7]=f[22]
        gearball[17][7]=f[23]
        gearball[18][7]=f[24]
        gearball[19][7]=f[25]

        gearball[21][7]=f[1]
        gearball[22][7]=f[2]
        gearball[23][7]=f[3]
        gearball[24][7]=f[4]
        gearball[25][7]=f[5]

        gearball[3][8]=e[10]
        gearball[10][8]=e[17]
        gearball[17][8]=e[23]
        gearball[23][8]=e[3]

        if gearball[0][10]=='=':
            gearball[0][10]='/'
            gearball[6][10]='/'
            gearball[14][10]='/'
            gearball[20][10]='/'

            gearball[5][9]=gearball[5][10]
            gearball[13][9]=gearball[13][10]
            gearball[19][9]=gearball[19][10]
            gearball[25][9]=gearball[25][10]

            gearball[1][11]=gearball[1][10]
            gearball[7][11]=gearball[7][10]
            gearball[15][11]=gearball[15][10]
            gearball[21][11]=gearball[21][10]

            gearball[5][10]=' '
            gearball[13][10]=' '
            gearball[19][10]=' '
            gearball[25][10]=' '

            gearball[1][10]=' '
            gearball[7][10]=' '
            gearball[15][10]=' '
            gearball[21][10]=' '

        elif gearball[0][10]=='/':
            gearball[0][10]="\\"
            gearball[6][10]="\\"
            gearball[14][10]="\\"
            gearball[20][10]="\\"

            gearball[5][11]=gearball[7][11]
            gearball[13][11]=gearball[15][11]
            gearball[19][11]=gearball[21][11]
            gearball[25][11]=gearball[1][11]

            gearball[1][9]= gearball[25][9]
            gearball[7][9]=gearball[5][9]
            gearball[15][9]=gearball[13][9]
            gearball[21][9]=gearball[19][9]

            gearball[5][9]=' '
            gearball[13][9]=' '
            gearball[19][9]=' '
            gearball[25][9]=' '

            gearball[1][11]=' '
            gearball[7][11]=' '
            gearball[15][11]=' '
            gearball[21][11]=' '

        elif gearball[0][10]=="\\":
            gearball[0][10]='='
            gearball[6][10]='='
            gearball[14][10]='='
            gearball[20][10]='='

            gearball[5][10]=gearball[5][11]
            gearball[13][10]=gearball[13][11]
            gearball[19][10]=gearball[19][11]
            gearball[25][10]=gearball[25][11]

            gearball[1][10]= gearball[1][9]
            gearball[7][10]=gearball[7][9]
            gearball[15][10]=gearball[15][9]
            gearball[21][10]=gearball[21][9]

            gearball[5][11]=' '
            gearball[13][11]=' '
            gearball[19][11]=' '
            gearball[25][11]=' '

            gearball[1][9]=' '
            gearball[7][9]=' '
            gearball[15][9]=' '
            gearball[21][9]=' '



    
        a=gearball[7][17]
        b=gearball[10][19]
        c=gearball[13][17]
        d=gearball[10][15]
        
        gearball[7][17]=b
        gearball[10][19]=c
        gearball[13][17]=d
        gearball[10][15]=a

        a=gearball[7][16]
        b=gearball[9][19]
        c=gearball[13][18]
        d=gearball[11][15]
        
        gearball[7][16]=b
        gearball[9][19]=c
        gearball[13][18]=d
        gearball[11][15]=a
        
        a=gearball[7][18]
        b=gearball[11][19]
        c=gearball[13][16]
        d=gearball[9][15]
        
        gearball[7][18]=b
        gearball[11][19]=c
        gearball[13][16]=d
        gearball[9][15]=a

#         a=gearball[6][17]
#         b=gearball[10][20]
#         c=gearball[14][17]
#         d=gearball[10][14]
        
#         gearball[6][17]=b
#         gearball[10][20]=c
#         gearball[14][17]=d
#         gearball[10][14]=a
        

        
        a=gearball[7][15]
        b=gearball[7][19]
        c=gearball[13][19]
        d=gearball[13][15]
        
        gearball[7][15]=b
        gearball[7][19]=c
        gearball[13][19]=d
        gearball[13][15]=a
        
        a=gearball[8][17]
        b=gearball[10][18]
        c=gearball[12][17]
        d=gearball[10][16]
        
        gearball[8][17]=b
        gearball[10][18]=c
        gearball[12][17]=d
        gearball[10][16]=a



        a=gearball[7][3]
        b=gearball[10][5]
        c=gearball[13][3]
        d=gearball[10][1]
        
        gearball[7][3]=b
        gearball[10][5]=c
        gearball[13][3]=d
        gearball[10][1]=a

        a=gearball[7][2]
        b=gearball[9][5]
        c=gearball[13][4]
        d=gearball[11][1]
        
        gearball[7][2]=b
        gearball[9][5]=c
        gearball[13][4]=d
        gearball[11][1]=a
        
        a=gearball[7][4]
        b=gearball[11][5]
        c=gearball[13][2]
        d=gearball[9][1]
        
        gearball[7][4]=b
        gearball[11][5]=c
        gearball[13][2]=d
        gearball[9][1]=a

#         a=gearball[6][3]
#         b=gearball[10][6]
#         c=gearball[14][3]
#         d=gearball[10][0]
        
#         gearball[6][3]=b
#         gearball[10][6]=c
#         gearball[14][3]=d
#         gearball[10][0]=a
        
    
        a=gearball[7][1]
        b=gearball[7][5]
        c=gearball[13][5]
        d=gearball[13][1]
        
        gearball[7][1]=b
        gearball[7][5]=c
        gearball[13][5]=d
        gearball[13][1]=a
        
        a=gearball[8][3]
        b=gearball[10][4]
        c=gearball[12][3]
        d=gearball[10][2]
        
        gearball[8][3]=b
        gearball[10][4]=c
        gearball[12][3]=d
        gearball[10][2]=a
        
        gearball[7][21]=gearball[25][13]
        gearball[7][22]=gearball[25][11]
        gearball[7][23]=gearball[25][10]
        gearball[7][24]=gearball[25][9]
        gearball[7][25]=gearball[25][7]
        gearball[9][21]=gearball[24][13]
        gearball[8][23]=gearball[24][10]
        gearball[9][25]=gearball[24][7]
        gearball[10][21]=gearball[23][13]
        gearball[10][22]=gearball[23][12]
        gearball[10][23]=gearball[23][10]
        gearball[10][24]=gearball[23][8]
        gearball[10][25]=gearball[23][7]
        gearball[11][21]=gearball[22][13]
        gearball[12][23]=gearball[22][10]
        gearball[11][25]=gearball[22][7]
        gearball[13][21]=gearball[21][13]
        gearball[13][21]=gearball[21][13]
        gearball[13][22]=gearball[21][11]
        gearball[13][23]=gearball[21][10]
        gearball[13][24]=gearball[21][9]
        gearball[13][25]=gearball[21][7]

        gearball[6][0]=gearball[0][6]
        gearball[14][0]=gearball[20][6]
        gearball[6][20]=gearball[0][14]
        gearball[14][20]=gearball[20][14]
        gearball[10][0]=gearball[23][6]
        gearball[10][20]=gearball[23][14]
        gearball[6][23]=gearball[0][10]
        gearball[14][23]=gearball[20][10]
        
        if gearball[3][6]=="\\":
            gearball[6][3]='/'
        elif gearball[3][6]=='/':
            gearball[6][3]="\\"
        else:
            gearball[6][3]=gearball[3][6]
            
        if gearball[17][6]=="\\":
            gearball[14][3]='/'
        elif gearball[17][6]=='/':
            gearball[14][3]="\\"
        else:
            gearball[14][3]=gearball[17][6]
                    
        if gearball[3][14]=="\\":
            gearball[6][17]='/'
        elif gearball[3][14]=='/':
            gearball[6][17]="\\"
        else:
            gearball[6][17]=gearball[3][14]

        if gearball[17][14]=="\\":
            gearball[14][17]='/'
        elif gearball[17][14]=='/':
            gearball[14][17]="\\"
        else:
            gearball[14][17]=gearball[17][14]

        
        return gearball

# Code for the move in which middle part is stable and front face goes anti-clockwise and back face goes clockwise.
    
def FrontFaceAntiClockwise_BackFaceClockwise(gearball):
    for k in range(1):
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        h=[]


        for i in range(26):
            a.append(gearball[i][10])        
            b.append(gearball[i][12])
            c.append(gearball[i][13])
            d.append(gearball[i][14])
            e.append(gearball[i][8])
            f.append(gearball[i][7])
            h.append(gearball[i][6])


        gearball[0][14]=d[6]
        gearball[3][14]=d[10]
        gearball[6][14]=d[14]
        gearball[10][14]=d[17]
        gearball[14][14]=d[20]
        gearball[17][14]=d[23]
        gearball[20][14]=d[0]
        gearball[23][14]=d[3]

        gearball[1][13]=c[7]
        gearball[2][13]=c[9]
        gearball[3][13]=c[10]
        gearball[4][13]=c[11]
        gearball[5][13]=c[13]

        gearball[7][13]=c[15]
        gearball[9][13]=c[16]
        gearball[10][13]=c[17]
        gearball[11][13]=c[18]
        gearball[13][13]=c[19]

        gearball[15][13]=c[21]
        gearball[16][13]=c[22]
        gearball[17][13]=c[23]
        gearball[18][13]=c[24]
        gearball[19][13]=c[25]

        gearball[21][13]=c[1]
        gearball[22][13]=c[2]
        gearball[23][13]=c[3]
        gearball[24][13]=c[4]
        gearball[25][13]=c[5]

        gearball[3][12]=b[10]
        gearball[10][12]=b[17]
        gearball[17][12]=b[23]
        gearball[23][12]=b[3]


        gearball[0][6]=h[20]
        gearball[3][6]=h[23]
        gearball[6][6]=h[0]
        gearball[10][6]=h[3]
        gearball[14][6]=h[6]
        gearball[17][6]=h[10]
        gearball[20][6]=h[14]
        gearball[23][6]=h[17]

        gearball[1][7]=f[21]
        gearball[2][7]=f[22]
        gearball[3][7]=f[23]
        gearball[4][7]=f[24]
        gearball[5][7]=f[25]

        gearball[7][7]=f[1]
        gearball[9][7]=f[2]
        gearball[10][7]=f[3]
        gearball[11][7]=f[4]
        gearball[13][7]=f[5]

        gearball[15][7]=f[7]
        gearball[16][7]=f[9]
        gearball[17][7]=f[10]
        gearball[18][7]=f[11]
        gearball[19][7]=f[13]

        gearball[21][7]=f[15]
        gearball[22][7]=f[16]
        gearball[23][7]=f[17]
        gearball[24][7]=f[18]
        gearball[25][7]=f[19]

        gearball[3][8]=e[23]
        gearball[10][8]=e[3]
        gearball[17][8]=e[10]
        gearball[23][8]=e[17]

        if gearball[0][10]=='=':
            gearball[0][10]="\\"
            gearball[6][10]="\\"
            gearball[14][10]="\\"
            gearball[20][10]="\\"

            gearball[5][11]=gearball[5][10]
            gearball[13][11]=gearball[13][10]
            gearball[19][11]=gearball[19][10]
            gearball[25][11]=gearball[25][10]

            gearball[1][9]=gearball[1][10]
            gearball[7][9]=gearball[7][10]
            gearball[15][9]=gearball[15][10]
            gearball[21][9]=gearball[21][10]

            gearball[5][10]=' '
            gearball[13][10]=' '
            gearball[19][10]=' '
            gearball[25][10]=' '

            gearball[1][10]=' '
            gearball[7][10]=' '
            gearball[15][10]=' '
            gearball[21][10]=' '

        elif gearball[0][10]=="\\":
            gearball[0][10]='/'
            gearball[6][10]='/'
            gearball[14][10]='/'
            gearball[20][10]='/'

            gearball[5][9]=gearball[7][9]
            gearball[13][9]=gearball[15][9]
            gearball[19][9]=gearball[21][9]
            gearball[25][9]=gearball[1][9]

            gearball[1][11]= gearball[25][11]
            gearball[7][11]=gearball[5][11]
            gearball[15][11]=gearball[13][11]
            gearball[21][11]=gearball[19][11]

            gearball[5][11]=' '
            gearball[13][11]=' '
            gearball[19][11]=' '
            gearball[25][11]=' '

            gearball[1][9]=' '
            gearball[7][9]=' '
            gearball[15][9]=' '
            gearball[21][9]=' '

        elif gearball[0][10]=='/':
            gearball[0][10]='='
            gearball[6][10]='='
            gearball[14][10]='='
            gearball[20][10]='='

            gearball[5][10]=gearball[5][9]
            gearball[13][10]=gearball[13][9]
            gearball[19][10]=gearball[19][9]
            gearball[25][10]=gearball[25][9]

            gearball[1][10]= gearball[1][11]
            gearball[7][10]=gearball[7][11]
            gearball[15][10]=gearball[15][11]
            gearball[21][10]=gearball[21][11]

            gearball[5][9]=' '
            gearball[13][9]=' '
            gearball[19][9]=' '
            gearball[25][9]=' '

            gearball[1][11]=' '
            gearball[7][11]=' '
            gearball[15][11]=' '
            gearball[21][11]=' '


    
        a=gearball[7][17]
        b=gearball[10][19]
        c=gearball[13][17]
        d=gearball[10][15]
        
        gearball[7][17]=d
        gearball[10][19]=a
        gearball[13][17]=b
        gearball[10][15]=c

        a=gearball[7][16]
        b=gearball[9][19]
        c=gearball[13][18]
        d=gearball[11][15]
        
        gearball[7][16]=d
        gearball[9][19]=a
        gearball[13][18]=b
        gearball[11][15]=c
        
        a=gearball[7][18]
        b=gearball[11][19]
        c=gearball[13][16]
        d=gearball[9][15]
        
        gearball[7][18]=d
        gearball[11][19]=a
        gearball[13][16]=b
        gearball[9][15]=c

#         a=gearball[6][17]
#         b=gearball[10][20]
#         c=gearball[14][17]
#         d=gearball[10][14]
        
#         gearball[6][17]=d
#         gearball[10][20]=a
#         gearball[14][17]=b
#         gearball[10][14]=c


        
        
        a=gearball[7][15]
        b=gearball[7][19]
        c=gearball[13][19]
        d=gearball[13][15]
        
        gearball[7][15]=d
        gearball[7][19]=a
        gearball[13][19]=b
        gearball[13][15]=c
        
        a=gearball[8][17]
        b=gearball[10][18]
        c=gearball[12][17]
        d=gearball[10][16]
        
        gearball[8][17]=d
        gearball[10][18]=a
        gearball[12][17]=b
        gearball[10][16]=c


        a=gearball[7][3]
        b=gearball[10][5]
        c=gearball[13][3]
        d=gearball[10][1]
        
        gearball[7][3]=d
        gearball[10][5]=a
        gearball[13][3]=b
        gearball[10][1]=c

        a=gearball[7][2]
        b=gearball[9][5]
        c=gearball[13][4]
        d=gearball[11][1]
        
        gearball[7][2]=d
        gearball[9][5]=a
        gearball[13][4]=b
        gearball[11][1]=c
        
        a=gearball[7][4]
        b=gearball[11][5]
        c=gearball[13][2]
        d=gearball[9][1]
        
        gearball[7][4]=d
        gearball[11][5]=a
        gearball[13][2]=b
        gearball[9][1]=c

#         a=gearball[6][3]
#         b=gearball[10][6]
#         c=gearball[14][3]
#         d=gearball[10][0]
        
#         gearball[6][3]=d
#         gearball[10][6]=a
#         gearball[14][3]=b
#         gearball[10][0]=c
        
        
    
        a=gearball[7][1]
        b=gearball[7][5]
        c=gearball[13][5]
        d=gearball[13][1]
        
        gearball[7][1]=d
        gearball[7][5]=a
        gearball[13][5]=b
        gearball[13][1]=c
        
        a=gearball[8][3]
        b=gearball[10][4]
        c=gearball[12][3]
        d=gearball[10][2]
        
        gearball[8][3]=d
        gearball[10][4]=a
        gearball[12][3]=b
        gearball[10][2]=c
        
        gearball[7][21]=gearball[25][13]
        gearball[7][22]=gearball[25][11]
        gearball[7][23]=gearball[25][10]
        gearball[7][24]=gearball[25][9]
        gearball[7][25]=gearball[25][7]
        gearball[9][21]=gearball[24][13]
        gearball[8][23]=gearball[24][10]
        gearball[9][25]=gearball[24][7]
        gearball[10][21]=gearball[23][13]
        gearball[10][22]=gearball[23][12]
        gearball[10][23]=gearball[23][10]
        gearball[10][24]=gearball[23][8]
        gearball[10][25]=gearball[23][7]
        gearball[11][21]=gearball[22][13]
        gearball[12][23]=gearball[22][10]
        gearball[11][25]=gearball[22][7]
        gearball[13][21]=gearball[21][13]
        gearball[13][21]=gearball[21][13]
        gearball[13][22]=gearball[21][11]
        gearball[13][23]=gearball[21][10]
        gearball[13][24]=gearball[21][9]
        gearball[13][25]=gearball[21][7]

        gearball[6][0]=gearball[0][6]
        gearball[14][0]=gearball[20][6]
        gearball[6][20]=gearball[0][14]
        gearball[14][20]=gearball[20][14]
        gearball[10][0]=gearball[23][6]
        gearball[10][20]=gearball[23][14]
        gearball[6][23]=gearball[0][10]
        gearball[14][23]=gearball[20][10]
        
        if gearball[3][6]=="\\":
            gearball[6][3]='/'
        elif gearball[3][6]=='/':
            gearball[6][3]="\\"
        else:
            gearball[6][3]=gearball[3][6]
            
        if gearball[17][6]=="\\":
            gearball[14][3]='/'
        elif gearball[17][6]=='/':
            gearball[14][3]="\\"
        else:
            gearball[14][3]=gearball[17][6]
                    
        if gearball[3][14]=="\\":
            gearball[6][17]='/'
        elif gearball[3][14]=='/':
            gearball[6][17]="\\"
        else:
            gearball[6][17]=gearball[3][14]

        if gearball[17][14]=="\\":
            gearball[14][17]='/'
        elif gearball[17][14]=='/':
            gearball[14][17]="\\"
        else:
            gearball[14][17]=gearball[17][14]

        
        return gearball

#Following is the code for randomizer function which takes parameter as the gearball which has to be randomized and 'm' means    
# the number of moves to randomize it

def randomizer(m,gearball):
    listOfFunctions=[rightUp_leftDown, upRight_downLeft, upLeft_downRight, rightDown_leftUp, FrontFaceAntiClockwise_BackFaceClockwise, FrontFaceClockwise_BackFaceAntiClockwise]
    x=random.choice(listOfFunctions)(gearball)
    for i in range(m-1):
        x=random.choice(listOfFunctions)(x)
    return x

# Following is the code for A* search algorithm
#It takes root node as parameter i.e. randomized gearball and goal state as parameter to compare if we reached goal state

def algorithm(gearball,goal):
    openList=[]                        #openList is 2-d list which stores nodes which can be expanded with their f values              
    closedList=[]                      #closedList is 2-d list which stores nodes which are already expanded with their f values
    costList=[]                        #costList is 2-d list which stores nodes with their cost so far(g value)
    openList.append([gearball,0])      #Set the f value of root node to zero
    costList.append([gearball,0])      #Set the cost so far(g value) to zero of root node
    while bool(openList)==True:     
        minimum=10000
        for i in openList:       # This code is to find node in openlist with minimum f value to expand
            if i[1]<minimum:
                minimum=i[1]
                s=i[0]
        gearball=s
        
        
        
        openList.remove([gearball,minimum])  #Remove the node which needs to be expanded from openList and create its 6 children
        v1=copy.deepcopy(gearball)
        v2=copy.deepcopy(gearball)
        v3=copy.deepcopy(gearball)
        v4=copy.deepcopy(gearball)
        v5=copy.deepcopy(gearball)
        v6=copy.deepcopy(gearball)
        
        a=rightUp_leftDown(v1)      #Create a children and check if it is equal to goal
        if a==goal:
            return a
        else:
            for i in costList:       #If it is not goal state then find its cost so far by adding 1 to its parents cost(g value)
                if i[0]==gearball:
                    g=i[1]+1
            h=heuristic(a)          #Call heuristic function to find how far it is from goal state
            f=g+h                   #Find f value by adding g and h value
            flag=0
            for i in openList:
                if i[0]==a and i[1]<f:   #find if already same node exist in openList with f value less than this node's f value
                    flag=1
            for i in closedList:
                if i[0]==a and i[1]<f:
                    flag=1

            if flag==0:                 #if same node does not exist with less f value then add this node to openList and 
                openList.append([a,f])  #also add this node to costlist with its cost so far(g value)
                costList.append([a,g])                
                
        b=rightDown_leftUp(v2)
        if b==goal:
            return b
        else:
            for i in costList:
                if i[0]==gearball:
                    g=i[1]+1
            h=heuristic(b)
            f=g+h
            flag=0
            for i in openList:
                if i[0]==b and i[1]<f:
                    flag=1
            for i in closedList:
                if i[0]==b and i[1]<f:
                    flag=1

            if flag==0:
                openList.append([b,f])
                costList.append([b,g])                


        c=upRight_downLeft(v3)
        if c==goal:
            return c
        else:
            for i in costList:
                if i[0]==gearball:
                    g=i[1]+1
            h=heuristic(c)
            f=g+h
            flag=0
            for i in openList:
                if i[0]==c and i[1]<f:
                    flag=1
            for i in closedList:
                if i[0]==c and i[1]<f:
                    flag=1

            if flag==0:
                openList.append([c,f])
                costList.append([c,g])                


        d=upLeft_downRight(v4)
        if d==goal:
            return d
        else:
            for i in costList:
                if i[0]==gearball:
                    g=i[1]+1
            h=heuristic(d)
            f=g+h
            flag=0
            for i in openList:
                if i[0]==d and i[1]<f:
                    flag=1
            for i in closedList:
                if i[0]==d and i[1]<f:
                    flag=1

            if flag==0:
                openList.append([d,f])
                costList.append([d,g])

        e=FrontFaceClockwise_BackFaceAntiClockwise(v5)
        if e==goal:
            return e
        else:
            for i in costList:
                if i[0]==gearball:
                    g=i[1]+1
            h=heuristic(e)
            f=g+h
            flag=0
            for i in openList:
                if i[0]==e and i[1]<f:
                    flag=1
            for i in closedList:
                if i[0]==e and i[1]<f:
                    flag=1

            if flag==0:
                openList.append([e,f])
                costList.append([e,g])                

        m=FrontFaceAntiClockwise_BackFaceClockwise(v6)
        if m==goal:
            return m
        else:
            for i in costList:
                if i[0]==gearball:
                    g=i[1]+1
            h=heuristic(m)
            f=g+h
            flag=0
            for i in openList:
                if i[0]==m and i[1]<f:
                    flag=1
            for i in closedList:
                if i[0]==m and i[1]<f:
                    flag=1

            if flag==0:
                openList.append([m,f])
                costList.append([m,g])                
                

        closedList.append([gearball,minimum])  #Finally add expanded node to closedList
            
# This is the heuristic function which calculates the number of pieces out of place and return that number divided by 36.
        
def heuristic(gearball):
    count=0
    for i in range(1,6):
        for j in range(7,14):
            if i==1:
                if j==7 or j==13:
                    if gearball[i][j]!='G':
                        count=count+1
            if j==10:
                if gearball[i][j]!='G':
                    count=count+1
                    
            if i==3 and j!=9 and j!=11:
                if gearball[i][j]!='G':
                    count=count+1
                        
    for i in range(15,20):
        for j in range(7,14):
            if i==15:
                if j==7 or j==13:
                    if gearball[i][j]!='B':
                        count=count+1
            if j==10:
                if gearball[i][j]!='B':
                    count=count+1
                    
            if i==17 and j!=9 and j!=11:
                if gearball[i][j]!='B':
                    count=count+1

    for i in range(21,26):
        for j in range(7,14):
            if i==21:
                if j==7 or j==13:
                    if gearball[i][j]!='O':
                        count=count+1
            if j==10:
                if gearball[i][j]!='O':
                    count=count+1
                    
            if i==23 and j!=9 and j!=11:
                if gearball[i][j]!='O':
                    count=count+1


    for i in range(7,14):
        for j in range(7,14):
            if i==7:
                if j==7 or j==13:
                    if gearball[i][j]!='Y':
                        count=count+1
            if j==10 and i!=9 and i!=11:
                if gearball[i][j]!='Y':
                    count=count+1
                    
            if i==10 and j!=9 and j!=11:
                if gearball[i][j]!='Y':
                    count=count+1

    for i in range(7,14):
        for j in range(1,6):
            if i==7:
                if j==1 or j==5:
                    if gearball[i][j]!='M':
                        count=count+1
            if j==3 and i!=9 and i!=11:
                if gearball[i][j]!='M':
                    count=count+1
                    
            if i==10:
                if gearball[i][j]!='M':
                    count=count+1

    for i in range(7,14):
        for j in range(15,20):
            if i==7:
                if j==15 or j==19:
                    if gearball[i][j]!='R':
                        count=count+1
            if j==17 and i!=9 and i!=11:
                if gearball[i][j]!='R':
                    count=count+1
                    
            if i==10:
                if gearball[i][j]!='R':
                    count=count+1

                        
    for j in range(25):
        for i in range(25):
            if j==6:
                if i==3 or i==10 or i==17 or  i==23:
                    if gearball[i][j]!='=':
                        count=count+1
            if j==10:
                if i==0 or i==6 or i==14 or  i==20:
                    if gearball[i][j]!='=':
                        count=count+1
            if j==14:
                if i==3 or i==10 or i==17 or  i==23:
                    if gearball[i][j]!='=':
                        count=count+1
                        
        return (int(count/36))
   
    
    
 # In the main function, the code is to store gearball in 2-d list where color blocks are represented by letters   
 # rotating gears are represented by =,/,\ and non-rotating gears are represented by X.
    
def main():
    gearball=[]
    for i in range(24):
        gearball.append([])

    for i in range(6):
        for j in range(25):
            if j in range(6,13):
                if j%3==0 and i%3==0:
                    gearball[i].append('x')
                else:
                    gearball[i].append(' ')
            else:
                gearball[i].append(' ')

    for i in range(6,13):
        for j in range(25):
            if j%3==0 and i%3==0:
                gearball[i].append('x')
            else:
                gearball[i].append(' ')


    for i in range(13,19):
        for j in range(25):
            if j in range(6,13):
                if j%3==0 and i%3==0:
                    gearball[i].append('x')
                else:
                    gearball[i].append(' ')
            else:
                gearball[i].append(' ')


    for i in range(13,24):
        for j in range(25):
            if j in range(6,13):
                if j%3==0 and i%3==0:
                    gearball[i].append('x')
                else:
                    gearball[i].append(' ')
            else:
                gearball[i].append(' ')




    for i in range(1,6):
        for j in range(7,12):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'G')
                if j==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'G')

            else:
                if i==3:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'G')


    for i in range(13,18):
        for j in range(7,12):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'B')
                if j==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'B')

            else:
                if i==15:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'B')

    for i in range(19,24):
        for j in range(7,12):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'O')
                if j==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'O')

            else:
                if i==21:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'O')


    for i in range(7,12):
        for j in range(7,12):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'Y')
                if j==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'Y')

            else:
                if i==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'Y')

    for i in range(7,12):
        for j in range(1,6):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'M')
                if j==3:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'M')

            else:
                if i==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'M')

    for i in range(7,12):
        for j in range(13,18):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'R')
                if j==15:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'R')

            else:
                if i==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'R')

    for i in range(7,12):
        for j in range(19,24):
            if j%2!=0:
                if i%2!=0:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'O')
                if j==21:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'O')

            else:
                if i==9:
                    gearball[i].pop(j)
                    gearball[i].insert(j,'O')

    for i in range(24):
        for j in range(25):
            if j==3 or j==9 or j==15 or j==21:
                if gearball[i][j]=='x':
                    gearball[i].pop(j)
                    gearball[i].insert(j,'=')

            if i==3 or i==15 or i==21:
                if j==6 or j==12:
                    if gearball[i][j]=='x':
                        gearball[i].pop(j)
                        gearball[i].insert(j,'=')

            if i==9:
                if j==0 or j==6 or j==12 or j==18 or j==24:
                    if gearball[i][j]=='x':
                        gearball[i].pop(j)
                        gearball[i].insert(j,'=')


    for i in range(24):
        gearball[i].insert(9,' ')
        gearball[i].insert(11,' ')

    space1=[]
    for i in range(26):
        space1.append(' ')

    space2=[]
    for i in range(26):
        space2.append(' ')


    for i in range(24):
        gearball[i].pop(26)

    gearball.insert(9,space1)
    gearball.insert(11,space2)
    goal=copy.deepcopy(gearball)
    
# Following code represents 2-d list into table format    
    
    s = [[str(e) for e in row] for row in gearball]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    
#Following code asks user to enter value between 5 to 20 to randomize gearball with that number of moves
#It creates 5 different randomized gearballs and produces it's solution

    m=int(input("Please enter the the randomizing parameter k between 5 to 20:"))
    for i in range(5):
        gearball1=randomizer(m,gearball)
        print('\n')
        print('Randomized gearball:')
        
        s = [[str(e) for e in row] for row in gearball1]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))


        gearball2=algorithm(gearball1,goal)   

        print('\n')
        print('Solved gearball:')
        
        s = [[str(e) for e in row] for row in gearball2]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
        
    
if __name__ == "__main__":
    main()


# In[ ]:




# In[ ]:



