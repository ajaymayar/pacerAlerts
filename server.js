/****
* create the pythonshell object
* run the shell with the commands received from the form
* if the user changes any settings, change the python script
*/


var express = require('express');
var app = express();
var router = express.Router();
var path = __dirname;

router.use(function (request, response, next) {
  console.log("/" + request.method);
  next();
});



app.get("/", function (request, response) {
  response.sendFile(path + "/index.html");
});

app.use("/", router);

console.log('about to create cronjob');
var CronJob = require('cron').CronJob;
var job = new CronJob('00 30 11 * * 1-5', function() {

  // 1:17-cv-10242-IT Government of Bermuda v. Lahey Clinic, Inc. et al
  var options = {
    args: ['1:17-cv-10242-IT']
  };

  var PythonShell = require('python-shell');
  var pyshell = new PythonShell('pacerSearch.py', options);
  // PythonShell.run('pacerSearch.py', options, function (err) {
  //  if (err) throw err;
  //  console.log('Ran search');
  // });
  
  pyshell.on('message', function(message) {
    console.log(message);
  });
}, function(){}, true);


app.listen(3000, function() {
  console.log("Port 3000");
});
