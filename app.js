const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const spawn = require("child_process").spawn;
const {
    data
} = require("jquery");

const app = express();

app.use(express.static("public"));
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({
    extended: true
}));

app.get('/', (req, res) => {
    res.render('index2');
});

app.post('/',(req,res)=>{
    console.log(req.body);
    

    // const pythonProcess = spawn('python',["gg\\gg2\\somefile.py", JSON.stringify(req.body)]);
    // pythonProcess.stdout.on('data', (data) => {
    //     console.log(JSON.parse(data));
    //     res.send(JSON.parse(data))
    // });

    // console.log(req.body);
    // res.send(req.body);

    const pythonProcess = spawn('python',["Phase1\\main.py", JSON.stringify(req.body)]);
    pythonProcess.stdout.on('data', (data) => {
        console.log(JSON.parse(data));
      
        res.send(JSON.parse(data));
    });


})


app.listen(80, function () {
    console.log("Server started Succesfully.");
});