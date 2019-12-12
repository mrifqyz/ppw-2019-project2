$(document).ready(function () {
    $.ajax({
        async: true ,
        type: "GET",
        url: "/danusan/dnajson&filter=user&keyword=current",
        dataType: "json",
        success: function (response) {
            let $data = $("#data");
            for(i = 0; i < response.length;i++){
                let field = response[i].fields;
                let $h5 = $("<h5>").addClass("card-title").text(field.name);
                let $h6 = $("<h6>").addClass("card-title").text("Rp. " + field.price);
                let $p = $("<p>").addClass("card-text").text("Some quick example text to build on the card title and make up the bulk of the card's content.");

                let $img = $("<img>").attr({"src":field.image});
                if(field.image == ""){
                    $img.attr({"src":"https://www.freeiconspng.com/uploads/no-image-icon-21.png"})
                }

                let divImg = $("<div>").addClass("card-img-top").append($img);

                let timestamp = $("<h6>").addClass("card-title mt-2").text(field.datetime);

                let $cardBody = $("<div>").addClass("card-body").append($h5, $h6, $p, timestamp);
                let $card = $("<div>").addClass("card").css({"width":"18rem"}).append(divImg, $cardBody);

                $data.append($("<div>").addClass("col my-2").append($card));
            }
        }
    });
});