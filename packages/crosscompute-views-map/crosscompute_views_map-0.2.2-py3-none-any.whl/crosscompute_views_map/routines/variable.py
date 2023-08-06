# TODO: Let creator override mapbox css and js
# TODO: Let creator override js template
import json
from os import environ

import geojson
import numpy as np
from crosscompute.routines.interface import Batch
from crosscompute.routines.variable import (
    Element, VariableView)

from ..constants import (
    DECK_JS_URI,
    MAPBOX_CSS_URI,
    MAPBOX_JS_URI,
    MAPBOX_STYLE_URI,
    TURF_JS_URI)
from .asset import (
    MAP_CSS,
    MAP_DECK_SCREENGRID_OUTPUT_HEADER_JS,
    MAP_DECK_SCREENGRID_OUTPUT_JS,
    MAP_MAPBOX_HEADER_JS,
    MAP_MAPBOX_HTML,
    MAP_MAPBOX_LOCATION_INPUT_HEADER_JS,
    MAP_MAPBOX_LOCATION_INPUT_HTML,
    MAP_MAPBOX_LOCATION_INPUT_JS,
    MAP_MAPBOX_OUTPUT_HEADER_JS,
    MAP_MAPBOX_OUTPUT_JS)


class MapMapboxView(VariableView):

    view_name = 'map-mapbox'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    css_texts = [MAP_CSS]
    js_uris = [MAPBOX_JS_URI, TURF_JS_URI]

    def process(self, path):
        with path.open('rt') as f:
            array = np.array(list(geojson.utils.coords(json.load(f))))
        save_map_configuration(array, path)

    def render_output(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        variable_id = self.variable_id
        data_uri = b.get_data_uri(variable_definition, x)
        c = b.get_data_configuration(variable_definition)
        element_id = x.id
        main_text = get_map_html(
            element_id, x.mode_name, self.view_name, variable_id)
        js_texts = [
            "mapboxgl.accessToken = '%s';" % environ['MAPBOX_TOKEN'],
            MAP_MAPBOX_HEADER_JS,
            MAP_MAPBOX_OUTPUT_HEADER_JS,
            MAP_MAPBOX_OUTPUT_JS.render({
                'variable_id': variable_id,
                'element_id': element_id,
                'data_uri': data_uri,
                'bounds': c.get('bounds'),
                'map': get_map_definition(
                    element_id, c, x.layout_settings['for_print']),
                'sources': get_source_definitions(element_id, c, data_uri),
                'layers': get_layer_definitions(element_id, c)})]
        return {
            'css_uris': self.css_uris, 'css_texts': self.css_texts,
            'js_uris': self.js_uris, 'js_texts': js_texts,
            'main_text': main_text}


class MapMapboxLocationView(VariableView):

    view_name = 'map-mapbox-location'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    css_texts = [MAP_CSS]
    js_uris = [MAPBOX_JS_URI]

    def render_input(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        view_name = self.view_name
        data = b.load_data(variable_definition)
        c = b.get_data_configuration(variable_definition)
        element_id = x.id
        if 'value' in data:
            longitude, latitude, zoom = get_location_pack_from_value(
                data['value'])
            c['longitude'], c['latitude'] = longitude, latitude
            c['zoom'] = zoom
        prefix_text = MAP_MAPBOX_LOCATION_INPUT_HTML.render({
            'view_name': view_name, 'element_id': element_id})
        main_text = prefix_text + get_map_html(
            element_id, x.mode_name, view_name, self.variable_id)
        js_texts = [
            "mapboxgl.accessToken = '%s';" % environ['MAPBOX_TOKEN'],
            MAP_MAPBOX_HEADER_JS,
            MAP_MAPBOX_LOCATION_INPUT_HEADER_JS.render({
                'view_name': view_name}),
            MAP_MAPBOX_LOCATION_INPUT_JS.render({
                'element_id': element_id,
                'map': get_map_definition(
                    element_id, c, x.layout_settings['for_print'])})]
        return {
            'css_uris': self.css_uris, 'css_texts': self.css_texts,
            'js_uris': self.js_uris, 'js_texts': js_texts,
            'main_text': main_text}


class MapDeckScreenGridView(VariableView):

    view_name = 'map-deck-screengrid'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    css_texts = [MAP_CSS]
    js_uris = [MAPBOX_JS_URI, DECK_JS_URI]

    def process(self, path):
        with path.open('rt') as f:
            array = np.array(json.load(f))
        save_map_configuration(array, path)

    def render_output(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        variable_id = self.variable_id
        data_uri = b.get_data_uri(variable_definition, x)
        c = b.get_data_configuration(variable_definition)
        element_id = x.id
        mapbox_token = environ['MAPBOX_TOKEN']
        main_text = get_map_html(
            element_id, x.mode_name, self.view_name, variable_id)
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}';",
            MAP_DECK_SCREENGRID_OUTPUT_HEADER_JS,
            MAP_DECK_SCREENGRID_OUTPUT_JS.render({
                'variable_id': variable_id,
                'element_id': element_id,
                'data_uri': data_uri,
                'opacity': c.get('opacity', 0.5),
                'get_position_definition_string': c.get('position', 'd => d'),
                'get_weight_definition_string': c.get('weight', 1),
                'style_uri': c.get('style', MAPBOX_STYLE_URI),
                'bounds': c.get('bounds'),
                'longitude': c.get('longitude', 0),
                'latitude': c.get('latitude', 0),
                'zoom': c.get('zoom', 0),
                'for_print': x.layout_settings['for_print']})]
        return {
            'css_uris': self.css_uris, 'css_texts': self.css_texts,
            'js_uris': self.js_uris, 'js_texts': js_texts,
            'main_text': main_text}


def save_map_configuration(xy_array, source_path):
    try:
        xs = xy_array[:, 0]
        ys = xy_array[:, 1]
    except IndexError:
        d = {'longitude': 0, 'latitude': 0, 'zoom': 0}
    else:
        d = {'longitude': xs.mean(), 'latitude': ys.mean()}
        if len(xs) == 1:
            d['zoom'] = 15
        else:
            d['bounds'] = xs.min(), ys.min(), xs.max(), ys.max()
    with open(str(source_path) + '.configuration', 'wt') as f:
        json.dump(d, f)


def get_map_html(element_id, mode_name, view_name, variable_id):
    return MAP_MAPBOX_HTML.substitute({
        'element_id': element_id,
        'mode_name': mode_name,
        'view_name': view_name,
        'variable_id': variable_id})


def get_map_definition(element_id, variable_configuration, for_print):
    style_uri = variable_configuration.get('style', MAPBOX_STYLE_URI)
    longitude = variable_configuration.get('longitude', 0)
    latitude = variable_configuration.get('latitude', 0)
    zoom = variable_configuration.get('zoom', 0)
    d = {
        'container': element_id,
        'style': style_uri,
        'center': [longitude, latitude],
        'zoom': zoom}
    if for_print:
        d['preserveDrawingBuffer'] = 1
    return d


def get_source_definitions(element_id, variable_configuration, data_uri):
    return variable_configuration.get('sources', [{
        'id': element_id,
        'type': 'geojson',
        'data': data_uri}])


def get_layer_definitions(element_id, variable_configuration):
    definitions = []
    for index, d in enumerate(variable_configuration.get('layers', [{
        'type': 'circle',
    }])):
        if 'id' not in d:
            d['id'] = element_id
        if 'source' not in d:
            d['source'] = element_id
        definitions.append(d)
    return definitions


def get_location_pack_from_value(value):
    try:
        longitude, latitude = value['center']
        zoom = value['zoom']
    except (KeyError, TypeError):
        longitude, latitude, zoom = 0, 0, 0
    return longitude, latitude, zoom
