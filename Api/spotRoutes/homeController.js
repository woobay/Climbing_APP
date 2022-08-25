const Spot = require('../model/spot')

exports.getSpots = async (req, res) => {
        const spots = await Spot.find({})
        console.log(spots)
  

}