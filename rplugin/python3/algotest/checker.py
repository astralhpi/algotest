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
    stdout, stderr = p.communicate(bytes(input, 'utf-8'))
    stdout = str(stdout, 'utf-8')
    stderr = str(stderr, 'utf-8')
    end_time = time.time()

    result = ''
    
    result += '=' * 30 + '\n'
    result += 'input\n'
    result += '=' * 30 + '\n'
    result += input + '\n'
    result += '=' * 30 + '\n'
    result += 'expected output' + '\n'
    result += '=' * 30 + '\n'
    result += output + '\n'
    result += '=' * 30 + '\n'
    result += 'output' + '\n'
    result += '=' * 30 + '\n'
    result += stdout + '\n'
    result += '=' * 30 + '\n'
    result += 'run time: %f' % (end_time-start_time) + '\n'
    result += '=' * 30 + '\n'
    if stdout.strip() == output.strip():
        result += 'succeed!' + '\n'
    elif stderr is not None and len(stderr) > 0:
        result += 'error!' + '\n'
        result += '=' * 30 + '\n'
        result += stderr + '\n'
    else:
        result += 'failed!' + '\n'

    return result

def main():
    pythonfile = sys.argv[1]
    dirname = os.path.dirname(pythonfile)
    inputfile = os.path.join(dirname, 'input.txt')
    outputfile = os.path.join(dirname, 'output.txt')

    print(check(pythonfile, inputfile, outputfile))

if __name__ == "__main__":
    main()

