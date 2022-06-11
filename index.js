const express= require('express');
const upload= require('express-fileupload')
const pythonShell=require('python-shell');
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
// let options ={ 
//     scriptPath="C:\Users\Admin\Desktop\Space_Data_Science-",
//     file=files
// }
// PythonShell.run("final_draft.py",options,(err,res)=>{
//     if(err) console.log(err);
//     if(res) console.log(res);

// })

app.listen(5000);