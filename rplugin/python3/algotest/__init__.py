import neovim
import os
from .checker import check

@neovim.plugin
class AlgoTestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('CheckSolution', nargs='*')
    def command(self, args):

        if len(args) == 0:
            args = [self.nvim.current.buffer.name]

        for filename in args:
            dirname = os.path.dirname(filename)
            inputfile = os.path.join(dirname, 'input.txt')
            outputfile = os.path.join(dirname, 'output.txt')

            result = check(filename, inputfile, outputfile)

            self.nvim.command('echo "%s"' % result)

    @neovim.autocmd("BufWritePost", pattern="*.py")
    def on_bufwrite_post(self):
        filename = self.nvim.current.buffer.name

        dirname = os.path.dirname(filename)
        inputfile = os.path.join(dirname, 'input.txt')
        outputfile = os.path.join(dirname, 'output.txt')

        # input/output 파일이 있는 경우에만 실행
        if all([os.path.exists(path) for path in [inputfile, outputfile]]):
            self.nvim.command('CheckSolution %s' % filename)

