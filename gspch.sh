#!/bin/bash
say() { local IFS=+;/usr/bin/omxplayer  "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=En-us"; }
say $*
