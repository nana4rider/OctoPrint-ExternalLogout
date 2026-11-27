$(function () {
    function ExternalLogoutViewModel([loginState, settings]) {
        this.onStartup = function () {
            const originalLogoutSupported = loginState.logoutSupported;
            const originalLogout = loginState.logout;

            loginState.logoutSupported = function () {
                if (originalLogoutSupported.call(loginState)) {
                    return true;
                }
                return !!settings.settings.plugins.octoprint_externallogout.logout_url();
            };

            loginState.logout = function (target, event) {
                const logoutUrl = settings.settings.plugins.octoprint_externallogout.logout_url();

                if (!logoutUrl || originalLogoutSupported.call(loginState)) {
                    return originalLogout.call(loginState, target, event);
                } else {
                    const originalFromResponse = loginState.fromResponse;
                    loginState.fromResponse = function (response) {
                        loginState.fromResponse = originalFromResponse;
                        if (response) {
                            window.location.assign(logoutUrl);
                        }
                    };
                    return originalLogout.call(loginState, target, event);
                }
            };
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ExternalLogoutViewModel,
        dependencies: ["loginStateViewModel", "settingsViewModel"]
    });
});
