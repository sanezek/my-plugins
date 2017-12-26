import subprocess
import sublime, sublime_plugin

class RunFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        name=self.view.file_name()
        print(name)
        print(type(name))
        if name.find('.py')!=-1:
        	subprocess.call('python3 '+name,shell=True)