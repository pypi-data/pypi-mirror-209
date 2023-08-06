from textual.app import App, ComposeResult
from textual.widgets import Tree

from json_log_viewer.logs.log import JsonLog


class TreeApp(App):
    def __init__(self, json_logs: list[JsonLog]):
        super().__init__()
        self.json_logs = json_logs

    def compose(self) -> ComposeResult:

        tree: Tree[dict] = Tree("")
        tree.root.expand()
        for log in self.json_logs:

            leaf = tree.root.add(
                f"[dim]{log.timestamp.isoformat()}[/dim] "
                f"{log.level.styled_string()} "
                f"\[[dim]{log.source:10}[/dim]] "
                f"— {log.message}"
            )
            add_leaf(leaf, log.extra)
        yield tree


def add_leaf(tree, vals):
    if isinstance(vals, dict):
        for k, v in vals.items():
            leaf = tree.add(k)
            leaf.expand()
            add_leaf(leaf, v)
    elif isinstance(vals, list):
        for v in vals:
            add_leaf(tree, v)
    else:
        tree.add_leaf(str(vals))
