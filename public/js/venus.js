var tables = $("table");
(function () {
    tables.hide().first().show();
    //Hides all the tables except first
    $("a.button").on("click", function () {
        //Adds eventListner to buttons
        tables.hide();
        //Hides all the tables
        var tableTarget = $(this).data("table");
        //Gets data# of button
        $("table#" + tableTarget).show();
        //Shows the table with an id equal to data attr of the button
    })
})();

const outputDialogue = document.querySelector("#output");
const submitDialogue = document.querySelector("#submitButton");
const code = document.querySelector("#code");
const inp = document.querySelector("#inp");
const pipelining = document.querySelector("#pipelining");
const data_forwarding = document.querySelector("#data_forwarding");
const register_after_each_cycle = document.querySelector("#register_after_each_cycle");
const print_pipeline_registers = document.querySelector("#print_pipeline_registers");
const req_inst=document.querySelector("#req_inst");
const register_values = document.querySelector("#register-values");
const data_values = document.querySelector("#data-values");
const instruction_values = document.querySelector("#instruction-values");
const stack_values = document.querySelector("#stack-values");
const reg_toggle = document.querySelector("#reg-toggle");
const show_stats=document.querySelector("#show_stats");
const a=document.querySelector("#a");
const b=document.querySelector("#b");
const c=document.querySelector("#c");
const d=document.querySelector("#d");
const e=document.querySelector("#e");
const f=document.querySelector("#f");
const g=document.querySelector("#g");
const h=document.querySelector("#h");


var results;
submitDialogue.addEventListener('click', (event) => {
    // console.log(a.value+"\n"+ b.value+"\n"+c.value+"\n"+e.value+"\n"+f.value+"\n"+g.value+"\n"+h.value);
    if(b.value=="" || c.value=="" || f.value=="" || g.value==""){

        alert("invalid! please fill the required empty field to avoid wrong result");
    }
    else{
    var text;
    alert("Your code has been submitted successfully\nPlease check the Registers/Memory");
    $('#register-values').empty();
    $('#data-values').empty();
    $('#stack-values').empty();
    $('#instruction-values').empty();
    text = '<tr><th>address</th><th>+0</th><th>+1</th><th>+2</th><th>+3</th></tr>'
    data_values.insertAdjacentHTML('beforeend', text);
    instruction_values.insertAdjacentHTML('beforeend', text);
    stack_values.insertAdjacentHTML('beforeend', text);
    var data = {};
    data.code = code.value.replace(/^\s*[\r\n]/gm, "")
    data.inp = inp.value.replace(/^\s*[\r\n]/gm, "")
    data.pipelining=$('#pipelining').is(":checked")?1:0;
    data.data_forwarding=$('#data_forwarding').is(":checked")?1:0;
    data.req_inst=req_inst.value;
    data.register_after_each_cycle=$('#register_after_each_cycle').is(":checked")?1:0;
    data.print_pipeline_registers=$('#print_pipeline_registers').is(":checked")?1:0;

    data.a=a.value;
    data.b=b.value;
    data.c=c.value;
    data.d=d.value;
    data.e=e.value;
    data.f=f.value;
    data.g=g.value;
    data.h=h.value;
//     console.log(data);

    //console.log(data); uncomment this to check the return data on frontend

    $.ajax({url:"/",type:'POST', data:data,async:false,success: (response, status) => { //ajax call to post the data on the app.post()
        // response=JSON.parse(response);
        //  console.log(results);
        console.log(status);
        results=response;
        // console.log(results);
    },error:(xhr,status,error)=>{
        console.log("Web request terminated with xhr:"+xhr+"status: "+status+ " error: "+error);
    }});
    
    console.log(results);
    var registers = results.registers;
        var inst_mem = results.Inst_Mem;
        var data_mem = results.Data_Mem;
        var stack_mem = results.Stack_Mem;
        var keys = Object.keys(registers);
        var values = Object.values(registers);  
        for (var i = 0; i < Object.keys(registers).length; i++) {
            text = '<li><div><label class="dropdown-label">' + keys[i] +
                '</label><input disabled placeholder="' + values[i] +
                '" class="dropdown-input"></div></li>';
            register_values.insertAdjacentHTML('beforeend', text);
        }

        keys = Object.keys(data_mem);
        values = Object.values(data_mem);
        for (var i = 0; i < keys.length; i += 4) {

            text = '<tr><td>' + keys[i] + '</td>'
            for (var j = 0; j < 4; j++) {
                if (values[i + j]) {
                    text += '<td>' + values[i + j] + '</td>'
                } else {
                    text += '<td>00</td>'
                }
            }
            text += '</tr>'
            data_values.insertAdjacentHTML('beforeend', text);
        }

        keys = Object.keys(inst_mem);
        values = Object.values(inst_mem);
        for (var i = 0; i < keys.length; i += 4) {

            text = '<tr><td>' + keys[i] + '</td>'
            for (var j = 0; j < 4; j++) {
                if (values[i + j]) {
                    text += '<td>' + values[i + j] + '</td>'
                } else {
                    text += '<td>00</td>'
                }
            }
            text += '</tr>'

            instruction_values.insertAdjacentHTML('beforeend', text);
        }
                




        keys = Object.keys(stack_mem);
        values = Object.values(stack_mem);
        for (var i = 0; i < keys.length; i += 4) {

            text = '<tr><td>' + keys[i] + '</td>'
            for (var j = 0; j < 4; j++) {
                if (values[i + j]) {
                    text += '<td>' + values[i + j] + '</td>'
                } else {
                    text += '<td>00</td>'
                }
            }
            text += '</tr>'
            stack_values.insertAdjacentHTML('beforeend', text);
       }
    }
       // console.log(results);
});

function openWin() {
  var add = "popup";
    myWindow = window.open(add, "myWindow", "width=1028,height=720");
}