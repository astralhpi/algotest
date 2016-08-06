from subprocess import Popen, PIPE
import subprocess
import sys
import os
import time

def check(pythonfile, inputfile, outputfile):
    with open(inputfile) as f:
        input = f.read()
    with open(outputfile) as f:
        output = f.read()

    p = Popen(['python', pythonfile], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    
    start_time = time.time()
    stdout, stderr = p.communicate(input)
    end_time = time.time()
    
    print('=' * 30)
    print('input')
    print('=' * 30)
    print(input)
    print('=' * 30)
    print('expected output')
    print('=' * 30)
    print(output)
    print('=' * 30)
    print('output')
    print('=' * 30)
    print(stdout)
    print('=' * 30)
    print('run time: %f' % (end_time-start_time))
    print('=' * 30)
    if stdout.strip() == output.strip():
        print('succeed!')
    elif stderr is not None and len(stderr) > 0:
        print('error!')
        print('=' * 30)
        print(stderr)
    else:
        print('failed!')

def main():
    pythonfile = sys.argv[1]
    dirname = os.path.dirname(pythonfile)
    inputfile = os.path.join(dirname, 'input.txt')
    outputfile = os.path.join(dirname, 'output.txt')

    check(pythonfile, inputfile, outputfile)

if __name__ == "__main__":
    main()

