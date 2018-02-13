<script>

    setInterval(function() {
        $.ajax({
            method: "GET",
            url: "/meat/",
            dataType: "text",
            success: function(data) {
                $("tbody").empty();
                $.each(data, function (key, value) {
                    var meatKey = key;
                    var meatType = meat.meat_type;
                    var meatName = meat.cut_type;
                    var meatProduct = meat.weight;
                    $("tbody").append(
                       "<tr><td>" + meatType + "</td><td>" + meatName + "</td><td>" + meatProduct + "</td><td>"
                    )
                })
            },
            error: function(data) {
                console.log("error")
                console.log(data)
            }
        })
    },500)
</script>
