# Callysto

An app and library to run and resume linear workflows in Bash and Python.

"Callysto" is a play on "Jupyter". What I really wanted was a Jupyter notebook where the state persisted
between runs of the kernel, so the notebook could be resumed from where it left off. I'd still like to figure out
how to do that (some combination of [Dill](https://pypi.org/project/dill/) and custom magics to serialize and
deserialize state to a bash shell), but in the meantime I wrote this much smaller-scoped project to provide some support
for resumable workflows. So like Callisto (Jupiter's second-largest moon) is a much smaller Jupiter, Callysto is a much
smaller version of what I want to do in Jupyter.

# Work in Progress

The README is a work in progress right now. In the meantime, I'm just pasting the "key elements" from 
[Art of Readme](https://github.com/hackergrrl/art-of-readme) below as a reminder on how to structure the README:

# Usage
rather than starting to delve into the API docs, it'd be great to see what the module looks like in action. I can quickly determine whether the example JS fits the desired style and problem. People have lots of opinions on things like promises/callbacks and ES6. If it does fit the bill, then I can proceed to greater detail.

# API 
the name, description, and usage of this module all sound appealing to me. I'm very likely to use this module at this point. I just need to scan the API to make sure it does exactly what I need and that it will integrate easily into my codebase. The API section ought to detail the module's objects and functions, their signatures, return types, callbacks, and events in detail. Types should be included where they aren't obvious. Caveats should be made clear.

# Installation
if I've read this far down, then I'm sold on trying out the module. If there are nonstandard installation notes, here's where they'd go, but even if it's just a regular npm install, I'd like to see that mentioned, too. New users start using Node all the time, so having a link to npmjs.org and an install command provides them the resources to figure out how Node modules work.

# License

[MIT License](https://opensource.org/licenses/MIT)

Copyright 2022 Dathan Bennett

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


