# OctoPrint-ExternalLogout

Redirects OctoPrint's existing Logout action to an external identity provider's logout URL. This is intended for header-authentication deployments using an OIDC-aware proxy such as Cloudflare Access.

## Setup

Install through OctoPrint's [Plugin Manager](https://docs.octoprint.org/en/main/bundledplugins/pluginmanager.html), or use this URL to install manually:

<https://github.com/nana4rider/OctoPrint-Externallogout/archive/main.zip>

## Configuration

After installation, open **Settings → Plugin Manager → External Logout** and set **Identity provider logout URL** to the URL provided by your IdP or authentication proxy.

When the URL is blank, OctoPrint's normal logout behavior remains active. In header-authentication setups where OctoPrint's built-in logout is unavailable, the plugin ends the local OctoPrint session before redirecting to the configured URL. Configure the IdP's post-logout redirect target there if desired, using a URL that your IdP accepts and allowlists.
