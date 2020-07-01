#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json
import requests
from datetime import datetime

def find_station(stations, name):
    for station in stations:
        if station['station_name'] == name:
            return station

    return None

def find_anno(annos, filename):
    for anno in annos:
        if anno['audio_url'].split("/")[-1] == filename:
            return anno

    return None

def import_json(path):
    with open(path) as f:
        data = json.load(f)
    
    resp = requests.get("http://localhost:5000/channels/")
    stations = resp.json()

    resp = requests.get("http://localhost:5000/recordings/")
    annos = resp.json()

    for anno in data:
        filename = anno['audio_url'].split("/")[-1]
        tags = set(anno['tags'].split(","))
        local_anno = find_anno(annos, filename)
        if local_anno:
            local_tags = set(local_anno['tags'].split(","))
            all_tags = tags.union(local_tags)
            if local_tags != all_tags:
                local_station = find_station(stations, anno['station']['station_name'])
                if not local_station:
                    requests.post("http://localhost:5000/channel/",
                            json={
                                'station_name': anno['station']['station_name'],
                                'station_image': anno['station']['station_image']
                                })
                requests.put("http://localhost:5000/recordings/{}".format(local_anno['id']),
                        json={
                            'audio_url' : filename,
                            'station_name' : anno['station']['station_name'],
                            'img_tags' : anno['img_tags'],
                            'tags' : ",".join(all_tags),
                            'upload_date' : datetime.now().strftime("%Y.%m.%d")
                            })

        else:
            #no local anno, create a new anno.
            local_station = find_station(stations, anno['station']['station_name'])
            if not local_station:
                requests.post("http://localhost:5000/channel/",
                            json={
                                'station_name': anno['station']['station_name'],
                                'station_image': anno['station']['station_image']
                                })

            requests.post("http://localhost:5000/recordings/",
                    json= {
                        'station_name': anno['station']['station_name'],
                        'audio_url': filename,
                        'img_tags': anno['img_tags'],
                        'tags': anno['tags'],
                        'upload_date': anno['upload_date']
                        })

