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
    let input_params={};
    input_params.pipelining=req.body.pipelining;
    input_params.register_after_each_cycle=req.body.register_after_each_cycle;
    input_params.data_forwarding=req.body.data_forwarding;
    input_params.print_pipeline_registers=req.body.print_pipeline_registers;
    input_params.req_inst=req.body.req_inst;
    input_params.a=req.body.a;
    input_params.b=req.body.b;
    input_params.c=req.body.c;
    input_params.d=req.body.d;
    input_params.e=req.body.e;
    input_params.f=req.body.f;
    input_params.g=req.body.g;
    input_params.h=req.body.h;
    console.log(req.body);
    const pythonProcess = spawn('python',["Phase3/main3.py", JSON.stringify(req.body)]);
    pythonProcess.on('close', (code,signal) => {
        console.log(`child process close all stdio with code ${signal}`);
        var data;
        try {
            data = fs.readFileSync('Phase2/test.txt', 'utf8')
        //    console.log(JSON.parse(data))
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
    // pythonProcess.stderr.on('data', (data) => {
    //     console.error(`child stderr:\n${data}`);
    //   });
    // //parsing the response from std.out.flush()
    // pythonProcess.stdout.on('data', (data) => {
    // //    data.input_params=input_params;
    //   //  console.log(JSON.parse(data)); uncomment this to check the output of the python file at console
    //    // dumping the data to the frontend ajax call
    //    console.log(data.toString())
    // });
    // res.send({some:'json'});

    
})


app.listen(process.env.PORT||80, function () {
    console.log("Server started Succesfully.");
});