# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

# This file implements the endpoints that can be utilized when
# the client needs to make a request with a latitude & longitude
# filter. Typically, when the client requests a list of campgrounds
# or trails local to a zipcode or partial address. Each endpoint
# serves the coordinates as well as the full address of the
# requested location.


from flask import (
    Blueprint, request, url_for, abort, jsonify
)
import campsights.services
import common

bp = Blueprint('coordinates', __name__)


@bp.route('/coordinates/partial_address', methods=['GET'])
def get_coordinates_by_partial_address():
    city = common.sanitize_input_string(request.form['city'])
    state = common.sanitize_input_string(request.form['state'])

    if not city:
        abort(400, 'Please provide a *city* and state.')

    if not state:
        abort(400, 'Please provide a city and *state*.')

    api = campsights.services.Geocode()
    name = "{0}, {1}".format(city, state)
    geoData = api.query_api_for_coordinates_by_name(name)

    if geoData is None:
        abort(400, 'Error: Request failed was a city & state provided?')

    return jsonify(geoData)


@bp.route('/coordinates/zipcode', methods=['GET'])
def get_coordinates_by_zipcode():
    zipcode = common.sanitize_input_string(request.form['zipcode'])

    if not zipcode:
        abort(400, 'Please provide a zipcode.')

    api = campsights.services.Geocode()
    geoData = api.query_api_for_coordinates_by_zipcode(zipcode)

    if geoData is None:
        abort(400, 'Error: Request failed was a zipcode provided?')

    return jsonify(geoData)


@bp.route('/coordinates/specified_trail', methods=['GET'])
def get_coordinates_by_specified_trail():
    trail = common.sanitize_input_string(request.form['trail'])

    if not trail:
        abort(400, 'Please provide the name of a trail.')

    api = campsights.services.Geocode()
    geoData = api.query_api_for_coordinates_by_name(trail)

    if geoData is None:
        abort(400, 'Error: Request failed was a city & state provided?')

    return jsonify(geoData)
