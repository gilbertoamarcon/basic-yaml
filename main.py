#!/usr/bin/env python

import yaml

database = {
	'glider-01': {
		'position': {
			'lat': -119.0,
			'lon': 34.0,
			'depth': 150.0,
		},
		'heading': {
			'x': 0.0,
			'y': 0.0,
			'z': 0.0,
		},
		'science': {
			'temperature': 15.0,
			'salinity': 31.0,
			'oxygen': 4.5,
		},
	},
	'glider-02': {
		'position': {
			'lat': -119.0,
			'lon': 34.0,
			'depth': 150.0,
		},
		'heading': {
			'x': 0.0,
			'y': 0.0,
			'z': 0.0,
		},
		'science': {
			'temperature': 15.0,
			'salinity': 31.0,
			'oxygen': 4.5,
		},
	},
}

# The Original Database (On the Server Side)
print "The Original Database (On the Server Side):"
print database

# The 'stringfied' version of the database
print "\nThe 'stringfied' version of the database:"
yaml_string = yaml.dump(database)
print yaml_string




# The 'de-stringfied' version of the database (on the client side)
print "The 'de-stringfied' version of the database (on the client side):"
received_database = yaml.load(yaml_string)
print received_database

