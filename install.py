#!/usr/bin/env python3

import os
import sys

if "HOME" not in os.environ:
    print("HOME is undefined -- are you on Windows or something?")
    sys.exit(1)

gdb_init_target_fn = os.path.join(os.environ["HOME"], ".gdbinit")
if os.path.exists(gdb_init_target_fn):
    print("$HOME/.gdbinit already exists, doing nothing")
    sys.exit(1)

mydir = os.path.dirname(os.path.realpath(__file__))
gdb_init_src_fn = os.path.join(mydir, "gdbinit")

with open(gdb_init_src_fn, "r") as f:
    gdb_init_text = f.read()

path_to_stlpretty = os.path.join(mydir, "stlpretty")
gdb_init_text = gdb_init_text.replace("/path/to/stlpretty", path_to_stlpretty)

with open(gdb_init_target_fn, "w") as f:
    f.write(gdb_init_text)
print("successfully wrote stlpretty .gdbinit")
sys.exit(0)
