
from __future__ import print_function

from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction
from frontend.models import Article, Upvote, Version

"""
===================
Clone DB: Reference
===================

1. Ensure you have installed the `MySQL driver <https://pypi.python.org/pypi/MySQL-python/>`::
  $ pip install MySQL-python

2. Add your database credentiasl to DATABASE in ``website.settings``::
  DATABASES = { ...,
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newsdiff',
        'USER': 'newsdiff',
        'PASSWORD': 'pw',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
  }

3. Sync the new db and run pending migrations::
  $ python frontend/manage.py syncdb
  $ python frontend/manage.py migrate --database=mysql

4. Clone the default db, add ``--forceclean`` to start from zero the destination db::
 $ python frontend/manage.py clonedb --forceclean default mysql
 #-> this could take some time

"""


FROM = 'from_db'
TO = 'to_db'


def clean(model, database):
    obj = model.objects.using(database)
    c = obj.count()
    obj.all().delete()
    return c


class Command(BaseCommand):
    help = 'Clone database'
    args = '<source_db> <destination_db>'
    option_list = BaseCommand.option_list + (
        make_option('--noarticle',
                    action="store_true",
                    default=False,
                    dest='noarticle',
                    help='No clone article items'
        ),
        make_option('--noupvote',
                    action="store_true",
                    default=False,
                    dest='noupvote',
                    help='No clone upvote entries'
        ),
        make_option('--noversion',
                    action="store_true",
                    dest='noversion',
                    default=False,
                    help='No clonne version entries'
        ),
        make_option('--forceclean',
                    action="store_true",
                    default=False,
                    dest='force_clean',
                    help='Drop all objects from the destination database'
        )
    )

    def handle(self, *args, **options):
        source = args[0]
        destiny = args[1]

        dbs = settings.DATABASES.keys()

        if source not in dbs or destiny not in dbs:
            return

        if not options['noarticle']:
            articles_source = Article.objects.using(source)
            total = articles_source.count()
            if options['force_clean']:
                c = clean(Article, destiny)
                print("{} elementos fueron eliminados en la db destino {}".format(
                    c, destiny
                ))
            with transaction.commit_on_success():
                for article in articles_source.all():
                    print("Copiyng article {}/{}\r".format(article.pk, total), end='')
                    article.save(using=destiny, force_insert=True)

        if not options['noupvote']:
            upvote_source = Upvote.objects.using(source)
            total = upvote_source.count()
            if options['force_clean']:
                c = clean(Upvote, destiny)
                print("{} elementos fueron eliminados en la db destino {}".format(
                    c, destiny
                ))

            with transaction.commit_on_success():
                for upvote in upvote_source.all():
                    print("Copiyng upvote id {}/{}\r".format(upvote.pk, total), end='')
                    upvote.save(using=destiny, force_insert=True)

        if not options['noversion']:
            version_source = Version.objects.using(source)
            total = version_source.count()
            if options['force_clean']:
                c = clean(Version, destiny)
                print("{} elementos fueron eliminados en la db destino {}".format(
                    c, destiny
                ))

            with transaction.commit_on_success():
                for version in version_source.all():
                    print("Copiyng version id {}/{}\r".format(version.pk, total), end='')
                    version.save(using=destiny, force_insert=True)
