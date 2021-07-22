from jinshinjyutsu.content import _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class ISkillsSection(model.Schema):

    """A skills_section."""

    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Skills section title'),
    )

    description = schema.Text(
        title=_(u'Skills section summary'),
    )

    details = RichText(
        title=_(u'Skills section details'),
        required=True
    )
