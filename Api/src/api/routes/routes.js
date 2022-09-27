const express = require("express")
const router = express.Router();
const spotController = require('../controllers/SpotController')
const userController = require('../controllers/UserController')

router.get("/spots", spotController.getAllSpots)
router.get('/spots/search/name/:name', spotController.getSpotByName)
router.get('/spots/search/area/:name', spotController.getSpotByArea)


// router.get('/user/add', userController.addUser)


module.exports = router;