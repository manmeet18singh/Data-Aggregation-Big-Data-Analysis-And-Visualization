// Express setup
var express = require('express'),
    app = express();
var port = 8080;

app.use(express.static(__dirname));

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.listen(port, () => {
    console.log("Server listening on port " + port);
});

var fs = require("fs");
// var path = data/cc/bleacher/bleacher_wc.txt
var text = fs.readFileSync("../../data/cc/bleacher/bleacher_wc.txt").toString('utf-8');
var textByLine = text.split("\n");
console.log(textByLine);