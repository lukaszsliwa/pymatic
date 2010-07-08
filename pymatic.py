#!/usr/bin/env python
import os, sys

if __name__ == "__main__":

    if len(sys.argv) == 2:
        cmd = sys.argv[1]
        if cmd == 'deploy':
            import pymatic_deploy
        elif cmd == 'init':
            import pymatic_init
        else:
            print 'There is no %s pymatic command' % sys.argv[1]
    else:
        print 'pymatic'

    sys.exit(0)
