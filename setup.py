from cx_Freeze import  setup, Executable
#para usar modelos/dependencias externas inserir em includes
#, "includes":[]
build_exe_options={"packages":["os"]}

# base = None

# if sys.platform == "win32":
#     base = "Win32GUI"


setup(
    name="invoiceXml",
    version="0.1",
    description="altera XML's",
    options={"build_exe":build_exe_options},
    executables=[Executable("invoiceXml.py")]
)