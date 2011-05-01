$(document).ready(function() {	
	
	// add handler for refreshing ip address
	$("#address_form_input").keyup(function(event) {
		var input = escape($("#address_form_input").val());
		
		if (input) {
			$.get("/"+input+"/partial", function(data, status) {
				if (status == "success") {
					$("#address_container").html(data);
					window.history.pushState("object or string", "Title", "/"+input);
				}

			})
		}
		else {
			$("#address_container").empty();
			window.history.pushState("object or string", "Title", "/");
		}

	});
	
	// expand string on losing focus
	$("#address_form_input").blur(function(event) {
		var input = escape($("#address_form_input").val());
		
		if (input) {
			$.get("/"+input+"/expand", function(data, status) {
				if (status == "success") {
					$("#address_form_input").val(data);
				}
			})
		}
	});
	
	// remove submit button
	$("#address_form_submit_container").remove();
	
	// remove attributes from form
	$("#address_form").removeAttr("action");
	$("#address_form").removeAttr("method");
	$("#address_form").submit(function(event) {
		return false;
	});
	
	// set focus to input field
	$("#address_form_input").focus();
	
	function escape(str) {
		return str.replace(/([ #;&%,+*~\'"!^$[\]()=>|])/g,'\\$1');
	}
});