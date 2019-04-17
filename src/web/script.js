// Express setup
var express = require("express"),
    app = express();
var port = 8080;

app.use(express.static(__dirname));

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

app.listen(port, () => {
    console.log("Server listening on port " + port);
});

var fs = require("fs");
// var path = data/cc/bleacher/bleacher_wc.txt
var text = fs.readFileSync("../../data/cc/bleacher/bleacher_wc.txt").toString('utf-8');

console.log("ajsdjasdj");


drawCloud(text);

function drawCloud(text) {
    var textByLine = text.split("\n");
    word_count = {};
    temp = [];
    word = "";
    count = 0;
    for (i = 0; i < textByLine.length; i++) {
        temp = textByLine[i].split(" ");
        word_count[temp[0]] = temp[1];
    }

    var svgloc = "#cloud"
    // var width = $(document).width();
    // var height = $(document).height();

    // var fill = d3.scale.category20();

    // var word_entries = d3.entries(word_count);

    // var xScale = d3.scale.linear()
    //     .domain([0, d3.max(word_entries, function (d) {
    //         return d.value;
    //     })])
    //     .range([10, 100]);

    // d3.layout.cloud().size([width, height])
    //     .timeInterval(20)
    //     .words(word_entries)
    //     .fontSize(function (d) {
    //         return xScale(+d.value);
    //     })
    //     .text(function (d) {
    //         return d.key;
    //     })
    //     .rotate(function () {
    //         return ~~(Math.random() * 2) * 90;
    //     })
    //     .font("Impact")
    //     .on("end", draw)
    //     .start();

    // function draw(words) {
    //     d3.select(svg_location).append("svg")
    //         .attr("width", width)
    //         .attr("height", height)
    //         .append("g")
    //         .attr("transform", "translate(" + [width >> 1, height >> 1] + ")")
    //         .selectAll("text")
    //         .data(words)
    //         .enter().append("text")
    //         .style("font-size", function (d) {
    //             return xScale(d.value) + "px";
    //         })
    //         .style("font-family", "Impact")
    //         .style("fill", function (d, i) {
    //             return fill(i);
    //         })
    //         .attr("text-anchor", "middle")
    //         .attr("transform", function (d) {
    //             return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
    //         })
    //         .text(function (d) {
    //             return d.key;
    //         });
    // }

    // d3.layout.cloud().stop();
}