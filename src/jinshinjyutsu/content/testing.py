# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import jinshinjyutsu.content


class JinshinjyutsuContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=jinshinjyutsu.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'jinshinjyutsu.content:default')


JINSHINJYUTSU_CONTENT_FIXTURE = JinshinjyutsuContentLayer()


JINSHINJYUTSU_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JINSHINJYUTSU_CONTENT_FIXTURE,),
    name='JinshinjyutsuContentLayer:IntegrationTesting',
)


JINSHINJYUTSU_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JINSHINJYUTSU_CONTENT_FIXTURE,),
    name='JinshinjyutsuContentLayer:FunctionalTesting',
)


JINSHINJYUTSU_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        JINSHINJYUTSU_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='JinshinjyutsuContentLayer:AcceptanceTesting',
)
