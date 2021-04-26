
function myFunction(){
  var results; 
    $.ajax({url:"/dataApi",type:'GET',async:false,success: (response, status) => { //ajax call to post the data on the app.post()
      // results=JSON.parse(results);
      //  console.log(results);
      console.log(status);
      results=response;
  },error:(xhr,status,error)=>{
      console.log("Web request terminated with xhr:"+xhr+"status: "+status+ " error: "+error);
  }});
  console.log(results);

let Table = [
    {Information:"", Count:0},
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


  
  
  function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data) {
      let th = document.createElement("th");
      let text = document.createTextNode(key);
      th.appendChild(text);
      row.appendChild(th);
    }
  }
  
  function generateTable(table, data) {
    for (let element of data) {
      let row = table.insertRow();
      for (key in element) {
        let cell = row.insertCell();
        let text = document.createTextNode(element[key]);
        cell.appendChild(text);
      }
    }
  }







  
  let table = document.getElementById("new_tab");
  let data = Object.keys(Table[0]);
  generateTableHead(table, data);
  generateTable(table, Table);





//  ------------------------------------------

var show = "";
function print_register_per_cycle(){
  var temp  = results.Stats.register_per_cycle;
  for(var key in temp){
    show+=(key+"\n"+"\t");
    for(var v in temp[key])
    {
      show+=(v+": ");
      show+=(temp[key][v]+"\n\t");
    }
  }
};
function print_req_inst_details(){
  var temp  = results.Stats.req_inst_details;
  for(var key in temp){
    show+=(key+"\n"+"\t");
    for(var v in temp[key])
    {
      show+=(v+": ");
      show+=(temp[key][v]+"\n\t");
    }
  }


};
function print_all_cycle_details()
{
  var temp  = results.Stats.all_cycle_details;
  for(var key in temp){
    show+=(key+"\n"+"\t");
    for(var v in temp[key])
    {
      show+=(v+": ");
      show+=(temp[key][v]+"\n\t");
    }
  }
};

var condn = results.input_params;
if(condn.req_ins!='')
{
  print_req_inst_details();
}
else if(condn.print_pipeline_registers==1)
print_all_cycle_details();
else if(condn.register_after_each_cycle==1)
print_register_per_cycle();


var x = document.getElementById('mm');

x.innerHTML = show;
}
