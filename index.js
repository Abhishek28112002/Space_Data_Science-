const express = require("express");
const upload = require("express-fileupload");
var bodyParser = require('body-parser');
const fs = require("fs");
const path = require("path");
const zip = require('express-zip');
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
            res.sendfile(path.resolve(__dirname, "./index2.html"));
          }
        });
      }
    });
  }
});
    app.get('/multiple', function(req, res) {
      const folderPath = __dirname+'/uploads';
      res.zip([
        { path: folderPath+'/python.csv',
            name: 'output.csv'},
            { path: folderPath+'/features.txt',
            name: 'Features.txt'},
      ])
      })

app.listen(5000);
