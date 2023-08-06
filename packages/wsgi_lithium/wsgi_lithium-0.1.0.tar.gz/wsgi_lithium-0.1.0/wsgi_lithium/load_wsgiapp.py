# This code was shamelessly stolen from the great Gunicorn project.



# 2009-2018 (c) Benoît Chesneau <benoitc@e-engura.org>
# 2009-2015 (c) Paul J. Davis <paul.joseph.davis@gmail.com>

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


import ast
import importlib
import logging
import os
import sys
import traceback


class AppImportError(Exception):
    """ Exception raised when loading an application """


def _called_with_wrong_args(f):
    """Check whether calling a function raised a ``TypeError`` because
    the call failed or because something in the function raised the
    error.

    :param f: The function that was called.
    :return: ``True`` if the call failed.
    """
    tb = sys.exc_info()[2]

    try:
        while tb is not None:
            if tb.tb_frame.f_code is f.__code__:
                # In the function, it was called successfully.
                return False

            tb = tb.tb_next

        # Didn't reach the function.
        return True
    finally:
        # Delete tb to break a circular reference in Python 2.
        # https://docs.python.org/2/library/sys.html#sys.exc_info
        del tb


def import_app(module):
    parts = module.split(":", 1)
    if len(parts) == 1:
        obj = "application"
    else:
        module, obj = parts[0], parts[1]

    try:
        mod = importlib.import_module(module)
    except ImportError:
        if module.endswith(".py") and os.path.exists(module):
            msg = "Failed to find application, did you mean '%s:%s'?"
            raise ImportError(msg % (module.rsplit(".", 1)[0], obj))
        raise

    # Parse obj as a single expression to determine if it's a valid
    # attribute name or function call.
    try:
        expression = ast.parse(obj, mode="eval").body
    except SyntaxError:
        raise AppImportError(
            "Failed to parse %r as an attribute name or function call." % obj
        )

    if isinstance(expression, ast.Name):
        name = expression.id
        args = kwargs = None
    elif isinstance(expression, ast.Call):
        # Ensure the function name is an attribute name only.
        if not isinstance(expression.func, ast.Name):
            raise AppImportError("Function reference must be a simple name: %r" % obj)

        name = expression.func.id

        # Parse the positional and keyword arguments as literals.
        try:
            args = [ast.literal_eval(arg) for arg in expression.args]
            kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in expression.keywords}
        except ValueError:
            # literal_eval gives cryptic error messages, show a generic
            # message with the full expression instead.
            raise AppImportError(
                "Failed to parse arguments as literal values: %r" % obj
            )
    else:
        raise AppImportError(
            "Failed to parse %r as an attribute name or function call." % obj
        )

    is_debug = logging.root.level == logging.DEBUG
    try:
        app = getattr(mod, name)
    except AttributeError:
        if is_debug:
            traceback.print_exception(*sys.exc_info())
        raise AppImportError("Failed to find attribute %r in %r." % (name, module))

    # If the expression was a function call, call the retrieved object
    # to get the real application.
    if args is not None:
        try:
            app = app(*args, **kwargs)
        except TypeError as e:
            # If the TypeError was due to bad arguments to the factory
            # function, show Python's nice error message without a
            # traceback.
            if _called_with_wrong_args(app):
                raise AppImportError(
                    "".join(traceback.format_exception_only(TypeError, e)).strip()
                )

            # Otherwise it was raised from within the function, show the
            # full traceback.
            raise

    if app is None:
        raise AppImportError("Failed to find application object: %r" % obj)

    if not callable(app):
        raise AppImportError("Application object must be callable.")
    return app
