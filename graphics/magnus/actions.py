#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/etc", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf magnus_%s-1_all.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
