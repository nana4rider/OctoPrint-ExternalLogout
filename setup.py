from setuptools import setup

PLUGIN_IDENTIFIER = "octoprint_externallogout"
PLUGIN_NAME = "External Logout"
PLUGIN_VERSION = "1.0.0"
PLUGIN_PACKAGES = ["octoprint_externallogout"]
PLUGIN_REQUIRES = []


setup(
    name="OctoPrint-ExternalLogout",
    version=PLUGIN_VERSION,
    description="Adds a header link to log out through an external identity provider.",
    packages=PLUGIN_PACKAGES,
    include_package_data=True,
    install_requires=PLUGIN_REQUIRES,
    entry_points={
        "octoprint.plugin": [
            "octoprint_externallogout = octoprint_externallogout"
        ]
    },
)
