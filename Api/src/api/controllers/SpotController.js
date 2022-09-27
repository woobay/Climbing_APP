const Spot = require('../models/spot')

exports.getAllSpots = async (req, res) => {
        const limit = parseInt(req.query.limit) || 10
        const page = parseInt(req.query.page) || 1

        if (isNaN(limit) || isNaN(page)) {
                res.status(400).send({
                        errorCode: 'INVALIDE_PARAMETERS',
                        message: 'Parameters must be a int'
                })
                return
        }

        const amountOfSpots = await Spot.countDocuments() 
        
       try {
        return Spot.find()
        .skip(limit * page - limit)
        .limit(limit)
        .sort({name: 1})
        .exec((err, climbingSpots)=> {
                if (err) {
                        res.status(500).send({
                                errorCode: "SERVER_ERROR",
                                message: 'An error occurred while retriving climbingSpots'
                        })
                        return
                } else {
                        res.status(200).send({
                                message: 'CLIMB_SPOTS_RETRIVED_SUCCESFULLY',
                                climbingSpots,
                                totalPages: Math.ceil(amountOfSpots / limit)
                        })
                        return
                }
        })
       } catch (e) {
        res.status(500).send({
                errorCode: 'SERVER_ERROR',
                message: 'An error occurred while retriving climbingSpots'
        })
        return
       }
}


exports.getSpotByName = async (req, res) => {
   
}
