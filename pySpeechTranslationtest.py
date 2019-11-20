#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = '/home/pi/Documents/CMUsphinx/pocketsphinx/model'
DATADIR = '/home/pi/Documents/CMUsphinx/pocketsphinx/test/data'

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, '/home/pi/Documents/CMUsphinx/cmusphinx-en-us-8khz-5.2'))
config.set_string('-lm', path.join(MODELDIR, '/home/pi/Documents/CMUsphinx/en-70k-0.1.lm'))
config.set_string('-dict', path.join(MODELDIR, '/home/pi/Documents/CMUsphinx/pocketsphinx/model/en-us/cmudict-en-us.dict'))

decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])