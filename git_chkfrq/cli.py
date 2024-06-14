import json
import sys
from git import Repo
import os
from git_chkfrq.utils import (
  get_diff_file, continguous_zip, get_commits, 
)

def main():
  #####################################
  # hashmap                           #
  # key: filepath                     #
  # value: tally of number of changes #
  #####################################
  occurence_map = {}


  if len(sys.argv) != 3:
    print("Usage: python3 -m git-chfrq {path_to_repo} {date_expr}")
    exit(1)

  # get where user is executing the script
  execution_path = os.getcwd()

  # input path relative to the CWD the user is in when executing the script
  relative_path = sys.argv[1]

  # get date expression
  date_expression = sys.argv[2]

  # relative to the user's execution context
  path = os.path.join(execution_path, relative_path)

  # try to initialise given path as a git repo object
  repo = Repo(path)
  
  # fetches commits based off a parsable date_expression
  commits = list(get_commits(repo, date_expr=date_expression))
  if len(commits) < 1:
    raise ValueError("this repo does not have any commits")
  
  # calculate the diffs between each contiguous commits
  # and tally up all file changes
  for pairs in continguous_zip(commits):
    c1, c2 = pairs
    # git.diff.Diff
    # https://gitpython.readthedocs.io/en/stable/reference.html?highlight=git.diff.Diff#git.diff.Diff
    diffs = c1.diff(c2)
    for diff in diffs:
      file_path = get_diff_file(diff)
      
      if file_path not in occurence_map:
        occurence_map[file_path] = 1
      else:
        occurence_map[file_path] += 1

  
  # now calculate frequency based off total file changes
  total_file_changes = sum(occurence_map.values())
  frequency_map = { key: value/total_file_changes for key, value in occurence_map.items() }
  frequency_map_sorted = dict(sorted(frequency_map.items(), key=lambda item: item[1]))

  # prints frequency sorted
  print(json.dumps(
    frequency_map_sorted,
    indent=2
  ))