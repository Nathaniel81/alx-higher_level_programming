exports.converter = function (base) {
	return function (nb) {
		return nb.toString(base);
	}
}