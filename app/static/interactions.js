///JAVASCRIPTTT


$('#create_trip').on('click', function create_trip() {
	var trip_name = $("input[name=trip_name]").val();
	var trip_owner = $("input[name=trip_owner]").val();
	var participant_1 = $("input[name=participant-1]").val();
	var participant_2 = $("input[name=participant-2]").val();
	var destination_1 = $("input[name=destination-1]").val();
	////// DELETE THIS PART FOR NUM. 5 /////////
	$.post('create_trip',
			{trip_name: trip_name,
			trip_owner: trip_owner,
			participant_1: participant_1,
			participant_2: participant_2,
			destination_1: destination_1},
			function responseHandler(data) {
			console.log(data);
			document.body.parentNode.innerHTML = data;
		});
	////// DELETE THIS PART FOR NUM. 5 /////////
});

$("textarea[name=comment]").on('click', function clear() {
	this.value = "";
});

$("#results-email-container").on('click', '#email-results-button', function emailResults() {
	console.log($(this));
});

$("#site-title-wrapper").on('click', function goHome() {
	window.location.href = '/';
});

$(document).ready(function applySliderLabels() {
	var currentValue = $("#fe-before").val();
	$("#fe-before").next().html(currentValue);

	currentValue = $("#fe-after").val();
	$("#fe-after").next().html(currentValue);
});


$("input[type='range']").on('change', function updateLabel() {
	var currentValue = $(this).val();
	$(this).next().html(currentValue);
});

$(document).ready(function (){
	var baseParticipants = 4;
	var baseDestinations = 2;
	$("#add-participants-button").on('click', function(){
		var newInput = '<input type="text" name="participant-' + baseParticipants +'"><br />';
		$("#enter-participants-list").append(newInput);
		baseParticipants = baseParticipants + 1;
  });
	$("#add-destination-button").on('click', function(){
		var newInput = '<input type="text" name="participant-' + baseDestinations +'"><br />';
		$("#enter-participants-list").append(newInput);
		baseDestinations = baseDestinations + 1;
  });
});
