import neovim
import os
from .checker import check

@neovim.plugin
class AlgoTestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('CheckSolution', nargs='*')
    def command(self, args):
        for filename in args:
            dirname = os.path.dirname(filename)
            inputfile = os.path.join(dirname, 'input.txt')
            outputfile = os.path.join(dirname, 'output.txt')

            result = check(filename, inputfile, outputfile)

            self.nvim.command('echo "%s"' % result)

