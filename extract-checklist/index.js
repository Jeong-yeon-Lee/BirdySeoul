"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var fs = require("fs");
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
var parse5 = require('parse5');
var file = fs.readFileSync('checklist_southkorea.html');
var data = file.toString();
var document = parse5.parse(data);
var table = document.childNodes[0].childNodes[1].childNodes[0].childNodes[1];
var count = 0;
var korSpecies = [];
table.childNodes.forEach(function (node) { return __awaiter(void 0, void 0, void 0, function () {
    var eN, sN, kn;
    return __generator(this, function (_a) {
        if (node.nodeName === 'tr') {
            if (node.attrs[0].name !== 'valign') {
                eN = node.childNodes[1].childNodes[0].value;
                sN = node.childNodes[3].childNodes[0].childNodes[0].childNodes[0].value;
                kn = undefined;
                if (node.childNodes[5].childNodes[0]) {
                    kn = node.childNodes[5].childNodes[0].value;
                }
                korSpecies.push({
                    korName: kn, engName: eN, scfName: sN
                });
            }
            //console.log(node.childNodes[3].childNodes[0].childNodes[0].childNodes[0].value);
            count++;
        }
        return [2 /*return*/];
    });
}); });
console.log("number of species : " + count);
var csvFile = fs.readFileSync('eBird-checklist-2019.csv');
var eBirdChecklist = csvFile.toString();
var parser = require('csv-parse');
var orders = [];
parser(eBirdChecklist, function (err, output) {
    console.log(output[0]);
    var entireSpecies = output.filter(function (row) { return row[2] === 'species'; }).map(function (row) {
        return {
            eBirdCode: row[0],
            scientificName: row[4],
            engName: row[3],
            order: row[6],
            family: row[7],
            index: output.findIndex(function (r) { return r[0] === row[0]; })
        };
    });
    var _loop_1 = function (kor) {
        var s = entireSpecies.find(function (s) { return s.scientificName === kor.scfName; });
        if (!s) {
            console.log(kor.engName + " (" + kor.korName + ", " + kor.scfName + ") \uACFC \uC77C\uCE58\uD558\uB294 \uC774\uB984\uC774 \uC5C6\uC2B5\uB2C8\uB2E4");
            return "continue";
        }
        var orderName = s.order;
        var familyName = s.family;
        var species = {
            eBirdCode: s.eBirdCode,
            korName: kor.korName,
            engName: s.engName,
            scientificName: s.scientificName,
            subSpecies: []
        };
        var i = s.index + 1;
        while (output[i][2] === 'subspecies') {
            var subspeciesName = output[i][4];
            species.subSpecies.push({
                korName: undefined,
                postFix: subspeciesName.replace(s.scientificName + " ", "")
            });
            i++;
        }
        if (!orders.find(function (o) { return o.name === orderName; })) {
            orders.push({
                name: orderName,
                families: [],
                korName: ""
            });
        }
        var order = orders.find(function (o) { return o.name === orderName; });
        if (!order.families.find(function (f) { return f.name === familyName; })) {
            order.families.push({
                name: familyName,
                korName: "",
                species: []
            });
        }
        var family = order.families.find(function (f) { return f.name === familyName; });
        family.species.push(species);
    };
    for (var _i = 0, korSpecies_1 = korSpecies; _i < korSpecies_1.length; _i++) {
        var kor = korSpecies_1[_i];
        _loop_1(kor);
    }
    fs.writeFileSync("birds.json", JSON.stringify(orders, null, 4));
});
