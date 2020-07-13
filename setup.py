import cx_Freeze
executables = [cx_Freeze.Executable("Visualiser.py")]

cx_Freeze.setup(
    name="Sorting",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["sort.png","back2.jpg"]}},
    executables = executables

    )