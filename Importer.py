import sublime, sublime_plugin


class importerCommand(sublime_plugin.TextCommand):

	def get_characters_html(self,s):
		resources = sublime.find_resources(s+'.html')
		content = sublime.load_resource(resources[0])
		return content


	def run(self, edit):
		self.al=['math','time','turtle']
		self.whith=''
		content=self.get_characters_html('importer')
		self.view.show_popup(content, flags=sublime.HTML, location=-1, max_width=450, on_navigate=self.on_choice_symbol)

	
	def on_choice_symbol(self, symbol):
		if symbol in self.al:
			self.whith=symbol
			content=self.get_characters_html(symbol)
			self.view.show_popup(content, flags=sublime.HTML, location=-1, max_width=450, on_navigate=self.on_choice_symbol)
		elif symbol=='simple':
			self.view.run_command("insert_zero",{'cha':'import '+self.whith+'\n'})
			self.view.hide_popup()
		elif self.whith!='':
			self.view.run_command("insert_zero",{'cha':'from '+self.whith+' import '+symbol+'\n'})
			self.view.hide_popup()
		else:
			self.view.run_command("insert_zero",{'cha':'import '+symbol+'\n'})
			self.view.hide_popup()