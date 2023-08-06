# WSGI Lithium

*A lightweight and dumb HTTP to WSGI server that relies on Python's included
batteries.*

This WSGI server is intended to be used in Kubernetes-like environments, where
some component handle load-balancing, application crashing, loggin, etc.

## How to install

`pip install wsgi_lithium`

## How to use

WSGI Lithium **should** be used behind a reverse proxy.

`wsgi-lithium -b [::]:8000 module:app`

### How to set `SCRIPT_NAME` from the HTTP server

Simply configure your reverse proxy to set the `Virtual-Location` header to the
value you want in `SCRIPT_NAME`. You **might** have to rewrite the path with
said reverse proxy.

For example, if you serve an application on `/foo/bar`, where `/bar` is the sub
path, and `/foo` is the "virtual location", set the `Virtual-Location` header to
`/foo` and rewrite the path so it become `/bar`.
