# WSGI Lithium

*A lightweight and dumb HTTP to WSGI server that relies on Python's included batteries.*

This WSGI server is intended to be used in Kubernetes-like environments, where some component handle load-balancing, application crashing, loggin, etc.

## How to install

`pip install wsgi_lithium`

## How to use

`wsgi-lithium -b [::]:8000 module:app`
