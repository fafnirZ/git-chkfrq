import math
import re
import sys
from git import Repo
from pathlib import Path
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os

# NOTE do not have support for h,m,s,ms,ns
allowed_time_units = ["d", "m", "y"] 

def extract_number(date_expr: str) -> int:
  found = re.match(rf'(-?\d+)({"|".join(allowed_time_units)})', date_expr)
  if found:
    return int(found.group(1))
  else:
    raise ValueError("date expr does not conform to regex and or allowed time units")



def parse_relative_time_expr(date_expr: str):
  number = abs(extract_number(date_expr))
  match(date_expr):
    case _ if date_expr.endswith("d"):
      return datetime.now() - relativedelta(days=number)
    case _ if date_expr.endswith("m"):
      return datetime.now() - relativedelta(months=number)
    case _ if date_expr.endswith("y"):
      return datetime.now() - relativedelta(years=number)
    case _ :
      raise ValueError(f"Cannot Parse date_expr {date_expr}")
  
def parse_date_expr(date_expr: str):
  """
  Args:
    date_expr: str
      Examples:
        relative_time:
          7d
          12m
          100y
  """
  is_relative_time_expr = any([date_expr.endswith(unit) for unit in allowed_time_units])
  if is_relative_time_expr:
    # is relative time expr
    return parse_relative_time_expr(date_expr)
  raise ValueError("Only Relative Time Expressions can be parsed right now")


def get_commits(repo: Repo, date_expr: str = None):
  start_time_interval = parse_date_expr(date_expr)
  for commit in repo.iter_commits():
    if datetime.fromtimestamp(commit.committed_date) >= start_time_interval:
      yield commit
    else:
      break

if __name__ == "__main__":
  # get where user is executing the script
  execution_path = os.getcwd()

  # input path relative to the CWD the user is in when executing the script
  relative_path = sys.argv[1]

  # relative to the user's execution context
  path = os.path.join(execution_path, relative_path)

  repo = Repo(path)
 
  commits = list(get_commits(repo, date_expr="6m"))
  if len(commits) < 1:
    raise ValueError("this repo does not have any commits")
  
  head = commits[0]
  tail = commits[-1]

  print(head)
  print(tail)