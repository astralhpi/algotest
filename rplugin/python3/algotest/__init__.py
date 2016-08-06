import neovim
import os
import checker

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

            result = checker.check(filename, inputfile, outputfile)

            self.nvim.command('echo "%s"' % result)

