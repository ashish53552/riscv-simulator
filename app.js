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
    res.render('index');
});

app.post('/',(req,res)=>{
    //console.log(req.body); uncomment this to check the input at console
    //calling python child process
    const pythonProcess = spawn('python',["Phase1/main.py", JSON.stringify(req.body)]);

    //parsing the response from std.out.flush()

    pythonProcess.stdout.on('data', (data) => {
      //  console.log(JSON.parse(data)); uncomment this to check the output of the python file at console
       res.send(JSON.parse(data)); // dumping the data to the frontend ajax call
    });


})


app.listen(process.env.PORT||80, function () {
    console.log("Server started Succesfully.");
});