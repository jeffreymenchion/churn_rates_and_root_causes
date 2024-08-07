#in your notebook cell
import sys

#path relative to your notebook
sys.path.insert(0, '../src')

#use if your files are in a package
sys.path.insert(0, '..')

#autoreload
%load_ext autoreload
%autoreload 2
