import neovim
import os
from .checker import check

@neovim.plugin
class AlgoTestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('CheckSolution', nargs='*', sync=True)
    def command(self, args):

        if len(args) == 0:
            args = [self.nvim.current.buffer.name]

        buffer = self.create_or_get_buffer('__algotest_result')
        self.clear_buffer(buffer)

        for filename in args:
            dirname = os.path.dirname(filename)
            inputfile = os.path.join(dirname, 'input.txt')
            outputfile = os.path.join(dirname, 'output.txt')

            result = check(filename, inputfile, outputfile)

            self.append_text(buffer, result)


    @neovim.autocmd("BufWritePost", pattern="*.py", sync=True)
    def on_bufwrite_post(self):
        filename = self.nvim.current.buffer.name

        dirname = os.path.dirname(filename)
        inputfile = os.path.join(dirname, 'input.txt')
        outputfile = os.path.join(dirname, 'output.txt')

        # input/output 파일이 있는 경우에만 실행
        if all([os.path.exists(path) for path in [inputfile, outputfile]]):
            self.nvim.command('CheckSolution %s' % filename)

    def create_or_get_buffer(self, name):
        # 이미 있는 버퍼 중, 이름이 일치하는 버퍼가 있으면 리턴
        for b in self.nvim.buffers:
            bname = os.path.basename(b.name)

            if bname == name:
                return b

        # 새 버퍼 생성
        self.nvim.command('set splitright')
        self.nvim.command('vnew')

        b = self.nvim.current.buffer
        b.name = name
        self.nvim.command("setlocal buftype=nofile noswapfile")
        return  b

    def clear_buffer(self, buffer):
        buffer[:] = []
    
    def append_text(self, buffer, text):
        lines = text.splitlines()
        buffer[len(buffer):] = lines

