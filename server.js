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


console.log('about to create cronjob');
var CronJob = require('cron').CronJob;
var job = new CronJob('00 30 11 * * 1-5', function() {

  var options = {
    args: ['1:17-cv-10242-IT', 'ajaymayar96@gmail.com']
  };

  var PythonShell = require('python-shell');
  PythonShell.run('pacerSearch.py', options, function (err) {
    if (err) throw err;
    console.log('finished');
  });
}, function(){}, true);

app.get("/", function (request, response) {
  response.sendFile(path + "/index.html");
});

app.use("/", router);

app.listen(3000, function() {
  console.log("Port 3000");
});
