import sublime
import sublime_plugin
import re

class ClickToPartial(sublime_plugin.TextCommand):
    def run(self, edit):
        print("Starting parsing partial")
        