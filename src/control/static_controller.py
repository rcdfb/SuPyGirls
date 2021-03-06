#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SuperPython
# Copyright 2013-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# SuperPython é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>


"""Main.py is the top level script.
Loads the Bottle framework and mounts controllers.  Also adds a custom error
handler.
"""
import bottle
from bottle import Bottle, redirect, request, get, static_file
# name and list your controllers here so their routes become accessible.
from . import img_dir, js_dir, css_dir, tpl_dir
# Enable debugging, which gives us tracebacks
bottle.DEBUG = True

# Run the Bottle wsgi application. We don't need to call run() since our
# application is embedded within an App Engine WSGI application server.
appbottle = Bottle()


@appbottle.get('/x')
def home():
    """ Return Hello World at application root URL"""
    prj = request.query.proj
    print("home project /", prj)
    redirect('/main?proj=%s' % prj)


# Static Routes
@get("<_:re:.*favicon.ico>")
def favicon(_):
    return static_file("favicon.ico", root=img_dir)


# Static Routes
@get("/site/<filepath:re:.*\.(html|tpl)>")
def ajs(filepath):
    return static_file(filepath, root=tpl_dir)


# Static Routes
@get("/site/css/<filepath:re:.*\.(js|css)>")
def ajs(filepath):
    return static_file(filepath, root=css_dir)


# Static Routes
@get("/css/<filepath:re:.*\.(js|css|map)>")
def ajs(filepath):
    return static_file(filepath, root=css_dir)


# Static Routes
@get("/js/<filepath:re:.*\.(js|css)>")
def ajs(filepath):
    return static_file(filepath, root=js_dir)


# Static Routes
@get("<filepath:re:.*\.(js|css)>")
def js(filepath):
    return static_file(filepath, root=js_dir)


# Static Routes
@get("/image/<filepath:re:.*\.(png|jpg|svg|gif|ico)>")
def img(filepath):
    return static_file(filepath, root=img_dir)


@appbottle.error(code=404)
def error_404(_):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'
