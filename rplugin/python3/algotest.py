import neovim
import os
from checker import check

@neovim.plugin
class AlgoTestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('CheckSolution', nargs='1')
    def command(self, pythonfile):
        dirname = os.path.dirname(pythonfile)
        inputfile = os.path.join(dirname, 'input.txt')
        outputfile = os.path.join(dirname, 'output.txt')

        check(pythonfile, inputfile, outputfile)

