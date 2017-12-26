import sublime, sublime_plugin

class InsertZeroCommand(sublime_plugin.TextCommand):
    def run(self, edit,cha):
        self.view.insert(edit, 0, cha)

