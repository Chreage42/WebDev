const webpack = require('webpack');

const config = {
	entry: _dirname + '/js/index.jsx',
	output: {
		pathL _dirname + '/dist',
		filename: 'bundle.js',
	},
	resolve: {
		extensions: ['.js', '.jsx', '.css']
	},
};

module.exports = config;
