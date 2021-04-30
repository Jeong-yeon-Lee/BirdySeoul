const { stringify } = require('node:querystring');

async function createOrders() {
    const fs = require('fs')
    const file = fs.readFileSync('birds.json');
    const data = await JSON.parse(file.toString())
    console.log(data);

    const mongoose = require('mongoose');
    mongoose.connect('mongodb+srv://sooyoung_shin_1:DyCZUkuCryAXwnPA@cluster0.nukm8.mongodb.net/birdySeoul?retryWrites=true&w=majority',
        { useNewUrlParser: true, useUnifiedTopology: true });
    
    const subSpecies = new mongoose.Schema({
        korName: String,
        
    });

    const orderSchema = new mongoose.Schema({
        name: String,
        korName: String,
        families: Array
    })
}

createOrders();