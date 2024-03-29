const mongoose = require("mongoose")
const Spot = require('./spot')

const userSchema = new mongoose.Schema({}).add({
    id: String,
    name: String,
    email: String,
    spots: [{type: mongoose.Schema.ObjectId}],
    password: String
})

module.exports = mongoose.model('User', user)