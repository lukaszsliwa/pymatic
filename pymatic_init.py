import os
import os.path
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="crh"
__date__ ="$2010-07-08 19:08:30$"

if __name__ == "__main__":

    if os.path.isdir('.pymatic'):
        print '.pymatic already exists'
    else:
        os.mkdir('.pymatic')
        os.mkdir('backup')
