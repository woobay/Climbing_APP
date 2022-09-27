const express = require("express")
const router = express.Router();
const spotController = require('../controllers/SpotController')

router.get("/spots", spotController.getAllSpots)
router.get('/spots/search/:name', spotController.getSpotByName)


module.exports = router;