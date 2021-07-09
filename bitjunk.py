# A code injection framework.
import sys

import importlib

def usage():
    print(f"{__file__} type options")
    plugins = os.listdir("./plugins")
    print("Plugins:")
    for p in plugins:
        print(p)
    sys.exit(-1)

if(__name__ == "__main__"):
    if(len(sys.argv) < 3):
        usage()

    try:
        src_module_path = sys.argv[1]
        src_mod = importlib.import_module("plugins"+"."+src_module_path)
        print(f"Using Module: {src_module_path}") 
        module_options = []
        if(len(sys.argv) > 2):
            module_options.extend(sys.argv[2:])
        # DO IT
        getattr(src_mod, "inject")(module_options)

    except Exception as e:
        print("Module Load Error")
        print(e)

    






