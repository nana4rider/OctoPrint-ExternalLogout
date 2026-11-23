# OctoPrint External Logout

Redirects OctoPrint's existing Logout action to an external identity provider's logout URL. This is intended for header-authentication deployments using an OIDC-aware proxy such as Cloudflare Access.

## Setup

To install directly from the repository, use this ZIP URL in OctoPrint's Plugin Manager:
<https://github.com/nana4rider/OctoPrint-ExternalLogout/archive/refs/heads/main.zip>

Install the plugin, then open **Settings → Plugin Manager → External Logout** and set **Identity provider logout URL** to the URL provided by your IdP or authentication proxy. When the URL is blank, OctoPrint's normal logout behavior remains active.

The existing Logout action first calls OctoPrint's local logout endpoint to end the current OctoPrint session, then navigates to the configured URL. Configure the IdP's post-logout redirect target there if desired; use a URL that your IdP accepts and allowlists.
