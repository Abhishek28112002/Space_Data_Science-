const express = require("express");
const upload = require("express-fileupload");
const fs = require("fs");
const path = require("path");
const download = require("download");
let { PythonShell } = require("python-shell");
const app = express();
app.use(express.static("./publick"));
app.use(upload());

app.get("/", function (req, res) {
  res.sendfile(path.resolve(__dirname, "./index.html"));
});
let options = {
  pythonOptions: ["-u"], 
};


app.post("/", function (req, res) {
  if (req.files) {
    console.log(req.files);
    var files = req.files.file;
    var filenames = "python.csv";
    files.mv("./uploads/" + filenames, (res1, err) => {
      if (err) res.send(err);
      else {
        PythonShell.run("final_draft.py", options, (err, results) => {
          if (err) console.log(err);
          if (results) {   
const folderPath = __dirname+'/uploads';
console.log(" path :", folderPath);
   download(folderPath+'/python.csv',`${__dirname}`).then(function(err,result) {
        if(err)Console.log(err);
        else
        console.log("done");
    })
    res.send(results);
}})
           
          }
        });
      }
    });

app.listen(5000);
