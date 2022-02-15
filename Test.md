# Mymov

`Mymov` is a shell script for moving files from the current directory to a sub-directory, based on the **last modification** date. It can be used to move files that were modified *before* or *after* a given date. It takes three arguments - 
1. `-O / -N` : where *O* indicates older, and *N* indicates newer than the given date
2. `dd/mm/yyyy` : the date
3.  `dir` name of the target sub-directory (where the files are to be moved)

The syntax is as follows
- To move files modified before the date *dd/mm/yyyy* to *dir*
```console
$ mymov -O dd/mm/yyyy dir
```
- to move files modified on or after the date *dd/mm/yyyy* to *dir*
```console
$ mymov -N dd/mm/yyyy dir
```
If any argument is missing, it will throw an error


It will also throw an error if an extra argument is provided
