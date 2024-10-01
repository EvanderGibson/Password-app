$(document).ready(function(){

	$(".simpletext").click(function() {
		$(".simple").show("slow");
		$(".complicatedtext").hide("fast");
	});
	$(".complicatedtext").click(function() {
		$(".complicated").show("slow");
		$(".simpletext").hide("fast");
	});
});

