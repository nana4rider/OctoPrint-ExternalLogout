---
layout: plugin

id: externallogout
title: OctoPrint-ExternalLogout
description: Adds external identity-provider logout to OctoPrint.
authors:
- nana4rider
license: AGPL-3.0-or-later

date: 2026-11-27

homepage: https://github.com/nana4rider/OctoPrint-ExternalLogout
source: https://github.com/nana4rider/OctoPrint-ExternalLogout
archive: https://github.com/nana4rider/OctoPrint-ExternalLogout/archive/main.zip

tags:
- authentication
- logout

compatibility:
  octoprint:
  - 1.4.0
  python: ">=3.7,<4"

---

OctoPrint-ExternalLogout adds external identity-provider logout to OctoPrint's existing **Logout** action. It is intended for installations that authenticate users through a header-authentication proxy, such as an OIDC-aware reverse proxy.

## Configuration

After installing the plugin, open **Settings → Plugin Manager → External Logout** and enter the logout URL provided by your identity provider or authentication proxy in **External logout URL**.

When a URL is configured and OctoPrint's built-in logout is unavailable, selecting **Logout** initiates OctoPrint's logout request. After its response is received, the browser is redirected to the configured external URL only if the response is truthy. The external service can use its own post-logout redirect setting to return the user to OctoPrint.

If the URL is left blank, the plugin does not redirect and OctoPrint's normal logout behavior is preserved. If OctoPrint already supports its built-in logout, that behavior is also preserved.

Make sure the configured URL and any post-logout return URL are accepted by your identity provider or proxy. Follow your provider's guidance for validating and allowlisting redirect destinations.

This plugin does not provide authentication or configure an identity provider; it only redirects the browser after the OctoPrint logout request.
