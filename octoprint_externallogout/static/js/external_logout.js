$(function () {
    function ExternalLogoutViewModel(parameters) {
        var loginState = parameters[0];
        var settings = parameters[1];

        this.onStartup = function () {
            var originalLogoutSupported = loginState.logoutSupported;
            var originalLogout = loginState.logout;

            loginState.logoutSupported = function () {
                if (originalLogoutSupported.call(loginState)) {
                    return true;
                }
                return !!settings.settings.plugins.octoprint_externallogout.logout_url();
            };

            loginState.logout = function (target, event) {
                var logoutUrl = settings.settings.plugins.octoprint_externallogout.logout_url();

                if (!logoutUrl || originalLogoutSupported.call(loginState)) {
                    return originalLogout.apply(loginState, arguments);
                } else {
                    event.stopPropagation();
                    var logoutRequest = originalLogout.apply(loginState, arguments);
                    if (logoutRequest && logoutRequest.done) {
                        logoutRequest.done(function () {
                            window.location.assign(logoutUrl);
                        });
                    } else {
                        window.location.assign(logoutUrl);
                    }
                    return logoutRequest;
                }
            };
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ExternalLogoutViewModel,
        dependencies: ["loginStateViewModel", "settingsViewModel"]
    });
});
