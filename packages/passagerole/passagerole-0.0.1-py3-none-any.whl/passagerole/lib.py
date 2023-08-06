import io
import logging
import pathlib
import sys

import jinja2
import pkg_resources

_logger = logging.getLogger(__name__)
package = __name__.split(".")[0]
templates_dir = pathlib.Path(pkg_resources.resource_filename(package, "templates"))

dummy_data_path = templates_dir / "authorized_keys_dummy_data"

loader = jinja2.FileSystemLoader(searchpath=templates_dir)
env = jinja2.Environment(loader=loader, keep_trailing_newline=True)


def create_user_data_script(outfile: str, contents: str) -> None:
    out = gen_user_data(aggregated_authoirzed_keys=contents)
    pathlib.Path(outfile).write_text(out)


def path_exists(path: str) -> bool:
    p = pathlib.Path(path).resolve()
    if not p.exists():
        _logger.critical(f"file {p} doesn't exist")
        return False
    return True


def aggregate_keys_files_to_str(paths: list[pathlib.Path]) -> str:
    vfile = io.StringIO()

    for path in paths:
        vfile.write(path.read_text())
        vfile.write("\n")

    return vfile.getvalue()


def gen_user_data(aggregated_authoirzed_keys: str) -> str:
    TEMPLATE_FILE = "userdata_bash_ssh_keys.sh.j2"

    template = env.get_template(TEMPLATE_FILE)
    data = {
        "authorized_keys_contents": aggregated_authoirzed_keys.strip(),
    }
    outputText = template.render(data=data)
    return outputText


def main(authorized_keys_files):
    paths = {pathlib.Path(x) for x in authorized_keys_files}
    paths_copy = paths.copy()
    for path in paths:
        if not path_exists(path):
            paths_copy.remove(path)

    if paths != paths_copy:
        for path in paths_copy - paths:
            _logger.critical(f"can't find path {path}")
        sys.exit(1)

    result = aggregate_keys_files_to_str(paths_copy)
    create_user_data_script("user_data.sh", contents=result)
