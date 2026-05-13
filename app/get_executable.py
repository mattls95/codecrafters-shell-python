import os
import shutil


def get_executable(cmd:str) -> (str | None):
   paths = os.environ["PATH"].split(":")
   for path in paths:
      file_path = os.path.abspath(path) + f"/{cmd}"
      if os.path.isfile(file_path):
        if is_executable(file_path):
          return file_path
        else:
            continue
   return None

def is_executable(file_path:str) -> (str | None):
    return shutil.which(file_path)