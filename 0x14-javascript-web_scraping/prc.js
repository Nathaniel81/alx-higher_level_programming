//
// fetch('https://jsonplaceholder.typicode.com/todos/1')
// 	.then(response=>response.json())
// 	.then(data=>console.log(data))
// 	.catch(error=>console.error(error));
const fs = require('fs')
const req = require('request')
const path = process.argv[2]
const text = process.argv[3]
// fs.readFile(path, (err, data)=>{
// 	if (err){console.log(err);
// 	//throw err;
// 	}
// 	console.log(data.toString());
// });

// fs.writeFile(path, text, (err)=>{
// 	if (err){console.log(err);}
// });


// const url = 'https://www.google.com'
// req(url, {json: true}, (err, res, data)=>{
// 	if (err){console.log(err);}
// 	else {console.log(res.statusCode);}
// });


// const request = require('request');

// const apiURL = 'https://swapi-api.alx-tools.com/api/films/';
// const characterID = 18;

// // Make a request to the Star Wars API films endpoint
// request(apiURL, (error, response, body) => {
//   if (error) {
//     console.error(error);
//   } else {
//     // Parse the response body as JSON
//     const films = JSON.parse(body).results;

//     // Filter the films array to include only the ones where Wedge Antilles is present
//     const wedgeFilms = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`));

//     // Print the number of films where Wedge Antilles is present
//     console.log(`Wedge Antilles appears in ${wedgeFilms.length} films.`);
//   }
// });

const url = 'https://swapi-api.hbtn.io/api/films/5'

// req(url, (err, res, data)=>{
// 	if (err){console.log(err);}
// 	else {
// 		let r = JSON.parse(data);
// 		var lst = r.characters.filter((char)=>
// 			char.includes('https://swapi-api.hbtn.io/api/people/82/')
// 		);
// 		console.log(lst.length);
// 	};
// });
req(url, {json: true}, (err, res, body) => {
	if (err){console.log(err);}
	else {
		for(const idx in body.characters){
			console.log(idx);
		}
	}});

