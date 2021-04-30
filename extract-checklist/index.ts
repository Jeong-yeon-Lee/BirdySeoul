import * as fs from 'fs'
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
const korSpecies: { korName: String | undefined, engName: String, scfName: String }[] = []
table.childNodes.forEach(async (node) => {
    if (node.nodeName === 'tr') {
        if (node.attrs[0].name !== 'valign') {
            const eN: String = node.childNodes[1].childNodes[0].value;
            const sN: String = node.childNodes[3].childNodes[0].childNodes[0].childNodes[0].value;
            let kn: String | undefined = undefined
            if (node.childNodes[5].childNodes[0]) {
                kn = node.childNodes[5].childNodes[0].value
            }
            korSpecies.push({
                korName: kn, engName: eN, scfName: sN
            });
        }
        //console.log(node.childNodes[3].childNodes[0].childNodes[0].childNodes[0].value);
        count++
    }
});
console.log(`number of species : ${count}`)

const csvFile = fs.readFileSync('eBird-checklist-2019.csv');
const eBirdChecklist = csvFile.toString()
const parser = require('csv-parse')
const orders: Order[] = [];

interface Order {
    name: String;
    korName: String | undefined;
    families: Family[];
}

interface Family {
    name: String;
    korName: String | undefined;
    species: Species[]
}

interface Species {
    eBirdCode: String;
    scientificName: String;
    engName: String;
    korName: String | undefined;
    subSpecies: SubSpecies[];
}

interface SubSpecies {
    korName: String | undefined,
    postFix: String
}

parser(eBirdChecklist, async (err, output) => {
    console.log(output[0])

    const entireSpecies: {
        eBirdCode: string,
        scientificName: string,
        order: string,
        family: string,
        engName: string,
        index: number
    }[] = output.filter(row => row[2] === 'species').map(row => {
        return {
            eBirdCode: row[0],
            scientificName: row[4],
            engName: row[3],
            order: row[6],
            family: row[7],
            index: output.findIndex(r => r[0] === row[0])
        }
    })

    for (const kor of korSpecies) {
        const s = entireSpecies.find(s => s.scientificName === kor.scfName)
        if(!s) {
            console.log(`${kor.engName} (${kor.korName}, ${kor.scfName}) 과 일치하는 이름이 없습니다`)
            continue;
        }
        const orderName = s.order;
        const familyName = s.family;
        const species: Species = {
            eBirdCode: s.eBirdCode,
            korName: kor.korName,
            engName: s.engName,
            scientificName: s.scientificName,
            subSpecies: []
        }

        let i = s.index + 1
        while (output[i][2] === 'subspecies') {
            const subspeciesName: string = output[i][4]
            species.subSpecies.push({
                korName: undefined,
                postFix: subspeciesName.replace(s.scientificName + " ", "")
            })
            i++
        }

        if (!orders.find((o) => o.name === orderName)) {
            orders.push({
                name: orderName,
                families: [],
                korName: ""
            })
        }
        const order: Order = orders.find(o => o.name === orderName)
        if (!order.families.find(f => f.name === familyName)) {
            order.families.push({
                name: familyName,
                korName: "",
                species: []
            })
        }
        const family = order.families.find(f => f.name === familyName);
        family.species.push(species);
    }

    

    fs.writeFileSync("birds.json", JSON.stringify(orders, null, 4));

})