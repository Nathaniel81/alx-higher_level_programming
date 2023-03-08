// fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
// 	.then(response => response.json())
// 	.then(data => {
// 		console.log(data.results[0].title);
// 	});

fetch('https://fourtonfish.com/hellosalut/?lang=fr')
	.then(response => response.json())
	.then(data => console.log(data));