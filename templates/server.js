const express = require('express');
const app = express();

app.use(express.static('public'));
const bodyParser = require('body-parser');
app.use(bodyParser.json()); //support json encoded bodies
app.use(bodyParser.urlencoded());

var data = JSON.stringify({
    user: "Doge",
    password: "0000",
    attend: 36,
    absent: 10,
    announcement: null,
    survey1_yes: 14,
    survey1_no: 32,
    survey2_yes: 10,
    survey2_no: 36
});

app.post('/server',(req, res)=>{
    // 设置相应头，设置允许跨越
    // var user_name = request.body;
    // var password = request.body.password;

    res.setHeader('Access-Control-Allow-Origin','*');
    // temp = response.json({requestBody: request.body});
    console.log(req.body);
    // 设置相应体
    res.send(data);
    // response.send("request.body");

});

// 监听端口启动服务
app.listen(8000,()=>{
    console.log("服务已经启动，端口8000");
})