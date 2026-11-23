"""Redirect OctoPrint's existing logout action to an external IdP."""

import octoprint.plugin


class LogoutPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.AssetPlugin,
):
    def get_settings_defaults(self):
        return {"logout_url": ""}

    def get_template_configs(self):
        return [{"type": "settings", "custom_bindings": False}]

    def get_assets(self):
        return {"js": ["js/external_logout.js"]}


__plugin_name__ = "External Logout"
__plugin_pythoncompat__ = ">=3.7,<4"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = LogoutPlugin()
