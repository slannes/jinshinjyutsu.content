from jinshinjyutsu.content import _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class IActivity(model.Schema):

    """An activity. Activities are managed inside activities_section."""

    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'Activity title'),
    )

    description = schema.Text(
        title=_(u'Activity summary'),
    )

    details = RichText(
        title=_(u'Activity details'),
        required=True
    )
