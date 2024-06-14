# git-chfrq

## Installation
```
git clone git@github.com:fafnirZ/git-chkfrq.git
cd git-chkfrq/

pip3 install .
```

this should install the `git-chkfrq` command

## Usage
run `git-chkfrq` for some usage instructions and notes


```
Usage: git-chkfrq {path_to_repo} {date_expr}
Example:
 git-chkfrq ./ 9d
 git-chkfrq ./ 1y

allowed date_expression regex: (-)?[0-9]+(d|m|y)
NOTE: it will always be a relative time from now to a point in the past
as you cannot compare with future commits that do not exist
```