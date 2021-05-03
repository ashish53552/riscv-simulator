const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const spawn = require("child_process").spawn;
const {
    data
} = require("jquery");
const fs = require('fs')
const app = express();

app.use(express.static("public"));
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({
    extended: true
}));

app.get('/', (req, res) => {
    res.render('index');
});
app.get("/popup",(req,res)=>{
    // let data = fs.readFileSync('Phase2/test.txt', 'utf8');
    // res.send(data);
    res.render('popup');
})
app.get("/dataApi",(req,res)=>{
    let data = fs.readFileSync('Phase2/popup.txt', 'utf8');
    data=JSON.parse(data);
    res.send(data);
})
app.post('/',(req,res)=>{
    //console.log(req.body); uncomment this to check the input at console
    //calling python child process
    //console.log(req.body)
    // let pipelining=1;
    // let register_after_each_cycle=1;
    // let data_forwarding=1;
    // let print_pipeline_registers=1;
    // let req_inst="0x00000004";
    let input_params={};
    input_params.pipelining=req.body.pipelining;
    input_params.register_after_each_cycle=req.body.register_after_each_cycle;
    input_params.data_forwarding=req.body.data_forwarding;
    input_params.print_pipeline_registers=req.body.print_pipeline_registers;
    input_params.req_inst=req.body.req_inst;
    // req.body.pipelining=pipelining;
    // req.body.register_after_each_cycle=register_after_each_cycle;
    // req.body.data_forwarding=data_forwarding;
    // req.body.print_pipeline_registers=print_pipeline_registers;
    // req.body.req_inst=req_inst;
    console.log(req.body);
    const pythonProcess = spawn('python',["Phase2/main.py", JSON.stringify(req.body)]);
    pythonProcess.on('close', (code,signal) => {
        console.log(`child process close all stdio with code ${signal}`);
        var data;
        try {
            data = fs.readFileSync('Phase2/test.txt', 'utf8')
        // console.log(JSON.parse(data))
            data=JSON.parse(data)
            data.input_params=input_params;
            fs.writeFile('Phase2/popup.txt', JSON.stringify(data), function (err) {
                if (err) throw err;
                console.log('Saved!');
            });
              
            res.send(data)
        } catch (err) {
            console.error(err)
        }
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`child stderr:\n${data}`);
      });
    //parsing the response from std.out.flush()
    pythonProcess.stdout.on('data', (data) => {
    //    data.input_params=input_params;
      //  console.log(JSON.parse(data)); uncomment this to check the output of the python file at console
       // dumping the data to the frontend ajax call
       console.log(data.toString())
    });
    

    
})


app.listen(process.env.PORT||80, function () {
    console.log("Server started Succesfully.");
});