$(document).ready(() => {
  var acc = document.getElementsByClassName("accordion");
  var i;

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
      this.classList.toggle("active-clicked");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  }
  $('#search').val('')
  $.ajax({
    method: 'GET',
    url: '/danusan/dnajson&filter=all&keyword=current',
    dataType: 'json',
    success: function (response) {
      let $cardDanus = $('.danus-card-deck')
      // cardDanus.empty()
      let semuaDanus = response.items
      console.log(response);

      for (let i = response.length-1; i > response.length-4; i--) {
        let field = response[i].fields;
        let $h5 = $("<h5>").addClass("card-title").text(field.name);
        let $h6 = $("<h6>").addClass("card-title").text("Rp. " + field.price);
        let $p = $("<p>").addClass("card-text").text("Ini deskripsi danusan");
        let $img = $("<img>").attr({ "src": field.image });

        if (field.image == "") {
          $img.attr({ "src": "https://www.freeiconspng.com/uploads/no-image-icon-21.png" })
        }

        let divImg = $("<div>").addClass("card-img-top").append($img);

        let timestamp = $("<h6>").addClass("card-title mt-2").text(field.datetime);

        let $cardBody = $("<div>").addClass("card-body").append($h5, $h6, $p, timestamp);
        let $card = $("<div>").addClass("card").css({ "width": "18rem" }).append(divImg, $cardBody);

        $cardDanus.append($("<div>").append($card));
      }
    }
  })
})
