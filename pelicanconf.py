AUTHOR = 'Gonzalo Rubio-Casas'
SITENAME = 'Gonzalo Rubio-Casas'
SITEURL = ""

PATH = "content"
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'favicon.ico': {'path': 'content/images/favicon.ico'},
}

TIMEZONE = 'Europe/Madrid'

THEME = "themes/my-theme"
STYLESHEET_URL = 'theme/css/style.css'
EXTERNAL_LIBS = [
    {"rel": "stylesheet", "url": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"}
]

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIALS = [
    {"url": "https://github.com/gzrubio/", "icon": "github", "text": "gzrubio"},
    {"url": "https://www.linkedin.com/in/gonzalo-rubio-casas/", "icon": "linkedin", "text": "gonzalo.rubio.casas"}
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ANALYTICS = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-L2Q3911H0V"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-L2Q3911H0V');
    </script>
"""
