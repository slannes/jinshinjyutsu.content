from jinshinjyutsu.content import _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class IActivitiesSection(model.Schema):

    """Am Activities_section."""

    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Activities section title'),
    )

    description = schema.Text(
        title=_(u'Activities section summary'),
    )

    details = RichText(
        title=_(u'Activities section details'),
        required=True
    )
