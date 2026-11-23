[app]
title = Foner.1.0
package.name = foner10
package.domain = org.hosny
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
icon.filename = %(source.dir)s/icon.png
requirements = python3,pygame
orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1

