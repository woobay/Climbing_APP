const mongoose = require('mongoose')

const climbSpotSchema = new mongoose.Schema({}).add({
    id: String,
    country: String,
    state: String,
    area: String,
    route: {
        name: String,
        grade: String,
        description: String,
        tags: String,
    },
    done: Boolean
})

module.exports = mongoose.model('Spot', climbSpotSchema)