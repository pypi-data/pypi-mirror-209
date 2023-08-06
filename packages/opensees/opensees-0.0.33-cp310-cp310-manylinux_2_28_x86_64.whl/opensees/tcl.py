import os
import sys
import pathlib

try:
    import tkinter
except:
    import tcinter as tkinter

from opensees.library.obj import Component


def TclInterpreter(verbose=False, tcl_lib=None, preload=True):

    if "OPENSEESRT_LIB" in os.environ:
        libOpenSeesRT_path = os.environ["OPENSEESRT_LIB"]

    else:
        import platform
        ext = {
            "Darwin": ".dylib",
            "Linux": ".so",
            "Windows": ".dll"
        }[platform.system()]

        install_dir = pathlib.Path(__file__).parents[0]
        libOpenSeesRT_path = install_dir/f"libOpenSeesRT{ext}"

    if verbose:
        print(f"OpenSeesRT: {libOpenSeesRT_path}", file=sys.stderr)

    interp = tkinter.Tcl()

    if preload:
        interp.eval(f"load {libOpenSeesRT_path}")

    def check():
        interp.after(50, check)

    interp.after(50, check)

    return interp

def eval(script: str):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    """)
    return interp


def dumps(obj):
    if not isinstance(obj, (Component,list,tuple)):
        from opensees.emit import OpenSeesWriter
        return OpenSeesWriter(obj).dump()
    else:
        from opensees.emit.opensees import TclScriptBuilder
        writer = TclScriptBuilder()
        try:
            writer.send(obj)
            if not writer.python_objects:
                return writer.getScript(indexed=True)
            else:
                return writer
        except Exception as e:
            raise e
            # print(writer.getScript(indexed=True), file=sys.stderr)
            # raise ValueError("Cannot dump model with binary objects")


class TclRuntime:
    def __init__(self,  model=None, verbose=False, safe=False, preload=True):
        from functools import partial
        self._partial = partial
        self._c_domain = None
        self._c_rt = None
        self._interp = TclInterpreter(verbose=verbose, preload=preload)

        if not safe:
            self._interp.createcommand("=", self.pyexpr)
            # self._interp.createcommand("import", self.pyimport)
        self._interp.createcommand("export", self.export)


        if model is not None:
            self.send(model)

    @property
    def registry(self):
        registry["UniaxialMaterial"][0].getStress()
        return

    def pyimport(self, *args):
        try:
            lib = __import__(args[0])
            print(lib)
        except:
            self.eval("opensees::import " + " ".join(args))
            return

    def export(self, *args):
        import io
        import os
        import sys
        import json
        import opensees.emit.mesh

        self.eval("print -json .abcd.json")

        with open(".abcd.json", "r") as f:
            model = json.load(f)
            model = model["StructuralAnalysisModel"]
        os.remove(".abcd.json")


        if args[0] == "stdout":
            file = io.StringIO()
        else:
            file = args[0]

        if len(args) > 1:
            fmt = args[1]
        else:
            fmt = "vtk"

        mesh = opensees.emit.mesh.dump(model, args[0], fmt)

        try:
            mesh.write(
                file,          # str, os.PathLike, or buffer/open file
                file_format=fmt,  # optional if first argument is a path; inferred from extension
            )
        except Exception as e:
            print(e, file=sys.stderr)
            # self.eval(f'error {{{e}}}')

        return ""



    def pyexpr(self, *args):
        try:
            import numpy as math
        except:
            import math

        env = math.__dict__
        env["locals"]   = None
        env["globals"]  = None
        env["__name__"] = None
        env["__file__"] = None
        env["__builtins__"] = {}
        for k in self.eval("info globals").split():
            try:
                update = {k: float(self._interp.getvar(k))}
            except:
                continue
            env.update(update)
        try:
            return __builtins__["eval"]((" ".join(args[:])).replace("$",""), env)

        except Exception as e:
            # raise e
            print(e, file=sys.stderr)

    def model(self, ndm, ndf, **kwds):
        # TODO: refactor this function
        """
        model(model: opensees.model)
        model(ndm:int, ndf:int)
        """
        self.eval(f"model basic -ndm {ndm} -ndf {ndf}")


    def send(self, obj, ndm=2, ndf=3, **kwds):
        self.model(ndm=ndm, ndf=ndf)

        m = dumps(obj)

        if isinstance(m, str):
            try:
                self.eval(m)
            except Exception as e:
                print(e, file=sys.stderr)
        else:
            self.eval(m.getIndex())
            from . import OpenSeesPyRT as libOpenSeesRT
            _builder = libOpenSeesRT.get_builder(self._interp.interpaddr())
            for ident,obj in m.python_objects.items():
                tag = self.eval(f"set {ident.tclstr()}")
                _builder.addPythonObject(tag, obj)

            self.eval(m.getScript())

    @property
    def _rt(self):
        if self._c_rt is None:
            from . import OpenSeesPyRT as libOpenSeesRT
            self._c_rt = libOpenSeesRT.getRuntime(self._interp.tk.interpaddr())
        return self._c_rt

    @property
    def _domain(self):
        if self._c_domain is None:
            from . import OpenSeesPyRT as libOpenSeesRT
            self._c_domain = libOpenSeesRT.get_domain(self._rt)
        return self._c_domain

    def getNodeResponse(self, node, typ):
        import numpy as np
        return np.array(self._domain.getNodeResponse(node, typ))

    def getTime(self):
        return self._domain.getTime()

    time = getTime


    @classmethod
    def _as_tcl_arg(cls, arg):
        if isinstance(arg, list):
            return f"{{{''.join(TclRuntime._as_tcl_arg(a) for a in arg)}}}"
        elif isinstance(arg, dict):
            return "{\n" + "\n".join([
              f"{cmd} " + " ".join(TclRuntime._as_tcl_arg(a) for a in val)
                  for cmd, val in kwds
        ]) + "}"
        else:
            return str(arg)

    def _tcl_call(self, arg, *args, **kwds):
        tcl_args = [TclRuntime._as_tcl_arg(arg) for arg in args]
        tcl_args += [
          f"-{key} " + TclRuntime._as_tcl_arg(val)
              for key, val in kwds.items()
        ]
        ret = self._interp.tk.eval(
            f"{arg} " + " ".join(tcl_args))
        return ret if ret != "" else None

    def eval(self, string):
        try:
            return self._interp.tk.eval(string)

        except tkinter._tkinter.TclError as e:
            print(self._interp.getvar("errorInfo"), file=sys.stderr)
            raise e


    def __getattr__(self, attr):
        return self._partial(self._tcl_call, attr)

    def fix(self, nodes, *dofs):
        if not isinstance(nodes,list):
            nodes = [nodes]
        for node in nodes:
            self.eval(f"fix {node} {' '.join(map(str,dofs))}")

    def add_tagged(self, objs):
        for k,v in objs.items():
            if isinstance(k, int):
                self.eval(v.cmd)

Runtime = TclRuntime

#
# Analysis
#
def eigen(script: str, modes=1, verbose=False):
    interp = TclInterpreter()
    interp.eval(f"""

    {script}

    set options(-verbose)  {int(verbose)}
    set options(-numModes) {modes}
    set options(-file) /dev/stdout

    set PI       3.1415159
    set DOFs     {{1 2 3 4 5 6}}
    set nodeList [getNodeTags]

    """ + """
    # Initialize variables `omega`, `f` and `T` to
    # empty lists.
    foreach {omega f T recorders} {{} {} {} {}} {}

    for {set k 1} {$k <= $options(-numModes)} {incr k} {
      lappend recorders [recorder Node -node {*}$nodeList -dof {*}$DOFs "eigen $k";]
    }

    set eigenvals [eigen $options(-numModes)];

    set T_scale 1.0
    foreach eig $eigenvals {
      lappend omega [expr sqrt($eig)];
      lappend f     [expr sqrt($eig)/(2.0*$PI)];
      lappend T     [expr $T_scale*(2.0*$PI)/sqrt($eig)];
    }

    # print info to `stdout`.
    #if {$options(-verbose)} {
    #  # puts "Angular frequency (rad/s): $omega\n";
    #  # puts "Frequency (Hz):            $f\n";
    #  # puts "Periods (sec):             $T\n";
    #}

    if {$options(-file) != 0} {
      source /home/claudio/brace/Scripts/OpenSeesScripts/brace2.tcl
      brace2::io::write_modes $options(-file) $options(-numModes)
    }

    foreach recorder $recorders {
      remove recorder $recorder
    }
    """)
    return interp

