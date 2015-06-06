# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# sample.py

# Testing ManHill functions

from ManHill.Matrix import Matrix

matrix = Matrix()
with open('sample.json') as json_file:
    matrix.loadFromJson(json_file)

matrix.getEdgesTo("IPA")
matrix.getEdgesFrom("IPA")
