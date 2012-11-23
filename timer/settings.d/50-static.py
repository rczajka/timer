MEDIA_ROOT = path.join(PROJECT_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = path.join(PROJECT_DIR, 'static/')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None
PIPELINE_CSS = {
    'base': {
        'source_filenames': (
          'css/base.scss',
          'timer/jquery.countdown.css',
        ),
        'output_filename': 'compressed/base.css',
    },
}
PIPELINE_JS = {
    'base': {
        'source_filenames': (
            'timer/jquery.min.js',
            'timer/jquery.countdown.js',
            'timer/jquery.countdown-pl.js',
            'timer/timer.js',
        ),
        'output_filename': 'compressed/base.js',
    },
}

PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_STORAGE = 'pipeline.storage.PipelineFinderStorage'
