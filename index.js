const express= require('express');
const upload= require('express-fileupload')
let {PythonShell} = require('python-shell')
const app= express();
app.use(upload());

app.get('/', function(req, res){
    res.sendfile(__dirname + '/index.html');
})
app.post('/', function(req, res){
    if(req.files)
   { console.log(req.files);
var files = req.files.file;
var filenames = "python.csv";
files.mv('./uploads/'+filenames,(req,err)=>{
    if(err) res.send(err);
    else
     res.send("file uploaded");
})
}
})
 PythonShell.run("final_draft.py",null,(res,err)=>{
    if(err) console.log(err);
    if(res){
        res.sendfile(__dirname + '/index2.html' +res);
    }
})

app.listen(5000);