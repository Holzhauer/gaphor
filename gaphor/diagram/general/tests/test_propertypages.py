import pytest

from gaphor.core.eventmanager import EventManager
from gaphor.core.modeling import Comment, ElementFactory
from gaphor.diagram.general.generalpropertypages import CommentItemPropertyPage


@pytest.fixture
def element_factory():
    return ElementFactory(EventManager())


def test_property_page_construction(element_factory):
    comment = element_factory.create(Comment)
    prop_page = CommentItemPropertyPage(comment)

    widget = prop_page.construct()
    text_view = widget.get_children()[-1]

    assert text_view
