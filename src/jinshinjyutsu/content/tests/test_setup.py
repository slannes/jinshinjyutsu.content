# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from jinshinjyutsu.content.testing import (
    JINSHINJYUTSU_CONTENT_INTEGRATION_TESTING  # noqa: E501,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that jinshinjyutsu.content is properly installed."""

    layer = JINSHINJYUTSU_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if jinshinjyutsu.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'jinshinjyutsu.content'))

    def test_browserlayer(self):
        """Test that IJinshinjyutsuContentLayer is registered."""
        from jinshinjyutsu.content.interfaces import (
            IJinshinjyutsuContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IJinshinjyutsuContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = JINSHINJYUTSU_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['jinshinjyutsu.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if jinshinjyutsu.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'jinshinjyutsu.content'))

    def test_browserlayer_removed(self):
        """Test that IJinshinjyutsuContentLayer is removed."""
        from jinshinjyutsu.content.interfaces import \
            IJinshinjyutsuContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IJinshinjyutsuContentLayer,
            utils.registered_layers())
