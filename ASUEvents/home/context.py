from django.conf import settings

import os

def context_fonts(request):
    return {
        'fonts': [
            (
                'http://fonts.googleapis.com/css?family=Open+Sans'
                ':400,300,600,700&subset=all'
            ),
        ]
    }


def context_styles(request):
    core_styles = [
        os.path.join(settings.PLUGINS_URL, i) for i in settings.STYLES_CORE
    ]
    page_styles = [
        os.path.join(settings.ASSETS_ADMIN, 'pages', 'css', 'tasks.css')
    ]
    core_styles.extend(page_styles)
    theme_styles = [
        os.path.join(settings.ASSETS_GLOBAL, 'css', 'components.css'),
        os.path.join(settings.ASSETS_GLOBAL, 'css', 'plugins.css'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'css', 'layout.css'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'css', 'themes', 'darkblue.css'),
        os.path.join(settings.ASSETS_ADMIN, 'layout', 'css', 'custom.css')
    ]
    core_styles.extend(theme_styles)
    return {
        'styles': [
            i.replace('\\', '/') for i in core_styles
        ]
    }

def context_scripts(request):
    return {
        'scripts': [
            os.path.join(settings.PLUGINS_URL, i).replace('\\', '/') \
                    for i in settings.PLUGINS_CORE
        ]
    }
