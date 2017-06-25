$(document).ready(function(){
  console.log('ready!');

  var night = true;

  var nightTheme = "ace/theme/kr_theme";
  var dayTheme = "ace/theme/tomorrow"

  var solutions = {};

  var heightUpdateFunction = function(edt, div) {
    console.log(edt);
		// http://stackoverflow.com/questions/11584061/
    // var newHeight = edt.getSession().getScreenLength() * (edt.renderer.lineHeight + 5) + edt.renderer.scrollBar.getWidth();
		var newHeight = edt.getSession().getScreenLength() * (21) + edt.renderer.scrollBar.getWidth();
		$("#"+div).height(newHeight.toString() + "px");
    console.log(edt.renderer.lineHeight);
    console.log("new height for "+div+" is "+newHeight.toString() + "px");
		// This call is required for the editor to fix all of
		// its inner structure for adapting to a change in size
		edt.resize();
	};

  if ($("#solutions_div").length){  // check if the page has a #solutions_div
    let len = $("#solutions_div").find(".countThis").length;  // find the number of solutions based on the class .countThis that is embedded in the HTML by Django
    for (let i = 0; i < len; i++){  // dynamically create ace editors for each solution
      solutions["solution"+i] = ace.edit("solution"+i);
      solutions["solution"+i].setTheme(nightTheme);
      solutions["solution"+i].getSession().setMode("ace/mode/javascript");
      solutions["solution"+i].setOptions({
          fontSize: "12px"
      });
      solutions["solution"+i].container.style.lineHeight = 1.7
      $("#solution"+i).width("95%")
      $("#solution"+i).height("200px")
      console.log(solutions["solution"+i]);
      heightUpdateFunction(solutions["solution"+i], "solution"+i);
    }
  }

  $("#dayNight").click(function(){
    if (night) {
      if ($("#solutions_div").length){
        let len = $("#solutions_div").find(".countThis").length;
        for (let i = 0; i < len; i ++) {
          solutions["solution"+i].setTheme(dayTheme);
        }
      }
      $("body").addClass("bodyDay");
      night = false;
    } else {
      if ($("#solutions_div").length){
        let len = $("#solutions_div").find(".countThis").length;
        for (let i = 0; i < len; i ++) {
          solutions["solution"+i].setTheme(nightTheme);
        }
      }
      $("body").removeClass("bodyDay");
      night = true;
    }
  });

  $("#show_hide").click(function(){
    $("#solutions_div").toggle();
  })

});
