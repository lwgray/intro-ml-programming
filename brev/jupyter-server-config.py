c = get_config() #noqa

c.ServerApp.ip = '0.0.0.0'

c.ServerApp.open_browser = False

c.ServerApp.allow_root = True
c.ServerApp.password = ''
c.IdentityProvider.token = ''

# Auth is handled by Brev's secure-link proxy, not Jupyter. Behind that proxy,
# the sandboxed iframe JupyterLab uses to preview HTML files sends /files/
# requests without a Referer, which Jupyter's XSRF referer check rejects with
# "403: Blocking request from unknown origin" — allow_origin '*' makes that
# check pass. allow_remote_access covers the non-local Host header case.
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
c.ServerApp.trust_xheaders = True

c.ServerApp.root_dir = '/'

c.ServerApp.terminado_settings = { 'shell_command': ['/bin/bash'] }

c.Application.log_level = 'INFO'
c.Application.logging_config = {
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": "/intro-ml-programming/logs/jupyter-server.log",
            "formatter": "console"
        }
    },
    "loggers": {
        "ServerApp": {
            "level": "INFO",
            "handlers": ["console", "file"]
        }
    }
}
