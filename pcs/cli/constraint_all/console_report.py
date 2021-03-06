from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from pcs.cli.constraint.console_report import (
    constraint_plain as constraint_plain_default,
    constraint_with_sets,
)
from pcs.cli.constraint_colocation.console_report import (
    constraint_plain as colocation_plain
)
from pcs.cli.constraint_order.console_report import (
    constraint_plain as order_plain
)
from pcs.cli.constraint_ticket.console_report import (
    constraint_plain as ticket_plain
)


def constraint(constraint_type, constraint_info, with_id=True):
    """
    dict constraint_info  see constraint in pcs/lib/exchange_formats.md
    bool with_id have to show id with options_dict
    """
    if "resource_sets" in constraint_info:
        return constraint_with_sets(constraint_info, with_id)
    return constraint_plain(constraint_type, constraint_info, with_id)

def constraint_plain(constraint_type, options_dict, with_id=False):
    """return console shape for any constraint_type of plain constraint"""
    type_report_map = {
        "rsc_colocation": colocation_plain,
        "rsc_order": order_plain,
        "rsc_ticket": ticket_plain,
    }

    if constraint_type not in type_report_map:
        return constraint_plain_default(constraint_type, options_dict, with_id)

    return type_report_map[constraint_type](options_dict, with_id)

def duplicate_constraints_report(report_item):
    line_list = []
    for constraint_info in report_item.info["constraint_info_list"]:
        line_list.append(
            constraint(report_item.info["constraint_type"], constraint_info)
        )

    return (
        "duplicate constraint already exists{force}\n"
        + "\n".join(["  " + line for line in line_list])
    )
