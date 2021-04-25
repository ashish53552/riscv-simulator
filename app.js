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
    console.log(req.body)
    let pipelining=1;
    let register_after_each_cycle=1;
    let dataforwarding=1;
    let print_pipeline_registers=1;
    let req_inst=0x00000004;
    let input_params={};
    input_params.pipelining=pipelining;
    input_params.register_after_each_cycle=register_after_each_cycle;
    input_params.dataforwarding=dataforwarding;
    input_params.print_pipeline_registers=print_pipeline_registers;
    input_params.req_inst=req_inst;
    req.body.pipelining=pipelining;
    req.body.register_after_each_cycle=register_after_each_cycle;
    req.body.dataforwarding=dataforwarding;
    req.body.print_pipeline_registers=print_pipeline_registers;
    req.body.req_inst=req_inst;
    const pythonProcess = spawn('python',["Phase2/main.py", JSON.stringify(req.body)]);

    //parsing the response from std.out.flush()

    pythonProcess.stdout.on('data', (data) => {
      console.log(JSON.parse(data));
    //    data.input_params=input_params;
      //  console.log(JSON.parse(data)); uncomment this to check the output of the python file at console
       res.send(data); // dumping the data to the frontend ajax call
    });


})


app.listen(process.env.PORT||80, function () {
    console.log("Server started Succesfully.");
});