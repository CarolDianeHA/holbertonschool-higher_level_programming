#!/usr/bin/node
const number = process.argv[2];
const phrase = 'C is fun';

if (number){
    for (let i = 0; i < number; i++){
        console.log(phrase);
    }
} else {
    console.log("Missing number of occurrences")
}
