import neovim
import os
import sys

@neovim.plugin
class AlgoTestPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('CheckSolution', nargs='1')
    def command(self, pythonfile):
        self.nvim.command('echo "%s"' % __file__)

