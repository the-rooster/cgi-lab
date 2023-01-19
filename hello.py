#!/usr/bin/env python3
import os
import json
import cgi
from templates import *
from secret import *

form = cgi.FieldStorage()

if form.getvalue("username") == username and form.getvalue("password") == password:
   print("Set-Cookie: loggedin=True")

print("Content-Type: text/html\n")
print()
print("<h1>ENV VARIABLES</h1>")
print(dict(os.environ.items()))


print("<h1>QUERY</h1>")
print(os.environ["QUERY_STRING"])

print("<h1>BROWSER INFO</h1>")
print(os.environ["HTTP_USER_AGENT"])

print(login_page())

 

print("<h1>POSTED DATA</h1>")
print(form)


if "loggedin=True" in os.environ["HTTP_COOKIE"]:
    print(secret_page(form.getvalue("username"),form.getvalue("password")))