import sublime, sublime_plugin
import re

def make_tab(tab_num):
	    result = ""
	    for j in range(tab_num):
	        result += "\t"

	    return result


def pretty_print_json(data):
    tab_num = 0
    data = str(data)

    data = re.sub("[\n]*", " ", data)
    data = re.sub("[\t]+", " ", data)
    data = re.sub("[ ]+", " ", data)

    result = ""

    for i in range(len(data)):
        if data[i] == '{' or data[i] == '[':
            result += "\n" + make_tab(tab_num) + data[i] + "\n"
            tab_num += 1
            result += make_tab(tab_num)
        elif data[i] == '}' or data[i] == ']':
            result += "\n"
            tab_num -= 1
            result += make_tab(tab_num) + data[i] + "\n" + make_tab(tab_num)
        elif data[i] == ',':
            result += data[i] + "\n" + make_tab(tab_num)
        elif data[i] == ' ':
            result += ''
        else:
            result += data[i]

    result = re.sub("\]\n[\t]*,", "],", result)
    result = re.sub("}\n[\t]*,", "},", result)
    result = re.sub("\n[\t]*[\n]+", "\n", result)

    return result

class Pretty_indentCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		text = self.view.substr(sublime.Region(0, self.view.size()))
		text = pretty_print_json(text)
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, text)
