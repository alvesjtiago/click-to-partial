import sublime
import sublime_plugin
import re
import os

class ClickToPartial(sublime_plugin.TextCommand):
    def run(self, edit, event):
      if (len(sublime.active_window().folders()) == 0):
        return

      vector = (event["x"], event["y"])
      point = self.view.window_to_text(vector)
      region = self.view.word(point)
      line_range = self.view.line(region)
      line_content = self.view.substr(line_range).strip()

      matched = self.get_quoted_string(line_content)
      if matched:
        partial_path = matched.group(1)
        file_name = partial_path
        pattern = re.compile(".+\/(.+)$")
        file_name_tmp = pattern.match(partial_path)
        if file_name_tmp:
          file_name = file_name_tmp.group(1)
      else:
        matched = self.get_symbol(line_content)
        if matched:
          partial_path = matched.group(1)
          file_name = partial_path


      # Tries to open absolute path
      pattern = re.compile("(.+)\/.+$")
      dir_path = pattern.match(partial_path)
      if dir_path:
        dir_path = dir_path.group(1)

        dir_path = self.remove_slash(dir_path)
        file_name = self.remove_slash(file_name)

        pattern = re.compile("(^.*app/views)")
        proj_root = pattern.match(self.view.file_name())
        if proj_root:
          proj_root = proj_root.group(1)

          walk_path = os.path.join(proj_root, dir_path)
          if self.look_for_file(file_name, walk_path):
            return


      # Find the first file that matches path on file folder
      walk_path = sublime.active_window().extract_variables()["file_path"]
      if self.look_for_file(file_name, walk_path):
        return


      # Last chance: find the first file that matches path on entire project folder
      base_folder = sublime.active_window().folders()[0]
      self.look_for_file(file_name, base_folder)
      return

    def get_quoted_string(self, line_content):
      pattern = re.compile("^.*render.*?['\"](.*?)['\"].*$")
      matched = pattern.match(line_content)
      if matched:
        return matched
      return False

    def get_symbol(self, line_content):
      pattern = re.compile("^.*render.*?:(.*?),? .*$")
      matched = pattern.match(line_content)
      if matched:
        return matched
      return False

    def remove_slash(self, str):
      if str.startswith("/"):
        return str[1:]
      else:
        return str
      return False

    def look_for_file(self, file_name, walk_path):
      walk = os.walk(walk_path)
      for root, dirs, files in walk:
        for file in files:
          if file.startswith("_" + file_name):
             file_name = os.path.join(root, file)
             sublime.active_window().open_file(file_name)
             return True
      return False

      
    def want_event(self):
      return True
