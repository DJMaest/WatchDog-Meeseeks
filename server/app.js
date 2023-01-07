const express = require('express');
const axios = require("axios");
let bodyParser = require("body-parser");
const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/notification', (req, res) => {

    res.send(req.body)
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});