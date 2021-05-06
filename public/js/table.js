
function myFunction(){
  var results; 
    $.ajax({url:"/dataApi",type:'GET',async:false,success: (response, status) => { //ajax call to post the data on the app.post()
      // response=JSON.parse(response);
      //  console.log(results);
      console.log(status);
      results=response;
  },error:(xhr,status,error)=>{
      console.log("Web request terminated with xhr:"+xhr+"status: "+status+ " error: "+error);
  }});
  console.log("ram", results);

let Table = [
    { Information:"Total Cycles", Count: results.Stats.total_cycles, }, 
    { Information:"Total instructions executed", Count: results.Stats.num_instructions, },
    { Information: "CPI", Count: results.Stats.CPI},
    { Information: "Data Trasfer Instructions", Count: results.Stats.num_data_transfer, },
    { Information: "ALU instructions", Count:results.Stats.num_alu,  }, 
    { Information: "Control instructions", Count: results.Stats.num_control, },
    {Information:"Stalls", Count:results.Stats.num_stalls,},
    {Information:"Data Hazards", Count:results.Stats.num_data_hazards, },
    {Information:"Control Hazards", Count:results.Stats.num_control_hazards, },
    {Information:"Branch misprediction", Count:results.Stats.num_branch_mispredictions, },
    {Information:"Stalls due to data hazards", Count:results.Stats.num_stalls_data, },
    {Information:"Stalls due to control hazards", Count:results.Stats.num_stalls_control, },
    {Information:"Number of data cache  hits", Count:results.Stats.num_data_cache_hits, },
    {Information:"Number of data cache  misses", Count:results.Stats.num_data_cache_misses, },
    {Information:"Number of data memory accesses", Count:results.Stats.num_data_memory_accesses, },
    {Information:"Number of data memory hitrate", Count:results.Stats.num_data_memory_hitrate, },
    {Information:"Number of instruction cache hits", Count:results.Stats.num_inst_cache_hits, },
    {Information:"Number of of instruction cache misses", Count:results.Stats.num_inst_cache_misses, },
    {Information:"Number of instruction memory accesses", Count:results.Stats.num_inst_memory_accesses, },
    {Information:"Number of instruction memory hitrate", Count:results.Stats.num_inst_memory_hitrate, },
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
    show+=("\n"+key+": ");
    for(var v in temp[key])
    {
      show+=("\n\t"+v+": ");
      // for(var k in temp[key][v]){
        // show+=("\n\t\t"+k+": ");
      show+=("  "+temp[key][v]+"; ");
    // }
    }
  }
 
};
function print_req_inst_details(){
  var temp  = results.Stats.req_inst_details;

  for(var key in temp){
    show+=("\n"+key+": ");
   
    for(var v in temp[key])
    {
      show+=("\n\t"+v+": ");
      if(v.includes('fetch_decode'))
      {
        show+=("\n\t"+temp[key][v]+": ");
        break;
      }
      for(var k in temp[key][v]){

        show+=("\n\t\t"+k+": ");
       

      show+=("  "+temp[key][v][k]+"; ");
    }
    }
  }

};
function print_all_cycle_details()
{
 
  var temp  = results.Stats.all_cycle_details;
 
  
  for(var key in temp){
    show+=("\n"+key+": ");
    for(var v in temp[key])
    {
      show+=("\n\t"+v+": ");
      if(v.includes('fetch_decode'))
      {
        show+=(""+temp[key][v]+"; ");
        break;
      }
      for(var k in temp[key][v]){
        show+=("\n\t\t"+k+": ");
      show+=("  "+temp[key][v][k]+"; ");
    }
    }
  }
};

var condn = results.input_params;
console.log(results)
console.log(condn)

if(condn.req_inst!='')
{ show +="Required instruction Details:\n\n";
  print_req_inst_details();
}
else if(condn.print_pipeline_registers==1){
  show+="All Cycle Details:\n\n";
print_all_cycle_details();
}
else if(condn.register_after_each_cycle==1){
  show+="Register Per Cycle:\n\n";
print_register_per_cycle();
}

var x = document.getElementById('mm');

x.innerHTML = show;


// ---------------------------------------------------

// printing accessed block

 var Show = "ACCESSED_BLOCK\n";

var temp = results.Stats.accessed_blocks;
for(var key in temp){
  Show+=("\n"+key+": ");
  for(var v in temp[key])
  {
    Show+=("\n\t"+v+": ");
    Show+=("  "+temp[key][v]+"; ");
  }
}


// ------ printing victim blocks
temp = results.Stats.victim_blocks;
Show+='\n';
Show+="VICTIMS_BLOCK\n";

for(var key in temp){
  Show+=("\n"+key+": ");
  for(var v in temp[key])
  {
    Show+=("\n\t"+v+": ");
    Show+=("  "+temp[key][v]+"; ");
  }
}


// ------- printing data cache
temp = results.Stats.data_cache;
Show+='\n\n';
Show+="DATA_CACHE\n";

for(var key in temp){
  Show+=("\n"+key+": ");
  for(var v in temp[key])
  {
    Show+=("\n\t"+v+": ");
    Show+=("  "+temp[key][v]+"; ");
  }
}
// ----printing instruction chache
temp = results.Stats.instruction_cache;
Show+='\n\n';
Show+="INSTRUCTION_CACHE\n";

for(var key in temp){
  Show+=("\n"+key+": ");
  for(var v in temp[key])
  {
    Show+=("\n\t"+v+": ");
    Show+=("  "+temp[key][v]+"; ");
  }
}



var y = document.getElementById('mm1');

y.innerHTML = Show;
// --------------------------




}