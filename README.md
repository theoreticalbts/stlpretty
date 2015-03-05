
Introduction
------------

`stlpretty` includes the GDB Python module for pretty printing support for STL programs, and a script to install it.

Original source for `stlpretty` subdirectory is https://gcc.gnu.org/svn/gcc/trunk/libstdc++-v3/python/libstdcxx/v6/printers.py

Installing
----------

    git clone https://github.com/theoreticalbts/stlpretty
    stlpretty/install.py

The installation creates a `.gdbinit` file in your `HOME` directory which tells GDB to load `stlpretty`.

Uninstalling
------------

Since the only file created by the installation is `.gdbinit`, uninstalling is as simple as

    rm ~/.gdbinit

and then deleting the local copy of `stlpretty` created with `git clone` above.

License
-------

Copy pasted from `printers.py`:

    # This program is free software; you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation; either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.

