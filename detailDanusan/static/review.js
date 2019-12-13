$(document).ready(function () {
	let path = window.location.pathname;
	path = path.split("/");
	// console.log(path);
	$.ajax({
        async: true ,
        type: "GET",
        url: "/reviewAPI&="+path[2],
        dataType: "json",
        success: function (response) {
        	for(i = 0; i < response.length;i++){
        		let $b = $("<b>").text(response[i].fields.Review);
        		let $td1 = $("<td>").append($b);
        		let $td2 = $("<td>").text(response[i].fields.Nama);
        		let $td3 = $("<td>").text(response[i].fields.Time);
        		let $tr = $("<tr>");

        		$tr.append($b, $td2, $td3);
        		$(".rev-tab").append($tr);
        	}
        }
      });	
});