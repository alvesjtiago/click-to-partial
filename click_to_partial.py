import sublime
import sublime_plugin
import re
import os

class ClickToPartial(sublime_plugin.TextCommand):
    def run(self, edit, event):
      vector = (event["x"], event["y"])
      point = self.view.window_to_text(vector)
      region = self.view.word(point)
      word = self.view.substr(region)

      if (len(sublime.active_window().folders()) == 0):
        return

      base_folder = sublime.active_window().folders()[0]

      # Find the first file that matches path on file folder
      for root, dirs, files in os.walk(sublime.active_window().extract_variables()["file_path"]):
        for file in files:
          if file.startswith("_" + word):
             file_name = os.path.join(root, file)
             sublime.active_window().open_file(file_name)
             return

      # Find the first file that matches path on entire project folder
      for root, dirs, files in os.walk(base_folder):
        for file in files:
          if file.startswith("_" + word):
            file_name = os.path.join(root, file)
            sublime.active_window().open_file(file_name)
            return

      return
      
    def want_event(self):
      return True