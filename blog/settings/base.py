# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *

# Name of the top-level module where you put all your apps.
# If you did not install Playdoh with the funfactory installer script
# you may need to edit this value. See the docs about installing from a
# clone.
PROJECT_MODULE = 'blog'

# Defines the views served for root URLs.
ROOT_URLCONF = '%s.urls' % PROJECT_MODULE

INSTALLED_APPS = list(INSTALLED_APPS) + [
	'django.contrib.admin',
	'django.contrib.messages',
    # Application base, containing global templates.
    '%s.base' % PROJECT_MODULE,
    # Example code. Can (and should) be removed for actual projects.
    '%s.examples' % PROJECT_MODULE,
	'%s.feeds' % PROJECT_MODULE,
	'south',
]

# Note! If you intend to add `south` to INSTALLED_APPS,
# make sure it comes BEFORE `django_nose`.
#INSTALLED_APPS.remove('django_nose')
#INSTALLED_APPS.append('django_nose')


LOCALE_PATHS = (
    os.path.join(ROOT, PROJECT_MODULE, 'locale'),
)

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = (
    'admin',
    'registration',
    'browserid',
)

# BrowserID configuration
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

SITE_URL = 'http://localhost:8000'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/'

TEMPLATE_CONTEXT_PROCESSORS += (
    'django_browserid.context_processors.browserid',
)


# Should robots.txt deny everything or disallow a calculated list of URLs we
# don't want to be crawled?  Default is false, disallow everything.
# Also see http://www.google.com/support/webmasters/bin/answer.py?answer=93710
ENGAGE_ROBOTS = False

# Always generate a CSRF token for anonymous users.
ANON_ALWAYS = True

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.
DOMAIN_METHODS['messages'] = [
    ('%s/**.py' % PROJECT_MODULE,
        'tower.management.commands.extract.extract_tower_python'),
    ('%s/**/templates/**.html' % PROJECT_MODULE,
        'tower.management.commands.extract.extract_tower_template'),
    ('templates/**.html',
        'tower.management.commands.extract.extract_tower_template'),
]

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable JS files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

LOGGING = {
    'loggers': {
        'playdoh': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django_browserid': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}
