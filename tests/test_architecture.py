import pytest
from pytest_arch import archrule

import gaphor


def test_core():
    (
        archrule("gaphor.core does not depend on the rest of the system")
        .match("gaphor.core*")
        .exclude("*.tests.*")
        .may_import(
            "gaphor.core*",
            "gaphor.abc",
            "gaphor.action",
            "gaphor.i18n",
            "gaphor.transaction",
            "gaphor.event",
        )
        .should_not_import("gaphor*")
        .check(gaphor, skip_type_checking=True)
    )


@pytest.mark.xfail
def test_diagram():
    (
        archrule("Diagrams are part of the core")
        .match("gaphor.diagram*")
        .exclude("*.tests.*")
        .should_not_import("gaphor.ui*")
        .should_not_import(
            "gaphor.C4Model*", "gaphor.RAAML*", "gaphor.SysML*", "gaphor.UML*"
        )
        .check(gaphor)
    )


def test_modeling_languages_do_not_depend_on_ui_package():
    (
        archrule("Modeling languages should not depend on the UI package")
        .match("gaphor.C4Model*", "gaphor.RAAML*", "gaphor.SysML*", "gaphor.UML*")
        .should_not_import("gaphor.ui*")
        .check(gaphor)
    )


def test_uml_package_does_not_depend_on_other_modeling_languages():
    (
        archrule("Modeling languages should not depend on the UI package")
        .match("gaphor.UML*")
        .exclude("*.tests.*")
        .should_not_import("gaphor.C4Model*", "gaphor.RAAML*", "gaphor.SysML*")
        .check(gaphor, only_toplevel_imports=True)
    )
