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

    result = ''
    
    result += ('=' * 30)
    result += ('input')
    result += ('=' * 30)
    result += (input)
    result += ('=' * 30)
    result += ('expected output')
    result += ('=' * 30)
    result += (output)
    result += ('=' * 30)
    result += ('output')
    result += ('=' * 30)
    result += (stdout)
    result += ('=' * 30)
    result += ('run time: %f' % (end_time-start_time))
    result += ('=' * 30)
    if stdout.strip() == output.strip():
        result += ('succeed!')
    elif stderr is not None and len(stderr) > 0:
        result += ('error!')
        result += ('=' * 30)
        result += (stderr)
    else:
        result += ('failed!')

    return result

def main():
    pythonfile = sys.argv[1]
    dirname = os.path.dirname(pythonfile)
    inputfile = os.path.join(dirname, 'input.txt')
    outputfile = os.path.join(dirname, 'output.txt')

    print(check(pythonfile, inputfile, outputfile))

if __name__ == "__main__":
    main()

