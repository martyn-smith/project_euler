# project_euler

Solutions to (some of) the problems posed by the good folks over at 
[project euler](https://projecteuler.net), mostly in python.

## layout
---

Fairly standard, soure data for large files is located in ./data/. with source code files 
located in the appropriate directory, e.g. ./python/e1.py, ./clojure/.e1.clj.  Where appropriate,
common library functions (e.g. prime generation) are in their own module.

## usage
---

Python scripts can be run directly from the command line (e.g. "python e1.py") or 
by importing the solution function ("Euler_#()") from any file. 

## tests
---

python tests follow standard test discovery rules, and are currently located solely in 
./python/test_all.py

## tools and credits
---

built primarily with python 3.6+, and some with clojure 1.9.0 and gcc 7.3.0.
(Numpy has been used, but only for data import).