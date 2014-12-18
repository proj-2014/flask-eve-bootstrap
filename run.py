# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2014 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os
from eve import Eve

from flask import render_template
from jinja2 import ChoiceLoader, FileSystemLoader

if __name__ == '__main__':
    # Heroku support: bind to PORT if defined, otherwise default to 5000.
    if 'PORT' in os.environ:
        port = int(os.environ.get('PORT'))
        # use '0.0.0.0' to ensure your REST API is reachable from all your
        # network (and not only your computer).
        host = '0.0.0.0'
    else:
        port = 5000
        #host = '127.0.0.1'
        host = '0.0.0.0'

    app = Eve()
    

    #  20141218 
    #  add for bootstrap , copy from flask-shared-templates  
    #  modify the settings.py , add URL_PREFIX = 'api' to default REST, so routes can work
        
    base_dir = os.path.dirname(os.path.realpath(__file__))

    app.jinja_loader = ChoiceLoader([FileSystemLoader(os.path.join(base_dir, 'templates')),
                                     FileSystemLoader(os.path.join(base_dir, 'static', 'templates'))]);
                                     
    app.static_folder = os.path.join(base_dir, 'static')
    
    @app.route('/')
    def hello_world():
        items = [{
            'title': 'Facebook',
            'body': 'Facebook is a social utility that connects people with friends and others who work, study and live around them.'
        }, {
            'title': 'Twitter',
            'body': 'Twitter is an online social networking and microblogging service that enables users to send and read "tweets", which are text messages limited to 140 characters.'
        }, {
            'title': 'LinkedIn',
            'body': 'LinkedIn is a social networking website for people in professional occupations.'
        }];
        return render_template('index.html', items=items )
    
    #  add end   
    
    app.run(host=host, port=port)
