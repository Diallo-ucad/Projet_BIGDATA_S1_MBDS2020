// bar chart

var data = [{ "situationFamiliale": "Celibataire", "Achat": 34553, "displayed": true }, { "situationFamiliale": "Divorce", "Achat": 52, "displayed": true }, { "situationFamiliale": "En Couple", "Achat": 63445, "displayed": true }, { "situationFamiliale": "Marie", "Achat": 652, "displayed": true }]

// the selection list for filtering the data
var div = d3.select('body')
    .append('div')
    .style('position', 'relative')
    .style('left', '10px')
    .style('top', '30px')

var ul = div.append('ul')

var items = ul.selectAll('li')
    .data(data)
    .enter()
    .append('li')

items.append('input')
    .attr('type', 'checkbox')
    .property('checked', true)
    .on('click', function(d) {
        var checked = this.checked;
        var value = d3.select(this).datum()

        data.forEach(function(d) {
            if (d.situationFamiliale == value.situationFamiliale && d.Achat == value.Achat) {
                console.log('found')
                d.displayed = checked;
            }
        })

        updateChart()
    })

items.append('text')
    .text(d => d.situationFamiliale)

//// chart svg and groups

var margin = { left: 50, right: 10, top: 10, bottom: 20 },
    width = 700,
    height = 500;

var svg = d3.select('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)

var chartGroup = svg.append('g')
    .attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')')

var yScale = d3.scaleBand()
    .domain(data.map(d => d.situationFamiliale))
    .range([height, 0])

var yAxis = d3.axisLeft(yScale)

var xScale = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return d.Achat; })])
    .range([0, width])

var xAxis = d3.axisBottom(xScale)

chartGroup.append('g')
    .attr('class', 'y-axis')
    .attr('transform', 'translate(0,0)')
    .call(yAxis)

chartGroup.append('g')
    .attr('class', 'x-axis')
    .attr('transform', 'translate(0,' + height + ')')
    .call(xAxis)


updateChart()


function updateChart() {
    var validData = data.filter(d => d.displayed)

    yScale.domain(validData.map(d => d.situationFamiliale))
        .range([height, 0])

    chartGroup.select('.y-axis')
        .transition()
        .duration(500)
        .call(yAxis)

    chartGroup
        .selectAll('rect')
        .data(validData)
        .join(
            enter => enter.append('rect')
            .attr('x', 0)
            .attr('class', 'rectangle'),
            update => update,
            exit => exit.remove()
        )
        .on('mouseenter', function(d) {
            var x = d3.event.pageX,
                y = d3.event.pageY;

            d3.selectAll('.tooltip')
                .style('display', 'block')
                .style('left', x + 'px')
                .style('top', y + 'px')
                .html('Achat: ' + d.Achat + '<br> situationFamiliale: $' + d.situationFamiliale)
        })
        .on('mouseleave', function(d) {
            d3.select('.tooltip').transition().duration(500).style('display', 'none')
        })
        .transition()
        .duration(500)
        .attr('y', function(d, i) { return yScale(d.situationFamiliale); })
        .attr('height', yScale.bandwidth())
        .attr('width', function(d) { return xScale(d.Achat); })

    svg.append("text")
        .attr("transform",
            "translate(" + (width / 2) + " ," +
            (height + margin.top + 20) + ")")
        .style("text-anchor", "middle")
        .text("Prix moyens d'Achats");

    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Situation Familiale");
}