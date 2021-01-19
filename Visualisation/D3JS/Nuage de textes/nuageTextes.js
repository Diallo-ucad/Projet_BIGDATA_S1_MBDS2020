// List of words
var myWords = [
    { marque: "Audi", TauxMoyen: 900.837, NombreMarque: 28852 },
    { marque: "BMW", TauxMoyen: 808.4649, NombreMarque: 28977 },
    { marque: "Dacia", TauxMoyen: 200.7554, NombreMarque: 1345 },
    { marque: "Daihatsu", TauxMoyen: 200.7901, NombreMarque: 2153 },
    { marque: "Fiat", TauxMoyen: 416.1036, NombreMarque: 7595 },
    { marque: "Ford", TauxMoyen: 419.2115, NombreMarque: 7562 },
    { marque: "Jaguar", TauxMoyen: 889.6697, NombreMarque: 18498 },
    { marque: "Kia", TauxMoyen: 200.593, NombreMarque: 2236 },
    { marque: "Lancia", TauxMoyen: 364.7798, NombreMarque: 1290 },
    { marque: "Mercedes", TauxMoyen: 709.8822, NombreMarque: 14816 },
    { marque: "Mini", TauxMoyen: 797.6129, NombreMarque: 1617 },
    { marque: "Nissan", TauxMoyen: 201.37, NombreMarque: 6802 },
    { marque: "Peugeot", TauxMoyen: 432.8853, NombreMarque: 9386 },
    { marque: "Renault", TauxMoyen: 418.8897, NombreMarque: 24897 },
    { marque: "Saab", TauxMoyen: 706.6363, NombreMarque: 8277 },
    { marque: "Seat", TauxMoyen: 200.3612, NombreMarque: 2168 },
    { marque: "Skoda", TauxMoyen: 201.9936, NombreMarque: 3307 },
    { marque: "Volkswagen", TauxMoyen: 425.7949, NombreMarque: 15350 },
    { marque: "Volvo", TauxMoyen: 421.1081, NombreMarque: 12244 }
];

// set the dimensions and margins of the graph
var margin = { top: 10, right: 10, bottom: 10, left: 10 },
    width = 450 - margin.left - margin.right,
    height = 450 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3
    .select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
// Wordcloud features that are different from one word to the other must be here
var layout = d3.layout
    .cloud()
    .size([width, height])
    .words(
        myWords.map(function(d) {
            return { text: d.marque, size: d.NombreMarque };
        })
    )
    .padding(5) //space between words
    .rotate(function() {
        return ~~(Math.random() * 2) * 90;
    })
    .fontSize(function(d) {
        return d.size;
    }) // font size of words
    .on("end", draw);
layout.start();

// This function takes the output of 'layout' above and draw the words
// Wordcloud features that are THE SAME from one word to the other can be here
function draw(words) {
    svg
        .append("g")
        .attr(
            "transform",
            "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")"
        )
        .selectAll("text")
        .data(words)
        .enter()
        .append("text")
        .style("font-size", function(d) {
            return d.size;
        })
        .style("fill", "#69b3a2")
        .attr("text-anchor", "middle")
        .style("font-family", "Impact")
        .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) {
            return d.text;
        });
}
console.log(myWords)