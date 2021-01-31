//var data = [{"age":18,"TotalPrix":35253.3256,"NombreClients":2472},{"age":19,"TotalPrix":35361.7098,"NombreClients":2457},{"age":20,"TotalPrix":35163.5935,"NombreClients":2519},{"age":21,"TotalPrix":35706.179,"NombreClients":2491},{"age":22,"TotalPrix":36773.1007,"NombreClients":2383},{"age":23,"TotalPrix":34439.479,"NombreClients":2453},{"age":24,"TotalPrix":34976.684,"NombreClients":2449},{"age":25,"TotalPrix":35360.3947,"NombreClients":2460},{"age":26,"TotalPrix":34604.0729,"NombreClients":2497},{"age":27,"TotalPrix":35370.6577,"NombreClients":2442},{"age":28,"TotalPrix":34067.7064,"NombreClients":2503},{"age":29,"TotalPrix":35647.7829,"NombreClients":2418},{"age":30,"TotalPrix":35316.2226,"NombreClients":1689},{"age":31,"TotalPrix":35362.7426,"NombreClients":1612},{"age":32,"TotalPrix":36235.5379,"NombreClients":1647},{"age":33,"TotalPrix":33934.4044,"NombreClients":1699},{"age":34,"TotalPrix":34801.2273,"NombreClients":1575},{"age":35,"TotalPrix":34495.4317,"NombreClients":1654},{"age":36,"TotalPrix":34679.4221,"NombreClients":1687},{"age":37,"TotalPrix":35896.8484,"NombreClients":1610},{"age":38,"TotalPrix":36482.6754,"NombreClients":1719},{"age":39,"TotalPrix":34940.7786,"NombreClients":1608},{"age":40,"TotalPrix":34543.1402,"NombreClients":1669},{"age":41,"TotalPrix":35023.25,"NombreClients":1680},{"age":42,"TotalPrix":35077.2275,"NombreClients":1697},{"age":43,"TotalPrix":34437.4818,"NombreClients":1652},{"age":44,"TotalPrix":35878.3134,"NombreClients":1656},{"age":45,"TotalPrix":35348.7365,"NombreClients":1643},{"age":46,"TotalPrix":35226.579,"NombreClients":1658},{"age":47,"TotalPrix":35586.854,"NombreClients":1596},{"age":48,"TotalPrix":34508.8589,"NombreClients":1588},{"age":49,"TotalPrix":34982.3947,"NombreClients":1624},{"age":50,"TotalPrix":34991.9137,"NombreClients":1645},{"age":51,"TotalPrix":35772.3588,"NombreClients":1647},{"age":52,"TotalPrix":35761.0334,"NombreClients":1675},{"age":53,"TotalPrix":36004.2755,"NombreClients":1630},{"age":54,"TotalPrix":34984.3492,"NombreClients":1601},{"age":55,"TotalPrix":35321.8017,"NombreClients":1634},{"age":56,"TotalPrix":34350.109,"NombreClients":1669},{"age":57,"TotalPrix":35161.9402,"NombreClients":1622},{"age":58,"TotalPrix":35094.4313,"NombreClients":1637},{"age":59,"TotalPrix":35203.7902,"NombreClients":1649},{"age":60,"TotalPrix":34006.075,"NombreClients":733},{"age":61,"TotalPrix":38604.0865,"NombreClients":740},{"age":62,"TotalPrix":38775.469,"NombreClients":791},{"age":63,"TotalPrix":40170.2746,"NombreClients":761},{"age":64,"TotalPrix":38488.2014,"NombreClients":844},{"age":65,"TotalPrix":36154.5318,"NombreClients":786},{"age":66,"TotalPrix":38575.6003,"NombreClients":768},{"age":67,"TotalPrix":36362.5339,"NombreClients":768},{"age":68,"TotalPrix":39303.4565,"NombreClients":782},{"age":69,"TotalPrix":39423.9309,"NombreClients":781},{"age":70,"TotalPrix":39420.2433,"NombreClients":826},{"age":71,"TotalPrix":40539.3959,"NombreClients":773},{"age":72,"TotalPrix":38959.2646,"NombreClients":805},{"age":73,"TotalPrix":37652.8177,"NombreClients":823},{"age":74,"TotalPrix":39573.8,"NombreClients":785},{"age":75,"TotalPrix":38651.4475,"NombreClients":791},{"age":76,"TotalPrix":37654.9684,"NombreClients":823},{"age":77,"TotalPrix":38166.3265,"NombreClients":775},{"age":78,"TotalPrix":39460.4976,"NombreClients":818},{"age":79,"TotalPrix":39566.4067,"NombreClients":836},{"age":80,"TotalPrix":37102.0121,"NombreClients":746},{"age":81,"TotalPrix":38537.7993,"NombreClients":812},{"age":82,"TotalPrix":40524.2888,"NombreClients":831},{"age":83,"TotalPrix":39048.1479,"NombreClients":798},{"age":84,"TotalPrix":37638.8608,"NombreClients":790}]

// set the dimensions and margins of the graph
var margin = { top: 10, right: 20, bottom: 30, left: 50 },
    width = 1000 - margin.left - margin.right,
    height = 900 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3
    .select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.json("Nuage de points.json", function(data) {
    // Add X axis
    var x = d3.scaleLinear().domain([0, 100]).range([0, width]);
    svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear().domain([32000, 42000]).range([height, 0]);
    svg.append("g").call(d3.axisLeft(y));

    // Add a scale for bubble size
    var z = d3.scaleLinear().domain([733, 2519]).range([1, 15]);

    // Add a scale for bubble color
    var myColor = d3
        .scaleOrdinal()
        .domain([1000, 1500, 2000, 2500])
        .range(d3.schemeSet2);

    // -1- Create a tooltip div that is hidden by default:
    var tooltip = d3
        .select("#my_dataviz")
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "black")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("color", "white");

    // -2- Create 3 functions to show / update (when mouse move but stay on same circle) / hide the tooltip
    var showTooltip = function(d) {
        tooltip.transition().duration(200);
        tooltip
            .style("opacity", 1)
            .html(d.age + "ans - " + "NombreClients: " + d.NombreClients)
            .style("left", d3.mouse(this)[0] + 30 + "px")
            .style("top", d3.mouse(this)[1] + 30 + "px");
    };
    var moveTooltip = function(d) {
        tooltip
            .style("left", d3.mouse(this)[0] + 30 + "px")
            .style("top", d3.mouse(this)[1] + 30 + "px");
    };
    var hideTooltip = function(d) {
        tooltip.transition().duration(200).style("opacity", 0);
    };

    // Add dots
    svg
        .append("g")
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "bubbles")
        .attr("cx", function(d) {
            return x(d.age);
        })
        .attr("cy", function(d) {
            return y(d.PrixMoyen);
        })
        .attr("r", function(d) {
            return z(d.NombreClients);
        })
        .style("fill", function(d) {
            return myColor(d.NombreClients);
        })
        // -3- Trigger the functions
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip);


    svg.append("text")
        .attr("transform",
            "translate(" + (width / 2) + " ," +
            (height + margin.top + 20) + ")")
        .style("text-anchor", "middle")
        .text("Age");

    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Prix Moyens");
});