import requests

"""
Tests server.py running on virtual machine 3587
"""

r_get = requests.get("http://vcm-3587.vm.duke.edu:5000") # get request
print r_get.text
r_get = requests.get("http://vcm-3587.vm.duke.edu:5000/hello/Suyash") # get request
print r_get.text
r_post = requests.post("http://vcm-3587.vm.duke.edu:5000/sum", json={"a": [0], "b": [1]}) # post request
print r_post.text
r_post = requests.post("http://vcm-3587.vm.duke.edu:5000/distance", json={"a": [0, 0], "b": [0, 1]}) # post request
print r_post.text
r_post = requests.post("http://vcm-3587.vm.duke.edu:5000/distance", json={"a": [-1, 0], "b": [0, 1]}) # post request
print r_post.text
r_post = requests.post("http://vcm-3587.vm.duke.edu:5000/distance", json={"a": [0, 0], "b": [0, 1.5]}) # post request
print r_post.text
