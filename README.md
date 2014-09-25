Todoo
======

Simple TODO tracker.

Inspired by http://lifehacker.com/5155450/todotxt-cli-manages-your-tasks-from-the-command-line

Setup
=====

Download todoo.py

add alias t="path/to/todoo.py" to ~/.profile

Usage
======
Add todo:

    # t add "Remember to upgrade servers"
    #

Add todo with tag:

    # t add "Remember to upgrade servers #vuln"
    #

Add todo with location:

    # t add "Remember to upgrade servers @work"
    #

List todos:
    # t ls
    1) Remember to upgrade servers
    2) Remember to upgrade servers #vuln
    3) Remember to upgrade servers @work
    #

Filter todos:

    # t filter "@work"
    3) Remember to upgrade servers @work
    #

Mark todo 3 done and remove it:

    # t do 3
    #


License
=======

The MIT License (MIT)

Copyright (c) 2014 Antti Jaakkola

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
