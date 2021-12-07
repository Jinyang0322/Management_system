var data = ({
    user: null,
    password: null,
    attend: null,
    absent: null,
    announcement: null,
    survey: null
});

const setCookie = (name, value, days = 7, path = '/') => {
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
    var url = "./login/";

    var loginPost = {
        username: user,
        password: password
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    if (data === null) {
        xhr.send();
    } else {
        xhr.setRequestHeader(
            "Content-Type",
            "application/json;charset=utf-8"
        );
        xhr.send(loginPost);
    }
    console.log(data);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            response = xhr.response;
            response = JSON.parse(response);
            console.log(response.user);
            if (response.user == user) {
                document.querySelector("#submit-status").innerHTML = "Successful Log In!";
                setCookie("user1", user);
            } else {
                document.querySelector("#submit-status").innerHTML = "Incorrect User Name of Password!";
                document.getElementById("userid").value = '';
                document.getElementById("password").value = '';
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
    var message = document.querySelector("#message").value;

    var url = "http://127.0.0.1:8000/server";

    var xhr = new XMLHttpRequest();

    xhr.open('POST', url);

    xhr.send(message);

    alert("Your announcement has been published successfully!");
}


function survey() {
    var message = document.querySelector("#message").value;
    var Q1 = document.querySelector("#Q1").value;
    var Q2 = document.querySelector("#Q2").value;

    var url = "http://127.0.0.1:8000/server";

    var xhr = new XMLHttpRequest();

    xhr.open('POST', url);

    xhr.send();

    alert("Your survey has been published successfully!");
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

    const namelist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
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
        .text("The students attend the course is: " + oData[0]["y"])
        .attr("x", 30)
        .attr("y", 30)
        .attr("font-family", "Verdana")
        .attr("font-size", "20px")

    map.append("text")
        .text("The students absent the course is: " + oData[1]["y"])
        .attr("x", 30)
        .attr("y", 60)
        .attr("font-family", "Verdana")
        .attr("font-size", "20px")

    map.append("text")
        .text("Absence Names: " + namelist)
        .attr("x", 30)
        .attr("y", 90)
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