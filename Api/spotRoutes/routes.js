const express = require("express")
const router = express.Router();
const homeController = require('./homeController')

router.get("/spots", homeController.getSpots)


module.exports = router;