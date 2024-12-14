import pathlib  # noqa: INP001

# Add this module to the parent README file
with open(pathlib.Path("../README.md"), "a") as readme:
    readme.write("* [Day {{cookiecutter.day_number}}: {{cookiecutter.puzzle_name}}](./{{cookiecutter.module_name}}/README.md)")
