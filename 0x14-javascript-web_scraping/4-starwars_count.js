#!/usr/bin/node
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error === null) {
    const jsonData = JSON.parse(body);
    let count = 0;
    for (const resultIndex in jsonData.results) {
      const film = jsonData.results[resultIndex];
      for (const characterIndex in film.characters) {
        const character = film.characters[characterIndex];
        if (character.endsWith('/18/')) count += 1;
      }
    }
    console.log(count);
  }
});
/*const url = 'https://swapi-api.hbtn.io/api/films/5'

req(url, (err, res, data)=>{
	if (err){console.log(err);}
	else {
		let r = JSON.parse(data);
		var lst = r.characters.filter((char)=>
			char.includes('https://swapi-api.hbtn.io/api/people/82/')
		);
		console.log(lst.length);
	};
});*/