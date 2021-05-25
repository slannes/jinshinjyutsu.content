from jinshinjyutsu.content import _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class ISkill(model.Schema):

    """A skill. Skills are managed inside skills_section."""

    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Skill title'),
    )

    description = schema.Text(
        title=_(u'Skill summary'),
    )

    details = RichText(
        title=_(u'Skill details'),
        required=True
    )
