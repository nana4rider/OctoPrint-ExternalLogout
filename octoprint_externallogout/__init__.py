import octoprint.plugin

class ExternalLogoutPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return {
            "logout_url": "",
        }

    def get_template_configs(self):
        return [{"type": "settings", "custom_bindings": False}]

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return {"js": ["js/external_logout.js"]}

    ##~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "octoprint_externallogout": {
                "displayName": "External Logout",
                "displayVersion": self._plugin_version,
                "type": "github_release",
                "user": "nana4rider",
                "repo": "OctoPrint-ExternalLogout",
                "current": self._plugin_version,
                "pip": (
                    "https://github.com/nana4rider/OctoPrint-ExternalLogout/"
                    "archive/{target_version}.zip"
                ),
            }
        }


__plugin_name__ = "External Logout"
__plugin_pythoncompat__ = ">=3.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = ExternalLogoutPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
