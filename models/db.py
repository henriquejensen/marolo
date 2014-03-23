# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

from gluon.tools import Auth
auth = Auth(db, controller='admin', function='index')

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## auth settings
#auth.settings.login_next = ''
db.define_table('noticia',
                Field('titulo',length=128,notnull=True,unique=True),
                Field('conteudo','text',notnull=True),
                Field('data_hora','datetime', default=request.now, notnull=True),
                Field('permalink',notnull=True,unique=True),
                Field('status',requires=IS_IN_SET(['publicado','não publicado']))
                )

define_table('membros',
             Field('nome',length=64,notnull=True),
             Field('foto','upload'),
             Field('e-mail',requires=IS_EMAIL())
            )

define_table('projeto',
             Field('nome',length=64,notnull=True),
             Field('e-mail',requires=IS_EMAIL(),notnull=True),
             Field('sobre','text',notnull=True)
            )

define_table('eventos',
             Field('data_hora')
            )



            )