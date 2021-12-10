var data = ({
    user: null,
    password: null,
    attend: null,
    absent: null,
    announcement: null,
    survey: null
});

const setCookie = (name, value, days = 0.02, path = '/') => {
    const expires = new Date(Date.now() + days * 864e5).toUTCString()
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=' + path
}

const getCookie = (name) => {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=')
        return parts[0] === name ? decodeURIComponent(parts[1]) : r
    }, '')
}

const deleteCookie = (name, path) => {
    setCookie(name, '', -1, path)
}

function login_submit() {
    var user = document.querySelector("#userid").value;
    var password = document.querySelector("#password").value;
    // var user = document.getElementById("userid").value;
    // var password = document.getElementById("password").value;
    // console.log(document.getElementById("password").value);

    // The request parameters
    var url = "./";

    // var loginPost = {
    //     username: user,
    //     password: password
    // };
    var loginPost = JSON.stringify({
        username: user,
        password: password
    });
    console.log(loginPost);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    // xhr.send(loginPost);
    // console.log("change")
    if (data === null) {
        xhr.send();
    } else {
        xhr.setRequestHeader(
            "Content-Type",
            "application/json;charset=utf-8"
        );
        xhr.send(loginPost);
    }
    // console.log(data);

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            response = xhr.response;
            response = JSON.parse(response);
            console.log(response.status);
            if (response.status == "ok") {
                document.querySelector("#submit-status").innerHTML = "Successful Log In!";
                alert("Welcome " + user);
                setCookie("user1", user);
            } else {
                document.querySelector("#submit-status").innerHTML = "Incorrect User Name of Password!";
                document.getElementById("userid").value = '';
                document.getElementById("password").value = '';
                alert("Incorrect User Name of Password!");
            }
        }
    }
}

function statusCheck() {
    x = getCookie("user1");
    if (x) {
        return x;
    }
}

function announce() {
    var title = document.querySelector("#titleform").value;
    var message = document.querySelector("#message").value;
    var url = "./";
    var announcePost = JSON.stringify({
        content: message,
        title: title
    });
    console.log(announcePost);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    // xhr.send(loginPost);
    // console.log("change")
    if (data === null) {
        xhr.send();
    } else {
        xhr.setRequestHeader(
            "Content-Type",
            "application/json;charset=utf-8"
        );
        xhr.send(announcePost);
    }

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            response = xhr.response;
            response = JSON.parse(response);
            console.log(response.status);
            if (response.status == "ok") {
                alert("Your announcement has been published!");
            } else {
                alert("Error");
            }
        }
    }
}


function survey(num) {
    var message = document.querySelector("#message").value;
    surveylst = new Object();
    surveylst["description"] = message;
    lst = ["#Q1", "#Q2", "#Q3", "#Q4", "#Q5", "#Q6", "#Q7"]
    for (i = 1; i < num + 1; i++) {
        temp = document.querySelector(lst[i - 1]).value;
        surveylst['Q' + String(i)] = temp;
        console.log(i);
    }
    var surveylst = JSON.stringify(surveylst);
    console.log(surveylst);
    var url = "./";
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    // xhr.send(loginPost);
    // console.log("change")
    if (data === null) {
        xhr.send();
    } else {
        xhr.setRequestHeader(
            "Content-Type",
            "application/json;charset=utf-8"
        );
        xhr.send(surveylst);
    }

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            response = xhr.response;
            console.log(response)
            response = JSON.parse(response);
            console.log(response.status);
            if (response.status == "ok") {
                alert("Your survey has been published successfully!");
            } else {
                alert("Error!");
            }
        }
    }
}


function chart(temp) {
    const oData = [{
            'x': 'Attend',
            'y': temp[0]
        },
        {
            'x': 'Absent',
            'y': temp[1]
        }
    ];

    const namelist = temp[2];
    const table = d3.select("div#table");
    const svg = table
        .append("svg")
        .attr("width", 500)
        .attr("height", 400)
        .style("margin", 20);
    const width = svg.attr("width");
    const height = svg.attr("height");
    const margin = 20;
    const map = svg
        .append("g")
        .attr("transform", "translate(" + 20 + "," + 20 + ")");

    console.log(oData[0]["y"]);
    map.append("text")
        .text("Recent Class Attendance:")
        .attr("x", 30)
        .attr("y", 60)
        .attr("font-family", "Ruda")
        .attr("font-size", "30px")

    map.append("text")
        .text("The students attend the course is: " + oData[0]["y"])
        .attr("x", 30)
        .attr("y", 120)
        .attr("font-family", "Verdana")
        .attr("font-size", "20px")

    map.append("text")
        .text("The students absent the course is: " + oData[1]["y"])
        .attr("x", 30)
        .attr("y", 150)
        .attr("font-family", "Verdana")
        .attr("font-size", "20px")

    map.append("text")
        .text("Absence Student Ids: " + namelist)
        .attr("x", 30)
        .attr("y", 180)
        .attr("font-family", "Verdana")
        .attr("font-size", "20px")

    const svg2 = table
        .append("svg")
        .attr("width", 600)
        .attr("height", 400)
        .style("margin", 20);
    const width2 = svg2.attr("width");
    const height2 = svg2.attr("height");
    const chart = svg2
        .append("g")
        .attr("transform", "translate(" + 20 + "," + 20 + ")");

    pieChart(oData);

    function pieChart(oriData) {

        console.log("asdfasdfadf");
        let g = chart.append('g')
            .attr('transform', 'translate( 140, 40 )')

        //设置饼图的半径
        let radius = Math.min(width2, height2) * 0.6 / 2

        let arc = d3.arc()
            .innerRadius(80)
            // .outerRadius(radius)
            .cornerRadius(10)

        //饼图与文字相连的曲线起点
        let pointStart = d3.arc()
            .innerRadius(radius)
            .outerRadius(radius)
        //饼图与文字相连的曲线终点
        let pointEnd = d3.arc()
            .innerRadius(radius + 20)
            .outerRadius(radius + 20)

        let drawData = d3
            .pie()
            .value(function (d) {

                return d.y
            })
            .sort(null)
            .sortValues(null)
            .startAngle(0)
            .endAngle(Math.PI * 2)
            .padAngle(0.05)(oriData)
        console.log(drawData)

        let colorScale = d3
            .scaleOrdinal()
            .domain(d3.range(0, oriData.length))
            .range(d3.schemeSet1);
        g.append('g')
            .attr('transform', 'translate( ' + radius + ', ' + radius + ' )')
            .attr('stroke', 'steelblue')
            .attr('stroke-width', 1)
            .selectAll('path')
            .data(drawData)
            .enter()
            .append('path')
            .attr('fill', function (d) {

                return colorScale(d.index)
            })
            .attr('d', function (d) {

                d.outerRadius = radius;
                return arc(d)
            })
            .on('mouseover', arcTween(radius + 20, 0))
            .on('mouseout', arcTween(radius, 150))
            .transition()
            .duration(2000)
            .attrTween('d', function (d) {

                //初始加载时的过渡效果
                let fn = d3.interpolate({

                    endAngle: d.startAngle
                }, d)
                return function (t) {

                    return arc(fn(t))
                }
            })

        function arcTween(outerRadius, delay) {

            // 设置缓动函数,为鼠标事件使用
            return function () {

                d3.select(this)
                    .transition()
                    .delay(delay)
                    .attrTween('d', function (d) {

                        let i = d3.interpolate(d.outerRadius, outerRadius)
                        return function (t) {

                            d.outerRadius = i(t)
                            return arc(d)
                        }
                    })
            }
        }
        //图例
        let legend = g.append('g')
            .attr('transform', 'translate( ' + radius * 2.5 + ', 0 )')
            .selectAll('g')
            .data(drawData)
            .enter()
            .append('g')
            .attr('transform', function (d, i) {

                return 'translate(0,' + i * 20 + ')'
            });

        legend
            .append('rect')
            .attr('width', 27)
            .attr('height', 18)
            .attr('fill', function (d) {

                return colorScale(d.index)
            });
        legend
            .append('text')
            .text(function (d) {

                return d.data.x
            })
            .style('font-size', 10)
            .attr('y', '1em')
            .attr('x', '3em')
            .attr('dy', 3)
    }
}

function Lchart(rateLst) {

    const linchart = d3.select("div#lineeechart");
    const svg = linchart
        .append("svg")
        .attr("width", 500)
        .attr("height", 400)
        .style("margin", 20);
    const width = svg.attr("width");
    const height = svg.attr("height");
    const map = svg
        .append("g")
        .attr("transform", "translate(" + 20 + "," + 20 + ")");

    map.append("text")
        .text("History Class Attendance:")
        .attr("x", 30)
        .attr("y", 60)
        .attr("font-family", "Ruda")
        .attr("font-size", "30px")

    const svg2 = linchart
        .append("svg")
        .attr("width", 600)
        .attr("height", 400)
    var margin = {
        top: 10,
        right: 10,
        bottom: 150,
        left: 50
    };
    const chartWidth = width - margin.left - margin.right;
    const chartHeight = height - margin.top - margin.bottom;

    const chartArea = svg2
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    lineChart(rateLst);

    function lineChart(oriData) {
        const timeScale = d3.scaleLinear().domain([0, 5]).range([0, chartWidth]);
        const rateScale = d3.scaleLinear().domain([0, 100]).range([chartHeight, 0]);
        let annotations = svg2.append("g").attr("id", "annotations");

        let leftAxis = d3.axisLeft(rateScale)
            .tickFormat(function (d) {
                return d + "%";
            });
        let leftGridlines = d3.axisLeft(rateScale)
            .tickSize(-chartWidth - 10)
            .tickFormat("")
        annotations.append("g")
            .attr("class", "y axis")
            .attr("transform", `translate(${margin.left - 10},${margin.top})`)
            .call(leftAxis)
        annotations.append("g")
            .attr("class", "y gridlines")
            .attr("transform", `translate(${margin.left - 10},${margin.top})`)
            .attr("color", "lightgrey")
        // .call(leftGridlines);

        // X axis
        var bottomLabel = ['0', '1', '2', '3', '4', '5'];
        let bottomAxis = d3.axisBottom(timeScale)
            .tickValues(bottomLabel)
            .tickFormat(d3.format("d"));
        let bottomGridlines = d3.axisBottom(timeScale)
            .tickSize(-chartHeight - 10)
            .tickFormat("")
        annotations.append("g")
            .attr("class", "x axis")
            .attr("transform", `translate(${margin.left},${chartHeight + margin.top + 10})`)
            .call(bottomAxis);
        annotations.append("g")
            .attr("class", "x gridlines")
            .attr("transform", `translate(${margin.left},${chartHeight + margin.top + 10})`)
            .attr("color", "lightgrey")

        lst = oriData;
        line_chart(lst);

        function line_chart(lst) {
            for (var i = 0; i < 4; i++) {
                chartArea.append("line")
                    .attr("stroke", '#377EB8')
                    .attr("stroke-width", 3)
                    .attr("x1", timeScale(i + 1))
                    .attr("y1", rateScale(lst[i] * 100))
                    .attr("x2", timeScale(i + 2))
                    .attr("y2", rateScale(lst[i + 1] * 100));
            }
            for (var i = 0; i < 5; i++) {
                chartArea.append("circle")
                    .attr("cx", timeScale(i + 1))
                    .attr("cy", rateScale(lst[i] * 100))
                    .attr("r", 8)
                    .attr("fill", '#377EB8');
            }
        }
    }
}