$(document).ready(() => {

	function addDanusan(danusan) {
		let html = "";
		html += '<tr>';

		html += '<td>';
		var rowCount = $('tbody tr').length;
		html += (rowCount + 1);
		html += '</td>';

		html += '<td>';
		html += '<img src= "';
		if (danusan.image != "") {
			html += danusan.image;
		} else {
			html += 'https://upload.wikimedia.org/wikipedia/commons/6/6c/No_image_3x4.svg';
		}
		html += '" class="card-img-top menu-img">';
		html += '</td>';

		html += '<td>';
		html += danusan.name;
		html += '</td>';

		html += '<td>';
		html += danusan.price;
		html += '</td>';

		html += '<td>';
		html += new Date(danusan.datetime).toLocaleString();
		html += '</td>';

		html += '</tr>';
		$(html).appendTo($('tbody'));
	}

	$.ajax({
		method: 'GET',
		url: '/danusan/get_danusan/',
		success: function(response) {
			for (let i = 0; i < response.length; i++) {
				addDanusan(response[i]);
			}
		}
	})

	$('#button').click(function(event) {
		event.preventDefault();
		var name = $("#name").val();
		var price = $("#price").val();
		var image = $("#image").val();
		var csrftoken = $("[name=csrfmiddlewaretoken]").val();
		// alert(key);
		$.ajax({
			method: 'POST',
			url: '/danusan/add_danusan/',
			data: {
				name: name,
				price: price,
				image: image,
				csrfmiddlewaretoken: csrftoken,
			},
			success: function(response) {	// response -> bebas
				addDanusan(response);
			}
		})
	})

	$('input').onKeyUp(function (event) {
		if (event.keyCode === 13) {
			$('#button').click();
		}
	});
})
