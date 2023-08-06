"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

# list of modules you do not want **any** documentation for
modules_to_skip = [
    "log.py",
]
# list of modules that you will manually make documentation for
manual_modules = ["src\\pymultiastar\\__init__.py"]

for path in sorted(Path("src").rglob("*.py")):
    # print(path)
    module_path = path.relative_to("src").with_suffix("")
    doc_path = path.relative_to("src", "pymultiastar").with_suffix(".md")
    full_doc_path = Path("reference", doc_path)
    parts = tuple(module_path.parts)

    if any(str(parts[-1]) in module for module in modules_to_skip):
        print(f"Skipping {path}")
        continue

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()
    # print("full doc path")

    if any(str(parts[-1]) in module for module in manual_modules):
        print(
            f"Manual Module {path}, {full_doc_path}. Added to nav but you must make markdown file!"
        )
    else:
        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            # print(full_doc_path, ident)
            fd.write(f"::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, Path("../") / path)

with mkdocs_gen_files.open("reference/SUMMARY.txt", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
