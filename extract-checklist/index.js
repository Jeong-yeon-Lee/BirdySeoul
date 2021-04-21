const { notStrictEqual } = require('assert');
const fs = require('fs');
// const pdf = require('pdf-parse');

// let dataBuffer = fs.readFileSync('checklist_0403_kor.pdf');

// pdf(dataBuffer).then((data) => {    
//     // console.log(data.numpages);
//     // // number of rendered pages
//     // console.log(data.numrender);
//     // // PDF info
//     // console.log(data.info);
//     // // PDF metadata
//     // console.log(data.metadata); 
//     // // PDF.js version
//     // // check https://mozilla.github.io/pdf.js/getting_started/
//     // console.log(data.version);
//     // // PDF text
//     console.log(data.text); 

// })

const parse5 = require('parse5');

const file = fs.readFileSync('checklist_southkorea.html');
const data = file.toString();
const document = parse5.parse(data);
const table = document.childNodes[0].childNodes[1].childNodes[0].childNodes[1];
let count = 0
table.childNodes.forEach(async (node) => {
    if (node.nodeName === 'tr') {
        if (node.attrs[0].name !== 'valign') {
            console.log('============');
            console.log(`영명   : ${node.childNodes[1].childNodes[0].value}`)
            console.log(`학명   : ${node.childNodes[3].childNodes[0].childNodes[0].childNodes[0].value}`);
            if (node.childNodes[5].childNodes[0]) {
                console.log(`한국명 : ${node.childNodes[5].childNodes[0].value}`)
            }
        }
        //console.log(node.childNodes[3].childNodes[0].childNodes[0].childNodes[0].value);
        count++
    }
});
console.log(`number of species : ${count}`)
