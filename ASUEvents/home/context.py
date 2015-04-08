from django.conf import settings

import os


_fonts = list(settings.FONT_CORE) + []
_styles = [i.replace('\\', '/') for i in 
    [os.path.join(settings.PLUGINS_URL, i) for i in settings.STYLES_CORE] + [
        os.path.join(settings.ASSETS_GLOBAL, 'plugins', 'fullcalendar', 'fullcalendar.min.css'),
        os.path.join(settings.ASSETS_GLOBAL, 'css', 'components.css'),
        os.path.join(settings.ASSETS_GLOBAL, 'css', 'plugins.css'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'css', 'layout.css'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'css', 'themes', 'darkblue.css'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'css', 'custom.css'),
    ]
]
_scripts = [i.replace('\\', '/') for i in 
    [os.path.join(settings.PLUGINS_URL, i) for i in settings.PLUGINS_CORE] + [
        os.path.join(settings.ASSETS_GLOBAL, 'plugins', 'moment.min.js'),
        os.path.join(settings.ASSETS_GLOBAL, 'plugins', 'fullcalendar', 'fullcalendar.min.js'),
        os.path.join(settings.ASSETS_GLOBAL, 'scripts', 'metronic.js'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'scripts', 'layout.js'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'scripts', 'quick-sidebar.js'),
        os.path.join(settings.ASSETS_ADMIN, 'pages', 'scripts', 'calendar.js'),
    ]
]
_context = {
    'title': 'Dashboard',
    'subtitle': 'current scheduled events',
    'fonts': _fonts,
    'styles': _styles,
    'scripts': _scripts
}


def context(request):
    return _context

