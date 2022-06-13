const express= require('express');
const upload= require('express-fileupload')
const fs = require('fs');
const path = require('path');
let {PythonShell} = require('python-shell')
const app= express();
app.use(express.static('./publick'));
 app.use(upload());

app.get('/', function(req, res){
    res.sendfile(path.resolve(__dirname , './index.html'));
})
let options = {
    pythonOptions: ['-u'], // get print results in real-time
  };
  
app.post('/', function(req, res){
    if(req.files)
   { console.log(req.files);
var files = req.files.file;
var filenames = "python.csv";
files.mv('./uploads/'+filenames,(res1,err)=>{
    if(err) res.send(err);
    else
    {PythonShell.run("final_draft.py",options,(err, results)=>{
        if(err) console.log(err);
        if(results){
            console.log('results: %j', results);
 
//     results.forEach(result=>{
//         fs.appendFile(path.join(__dirname,'index2.html'),result,(res,err)=>{
// if(err) console.log(err);
//    }
//         )
//     })
 res.sendfile(__dirname +'/index2.html');
  
//   res.writeHead(200, { 'Content-Type': 'html/json' });
//  res.write(``)
//    res.write(`<h3>Our Features</h3>`)
//  res.write(JSON.stringify(results));
 res.send(results);

        }
    })}
})

}

})
 

app.listen(5000);