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

app.post("/grabFile", (req, res) => {
    var path = req.body.file;
    var text = fs.readFileSync(path).toString('utf-8');
    var jsonToSend = {
        "text": text
    }
    res.send(JSON.stringify(jsonToSend));
})


app.listen(port, () => {
    console.log("Server listening on port " + port);
});