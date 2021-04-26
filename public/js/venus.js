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
// DOM 
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

//     submitDialogue.addEventListener('click', (event) => {
//         var text;
//         alert("Your code has been submitted successfully\nPlease check the Registers/Memory");
//         $('#register-values').empty();
//         $('#data-values').empty();
//         $('#stack-values').empty();
//         $('#instruction-values').empty();
//         text = '<tr><th>address</th><th>+0</th><th>+1</th><th>+2</th><th>+3</th></tr>'
//         data_values.insertAdjacentHTML('beforeend', text);
//         instruction_values.insertAdjacentHTML('beforeend', text);
//         stack_values.insertAdjacentHTML('beforeend', text);
//         var data = {};
//         data.code = code.value.replace(/^\s*[\r\n]/gm, "")
//         data.inp = inp.value.replace(/^\s*[\r\n]/gm, "")
//         data.pipelining=$('#pipelining').is(":checked")?1:0;
//         data.data_forwarding=$('#data_forwarding').is(":checked")?1:0;
//         data.req_inst=req_inst.value;
//         data.register_after_each_cycle=$('#register_after_each_cycle').is(":checked")?1:0;
//         data.print_pipeline_registers=$('#print_pipeline_registers').is(":checked")?1:0;
//    //     console.log(data);

//         //console.log(data); uncomment this to check the return data on frontend

//         $.post("/", data, (results, error) => { //ajax call to post the data on the app.post()
//             // results=JSON.parse(results);
//            console.log(results);
//             var registers = results.registers;
//             var inst_mem = results.Inst_Mem;
//             var data_mem = results.Data_Mem;
//             var stack_mem = results.Stack_Mem;
//             var keys = Object.keys(registers);
//             var values = Object.values(registers);  
//             for (var i = 0; i < Object.keys(registers).length; i++) {
//                 text = '<li><div><label class="dropdown-label">' + keys[i] +
//                     '</label><input disabled placeholder="' + values[i] +
//                     '" class="dropdown-input"></div></li>';
//                 register_values.insertAdjacentHTML('beforeend', text);
//             }

//             keys = Object.keys(data_mem);
//             values = Object.values(data_mem);
//             for (var i = 0; i < keys.length; i += 4) {

//                 text = '<tr><td>' + keys[i] + '</td>'
//                 for (var j = 0; j < 4; j++) {
//                     if (values[i + j]) {
//                         text += '<td>' + values[i + j] + '</td>'
//                     } else {
//                         text += '<td>00</td>'
//                     }
//                 }
//                 text += '</tr>'
//                 data_values.insertAdjacentHTML('beforeend', text);
//             }

//             keys = Object.keys(inst_mem);
//             values = Object.values(inst_mem);
//             for (var i = 0; i < keys.length; i += 4) {

//                 text = '<tr><td>' + keys[i] + '</td>'
//                 for (var j = 0; j < 4; j++) {
//                     if (values[i + j]) {
//                         text += '<td>' + values[i + j] + '</td>'
//                     } else {
//                         text += '<td>00</td>'
//                     }
//                 }
//                 text += '</tr>'

//                 instruction_values.insertAdjacentHTML('beforeend', text);
//             }
                




//             keys = Object.keys(stack_mem);
//             values = Object.values(stack_mem);
//             for (var i = 0; i < keys.length; i += 4) {

//                 text = '<tr><td>' + keys[i] + '</td>'
//                 for (var j = 0; j < 4; j++) {
//                     if (values[i + j]) {
//                         text += '<td>' + values[i + j] + '</td>'
//                     } else {
//                         text += '<td>00</td>'
//                     }
//                 }
//                 text += '</tr>'
//                 stack_values.insertAdjacentHTML('beforeend', text);
//             }

//         }).done(function(){
//             console.log("success");
//         }).fail(function (xhr, status, error) {
//             // error handling
//             console.log(error);
//         });
//         setTimeout(() => {
//             console.log(cont)
//         }, (2000));
    
//     });
var results;
submitDialogue.addEventListener('click', (event) => {
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
//     console.log(data);

    //console.log(data); uncomment this to check the return data on frontend

    $.ajax({url:"/",type:'POST', data:data,async:false,success: (response, status) => { //ajax call to post the data on the app.post()
        // results=JSON.parse(results);
        //  console.log(results);
        console.log(status);
        results=response;
    },error:(xhr,status,error)=>{
        console.log("Web request terminated with xhr:"+xhr+"status: "+status+ " error: "+error);
    }});
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

        console.log(results);
});
show_stats.addEventListener('click',(event)=>{
    console.log(results);
    
let Table = [
   
    { Information:"Total Cycles", Count: results.Stats.total_cycles, }, 
    { Information:"Total instructions executed", Count: results.Stats.num_instructions, },
    { Information: "CPI", Count: results.Stats.CPI},
    { Information: "Data Trasfer Instructions", Count: results.Stats.num_data_trasfer, },
    { Information: "ALU instructions", Count:results.Stats.num_alu,  }, 
    {Information: "Control instructions", Count: results.Stats.num_control, },
    {Information:"Stalls", Count:results.Stats.num_stalls,},
    {Information:"Data Hazards", Count:results.Stats.num_data_hazards, },
    {Information:"Control Hazards", Count:results.Stats.num_control_hazards, },
    {Information:"Branch misprediction", Count:results.Stats_num_branch_mispredictions, },
    {Information:"Stalls due to data hazards", Count:results.Stats.num_stalls_data, },
    {Information:"Stalls due to control hazards", Count:results.Stats.num_stalls_control, },
  ];
    console.log(Table);
    // function generateTableHead(table, data) {
    //   let thead = table.createTHead();
    //   let row = thead.insertRow();
    //   for (let key of data) {
    //     let th = document.createElement("th");
    //     let text = document.createTextNode(key);
    //     th.appendChild(text);
    //     row.appendChild(th);
    //   }
    // }
    
    // function generateTable(table, data) {
    //   for (let element of data) {
    //     let row = table.insertRow();
    //     for (key in element) {
    //       let cell = row.insertCell();
    //       let text = document.createTextNode(element[key]);
    //       cell.appendChild(text);
    //     }
    //   }
    // }
  
  
  
    function addTable() {
        var myTableDiv = document.getElementById("myDynamicTable");
      
        var table = document.createElement('TABLE');
        table.border = '1';
      
        var tableBody = document.createElement('TBODY');
        table.appendChild(tableBody);
      
        for (var i = 0; i < 12; i++) {
          var tr = document.createElement('TR');
          tableBody.appendChild(tr);
      
        //   for (var j = 0; j < 2; j++) {
            var td = document.createElement('TD');
            td.width = '75';
            td.appendChild(document.createTextNode(Table[i]['Information']));
            tr.appendChild(td);
            var td = document.createElement('TD');
            td.width = '75';
            td.appendChild(document.createTextNode(Table[i]['Count']));
            tr.appendChild(td);
        //   }
        }
        myTableDiv.appendChild(table);
      }
      addTable();
      var myWindow;
        
      function openWin() {
      var add = "C:\\Users\\SHRISH\\Downloads\\RISC-V-Simulator-main\\public\\p2.HTML";
        myWindow = window.open(add, "myWindow", "width=800,height=600");
      //   var html = "<html><head></head><body>Hello, <b>"+"</b>.";
      //     html += "How are you today?</body></html>"
      //   myWindow.document.write(html);
      }
  
  
  
    
    // let table = document.querySelector("table");
    // let data = Object.keys(Table[0]);
    // generateTableHead(table, data);
    // generateTable(table, Table);
  
  
  
  
  
  //  ------------------------------------------
  
  var show = "";
  
  function print_register_per_cycle(){
    var temp  = results.Stats.register_per_cycle;
    for(var key in temp){
      show+=(key+"\n");
      for(var v in temp[key])
      {
          show+='\t';
        show+=(v+": ");
        show+=(temp[key][v]+"\n");
      }
    }
  };
  function print_req_inst_details(){
    var temp  = results.Stats.req_inst_details;
    for(var key in temp){
      show+=(key+"\n");
      for(var v in temp[key])
      {
        show+="\t";
        show+=(v+": ");
        show+=(temp[key][v]+"\n");
      }
    }
  
  
  };
  function print_all_cycle_details()
  {
    var temp  = results.Stats.all_cycle_details;
    for(var key in temp){
      show+=(key+"\n");
      for(var v in temp[key])
      {   
         if(v.includes('fetch'))
         {
            show+="\t";
            show+=(v+": ");
            show+=(temp[key][v]+"\n");
         }
          else{
              show+="\t";
            show+=(v+": ");
          for(t in temp[key][v]){
          show+="\t";
        show+=(t+": ");
        show+=(temp[key][v][t]+"\n");
    }
      
          }
      
    }
  }
};
  
  var condn = results.input_params;
  console.log(condn);
  console.log(condn.req_ins);
  console.log(print_pipeline_registers);
  console.log(register_after_each_cycle);
//   console.l
  if(condn.req_ins!=undefined)
  {
    console.log("yes");
    print_req_inst_details();
  }
  else if(condn.print_pipeline_registers=="1"){
      console.log("Yes");
  print_all_cycle_details();
}
  else if(condn.register_after_each_cycle=="1"){
      console.log("YES");
  print_register_per_cycle();};
  
  console.log(show);
  
  var x = document.getElementById('mm');
  
  x.innerHTML = show;
    
});




// let Table = [
//     {name:"Ss", score:5,},
//     {name:"Ss", score:5,},
//     {name:"Ss", score:5,},
    
    
    
//   ];
