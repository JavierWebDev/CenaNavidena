import os
import functions.corefile as core
import functions.regCamper as rc

import json
import os

core.MY_DATABASE='data/campus.json'

campus = {}

def NewCamper(camper:dict):
    rc.campers.update(camper)
    core.AddData(camper)