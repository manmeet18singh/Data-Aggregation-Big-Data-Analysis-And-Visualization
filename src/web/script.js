var fs = require("fs");
// Express setup
var express = require('express'),
    app = express();
var port = 8080;

var fs = require("fs");

app.use(express.static(__dirname));

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

app.post("/grabFile", (req, res) =>{
    var path = req.body.file;
    console.log(path);
    var text = fs.readFileSync(path).toString('utf-8');
    // console.log(text);
})


app.listen(port, () => {
    console.log("Server listening on port " + port);
});