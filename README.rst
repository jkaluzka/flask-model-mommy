===============
Flask-Model-Mommy
===============

.. image:: https://travis-ci.org/jkaluzka/flask-model-mommy.png?branch=master
   :target: https://travis-ci.org/jkaluzka/flask-model-mommy

Flask-Model-Mommy is an simple package for making testing in Flask easier.
It can create ``model`` instance without bothering about missing relationships
and required fields. This package was inspired by `@vandersonmota <https://github.com/vandersonmota>`_ and his
`model_mommy <https://github.com/vandersonmota/model_mommy>`_ which I recommend
if you are developing applications in Django.


Install
-------

   pip install flask-model-mommy


Usage
-----

Here is an example::

  from flask_model_mommy import mommy

  mommy.make(model_class)

This creates instance of ``model_class`` containing generated data for required fields
and default values if such was provided for field.

For more examples please check [documentation](http://flask-model-mommy.readthedocs.io/en/latest/index.html)