//it works

var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request('http://www.imdb.com/movies-in-theaters/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2750721702&pf_rd_r=0JTF51AH9SYXCF1JZGH0&pf_rd_s=right-2&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_hd', function (error, response, html) {
  if (!error && response.statusCode == 200) {
    var $ = cheerio.load(html);
    $('h4').each(function(i, element){
      
	  name = $(this).children().first().attr('title');
	  imtext = $(this).parent().parent().children().first().attr('alt');
	  
      //console.log(metadata);
  	  
	  fs.appendFile("testdata.txt","\n"+ name + "\n" + imtext + "\n", function(err) {
  	    if(err) {
  	        return console.log(err);
  	    }

  	    console.log("The file was saved!");
  	}); 
	  
    });

  }
  
});