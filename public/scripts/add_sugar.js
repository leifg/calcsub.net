$(document).ready(function() {	
	
	// add handler for refreshing ip address
	$("#address_form_input").keyup(function(event) {
		var input = escape($("#address_form_input").val());
		
		if (input) {
			$.get("/"+input+"/partial", function(data, status) {
				if (status == "success") {
					$("#address_container").html(data);
				}

			})
		}
		else {
			$("#address_container").empty();
		}

	});
	
	// expand string on losing focus
	$("#address_form_input").blur(function(event) {
		var input = escape($("#address_form_input").val());
		
		$.get("/"+input+"/expand", function(data, status) {
			if (status == "success") {
				$("#address_form_input").val(data);
			}
		})
	});
	
	// remove submit button
	$("#address_form_submit_container").remove();
	
	// remove attributes from form
	$("#address_form").removeAttr("action");
	$("#address_form").removeAttr("method");
	$("#address_form").submit(function(event) {
		return false;
	});
	
	function escape(str) {
		return str.replace(/([ #;&%,+*~\'"!^$[\]()=>|])/g,'\\$1');
	}
});